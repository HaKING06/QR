"""Build localized HTML and clean browser packages from shared sources."""
from pathlib import Path
import hashlib,html,json,shutil,zipfile
from urllib.parse import urlparse
import templates as ui
from edge_package import prepare_edge
from chrome_package import prepare_chrome
from experience import updates as update_page
ROOT=Path(__file__).resolve().parents[1]
VERSION=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))['version']
LOCALES=json.loads((ROOT/'shared/locales.json').read_text(encoding='utf-8'))
RELEASE=json.loads((ROOT/'release-notes.json').read_text(encoding='utf-8'))
DATE=RELEASE['date']
EDGE='https://microsoftedge.microsoft.com/addons/detail/qr-scanner/klblmhlgnbnclpdhddadkbbccmdjknmf'
STORE_LINKS=json.loads((ROOT/'store-links.json').read_text(encoding='utf-8'))
CHROME=STORE_LINKS.get('chrome')
if CHROME:
    parsed=urlparse(CHROME)
    assert parsed.scheme=='https' and parsed.netloc=='chromewebstore.google.com' and parsed.path.startswith('/detail/'),'Use the real Chrome Web Store listing URL'
    import re
    assert re.fullmatch(r'[a-p]{32}',parsed.path.rstrip('/').split('/')[-1]),'Chrome listing must include its actual extension ID'

def render(source,language):
    for key,value in LOCALES[language].items():
        source=source.replace('{{'+key+'}}',html.escape(value))
    return source

def scripts(prefix='/'):
    files=['vendor/qrcode.js','vendor/jsQR.js','shared/core.js','shared/update-core.js','shared/i18n.js','shared/app.js','shared/site.js']
    if prefix=='/':files.append('shared/experience.js')
    return '\n'.join(f'<script src="{prefix}{path}" defer></script>' for path in files)

def build_site():
    urls=['https://qr.haking.tr/']
    for language,dictionary in LOCALES.items():
        folder=ROOT/language;folder.mkdir(exist_ok=True)
        for page in ['index','about','privacy','help','updates']:
            path='' if page=='index' else page+'.html'
            canonical=f'https://qr.haking.tr/{language}/{path}'
            title=dictionary['create']+' & '+dictionary['navRead'] if page=='index' else dictionary[{'about':'navAbout','privacy':'privacy','help':'helpTitle','updates':'updates'}[page]]
            title+=' — QR Scanner'
            description=(dictionary['subtitle']+' '+dictionary['extensionDesc']) if page=='index' else dictionary[{'about':'aboutDesc','privacy':'privacyDesc','help':'installIntro','updates':'updateIntro'}[page]]
            alternates=''.join(f'<link rel="alternate" hreflang="{lang}" href="https://qr.haking.tr/{lang}/{path}">' for lang in LOCALES)
            alternates+=f'<link rel="alternate" hreflang="x-default" href="https://qr.haking.tr/{path}">'
            schema={'@context':'https://schema.org','@type':'WebApplication' if page=='index' else 'WebPage','name':'QR Scanner','url':canonical,'inLanguage':language,'description':description,'author':{'@type':'Person','name':'Halit (HaKING)','url':'https://haking.tr/'}}
            if page=='index':schema.update(applicationCategory='UtilitiesApplication',operatingSystem='Any',offers={'@type':'Offer','price':'0','priceCurrency':'USD'})
            body={'index':lambda:ui.home(VERSION,EDGE,CHROME),'about':lambda:ui.about(VERSION),'help':lambda:ui.guide(VERSION),'privacy':lambda:ui.privacy(VERSION),'updates':lambda:update_page(VERSION,DATE)}[page]()
            source=f'''<!doctype html>
<html lang="{language}" dir="{'rtl' if language=='ar' else 'ltr'}" data-page="{page}" data-version="{VERSION}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(description,quote=True)}">
<link rel="canonical" href="{canonical}">{alternates}<meta name="theme-color" content="#4864ff">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title,quote=True)}">
<meta property="og:description" content="{html.escape(description,quote=True)}"><meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://qr.haking.tr/assets/brand/social-card.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/brand/favicon.ico"><link rel="icon" type="image/svg+xml" href="/assets/brand/logo.svg">
<link rel="apple-touch-icon" href="/assets/brand/icon-192.png"><link rel="stylesheet" href="/shared/ui.css"><link rel="stylesheet" href="/style.css"><link rel="stylesheet" href="/experience.css">
<script src="/shared/preferences.js"></script><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
</head><body>{ui.header()}{body}{ui.footer(VERSION)}<p id="status" role="status" aria-live="polite"></p>{scripts()}</body></html>'''
            output=render(source,language);(folder/(page+'.html')).write_text(output,encoding='utf-8');urls.append(canonical)
            if language=='tr':(ROOT/(page+'.html')).write_text(output.replace(f'href="{canonical}"',f'href="https://qr.haking.tr/{path}"',1),encoding='utf-8')
    sitemap='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    sitemap+=''.join(f'<url><loc>{url}</loc><lastmod>{DATE}</lastmod></url>' for url in urls)+'</urlset>'
    (ROOT/'sitemap.xml').write_text(sitemap,encoding='utf-8')

