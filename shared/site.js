(() => {
  'use strict';
  if(document.documentElement.dataset.extension==='true')return;
  const version=document.documentElement.dataset.version;
  const browsers=['chrome','edge','brave','opera','firefox'];
  const params=new URLSearchParams(location.search);
  const guide=document.getElementById('guide-download');
  let current=browsers.includes(params.get('browser'))?params.get('browser'):'chrome';
  const packageName=browser=>`qr-scanner-${version}-${browser==='firefox'?'firefox':'chromium'}.zip`;
  function updateGuide(browser,updateURL=false){
    current=browser;
    document.querySelectorAll('[data-guide-browser]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.guideBrowser===browser)));
    document.getElementById('chromium-guide').hidden=browser==='firefox';
    document.getElementById('firefox-guide').hidden=browser!=='firefox';
    document.getElementById('extensions-address').textContent={chrome:'chrome://extensions',edge:'edge://extensions',brave:'brave://extensions',opera:'opera://extensions',firefox:'about:debugging'}[browser];
    guide.href='/downloads/'+packageName(browser);guide.dataset.browser=browser;
    if(updateURL){const url=new URL(location.href);url.searchParams.set('browser',browser);url.searchParams.delete('download');history.replaceState(null,'',url);document.getElementById('download-success').hidden=true;}
  }
  if(guide){
    updateGuide(current);
    document.querySelectorAll('[data-guide-browser]').forEach(button=>button.onclick=()=>updateGuide(button.dataset.guideBrowser,true));
    if(params.get('download')==='1'){document.getElementById('download-success').hidden=false;document.getElementById('download-name').textContent=packageName(current);}
    document.getElementById('copy-address').onclick=async()=>{try{await navigator.clipboard.writeText(document.getElementById('extensions-address').textContent);const toast=document.getElementById('status');toast.textContent=window.QRText('copied');toast.classList.add('visible');setTimeout(()=>toast.classList.remove('visible'),2500);}catch{const range=document.createRange();range.selectNodeContents(document.getElementById('extensions-address'));getSelection().removeAllRanges();getSelection().addRange(range);}};
  }
  // Preserve the anchor's native user-initiated download, then open its guide.
  document.querySelectorAll('.pack-download').forEach(link=>link.addEventListener('click',event=>{
    if(event.button!==0||event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return;
    const browser=browsers.includes(link.dataset.browser)?link.dataset.browser:'chrome';
    const destination=new URL('help.html',location.href);destination.searchParams.set('browser',browser);destination.searchParams.set('download','1');
    setTimeout(()=>location.assign(destination.href),400);
  }));
})();
