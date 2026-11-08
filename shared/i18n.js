window.QRI18n = (async () => {
  const res=await fetch(new URL('locales.json',document.currentScript.src));
  if (!res.ok) throw new Error('Translations unavailable');
  const locales=await res.json();
  const stored=(()=>{try{return localStorage.getItem('qr-language')||'auto';}catch{return 'auto';}})();
  const segment=location.pathname.split('/')[1];
  const preferred=(navigator.languages||[navigator.language]).map(x=>x.split('-')[0]).find(x=>locales[x])||'en';
  const lang=locales[segment]?segment:(locales[stored]?stored:preferred);
  // Localized pages are real HTML so search engines can index each language.
  if (!globalThis.chrome?.runtime?.id && !globalThis.browser?.runtime?.id && !locales[segment] && lang!=='tr') {
    const page=location.pathname.split('/').pop()||'';
    location.replace('/'+lang+'/'+page+location.search+location.hash);
  }
  const t=k=>locales[lang][k]||locales.en[k]||k;
  document.documentElement.lang=lang;
  document.querySelectorAll('[data-i18n]').forEach(el=>{el.textContent=t(el.dataset.i18n);});
  const select=document.getElementById('language');
  if(select){select.value=locales[segment]?lang:stored;select.onchange=()=>{
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
  return {t,lang};
})();
