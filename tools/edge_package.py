"""Prepare the local Edge handoff folder without publishing anything."""
from pathlib import Path
import hashlib
import json
import shutil
import zipfile

ROOT=Path(__file__).resolve().parents[1]

def prepare_edge():
    version=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))['version']
    source=ROOT/'downloads'/f'qr-scanner-{version}-chromium.zip'
    with zipfile.ZipFile(source) as archive:
        manifest=json.loads(archive.read('manifest.json'))
        assert manifest['version']==version,'Package version differs from package.json'
        assert manifest['action']['default_popup'] in archive.namelist()
        assert all(path in archive.namelist() for path in manifest['icons'].values())
    destination=(ROOT/'edge').resolve()
    assert destination.is_relative_to(ROOT) and destination!=ROOT
    destination.mkdir(exist_ok=True)
    name=f'qr-scanner-{version}-edge.zip'
    for previous in destination.glob('qr-scanner-*-edge.zip'):
        if previous.name!=name:previous.unlink()
    shutil.copy2(source,destination/name)
    digest=hashlib.sha256((destination/name).read_bytes()).hexdigest()
    (destination/'SHA256SUMS.txt').write_text(f'{digest}  {name}\n',encoding='utf-8')
    locales=json.loads((ROOT/'shared/locales.json').read_text(encoding='utf-8'))
    listings=destination/'store-listings';listings.mkdir(exist_ok=True)
    for language,strings in locales.items():
        types=', '.join(strings[key] for key in ['url','text','wifi','email','phone','sms','vcard'])
        description='\n\n'.join([strings['extensionDesc'],types+'.',strings['currentTab']+'. '+strings['screenshot']+'.',strings['exportDesc'],strings['noExpiryDesc'],strings['privacyDesc'],strings['linkNote']])
        assert 250<=len(description)<=10000
        content=f'QR Scanner — v{version}\n\nName: QR Scanner\n\nShort description:\n{strings["extensionDesc"]}\n\nDescription:\n{description}\n\nWebsite: https://qr.haking.tr/\nPrivacy policy: https://qr.haking.tr/{language}/privacy.html\nSupport: qr@haking.tr\n'
        (listings/f'{language}.txt').write_text(content,encoding='utf-8')
    (destination/'release.json').write_text(json.dumps({'version':version,'package':name,'sha256':digest,'source':source.relative_to(ROOT).as_posix(),'automatic_publication':False},indent=2),encoding='utf-8')
    print(f'Prepared local Edge package: edge/{name} (not published)')

if __name__=='__main__':prepare_edge()
