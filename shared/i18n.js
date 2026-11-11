(() => {
  'use strict';
  const localeURL=new URL('locales.json',document.currentScript.src);
  const languages=['tr','en','de','es','fr','pt','ru','ar'];
  const popup=document.documentElement.dataset.extension==='true';
  const read=(key,fallback)=>{try{return localStorage.getItem(key)||fallback;}catch{return fallback;}};
  const save=(key,value)=>{try{localStorage.setItem(key,value);}catch{}};
  const preferred=(navigator.languages||[navigator.language]).map(value=>value.split('-')[0]).find(value=>languages.includes(value))||'en';
  const segment=location.pathname.split('/')[1];
  let choice=read('qr-language','auto');
  if(!['auto',...languages].includes(choice))choice='auto';
  let language=!popup&&languages.includes(segment)?segment:choice==='auto'?preferred:choice;
  let theme=read('qr-theme','auto'), dictionaries=null;
  if(!['auto','light','dark'].includes(theme))theme='auto';
  const fallback={empty:'Enter your content first.',invalid:'Please check your content.',tooLong:'Content is too long for a QR code.',ready:'Your QR is ready.',copied:'Copied.',copyError:'Copy unavailable. Try downloading instead.',notFound:'No QR code found. Try a clearer image.',badFile:'Choose a PNG, JPEG or WebP image up to 15 MB.',fileError:'The image could not be read.',scanning:'Reading image…',cameraError:'Camera unavailable. Check permission.',screenError:'This tab cannot be captured.',engineError:'The QR engine could not load. Reopen the page or extension.'};
  const text=key=>dictionaries?.[language]?.[key]||dictionaries?.en?.[key]||document.querySelector(`[data-i18n="${key}"]`)?.textContent||fallback[key]||key;
  window.QRText=text;

  function translate(){
    document.documentElement.lang=language;
    document.documentElement.dir=language==='ar'?'rtl':'ltr';
    if(dictionaries)document.querySelectorAll('[data-i18n]').forEach(node=>{node.textContent=text(node.dataset.i18n);});
    document.querySelectorAll('[data-language]').forEach(button=>button.setAttribute('aria-checked',String(button.dataset.language===(popup?choice:language))));
    const label=document.getElementById('language-label');
    if(label)label.textContent=language.toUpperCase();
    mirrorPreferences();
    document.dispatchEvent(new CustomEvent('qr:locale',{detail:{language}}));
  }
  function applyTheme(){
    document.documentElement.dataset.theme=theme==='auto'?(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'):theme;
    document.querySelectorAll('[data-theme-choice]').forEach(button=>button.setAttribute('aria-checked',String(button.dataset.themeChoice===theme)));
    const glyph=document.querySelector(`[data-theme-choice="${theme}"]>.icon`);
    if(glyph)document.getElementById('theme-icon')?.replaceChildren(glyph.cloneNode(true));
    mirrorPreferences();
  }
  function mirrorPreferences(){
    const api=globalThis.browser||globalThis.chrome;
    if(popup&&api?.runtime?.id&&api.storage?.local)api.storage.local.set({preferences:{language:choice,theme}}).catch(()=>{});
  }
  function closeMenus(){document.querySelectorAll('.pref-menu').forEach(menu=>{menu.open=false;});}
  document.querySelectorAll('[data-language]').forEach(button=>button.addEventListener('click',()=>{
    choice=button.dataset.language;save('qr-language',choice);language=choice==='auto'?preferred:choice;closeMenus();
    if(popup){translate();return;}
    const parts=location.pathname.split('/').filter(Boolean);
    if(languages.includes(parts[0]))parts.shift();
    location.assign('/'+language+'/'+parts.join('/')+location.search+location.hash);
  }));
  document.querySelectorAll('[data-theme-choice]').forEach(button=>button.addEventListener('click',()=>{theme=button.dataset.themeChoice;save('qr-theme',theme);applyTheme();closeMenus();}));
  document.querySelectorAll('.pref-menu').forEach(menu=>menu.addEventListener('toggle',()=>{if(menu.open)document.querySelectorAll('.pref-menu').forEach(other=>{if(other!==menu)other.open=false;});}));
  document.addEventListener('click',event=>{if(!event.target.closest('.pref-menu'))closeMenus();});
  document.addEventListener('keydown',event=>{
    if(event.key==='Escape'){const menu=document.querySelector('.pref-menu[open]');closeMenus();menu?.querySelector('summary').focus();}
    if(['ArrowDown','ArrowUp'].includes(event.key)&&event.target.closest('.pref-options')){
      const buttons=[...event.target.closest('.pref-options').querySelectorAll('button')];const index=buttons.indexOf(event.target);buttons[(index+(event.key==='ArrowDown'?1:-1)+buttons.length)%buttons.length].focus();event.preventDefault();
    }
  });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(theme==='auto')applyTheme();});
  applyTheme();translate();
  if(!popup&&!languages.includes(segment)&&language!=='tr')location.replace('/'+language+location.pathname+location.search+location.hash);
  window.QRI18n=fetch(localeURL).then(response=>{if(!response.ok)throw new Error('Translations unavailable');return response.json();}).then(value=>{dictionaries=value;translate();return {t:text,lang:language};}).catch(()=>({t:text,lang:language}));
})();
