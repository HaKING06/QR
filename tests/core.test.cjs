const {test}=require('node:test');
const assert=require('node:assert/strict');
const core=require('../shared/core.js');
const qrcode=require('qrcode-generator');
const jsQR=require('jsqr');
test('version comparisons are numeric and reject malformed releases',()=>{
 assert.equal(core.compareVersions('1.1.1','1.1.0'),1);
 assert.equal(core.compareVersions('1.1.1','1.1.1'),0);
 assert.equal(core.compareVersions('1.0.1','1.1.0'),-1);
 assert.equal(core.compareVersions('1.10.0','1.9.9'),1);
 assert.equal(core.compareVersions('broken','1.1.0'),0);
});
test('payload validation and escaping',()=>{
 assert.equal(core.payload('url',{text:'example.com'}),'https://example.com/');
 assert.throws(()=>core.payload('url',{text:'javascript:alert(1)'}));
 assert.throws(()=>core.payload('email',{text:'invalid'}));
 assert.equal(core.payload('wifi',{text:'office;net',password:'x:y\\z'}),'WIFI:T:WPA;S:office\\;net;P:x\\:y\\\\z;H:false;;');
 assert.equal(core.payload('email',{text:'a@example.com',subject:'Hello & you'}),'mailto:a@example.com?subject=Hello%20%26%20you');
 assert.equal(core.safeLink('javascript:alert(1)'),null);
 assert.equal(core.safeLink('data:text/html,test'),null);
 assert.equal(core.safeLink('https://example.com'),'https://example.com/');
});
test('UTF-8 QR round-trips through the actual decoder with a quiet zone',()=>{
 qrcode.stringToBytes=qrcode.stringToBytesFuncs['UTF-8'];
 for(const value of ['https://qr.haking.tr/','Türkçe: ıİşğüöç — 日本語 😀','WIFI:T:WPA;S:Office;P:secret;;']){
  const qr=qrcode(0,'M');qr.addData(value);qr.make();const n=qr.getModuleCount(),scale=6,w=(n+8)*scale,data=new Uint8ClampedArray(w*w*4);data.fill(255);
  for(let y=0;y<n;y++)for(let x=0;x<n;x++)if(qr.isDark(y,x))for(let dy=0;dy<scale;dy++)for(let dx=0;dx<scale;dx++){const p=(((y+4)*scale+dy)*w+(x+4)*scale+dx)*4;data[p]=data[p+1]=data[p+2]=0;}
  assert.equal(jsQR(data,w,w)?.data,value);
 }
});
