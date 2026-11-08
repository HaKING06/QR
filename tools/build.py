"""Reproducible static site and Chromium/Firefox release builder. No cloud credentials."""
from pathlib import Path
import json, shutil, zipfile, hashlib, html
R=Path(__file__).resolve().parents[1]
V=json.loads((R/'package.json').read_text(encoding='utf-8'))['version']
L=json.loads((R/'shared/locales.json').read_text(encoding='utf-8'))
EDGE='https://microsoftedge.microsoft.com/addons/detail/qr-scanner/klblmhlgnbnclpdhddadkbbccmdjknmf'
def text(k): return f'<span data-i18n="{k}">{{{{{k}}}}}</span>'
def a(k,href,cls=''): return f'<a class="{cls}" href="{href}">{text(k)}</a>'
def tool():
 return f'''<section class="tool card" id="toolkit" aria-label="QR toolkit">
 <div class="tool-tabs" role="tablist"><button id="create-tab" role="tab" aria-controls="create-panel" aria-selected="true">◧ {text('navCreate')}</button><button id="read-tab" role="tab" aria-controls="read-panel" aria-selected="false">⌕ {text('navRead')}</button></div>
 <div id="create-panel" role="tabpanel" aria-labelledby="create-tab"><div class="tool-grid"><form id="generator"><div class="section-tag">01 / QR STUDIO</div><h2>{text('toolTitle')}</h2><p class="muted">{text('toolDesc')}</p>
 <label for="type">{text('create')}</label><select id="type">{''.join(f'<option value="{v}" data-i18n="{k}">{{{{{k}}}}}</option>' for v,k in [('url','url'),('text','text'),('wifi','wifi'),('email','email')])}</select>
 <label for="content">{text('content')}</label><textarea id="content" rows="3" maxlength="2000" placeholder="https://example.com" required spellcheck="false"></textarea>
 <div id="wifi-fields" hidden><label for="password">{text('password')}</label><input type="password" id="password" maxlength="128" autocomplete="off"><label for="security">{text('security')}</label><select id="security"><option value="WPA">WPA / WPA2 / WPA3</option><option value="WEP">WEP</option><option value="nopass">Open / Açık</option></select></div>
 <div id="email-fields" hidden><label for="subject">{text('subject')}</label><input id="subject" maxlength="200"></div>
 <div class="field-row"><div><label for="size">{text('size')}</label><select id="size"><option>512</option><option selected>1024</option><option>2048</option></select></div><div><label for="color">{text('color')}</label><select id="color"><option value="#142724">Graphite</option><option value="#087f73">Teal</option><option value="#153d8a">Blue</option><option value="#582c83">Violet</option></select></div></div>
 <button class="button primary wide" type="submit">{text('generate')} <span aria-hidden="true">↗</span></button></form>
 <div class="preview"><span class="section-tag">LIVE PREVIEW</span><div class="qr-paper" id="qr-preview" role="img" aria-label="QR preview"><span class="placeholder-mark" aria-hidden="true">▦</span></div><h3>{text('preview')}</h3><p class="muted">{text('previewNote')}</p><div class="exports"><button class="button primary" id="png" disabled>↓ {text('png')}</button><button class="button secondary" id="svg" disabled>↓ SVG</button></div><button class="text-button" id="clear" type="button">{text('clear')}</button></div></div></div>
 <div id="read-panel" role="tabpanel" aria-labelledby="read-tab" hidden><div class="reader"><div class="section-tag">02 / QR READER</div><h2>{text('scanTitle')}</h2><p class="muted">{text('scanDesc')}</p><div class="drop-zone" id="drop-zone"><div class="upload-icon" aria-hidden="true">↥</div><p>{text('drop')}</p><label class="button secondary" for="file">{text('choose')}</label><input type="file" id="file" accept="image/png,image/jpeg,image/webp" class="file-input"><small>{text('imageOnly')}</small></div><button id="screenshot" class="button secondary wide" hidden>{text('screenshot')}</button><div id="scan-result" hidden><label for="result">{text('result')}</label><textarea id="result" rows="4" readonly></textarea><p class="muted">{text('linkNote')}</p><div class="exports"><button id="copy" class="button secondary">{text('copy')}</button><a id="open" class="button primary" target="_blank" rel="noopener noreferrer" hidden>{text('open')}</a></div></div></div></div>
 <div class="tool-bottom"><span class="live-dot"></span> {text('local')} <span class="bottom-right">QR Scanner · v{V}</span></div></section>'''
