(function (root) {
  'use strict';
  function payload(type, values) {
    const text = (values.text || '').trim();
    if (type === 'wifi') {
      const escape = s => String(s || '').replace(/([\\;,:\"])/g, '\\$1');
      if (!text) throw new Error('empty');
      const security=['WPA','WEP','nopass'].includes(values.security)?values.security:'WPA';
      return `WIFI:T:${security};S:${escape(text)};P:${security==='nopass'?'':escape(values.password)};H:${values.hidden?'true':'false'};;`;
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
    if (type === 'phone' || type === 'sms') {
      if (!/^\+?[\d\s().-]{3,40}$/.test(text)) throw new Error('invalid');
      const phone=text.replace(/[\s().-]/g,'');
      if (!/^\+?\d{3,20}$/.test(phone)) throw new Error('invalid');
      return type==='phone'?'tel:'+phone:'SMSTO:'+phone+':'+(values.message||'');
    }
    if (type === 'vcard') {
      const escape=s=>String(s||'').replace(/\\/g,'\\\\').replace(/\r?\n/g,'\\n').replace(/;/g,'\\;').replace(/,/g,'\\,');
      if (values.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(values.email)) throw new Error('invalid');
      return ['BEGIN:VCARD','VERSION:3.0','FN:'+escape(text),'N:;'+escape(text)+';;;','ORG:'+escape(values.organization),'TEL:'+escape(values.phone),'EMAIL:'+escape(values.email),'END:VCARD'].join('\r\n');
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
