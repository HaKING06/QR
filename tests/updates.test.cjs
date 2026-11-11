const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm');
const core=require('../shared/core.js'),updates=require('../shared/update-core.js');
test('release URLs contain only version metadata and trusted paths',()=>{
 const url=new URL(updates.releaseURL({version:'1.1.3',previous:'1.1.2',locale:'ar-SA',source:'edge'}));
 assert.equal(url.origin,'https://qr.haking.tr');assert.equal(url.pathname,'/ar/updates.html');
 assert.equal(url.searchParams.get('previous'),'1.1.2');assert.equal(url.searchParams.get('source'),'edge');
 assert.throws(()=>updates.releaseURL({version:'javascript:alert(1)'}));
 assert.equal(updates.shouldOpen({reason:'update',previousVersion:'1.1.2'},'1.1.3',null),true);
 assert.equal(updates.shouldOpen({reason:'update',previousVersion:'1.1.3'},'1.1.3',null),false);
 assert.equal(updates.shouldOpen({reason:'update',previousVersion:'1.1.4'},'1.1.3',null),false);
 assert.equal(updates.shouldOpen({reason:'update',previousVersion:'1.1.2'},'1.1.3','1.1.3'),false);
});
function fixture(){
 const data={},tabs=[],notifications=[],handlers={},permission={enabled:false};
 const api={
  runtime:{id:'pmhjjnijononbcfddpimpegdobibhijo',getManifest:()=>({version:'1.1.3'}),getURL:p=>'chrome-extension://test/'+p,onInstalled:{addListener:fn=>handlers.installed=fn},onMessage:{addListener:fn=>handlers.message=fn}},
  storage:{local:{get:async keys=>Object.fromEntries((Array.isArray(keys)?keys:[keys]).map(key=>[key,data[key]])),set:async values=>Object.assign(data,values)}},
  tabs:{create:async item=>{tabs.push(item);}},
  i18n:{getUILanguage:()=> 'ar-SA',getMessage:key=>key==='notificationAvailable'?'QR Scanner {version} is available':'Update installed'},
  action:{setBadgeBackgroundColor:async()=>{},setBadgeText:async()=>{}},
  permissions:{contains:async()=>permission.enabled},
  notifications:{create:async(id,options)=>notifications.push({id,options}),clear:async()=>{},onClicked:{addListener:fn=>handlers.click=fn}},
 };
 const context={chrome:api,navigator:{userAgent:'Chrome'},QRCore:core,QRUpdates:updates,URL,importScripts:()=>{}};
 vm.runInNewContext(fs.readFileSync(require.resolve('../background.js'),'utf8'),context);
 return {api,data,tabs,notifications,handlers,permission,flush:()=>new Promise(resolve=>setTimeout(resolve,10))};
}
test('mocked browser lifecycle opens the update page once and ignores reloads',async()=>{
 const f=fixture();f.handlers.installed({reason:'update',previousVersion:'1.1.2'});await f.flush();
 assert.equal(f.tabs.length,1);assert.equal(new URL(f.tabs[0].url).pathname,'/ar/updates.html');
 f.handlers.installed({reason:'update',previousVersion:'1.1.2'});f.handlers.installed({reason:'update',previousVersion:'1.1.3'});await f.flush();
 assert.equal(f.tabs.length,1);assert.equal(f.notifications.length,0);
});
test('mocked optional notifications require permission and do not auto-open available releases',async()=>{
 const f=fixture(),message={type:'release.available',version:'1.1.4'},sender={id:f.api.runtime.id};
 f.handlers.message(message,sender);await f.flush();assert.equal(f.notifications.length,0);
 f.permission.enabled=true;f.handlers.message(message,sender);f.handlers.message(message,sender);await f.flush();
 assert.equal(f.notifications.length,1);assert.equal(f.tabs.length,0);
 f.handlers.click('qr-available-1.1.4');await f.flush();assert.equal(f.tabs.length,1);
 assert.equal(new URL(f.tabs[0].url).searchParams.get('reason'),'available');
});
