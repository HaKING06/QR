(() => {
  'use strict';
  if(document.documentElement.dataset.extension==='true')return;
  const root=document.documentElement;
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  const story=document.querySelector('[data-scroll-story]');
  const scenes=[...document.querySelectorAll('[data-story-scene]')];
  const controls=[...document.querySelectorAll('[data-story-goto]')];
  let scheduled=false,current=-1;
  function paint(){
    scheduled=false;
    const range=Math.max(1,root.scrollHeight-innerHeight);
    root.style.setProperty('--scroll-progress',String(Math.min(1,Math.max(0,scrollY/range))));
    const header=document.querySelector('.site-header');
    const headerHeight=header?.getBoundingClientRect().height||86;
    root.style.setProperty('--header-height',headerHeight+'px');
    if(!story||reduced.matches)return;
    const rect=story.getBoundingClientRect();
    const progress=Math.min(1,Math.max(0,(headerHeight+12-rect.top)/Math.max(1,rect.height-innerHeight+headerHeight+24)));
    story.style.setProperty('--story-progress',String(progress));
    const index=Math.min(2,Math.floor(progress*3));
    if(index===current)return;current=index;
    scenes.forEach((scene,i)=>{scene.classList.toggle('is-active',i===index);scene.setAttribute('aria-hidden',String(i!==index));});
    controls.forEach((button,i)=>button.setAttribute('aria-pressed',String(i===index)));
    const number=document.querySelector('[data-story-number]');if(number)number.textContent='0'+(index+1);
  }
  const schedule=()=>{if(!scheduled){scheduled=true;requestAnimationFrame(paint);}};
  function motionMode(){
    root.classList.toggle('motion-ready',!reduced.matches);
    if(reduced.matches)scenes.forEach(scene=>scene.removeAttribute('aria-hidden'));
    current=-1;schedule();
  }
  controls.forEach(button=>button.onclick=()=>{
    if(!story)return;const top=story.getBoundingClientRect().top+scrollY;
    const header=document.querySelector('.site-header')?.offsetHeight||86;
    const travel=Math.max(1,story.offsetHeight-innerHeight+header+24);
    const fraction=(Number(button.dataset.storyGoto)+.35)/3;
    scrollTo({top:Math.max(0,top-header-12+travel*fraction),behavior:reduced.matches?'instant':'smooth'});
  });
  const revealed=[...document.querySelectorAll('.benefit-strip>div,.browser-card,.about-values>article,.contact-card,.section-heading,[data-reveal]')];
  if('IntersectionObserver' in window){
    const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');observer.unobserve(entry.target);}}),{rootMargin:'0px 0px 50px 0px',threshold:.08});
    revealed.forEach(element=>{element.dataset.reveal='';observer.observe(element);});
  }else revealed.forEach(element=>element.classList.add('is-visible'));
  addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule,{passive:true});
  reduced.addEventListener('change',motionMode);motionMode();
  if(matchMedia('(pointer:fine)').matches){
    const hero=document.querySelector('.hero');
    hero?.addEventListener('pointermove',event=>{
      if(reduced.matches)return;const rect=hero.getBoundingClientRect();
      hero.style.setProperty('--pointer-x',((event.clientX-rect.left)/rect.width*10-5)+'deg');
      hero.style.setProperty('--pointer-y',((event.clientY-rect.top)/rect.height*-8+4)+'deg');
    },{passive:true});
    hero?.addEventListener('pointerleave',()=>{hero.style.setProperty('--pointer-x','0deg');hero.style.setProperty('--pointer-y','0deg');});
  }

  const dialog=document.getElementById('review-dialog');
  if(!dialog)return;
  const params=new URLSearchParams(location.search),version=root.dataset.version;
  const t=key=>window.QRText?.(key)||key;
  let viewed=false;
  const reviewKey='qr-review-seen-'+version;
  function showReview(){
    if(dialog.open)return;
    try{localStorage.setItem(reviewKey,'1');}catch{}
    viewed=true;dialog.showModal();
  }
  document.getElementById('open-review').onclick=showReview;
  dialog.querySelectorAll('.review-link').forEach(link=>link.addEventListener('click',()=>dialog.close()));
  dialog.addEventListener('click',event=>{if(event.target===dialog)dialog.close();});
  const previous=params.get('previous');
  if(/^\d+\.\d+\.\d+$/.test(previous||'')&&previous!==version){
    document.getElementById('previous-version').textContent='v'+previous;
    document.getElementById('update-transition').hidden=false;
  }
  function releaseCopy(){
    const reason=params.get('reason');
    if(reason==='update')document.getElementById('update-heading').textContent=t('updatedTitle');
    if(reason==='install')document.getElementById('update-heading').textContent=t('installedTitle');
    if(reason==='available')document.getElementById('update-heading').textContent=t('updateAvailable');
  }
  document.addEventListener('qr:locale',releaseCopy);releaseCopy();
  Promise.resolve(window.QRI18n).then(()=>{
    releaseCopy();
    const reason=params.get('reason');
    if(['update','available'].includes(reason)){
      const notice=document.createElement('div');notice.className='release-toast';notice.setAttribute('role','status');
      notice.textContent=(t(reason==='update'?'updateInstalledBody':'notificationTitle')).replace('{version}',version);
      document.body.append(notice);setTimeout(()=>notice.remove(),6000);
    }
    let seen=false;try{seen=localStorage.getItem(reviewKey)==='1';}catch{}
    if(!seen&&params.get('reason')!=='install')setTimeout(()=>{if(!viewed)showReview();},700);
  });
})();
