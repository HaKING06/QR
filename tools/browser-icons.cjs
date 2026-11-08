const fs=require('node:fs'),path=require('node:path');
const icons=require('@fortawesome/free-brands-svg-icons');
const root=path.resolve(__dirname,'..','assets','browsers');fs.mkdirSync(root,{recursive:true});
const names={chrome:'faChrome',edge:'faEdge',firefox:'faFirefoxBrowser',brave:'faBrave',opera:'faOpera'};
const colors={chrome:'#4864ff',edge:'#1688a6',firefox:'#f07932',brave:'#ed632a',opera:'#e94d66'};
for(const [name,key]of Object.entries(names)){
 const [width,height,,,paths]=icons[key].icon;
 const body=(Array.isArray(paths)?paths:[paths]).map(d=>`<path d="${d}"/>`).join('');
 fs.writeFileSync(path.join(root,name+'.svg'),`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" fill="${colors[name]}">${body}</svg>\n`);
}
console.log('Exported five local Font Awesome browser marks.');
