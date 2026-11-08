(() => {
  'use strict';
  const $=id=>document.getElementById(id);
  if(!$('generator'))return;
  const t=key=>window.QRText?.(key)||key;
  const popup=document.documentElement.dataset.extension==='true';
  const api=globalThis.browser||globalThis.chrome;
  let qr=null,payload='',timer,toastTimer,scanJob=0,stream=null,cameraFrame=0,cameraBusy=false;
  function toast(key){$('status').textContent=t(key);$('status').classList.add('visible');clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('status').classList.remove('visible'),3500);}
  function readerStatus(key,error=false){$('reader-status').textContent=t(key);$('reader-status').classList.toggle('error',error);}
  function tab(mode){
    if(mode!=='read')stopCamera();
    ['create','read'].forEach(name=>{$(name+'-panel').hidden=name!==mode;$(name+'-tab').setAttribute('aria-selected',String(name===mode));});
    if(popup)$('main').scrollTop=0;
  }
  for(const name of ['create','read']){
    $(name+'-tab').onclick=()=>tab(name);
    $(name+'-tab').onkeydown=event=>{if(['ArrowLeft','ArrowRight'].includes(event.key)){event.preventDefault();const next=name==='create'?'read':'create';tab(next);$(next+'-tab').focus();}};
  }
  function setType(type,clear=true){
    $('type').value=type;
    for(const name of ['wifi','email','sms','vcard'])$(name+'-fields').hidden=type!==name;
    $('content-label').replaceChildren(Object.assign(document.createElement('span'),{textContent:t(type==='vcard'?'fullName':type==='phone'||type==='sms'?'phone':'content')}));
    $('content').placeholder={url:'https://example.com',text:'…',wifi:'SSID',email:'hello@example.com',phone:'+90 555 123 4567',sms:'+90 555 123 4567',vcard:'Ada Lovelace'}[type];
    document.querySelectorAll('[data-qr-type]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.qrType===type)));
    if(clear){$('content').value='';$('form-message').textContent='';invalidate();}
  }
  document.querySelectorAll('[data-qr-type]').forEach(button=>button.onclick=()=>setType(button.dataset.qrType));
  $('type').onchange=()=>setType($('type').value);
  function invalidate(){
    qr=null;payload='';for(const id of ['png','svg','copy-image'])$(id).disabled=true;
    const empty=document.createElement('div');empty.className='empty-qr';empty.textContent=t('preview');$('qr-preview').replaceChildren(empty);$('preview-caption').textContent=t('contentHint');
  }
  function makeCanvas(){
    const canvas=document.createElement('canvas'),size=Number($('size').value);canvas.width=canvas.height=size;
    const ctx=canvas.getContext('2d');ctx.fillStyle='#fff';ctx.fillRect(0,0,size,size);ctx.fillStyle=$('color').value;
    const count=qr.getModuleCount(),cell=Math.floor(size/(count+8)),offset=Math.floor((size-count*cell)/2);
    for(let row=0;row<count;row++)for(let col=0;col<count;col++)if(qr.isDark(row,col))ctx.fillRect(offset+col*cell,offset+row*cell,cell,cell);
    return canvas;
  }
  function generate(manual=false){
    clearTimeout(timer);$('content').removeAttribute('aria-invalid');$('form-message').textContent='';
    if(!globalThis.qrcode||!globalThis.QRCore){$('form-message').textContent=t('engineError');return;}
    if(!$('content').value.trim()){invalidate();if(manual){$('form-message').textContent=t('empty');$('content').setAttribute('aria-invalid','true');$('content').focus();}return;}
    try{
      const value=QRCore.payload($('type').value,{text:$('content').value,password:$('password').value,security:$('security').value,hidden:$('hidden-network').checked,subject:$('subject').value,message:$('message').value,organization:$('organization').value,phone:$('contact-phone').value,email:$('contact-email').value});
      qrcode.stringToBytes=qrcode.stringToBytesFuncs['UTF-8'];const next=qrcode(0,$('correction').value);next.addData(value);next.make();qr=next;payload=value;
      const canvas=makeCanvas();canvas.setAttribute('aria-label',t('preview'));$('qr-preview').replaceChildren(canvas);
      for(const id of ['png','svg','copy-image'])$(id).disabled=false;
      $('preview-caption').textContent=t('ready');if(manual)toast('ready');
    }catch(error){invalidate();$('form-message').textContent=t(error.message==='invalid'?'invalid':'tooLong');$('content').setAttribute('aria-invalid','true');}
  }
  $('generator').onsubmit=event=>{event.preventDefault();generate(true);};
  $('generator').addEventListener('input',()=>{clearTimeout(timer);for(const id of ['png','svg','copy-image'])$(id).disabled=true;timer=setTimeout(()=>generate(),250);});
  $('generator').addEventListener('change',event=>{if(event.target.id!=='type')generate();});
  $('security').addEventListener('change',()=>{$('password').disabled=$('security').value==='nopass';});
  function download(blob,format){const url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download='qr-scanner.'+format;document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),30000);}
  $('png').onclick=()=>{if(qr)makeCanvas().toBlob(blob=>{if(blob)download(blob,'png');},'image/png');};
  $('svg').onclick=()=>{
    if(!qr)return;const count=qr.getModuleCount(),size=count+8;let path='';
    for(let row=0;row<count;row++)for(let col=0;col<count;col++)if(qr.isDark(row,col))path+=`M${col+4} ${row+4}h1v1h-1z`;
    const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="${$('size').value}" height="${$('size').value}" viewBox="0 0 ${size} ${size}" shape-rendering="crispEdges"><rect width="${size}" height="${size}" fill="#fff"/><path d="${path}" fill="${$('color').value}"/></svg>`;
    download(new Blob([svg],{type:'image/svg+xml'}),'svg');
  };
  $('copy-image').onclick=async()=>{
    if(!qr)return;
    try{const blob=new Promise(resolve=>makeCanvas().toBlob(resolve,'image/png'));await navigator.clipboard.write([new ClipboardItem({'image/png':blob})]);toast('copied');}catch{toast('copyError');}
  };
  $('clear').onclick=()=>{clearTimeout(timer);$('generator').reset();setType('url');$('password').disabled=false;$('content').focus();};
  function showResult(value){
    $('result').value=value;$('scan-result').hidden=false;const safe=QRCore.safeLink(value);$('open').hidden=!safe;$('open').removeAttribute('href');if(safe)$('open').href=safe;readerStatus('ready');
  }
  function decodeCanvas(canvas){
    const ctx=canvas.getContext('2d',{willReadFrequently:true}),image=ctx.getImageData(0,0,canvas.width,canvas.height);
    return jsQR(image.data,canvas.width,canvas.height,{inversionAttempts:'attemptBoth'});
  }
  async function scanImage(blob){
    const job=++scanJob;stopCamera();$('scan-result').hidden=true;$('result').value='';$('open').hidden=true;$('open').removeAttribute('href');
    if(!blob||!['image/png','image/jpeg','image/webp'].includes(blob.type)||blob.size>15*1024*1024){readerStatus('badFile',true);return;}
    if(!globalThis.jsQR){readerStatus('engineError',true);return;}
    readerStatus('scanning');const url=URL.createObjectURL(blob);
    try{
      const image=new Image();await new Promise((resolve,reject)=>{image.onload=resolve;image.onerror=reject;image.src=url;});if(job!==scanJob)return;
      const scale=Math.min(1,2200/Math.max(image.naturalWidth,image.naturalHeight)),canvas=document.createElement('canvas');canvas.width=Math.max(1,Math.round(image.naturalWidth*scale));canvas.height=Math.max(1,Math.round(image.naturalHeight*scale));
      const ctx=canvas.getContext('2d',{willReadFrequently:true});ctx.fillStyle='#fff';ctx.fillRect(0,0,canvas.width,canvas.height);ctx.drawImage(image,0,0,canvas.width,canvas.height);
      let code=decodeCanvas(canvas);
      if(!code){const pixels=ctx.getImageData(0,0,canvas.width,canvas.height);for(let index=0;index<pixels.data.length;index+=4){const v=(pixels.data[index]+pixels.data[index+1]+pixels.data[index+2])/3>128?255:0;pixels.data[index]=pixels.data[index+1]=pixels.data[index+2]=v;}ctx.putImageData(pixels,0,0);code=decodeCanvas(canvas);}
      if(job!==scanJob)return;if(code)showResult(code.data);else readerStatus('notFound',true);
    }catch{if(job===scanJob)readerStatus('fileError',true);}finally{URL.revokeObjectURL(url);$('file').value='';}
  }
  $('file').onchange=event=>{if(event.target.files[0])scanImage(event.target.files[0]);};
  const zone=$('drop-zone');zone.ondragover=event=>{event.preventDefault();zone.classList.add('dragging');};zone.ondragleave=()=>zone.classList.remove('dragging');zone.ondrop=event=>{event.preventDefault();zone.classList.remove('dragging');if(event.dataTransfer.files[0])scanImage(event.dataTransfer.files[0]);};
  document.addEventListener('paste',event=>{if($('read-panel').hidden)return;const image=[...event.clipboardData.items].find(item=>item.type.startsWith('image/'))?.getAsFile();if(image){event.preventDefault();scanImage(image);}});
  $('copy').onclick=async()=>{try{await navigator.clipboard.writeText($('result').value);toast('copied');}catch{$('result').focus();$('result').select();toast('copyError');}};
  $('reset-scan').onclick=()=>{++scanJob;stopCamera();$('scan-result').hidden=true;$('result').value='';$('open').hidden=true;$('open').removeAttribute('href');readerStatus('readyScan');};
  function stopCamera(){if(stream){stream.getTracks().forEach(track=>track.stop());stream=null;}cancelAnimationFrame(cameraFrame);$('camera-video').srcObject=null;$('camera-view').hidden=true;$('camera').disabled=false;}
  $('stop-camera').onclick=stopCamera;
  $('camera').onclick=async()=>{
    try{
      $('camera').disabled=true;stream=await navigator.mediaDevices.getUserMedia({video:{facingMode:'environment',width:{ideal:1280}},audio:false});
      if($('read-panel').hidden){stopCamera();return;}
      $('camera-view').hidden=false;$('camera-video').srcObject=stream;await $('camera-video').play();readerStatus('scanning');
      let last=0;const canvas=document.createElement('canvas');
      function frame(now){
        if(!stream)return;
        if(now-last>300&&!cameraBusy&&$('camera-video').readyState>=2){
          cameraBusy=true;last=now;const video=$('camera-video'),scale=Math.min(1,900/video.videoWidth);canvas.width=Math.round(video.videoWidth*scale);canvas.height=Math.round(video.videoHeight*scale);canvas.getContext('2d').drawImage(video,0,0,canvas.width,canvas.height);
          try{const code=decodeCanvas(canvas);if(code){showResult(code.data);stopCamera();cameraBusy=false;return;}}catch{}cameraBusy=false;
        }
        cameraFrame=requestAnimationFrame(frame);
      }
      cameraFrame=requestAnimationFrame(frame);
    }catch{stopCamera();readerStatus('cameraError',true);}
  };
  window.addEventListener('pagehide',stopCamera);document.addEventListener('visibilitychange',()=>{if(document.hidden)stopCamera();});
  if(popup){
    $('camera').hidden=true;
    if(api?.runtime?.id){
      $('screenshot').hidden=false;$('tab-qr').hidden=false;
      $('screenshot').onclick=async()=>{const button=$('screenshot');button.disabled=true;try{const screenshot=await api.tabs.captureVisibleTab(null,{format:'png'});await scanImage(await(await fetch(screenshot)).blob());}catch{readerStatus('screenError',true);}finally{button.disabled=false;}};
      $('tab-qr').onclick=async()=>{try{const [current]=await api.tabs.query({active:true,currentWindow:true});const url=QRCore.safeLink(current?.url);if(!url)throw new Error();setType('url');$('content').value=url;generate();tab('create');}catch{toast('screenError');}};
      checkRelease();
    }
  }
  async function checkRelease(){
    let latest=null;
    try{const cached=JSON.parse(localStorage.getItem('qr-release')||'null');latest=cached?.value;
      if(!cached||Date.now()-cached.time>3600000){try{const response=await fetch('https://qr.haking.tr/version.json',{cache:'no-store',credentials:'omit',signal:AbortSignal.timeout(5000)});if(response.ok){const value=await response.json();if(/^\d+\.\d+\.\d+$/.test(value.version)){latest=value;localStorage.setItem('qr-release',JSON.stringify({time:Date.now(),value}));}}}catch{}}
    }catch{}
    $('update').hidden=!latest||QRCore.compareVersions(latest.version,api.runtime.getManifest().version)<=0;
  }
  document.addEventListener('qr:locale',()=>{setType($('type').value,false);if(qr)$('preview-caption').textContent=t('ready');});
  setType('url',false);
  if(!popup){$('content').value='https://qr.haking.tr/';generate();$('preview-caption').textContent=t('sample');}
})();
