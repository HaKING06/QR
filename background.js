/* Registers listeners synchronously for MV3 service-worker wakeups. No QR payloads. */
if(typeof importScripts==='function')importScripts('shared/core.js','shared/update-core.js');
(() => {
  'use strict';
  const api=globalThis.browser||globalThis.chrome;
  const version=api.runtime.getManifest().version;
  const source=api.runtime.id==='klblmhlgnbnclpdhddadkbbccmdjknmf'||/Edg\//.test(navigator.userAgent)?'edge':/Firefox\//.test(navigator.userAgent)?'firefox':'chrome';
  let serial=Promise.resolve();
  const run=job=>{serial=serial.then(job,job).catch(()=>{});};
  async function preferences(){
    const stored=await api.storage.local.get('preferences');
    return QRUpdates.language(stored.preferences?.language==='auto'?api.i18n.getUILanguage():stored.preferences?.language||api.i18n.getUILanguage());
  }
  async function urlFor(reason,target=version,previous){return QRUpdates.releaseURL({version:target,previous,reason,source,locale:await preferences()});}
  async function notify(reason,target){
    if(!await api.permissions.contains({permissions:['notifications']}))return;
    const title=(api.i18n.getMessage(reason==='update'?'notificationInstalled':'notificationAvailable')||'QR Scanner {version}').replace('{version}',target);
    const message=api.i18n.getMessage('notificationBody')||'See what is new in QR Scanner.';
    await api.notifications.create('qr-'+reason+'-'+target,{type:'basic',iconUrl:api.runtime.getURL('assets/brand/icon-128.png'),title,message});
  }
  async function installed(details){
    const state=await api.storage.local.get(['lastOpenedVersion','welcomeOpened']);
    if(details.reason==='install'){
      if(!state.welcomeOpened){await api.tabs.create({url:await urlFor('install')});await api.storage.local.set({welcomeOpened:true,lastOpenedVersion:version});}
      return;
    }
    if(!QRUpdates.shouldOpen(details,version,state.lastOpenedVersion))return;
    await api.tabs.create({url:await urlFor('update',version,details.previousVersion)});
    await api.storage.local.set({lastOpenedVersion:version});
    await api.action?.setBadgeBackgroundColor({color:'#4864ff'});
    await api.action?.setBadgeText({text:'NEW'});
    await notify('update',version);
  }
  async function available(target){
    if(QRCore.compareVersions(target,version)<=0)return;
    const state=await api.storage.local.get('lastNotifiedVersion');
    if(state.lastNotifiedVersion===target)return;
    if(!await api.permissions.contains({permissions:['notifications']}))return;
    await notify('available',target);
    await api.storage.local.set({lastNotifiedVersion:target});
  }
  api.runtime.onInstalled.addListener(details=>run(()=>installed(details)));
  api.runtime.onMessage.addListener((message,sender)=>{
    if(sender.id!==api.runtime.id||message?.type!=='release.available')return;
    if(!/^\d+\.\d+\.\d+$/.test(message.version||''))return;
    run(()=>available(message.version));
  });
  api.notifications?.onClicked.addListener(id=>{
    const match=/^qr-(update|available)-(\d+\.\d+\.\d+)$/.exec(id);
    if(match)run(async()=>{await api.tabs.create({url:await urlFor(match[1],match[2])});await api.notifications.clear(id);});
  });
})();
