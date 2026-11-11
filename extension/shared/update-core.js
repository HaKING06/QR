(function(root){
  'use strict';
  const languages=['tr','en','de','es','fr','pt','ru','ar'];
  function language(value){const code=String(value||'en').split('-')[0];return languages.includes(code)?code:'en';}
  function releaseURL({version,previous,reason='update',source='chrome',locale='en'}){
    if(!/^\d+\.\d+\.\d+$/.test(version))throw new Error('Invalid version');
    const url=new URL('https://qr.haking.tr/'+language(locale)+'/updates.html');
    url.searchParams.set('version',version);
    if(/^\d+\.\d+\.\d+$/.test(previous||''))url.searchParams.set('previous',previous);
    url.searchParams.set('reason',['install','update','available'].includes(reason)?reason:'update');
    url.searchParams.set('source',['chrome','edge','firefox'].includes(source)?source:'chrome');
    return url.href;
  }
  function shouldOpen(details,version,lastOpened){
    return details.reason==='update'&&/^\d+\.\d+\.\d+$/.test(details.previousVersion||'')&&root.QRCore.compareVersions(version,details.previousVersion)>0&&lastOpened!==version;
  }
  const api={language,releaseURL,shouldOpen};
  if(typeof module!=='undefined')module.exports=api;
  root.QRUpdates=api;
})(typeof globalThis!=='undefined'?globalThis:this);
