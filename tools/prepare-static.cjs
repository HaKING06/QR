// Package committed, verified static output for the existing Cloudflare Worker build.
// No Python or generated source code execution is required on the hosting provider.
const fs=require('node:fs');
const path=require('node:path');
const root=path.resolve(__dirname,'..'),out=path.join(root,'dist');
if(!out.startsWith(root+path.sep))throw new Error('Output escaped repository');
fs.rmSync(out,{recursive:true,force:true});
fs.mkdirSync(out,{recursive:true});
const files=['index.html','about.html','privacy.html','help.html','updates.html','404.html','style.css','experience.css','robots.txt','sitemap.xml','version.json','_headers','LICENSE','THIRD_PARTY_NOTICES.md'];
const directories=['assets','vendor','shared','downloads','tr','en','de','es','fr','pt','ru','ar'];
for(const name of [...files,...directories])fs.cpSync(path.join(root,name),path.join(out,name),{recursive:true});
// Brand production exports only; source scripts and rejected explorations stay out of hosting.
for(const name of fs.readdirSync(path.join(out,'assets','brand'))){
 if(name.endsWith('.py')||name.endsWith('.md')||name.includes('generated'))fs.unlinkSync(path.join(out,'assets','brand',name));
}
console.log('Prepared dist/ for the existing qr Worker.');
