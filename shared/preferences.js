(() => {
  try {
    const theme=localStorage.getItem('qr-theme') || 'auto';
    document.documentElement.dataset.theme=theme==='auto'?(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'):theme;
  } catch { /* System theme remains available through CSS. */ }
})();
