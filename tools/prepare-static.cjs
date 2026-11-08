// Package committed, verified static output for the existing Cloudflare Worker build.
// No Python or generated source code execution is required on the hosting provider.
const fs=require('node:fs');
const path=require('node:path');
const root=path.resolve(__dirname,'..'),out=path.join(root,'dist');
fs.mkdirSync(out,{recursive:true});
const files=['index.html','about.html','privacy.html','help.html','404.html','style.css','robots.txt','sitemap.xml','version.json','_headers'];
const directories=['assets','vendor','shared','downloads','tr','en','de','es','fr','pt'];
for(const name of [...files,...directories])fs.cpSync(path.join(root,name),path.join(out,name),{recursive:true});
console.log('Prepared dist/ for the existing qr Worker.');
