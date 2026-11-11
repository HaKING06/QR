from pathlib import Path
import json,zipfile,hashlib,re,struct
R=Path(__file__).resolve().parents[1]
version=json.loads((R/'package.json').read_text(encoding='utf-8'))['version']
locales=json.loads((R/'shared/locales.json').read_text(encoding='utf-8'))
store_copy=json.loads((R/'tools/store-descriptions.json').read_text(encoding='utf-8'))
assert set(store_copy)==set(locales),'Every store language needs edited description copy'
for lang,description in store_copy.items():
 paragraphs=description.split('\n\n')
 assert 250<=len(description)<=4000,(lang,'Invalid description length')
 bare_types=', '.join(locales[lang][key] for key in ['url','text','wifi','email','phone','sms','vcard'])+'.'
 assert bare_types not in description,(lang,'Yellow Argon: standalone keyword enumeration')
 assert all(p.replace('،',',').count(',')<4 or len(p)>200 for p in paragraphs),(lang,'Check keyword-list formatting')
 assert all('{{' not in p and '}}' not in p for p in paragraphs),(lang,'Unrendered store copy')
for lang,d in locales.items():
 assert set(d)==set(locales['en']),lang
 for page in ['index','about','help','privacy','updates']:
  p=R/lang/(page+'.html');s=p.read_text(encoding='utf-8');assert '{{' not in s,str(p)
  assert f'lang="{lang}"' in s
  assert f'dir="{"rtl" if lang=="ar" else "ltr"}"' in s
  for asset in re.findall(r'(?:src|href)="(/(?:assets|vendor|shared)/[^"]+)"',s):assert (R/asset[1:]).is_file(),asset
for path in (R/'downloads').glob('*.zip'):
 with zipfile.ZipFile(path) as z:
  m=json.loads(z.read('manifest.json'));assert m['version']==version
  assert set(m['permissions'])=={'activeTab','storage'}
  assert m['optional_permissions']==['notifications']
  assert 'background.js' in z.namelist()
  assert ('scripts' in m['background']) if 'firefox' in path.name else ('service_worker' in m['background'])
  assert m['action']['default_popup'] in z.namelist()
  assert all(v in z.namelist() for v in m['icons'].values())
  assert 'LICENSE' in z.namelist() and 'vendor/jsQR-LICENSE.txt' in z.namelist()
  assert 'popup.css' in z.namelist() and 'style.css' not in z.namelist()
for line in (R/'downloads/SHA256SUMS.txt').read_text().splitlines():
 digest,name=line.split();assert hashlib.sha256((R/'downloads'/name).read_bytes()).hexdigest()==digest
edge=R/'edge'
edge_release=json.loads((edge/'release.json').read_text(encoding='utf-8'))
assert edge_release['version']==version
assert hashlib.sha256((edge/edge_release['package']).read_bytes()).hexdigest()==edge_release['sha256']
assert (edge/edge_release['package']).read_bytes()==(R/'downloads'/f'qr-scanner-{version}-chromium.zip').read_bytes()
for name,size in [('logo-300x300.png',(300,300)),('small-promo-440x280.png',(440,280)),('large-promo-1400x560.png',(1400,560))]:
 assert struct.unpack('>II',(edge/name).read_bytes()[16:24])==size,name
chrome=R/'chrome'
chrome_release=json.loads((chrome/'release.json').read_text(encoding='utf-8'))
assert chrome_release['version']==version
assert hashlib.sha256((chrome/chrome_release['package']).read_bytes()).hexdigest()==chrome_release['sha256']
with zipfile.ZipFile(chrome/chrome_release['package']) as zipped, zipfile.ZipFile(R/'downloads'/f'qr-scanner-{version}-chromium.zip') as original:
 manifest=json.loads(zipped.read('manifest.json'))
 assert manifest['version']==version and manifest['manifest_version']==3
 icon=manifest['icons']['128']
 assert set(zipped.namelist())==set(original.namelist())
 assert zipped.read(icon)==(chrome/'store-icon-128x128.png').read_bytes()
 assert all(zipped.read(name)==original.read(name) for name in zipped.namelist() if name!=icon)
for name,size in [('store-icon-128x128.png',(128,128)),('small-promo-440x280.png',(440,280)),('marquee-1400x560.png',(1400,560))]:
 assert struct.unpack('>II',(chrome/name).read_bytes()[16:24])==size,name
for lang in locales:
 assert (chrome/'privacy-forms'/f'{lang}.txt').is_file()
 assert (edge/'descriptions'/f'{lang}.txt').is_file()
 assert (chrome/'descriptions'/f'{lang}.txt').is_file()
 for store in [chrome,edge]:
  assert (store/'descriptions'/f'{lang}.txt').read_text(encoding='utf-8')==store_copy[lang],(store,lang,'Stale store description')
 for mode in ['01-reader','02-generator']:
  assert struct.unpack('>II',(chrome/'screenshots'/lang/f'{mode}-1280x800.png').read_bytes()[16:24])==(1280,800)
  assert struct.unpack('>II',(edge/'screenshots'/lang/f'{mode}-1280x800.png').read_bytes()[16:24])==(1280,800)
 if not json.loads((R/'store-links.json').read_text())['chrome']:
  assert 'data-store="chrome"' not in (R/lang/'index.html').read_text(encoding='utf-8')
assert set(locales)=={'en','tr','de','es','fr','pt','ru','ar'}
assert json.loads((R/'version.json').read_text())['version']==version
for store in [chrome,edge]:
 assert json.loads((store/'screenshots/release.json').read_text())['version']==version
print(f'Validated {len(locales)} languages, HTML assets, browser ZIPs, both store handoffs and SHA-256 checksums.')