def build_extension():
    extension=(ROOT/'extension').resolve()
    assert extension.is_relative_to(ROOT) and extension!=ROOT,str(extension)
    if extension.exists():shutil.rmtree(extension)
    extension.mkdir()
    for folder in ['shared','vendor']:shutil.copytree(ROOT/folder,extension/folder)
    brand=extension/'assets/brand';brand.mkdir(parents=True)
    for name in ['logo.svg']+[f'icon-{size}.png' for size in [16,32,48,128]]:shutil.copy2(ROOT/'assets/brand'/name,brand/name)
    shutil.copy2(ROOT/'popup.css',extension/'popup.css')
    shutil.copy2(ROOT/'background.js',extension/'background.js')
    popup=f'''<!doctype html><html lang="en" data-extension="true" data-version="{VERSION}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>QR Scanner</title><link rel="stylesheet" href="shared/ui.css">
<link rel="stylesheet" href="popup.css"><script src="shared/preferences.js"></script></head><body>{ui.popup(VERSION)}{scripts('')}</body></html>'''
    (extension/'popup.html').write_text(render(popup,'en'),encoding='utf-8')
    icons={str(size):f'assets/brand/icon-{size}.png' for size in [16,32,48,128]}
    manifest={'manifest_version':3,'name':'__MSG_extensionName__','description':'__MSG_extensionDescription__','default_locale':'en','version':VERSION,'homepage_url':'https://qr.haking.tr/','permissions':['activeTab','storage'],'optional_permissions':['notifications'],'background':{'service_worker':'background.js'},'host_permissions':['https://qr.haking.tr/*'],'icons':icons,'action':{'default_popup':'popup.html','default_title':'QR Scanner','default_icon':icons},'content_security_policy':{'extension_pages':"script-src 'self'; object-src 'self'"}}
    for language,dictionary in LOCALES.items():
        target=extension/'_locales'/language;target.mkdir(parents=True)
        messages={'extensionName':{'message':'QR Scanner — '+dictionary['navRead']+' & '+dictionary['navCreate']},'extensionDescription':{'message':dictionary['extensionDesc']}}
        messages['notificationInstalled']={'message':dictionary['updatedTitle']+' · {version}'}
        messages['notificationAvailable']={'message':dictionary['notificationTitle']}
        messages['notificationBody']={'message':dictionary['notificationBody']}
        (target/'messages.json').write_text(json.dumps(messages,ensure_ascii=False,indent=2),encoding='utf-8')
    (extension/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    downloads=ROOT/'downloads';downloads.mkdir(exist_ok=True);hashes={}
    for old in downloads.glob('qr-scanner-*.zip'):old.unlink()
    for browser in ['chromium','firefox']:
        browser_manifest=dict(manifest)
        if browser=='firefox':
            browser_manifest['background']={'scripts':['shared/core.js','shared/update-core.js','background.js']}
            browser_manifest['browser_specific_settings']={'gecko':{'id':'qr-scanner@haking.tr','strict_min_version':'142.0','data_collection_permissions':{'required':['none']}}}
        name=f'qr-scanner-{VERSION}-{browser}.zip'
        with zipfile.ZipFile(downloads/name,'w',zipfile.ZIP_DEFLATED) as archive:
            for source in sorted(extension.rglob('*')):
                if source.is_file() and source.name!='manifest.json':archive.write(source,source.relative_to(extension).as_posix())
            archive.writestr('manifest.json',json.dumps(browser_manifest,indent=2))
            for license_name in ['LICENSE','THIRD_PARTY_NOTICES.md']:archive.write(ROOT/license_name,license_name)
        hashes[name]=hashlib.sha256((downloads/name).read_bytes()).hexdigest()
    (downloads/'SHA256SUMS.txt').write_text(''.join(f'{digest}  {name}\n' for name,digest in hashes.items()),encoding='utf-8')
    (ROOT/'version.json').write_text(json.dumps({'version':VERSION,'released':DATE,'url':f'https://qr.haking.tr/updates.html?version={VERSION}','downloads':hashes},indent=2),encoding='utf-8')

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--site-only',action='store_true',help='Render website without changing extension/store packages')
    arguments=parser.parse_args()
    build_site()
    if arguments.site_only:print('Built website only; extension packages unchanged.')
    else:
        build_extension();prepare_chrome();prepare_edge();print('Built localized site and browser packages v'+VERSION)
