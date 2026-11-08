(async () => {
  'use strict';
  // Bind controls synchronously: the first interaction must not wait on a
  // translation fetch (especially on a fresh CDN edge or slow connection).
  let t=k=>document.querySelector(`[data-i18n="${k}"]`)?.textContent||k;
  window.QRI18n?.then(locale=>{t=locale.t;}).catch(()=>{});
  const $=id=>document.getElementById(id), api=globalThis.browser||globalThis.chrome;
  let toastTimer, qr=null, generated='', scanJob=0;
  function status(key){const el=$('status');el.textContent=t(key);el.classList.add('visible');clearTimeout(toastTimer);toastTimer=setTimeout(()=>el.classList.remove('visible'),4500);}
  if(!$('generator'))return;
  function tab(mode){
    ['create','read'].forEach(name=>{$(name+'-panel').hidden=name!==mode;$(name+'-tab').setAttribute('aria-selected',String(name===mode));});
  }
  ['create','read'].forEach(name=>{$(name+'-tab').onclick=()=>tab(name);$(name+'-tab').onkeydown=e=>{if(['ArrowLeft','ArrowRight'].includes(e.key)){e.preventDefault();const other=name==='create'?'read':'create';tab(other);$(other+'-tab').focus();}};});
  document.querySelectorAll('a[href="#toolkit"]').forEach(el=>el.addEventListener('click',()=>tab('create')));
  function invalidate(){qr=null;generated='';$('png').disabled=true;$('svg').disabled=true;$('qr-preview').replaceChildren();const mark=document.createElement('span');mark.className='placeholder-mark';mark.textContent='▦';$('qr-preview').append(mark);}
  $('type').onchange=()=>{$('wifi-fields').hidden=$('type').value!=='wifi';$('email-fields').hidden=$('type').value!=='email';$('content').placeholder={url:'https://example.com',text:'…',wifi:'SSID',email:'hello@example.com'}[$('type').value];invalidate();};
  $('generator').addEventListener('input',invalidate);
  function svgString(){
    const n=qr.getModuleCount(),s=n+8,color=$('color').value;
    let path='';for(let y=0;y<n;y++)for(let x=0;x<n;x++)if(qr.isDark(y,x))path+=`M${x+4} ${y+4}h1v1h-1z`;
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${$('size').value}" height="${$('size').value}" viewBox="0 0 ${s} ${s}" shape-rendering="crispEdges"><rect width="${s}" height="${s}" fill="#fff"/><path d="${path}" fill="${color}"/></svg>`;
  }
  function canvas(){const c=document.createElement('canvas'),size=Number($('size').value);c.width=c.height=size;const ctx=c.getContext('2d');ctx.fillStyle='#fff';ctx.fillRect(0,0,size,size);ctx.fillStyle=$('color').value;const n=qr.getModuleCount(),cell=Math.floor(size/(n+8)),offset=Math.floor((size-n*cell)/2);for(let y=0;y<n;y++)for(let x=0;x<n;x++)if(qr.isDark(y,x))ctx.fillRect(offset+x*cell,offset+y*cell,cell,cell);return c;}
  $('generator').onsubmit=e=>{e.preventDefault();
    let value;try{value=QRCore.payload($('type').value,{text:$('content').value,password:$('password').value,security:$('security').value,subject:$('subject').value});}catch(err){status(err.message==='empty'?'empty':'invalid');return;}
    try{qrcode.stringToBytes=qrcode.stringToBytesFuncs['UTF-8'];qr=qrcode(0,'M');qr.addData(value);qr.make();generated=value;const c=canvas();c.setAttribute('aria-label',t('preview'));$('qr-preview').replaceChildren(c);$('png').disabled=false;$('svg').disabled=false;status('ready');}catch{invalidate();status('tooLong');}
  };
  function download(blob,ext){const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='qr-scanner.'+ext;a.click();setTimeout(()=>URL.revokeObjectURL(url),10000);}
  $('png').onclick=()=>{if(qr)canvas().toBlob(blob=>{if(blob)download(blob,'png');},'image/png');};
  $('svg').onclick=()=>{if(qr)download(new Blob([svgString()],{type:'image/svg+xml'}),'svg');};
  $('clear').onclick=()=>{$('content').value='';$('password').value='';$('subject').value='';invalidate();$('content').focus();};
  async function scanImage(blob){
    const job=++scanJob;$('scan-result').hidden=true;$('result').value='';$('open').hidden=true;$('open').removeAttribute('href');
    if(!blob||!['image/png','image/jpeg','image/webp'].includes(blob.type)||blob.size>15*1024*1024){status('badFile');return;}
    status('scanning');const url=URL.createObjectURL(blob);
    try{const img=new Image();await new Promise((resolve,reject)=>{img.onload=resolve;img.onerror=reject;img.src=url;});if(job!==scanJob)return;
      // Bound decoded pixel memory and scanner CPU; preserve original size when practical.
      const max=1800,scale=Math.min(1,max/Math.max(img.naturalWidth,img.naturalHeight));
      const c=document.createElement('canvas');c.width=Math.max(1,Math.round(img.naturalWidth*scale));c.height=Math.max(1,Math.round(img.naturalHeight*scale));const ctx=c.getContext('2d',{willReadFrequently:true});ctx.fillStyle='#fff';ctx.fillRect(0,0,c.width,c.height);ctx.drawImage(img,0,0,c.width,c.height);
      const data=ctx.getImageData(0,0,c.width,c.height);let code=jsQR(data.data,c.width,c.height,{inversionAttempts:'attemptBoth'});
      if(!code){for(let i=0;i<data.data.length;i+=4){const v=(data.data[i]+data.data[i+1]+data.data[i+2])/3>128?255:0;data.data[i]=data.data[i+1]=data.data[i+2]=v;}code=jsQR(data.data,c.width,c.height,{inversionAttempts:'attemptBoth'});}
      if(job!==scanJob)return;if(!code){status('notFound');return;}
      $('result').value=code.data;$('scan-result').hidden=false;const safe=QRCore.safeLink(code.data);$('open').hidden=!safe;if(safe)$('open').href=safe;status('ready');
    }catch{if(job===scanJob)status('fileError');}finally{URL.revokeObjectURL(url);$('file').value='';}
  }
  $('file').onchange=e=>{if(e.target.files[0])scanImage(e.target.files[0]);};
  const zone=$('drop-zone');zone.ondragover=e=>{e.preventDefault();zone.classList.add('dragging');};zone.ondragleave=()=>zone.classList.remove('dragging');zone.ondrop=e=>{e.preventDefault();zone.classList.remove('dragging');if(e.dataTransfer.files[0])scanImage(e.dataTransfer.files[0]);};
  document.addEventListener('paste',e=>{if($('read-panel').hidden)return;const file=[...e.clipboardData.items].find(x=>x.type.startsWith('image/'))?.getAsFile();if(file){e.preventDefault();scanImage(file);}});
  $('copy').onclick=async()=>{try{await navigator.clipboard.writeText($('result').value);status('copied');}catch{$('result').focus();$('result').select();status('copyError');}};
  if(api?.runtime?.id){
    const shot=$('screenshot');shot.hidden=false;shot.onclick=async()=>{shot.disabled=true;try{const data=await api.tabs.captureVisibleTab(null,{format:'png'});const blob=await(await fetch(data)).blob();await scanImage(blob);}catch{status('screenError');}finally{shot.disabled=false;}};
    // No QR data in this request. Cache version checks for 24h; network failure stays silent.
    try{
      const cache=JSON.parse(localStorage.getItem('qr-release')||'null');let latest=cache?.value;
      if(!cache||Date.now()-cache.time>86400000){const response=await fetch('https://qr.haking.tr/version.json',{cache:'no-store',credentials:'omit',signal:AbortSignal.timeout(5000)});if(response.ok){latest=await response.json();if(/^\d+\.\d+\.\d+$/.test(latest.version))localStorage.setItem('qr-release',JSON.stringify({time:Date.now(),value:latest}));}}
      if(latest&&QRCore.compareVersions(latest.version,api.runtime.getManifest().version)>0)$('update').hidden=false;
    }catch{/* Offline operation remains fully functional. */}
  }
})();