def header():
 return f'''<a href="#main" class="skip">{text('skip')}</a><header class="site-header"><div class="container nav"><a class="brand" href="./"><img src="/assets/brand/logo.svg" width="36" height="36" alt=""><span>QR Scanner<small>BY HAKING</small></span></a><nav aria-label="Main">{a('navCreate','#toolkit')}{a('navExtension','#extension')}{a('navAbout','about.html')}</nav><div class="preferences"><select id="language" aria-label="Language">{''.join(f'<option value="{k}">{v}</option>' for k,v in [('auto','◎ Auto'),('tr','Türkçe'),('en','English'),('de','Deutsch'),('es','Español'),('fr','Français'),('pt','Português')])}</select><select id="theme" aria-label="Theme"><option value="auto" data-i18n="auto">System</option><option value="light" data-i18n="light">Light</option><option value="dark" data-i18n="dark">Dark</option></select></div></div></header>'''
def footer(): return f'''<footer class="container footer"><div class="brand-text">QR Scanner <small>v{V} · © 2026 HaKING</small><p>{text('footerTag')}</p></div><div>{a('navAbout','about.html')}{a('privacy','privacy.html')}{a('install','help.html')}{a('source','https://github.com/HaKING06/QR')}{a('release','https://github.com/HaKING06/QR/blob/main/CHANGELOG.md')}</div></footer>'''
def home(): return f'''<main id="main"><section class="hero container"><div class="hero-kicker"><span class="live-dot"></span> {text('eyebrow')}</div><h1>{text('title')}</h1><p>{text('subtitle')}</p><div class="hero-notes"><span>✓ {text('free')}</span><span>✓ {text('local')}</span><span>✓ PNG & SVG</span></div></section><div class="container">{tool()}<section class="features">{''.join(f'<article><div class="feature-icon">{icon}</div><h3>{text(k)}</h3><p>{text(k+"Desc")}</p></article>' for icon,k in [('◈','local'),('↗','export'),('∞','noExpiry')])}</section><section id="extension" class="extension-card"><div><div class="section-tag">03 / BROWSER COMPANION · v{V}</div><h2>{text('extensionTitle')}</h2><p>{text('extensionDesc')}</p><div class="exports">{a('edge',EDGE,'button primary')}{a('download','/downloads/qr-scanner-1.1.1-chromium.zip','button secondary')}</div><p><a href="/downloads/qr-scanner-1.1.1-firefox.zip">Firefox ZIP ↗</a> · {a('install','help.html')}</p><small>{text('downloadNote')}</small><p class="muted">{text('compat')}</p></div><div class="extension-art" aria-hidden="true"><img src="/assets/brand/logo.svg" width="112" height="112" alt=""><span>QR Scanner</span><small>YOUR BROWSER. YOUR TOOLKIT.</small><div class="mini-tabs">◧ CREATE <span>⌕ SCAN</span></div><div class="browser-tags">Chrome · Edge · Firefox<br>Brave · Opera</div></div></section><section class="faq" id="faq"><div class="section-tag">04 / GOOD TO KNOW</div><h2>{text('faqTitle')}</h2>{''.join(f'<details><summary>{text("q"+str(i))}</summary><p>{text("a"+str(i))}</p></details>' for i in range(1,5))}</section><section class="about-strip"><h2>{text('aboutTitle')}</h2><p>{text('aboutDesc')}</p>{a('navAbout','about.html','text-button')}</section></div></main>'''
def info(page):
 content={'about':f'<h1>{text("aboutTitle")}</h1><p>{text("aboutDesc")}</p><h2>{text("local")}</h2><p>{text("privacyDesc")}</p><h2>{text("compat")}</h2><p>{text("downloadNote")}</p><h2>{text("release")}</h2><p>v{V} · 2026-11-08</p><p>{text("extensionDesc")}</p><p>{a("source","https://github.com/HaKING06/QR")}</p>', 'privacy':f'<h1>{text("privacyTitle")}</h1><p>{text("privacyDesc")}</p><h2>{text("local")}</h2><p>{text("a2")}</p><h2>{text("latest")}</h2><p>{text("downloadNote")}</p><p>2026-11-08 · HaKING · <a href="https://haking.tr/">haking.tr</a></p>', 'help':f'<h1>{text("helpTitle")}</h1><ol>{"".join(f"<li>{text(k)}</li>" for k in ["step1","step2","step3"])}</ol><p>{text("keepFolder")}</p><h2>v{V}</h2><p>{text("downloadNote")}</p><div class="exports">{a("download","/downloads/qr-scanner-1.1.1-chromium.zip","button primary")}<a class="button secondary" href="/downloads/qr-scanner-1.1.1-firefox.zip">Firefox ZIP</a></div>'}[page]
 return f'<main class="container prose" id="main">{content}</main>'
