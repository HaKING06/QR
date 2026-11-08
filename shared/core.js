(function (root) {
  'use strict';
  function payload(type, values) {
    const text = (values.text || '').trim();
    if (type === 'wifi') {
      const escape = s => String(s || '').replace(/([\\;,:\"])/g, '\\$1');
      if (!text) throw new Error('empty');
      return `WIFI:T:${values.security || 'WPA'};S:${escape(text)};P:${escape(values.password)};H:false;;`;
    }
    if (!text) throw new Error('empty');
    if (type === 'url') {
      const url = new URL(/^https?:\/\//i.test(text) ? text : 'https://' + text);
      if (!['http:', 'https:'].includes(url.protocol) || !url.hostname.includes('.')) throw new Error('invalid');
      return url.href;
    }
    if (type === 'email') {
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(text)) throw new Error('invalid');
      return 'mailto:' + text + '?subject=' + encodeURIComponent(values.subject || '');
    }
    return text;
  }
  function compareVersions(a, b) {
    if (![a,b].every(v => /^\d+\.\d+\.\d+$/.test(v))) return 0;
    const x=a.split('.').map(Number), y=b.split('.').map(Number);
    for (let i=0;i<3;i++) if (x[i]!==y[i]) return x[i]>y[i]?1:-1;
    return 0;
  }
  function safeLink(value) {
    try { const u=new URL(value); return ['https:','http:'].includes(u.protocol)?u.href:null; } catch { return null; }
  }
  const api={payload,compareVersions,safeLink};
  if (typeof module !== 'undefined') module.exports=api;
  root.QRCore=api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
