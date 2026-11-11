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
    prepare_edge_copy()
    (destination/'release.json').write_text(json.dumps({'version':version,'package':name,'sha256':digest,'source':source.relative_to(ROOT).as_posix(),'automatic_publication':False},indent=2),encoding='utf-8')
    print(f'Prepared local Edge package: edge/{name} (not published)')

def prepare_edge_copy():
    destination=ROOT/'edge';destination.mkdir(exist_ok=True)
    locales=json.loads((ROOT/'shared/locales.json').read_text(encoding='utf-8'))
    descriptions_by_language=json.loads((ROOT/'tools/store-descriptions.json').read_text(encoding='utf-8'))
    assert set(descriptions_by_language)==set(locales)
    for language in locales:
        description=descriptions_by_language[language]
        descriptions=destination/'descriptions';descriptions.mkdir(exist_ok=True)
        (descriptions/f'{language}.txt').write_text(description,encoding='utf-8')
        fields=destination/'privacy-forms';fields.mkdir(exist_ok=True)
        chrome_copy=ROOT/'chrome/privacy-forms'/f'{language}.txt'
        if chrome_copy.exists():shutil.copy2(chrome_copy,fields/f'{language}.txt')
    print(f'Prepared {len(locales)} Edge descriptions/privacy files; packages unchanged.')

if __name__=='__main__':
    prepare_edge()