def scripts(): return '<script src="/vendor/qrcode.js" defer></script><script src="/vendor/jsQR.js" defer></script><script src="/shared/core.js" defer></script><script src="/shared/i18n.js" defer></script><script src="/shared/app.js" defer></script>'
def render(source,lang):
 for k,v in L[lang].items(): source=source.replace('{{'+k+'}}',html.escape(v))
 return source.replace('1.1.1',V)
def build_site():
 urls=[]
 for lang in L:
  folder=R/lang;folder.mkdir(exist_ok=True)
  for page in ['index','about','privacy','help']:
   path='' if page=='index' else page+'.html'
   canonical=f'https://qr.haking.tr/{lang}/{path}'
   title={'index':L[lang]['create']+' & '+L[lang]['navRead']+' — QR Scanner','about':L[lang]['navAbout']+' — QR Scanner','privacy':L[lang]['privacy']+' — QR Scanner','help':L[lang]['helpTitle']+' — QR Scanner'}[page]
   alternates=''.join(f'<link rel="alternate" hreflang="{l}" href="https://qr.haking.tr/{l}/{path}">' for l in L)+f'<link rel="alternate" hreflang="x-default" href="https://qr.haking.tr/{path}">'
   desc=L[lang]['subtitle']+' '+L[lang]['extensionDesc']
   schema={'@context':'https://schema.org','@type':'WebApplication','name':'QR Scanner','url':canonical,'applicationCategory':'UtilitiesApplication','operatingSystem':'Any','inLanguage':lang,'description':desc,'offers':{'@type':'Offer','price':'0','priceCurrency':'USD'},'author':{'@type':'Person','name':'Halit (HaKING)','url':'https://haking.tr/'}}
   source=f'<!doctype html><html lang="{lang}" data-page="{page}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc,quote=True)}"><link rel="canonical" href="{canonical}">{alternates}<meta name="theme-color" content="#087f73"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title,quote=True)}"><meta property="og:description" content="{html.escape(desc,quote=True)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://qr.haking.tr/assets/brand/social-card.png"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/brand/favicon.ico"><link rel="icon" type="image/svg+xml" href="/assets/brand/logo.svg"><link rel="apple-touch-icon" href="/assets/brand/icon-192.png"><link rel="stylesheet" href="/style.css"><script src="/shared/preferences.js"></script><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body>{header()}{home() if page=="index" else info(page)}{footer()}<p id="status" role="status" aria-live="polite"></p>{scripts()}</body></html>'
   output=render(source,lang);(folder/(page+'.html')).write_text(output,encoding='utf-8');urls.append(canonical)
   if lang=='tr': (R/(page+'.html')).write_text(output.replace(f'href="{canonical}"',f'href="https://qr.haking.tr/{path}"',1),encoding='utf-8')
 (R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{u}</loc><lastmod>2026-11-08</lastmod></url>' for u in ['https://qr.haking.tr/']+urls)+'</urlset>',encoding='utf-8')
def build_extension():
 E=R/'extension';E.mkdir(exist_ok=True)
 for name in ['shared','vendor']:
  shutil.copytree(R/name,E/name,dirs_exist_ok=True)
 brand=E/'assets/brand';brand.mkdir(parents=True,exist_ok=True)
 needed=['logo.svg']+[f'icon-{n}.png' for n in [16,32,48,128]]
 for p in brand.iterdir():
  if p.is_file() and p.name not in needed:p.unlink()
 for name in needed:shutil.copy2(R/'assets/brand'/name,brand/name)
 shutil.copy2(R/'style.css',E/'style.css')
 popup=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>QR Scanner</title><link rel="stylesheet" href="style.css"><script src="shared/preferences.js"></script></head><body class="extension"><header class="popup-header"><img src="assets/brand/logo.svg" width="30" height="30" alt=""><strong>QR Scanner</strong><small>v{V}</small></header><div class="popup-settings"><select id="language" aria-label="Language"><option value="auto">Auto</option>'+''.join(f'<option value="{k}">{k.upper()}</option>' for k in L)+'</select><select id="theme" aria-label="Theme"><option value="auto" data-i18n="auto">System</option><option value="light" data-i18n="light">Light</option><option value="dark" data-i18n="dark">Dark</option></select></div><a id="update" class="update-banner" href="https://qr.haking.tr/#extension" target="_blank" rel="noopener noreferrer" hidden>'+text('update')+'</a><main id="main">'+tool()+'</main><footer class="popup-footer"><a href="https://qr.haking.tr/" target="_blank" rel="noopener noreferrer">qr.haking.tr ↗</a></footer><p id="status" role="status" aria-live="polite"></p>'+scripts().replace('src="/','src="')+'</body></html>'
 (E/'popup.html').write_text(render(popup,'en'),encoding='utf-8')
 manifest={'manifest_version':3,'name':'__MSG_extensionName__','description':'__MSG_extensionDescription__','default_locale':'en','version':V,'homepage_url':'https://qr.haking.tr/','permissions':['activeTab'],'host_permissions':['https://qr.haking.tr/*'],'icons':{str(n):f'assets/brand/icon-{n}.png' for n in [16,32,48,128]},'action':{'default_popup':'popup.html','default_title':'QR Scanner','default_icon':{str(n):f'assets/brand/icon-{n}.png' for n in [16,32,48,128]}},'content_security_policy':{'extension_pages':"script-src 'self'; object-src 'self'"}}
 for lang,d in L.items():
  p=E/'_locales'/lang;p.mkdir(parents=True,exist_ok=True)
  (p/'messages.json').write_text(json.dumps({'extensionName':{'message':'QR Scanner — '+d['navRead']+' & '+d['navCreate']},'extensionDescription':{'message':d['extensionDesc']}},ensure_ascii=False,indent=2),encoding='utf-8')
 (E/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
 downloads=R/'downloads';downloads.mkdir(exist_ok=True);hashes={}
 for browser in ['chromium','firefox']:
  m=dict(manifest)
  if browser=='firefox':m['browser_specific_settings']={'gecko':{'id':'qr-scanner@haking.tr','strict_min_version':'142.0','data_collection_permissions':{'required':['none']}}}
  name=f'qr-scanner-{V}-{browser}.zip'
  with zipfile.ZipFile(downloads/name,'w',zipfile.ZIP_DEFLATED) as z:
   for p in E.rglob('*'):
    if p.is_file() and p.name!='manifest.json':z.write(p,p.relative_to(E).as_posix())
   z.writestr('manifest.json',json.dumps(m,indent=2))
   z.write(R/'LICENSE','LICENSE');z.write(R/'THIRD_PARTY_NOTICES.md','THIRD_PARTY_NOTICES.md')
  hashes[name]=hashlib.sha256((downloads/name).read_bytes()).hexdigest()
 (downloads/'SHA256SUMS.txt').write_text(''.join(f'{v}  {k}\n' for k,v in hashes.items()),encoding='utf-8')
 (R/'version.json').write_text(json.dumps({'version':V,'released':'2026-11-08','url':'https://qr.haking.tr/#extension','downloads':{k:v for k,v in hashes.items()}},indent=2),encoding='utf-8')
if __name__=='__main__':build_site();build_extension();print('Built site and extension v'+V)
