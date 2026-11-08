from pathlib import Path
import json,zipfile,hashlib,re,struct
R=Path(__file__).resolve().parents[1]
version=json.loads((R/'package.json').read_text(encoding='utf-8'))['version']
locales=json.loads((R/'shared/locales.json').read_text(encoding='utf-8'))
for lang,d in locales.items():
 assert set(d)==set(locales['en']),lang
 for page in ['index','about','help','privacy']:
  p=R/lang/(page+'.html');s=p.read_text(encoding='utf-8');assert '{{' not in s,str(p)
  assert f'lang="{lang}"' in s
  for asset in re.findall(r'(?:src|href)="(/(?:assets|vendor|shared)/[^"]+)"',s):assert (R/asset[1:]).is_file(),asset
for path in (R/'downloads').glob('*.zip'):
 with zipfile.ZipFile(path) as z:
  m=json.loads(z.read('manifest.json'));assert m['version']==version
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
print(f'Validated {len(locales)} languages, HTML assets, release ZIPs, Edge store assets and SHA-256 checksums.')
