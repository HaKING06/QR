window.QRI18n = (async () => {
  const localeURL=new URL('locales.json',document.currentScript.src);
  const supported=new Set(['tr','en','de','es','fr','pt']);
  const stored=(()=>{try{return localStorage.getItem('qr-language')||'auto';}catch{return 'auto';}})();
  const segment=location.pathname.split('/')[1];
  const preferred=(navigator.languages||[navigator.language]).map(x=>x.split('-')[0]).find(x=>supported.has(x))||'en';
  const lang=supported.has(segment)?segment:(supported.has(stored)?stored:preferred);
  // Localized pages are real HTML so search engines can index each language.
  if (!globalThis.chrome?.runtime?.id && !globalThis.browser?.runtime?.id && !supported.has(segment) && lang!=='tr') {
    const page=location.pathname.split('/').pop()||'';
    location.replace('/'+lang+'/'+page+location.search+location.hash);
  }
  document.documentElement.lang=lang;
  const select=document.getElementById('language');
  if(select){select.value=supported.has(segment)?lang:stored;select.onchange=()=>{
    try {localStorage.setItem('qr-language',select.value);}catch{}
    if(globalThis.chrome?.runtime?.id||globalThis.browser?.runtime?.id)location.reload();
    else {const next=select.value==='auto'?preferred:select.value;const page=location.pathname.split('/').pop()||'';location.assign('/'+next+'/'+page+location.search+location.hash);}
  };}
  const theme=document.getElementById('theme');
  if(theme){try{theme.value=localStorage.getItem('qr-theme')||'auto';}catch{}
    const apply=()=>{const value=theme.value;document.documentElement.dataset.theme=value==='auto'?(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'):value;};
    theme.onchange=()=>{try{localStorage.setItem('qr-theme',theme.value);}catch{}apply();};
    matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(theme.value==='auto')apply();});
  }
  const res=await fetch(localeURL);
  if (!res.ok) throw new Error('Translations unavailable');
  const locales=await res.json();
  const t=k=>locales[lang][k]||locales.en[k]||k;
  document.querySelectorAll('[data-i18n]').forEach(el=>{el.textContent=t(el.dataset.i18n);});
  return {t,lang};
})();
