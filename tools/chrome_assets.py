"""Export native brand artwork and real UI captures for Chrome Web Store."""
from pathlib import Path
import importlib.util
import json
from PIL import Image,ImageDraw
from text_layout import text,width

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'chrome'
LOCALES=json.loads((ROOT/'shared/locales.json').read_text(encoding='utf-8'))
spec=importlib.util.spec_from_file_location('qr_brand',ROOT/'assets/brand/build-brand.py')
brand=importlib.util.module_from_spec(spec);spec.loader.exec_module(brand)

def wrapped(draw,value,font,max_width):
    lines=[];line=''
    for word in value.split():
        candidate=(line+' '+word).strip()
        if line and width(draw,candidate,font)>max_width:lines.append(line);line=word
        else:line=candidate
    if line:lines.append(line)
    return lines

def tile(lang,size,out=OUT,large_name='marquee-1400x560.png'):
    small=size==(440,280);s=LOCALES[lang]
    im=Image.new('RGB',size,'#11162b');d=ImageDraw.Draw(im)
    x,y,mark_size=(24,24,40) if small else (64,38,60)
    mark=brand.icon(mark_size);im.paste(mark,(x,y),mark)
    text(d,(x+mark_size+10,y+5),'QR Scanner',font=brand.font(18 if small else 27,True),fill='#f5f7ff')
    if small:
        font=brand.font(21,True)
        for index,key in enumerate(['navRead','navCreate']):
            lines=wrapped(d,s[key],font,245)
            assert len(lines)==1,(lang,key)
            text(d,(24,112+index*34),lines[0],font=font,fill='#f5f7ff',rtl_width=245)
        mark=brand.icon(126);im.paste(mark,(290,102),mark)
        d.line((24,244,416,244),fill='#303957');text(d,(24,253),'qr.haking.tr',font=brand.font(11),fill='#acb6d4')
    else:
        for xx in range(960,1400,40):d.line((xx,0,xx,560),fill='#1b2342')
        for yy in range(0,560,40):d.line((960,yy,1400,yy),fill='#1b2342')
        headline=s['heroLead']+' '+s['heroAccent']
        lines=wrapped(d,headline,brand.font(58,True),850)
        assert len(lines)<=2,(lang,lines)
        for index,line in enumerate(lines):text(d,(60,163+index*78),line,font=brand.font(58,True),fill='#f5f7ff',rtl_width=850)
        for index,line in enumerate(wrapped(d,s['subtitle'],brand.font(22),830)):
            text(d,(64,347+index*32),line,font=brand.font(22),fill='#acb6d4',rtl_width=830)
        mark=brand.icon(310);im.paste(mark,(1020,123),mark)
        d.line((64,464,1336,464),fill='#303957');text(d,(64,491),'qr.haking.tr',font=brand.font(20,True),fill='#f5f7ff')
    folder=out if lang=='tr' else out/'promotional'/lang
    folder.mkdir(parents=True,exist_ok=True)
    name='small-promo-440x280.png' if small else large_name
    im.save(folder/name,optimize=True)

def screenshot(lang,mode,out=OUT):
    source=ROOT/'test-results/chrome-captures'/f'{lang}-{mode}.png'
    if not source.exists():return False
    s=LOCALES[lang]
    im=Image.new('RGB',(1280,800),'#11162b');d=ImageDraw.Draw(im)
    mark=brand.icon(58);im.paste(mark,(64,50),mark)
    text(d,(139,59),'QR Scanner',font=brand.font(29,True),fill='#f5f7ff')
    key='scanTitle' if mode=='reader' else 'create'
    lines=wrapped(d,s[key],brand.font(49,True),650)
    assert len(lines)<=3,(lang,lines)
    for index,line in enumerate(lines):text(d,(60,215+index*67),line,font=brand.font(49,True),fill='#f5f7ff',rtl_width=650)
    caption=s['readerHint'] if mode=='reader' else s['previewNote']
    for index,line in enumerate(wrapped(d,caption,brand.font(23),630)):
        text(d,(64,450+index*35),line,font=brand.font(23),fill='#acb6d4',rtl_width=630)
    for index,key in enumerate(['local','noHistory','export']):
        bullet=704 if lang=='ar' else 66
        d.ellipse((bullet,590+index*34,bullet+6,596+index*34),fill='#8294ff')
        text(d,(64 if lang=='ar' else 86,580+index*34),s[key],font=brand.font(17),fill='#d4dcf6',rtl_width=630)
    capture=Image.open(source).convert('RGB')
    assert capture.width==390 and capture.height<=620,(source,capture.size)
    # Actual captured extension UI, unchanged and unscaled, on a full-bleed presentation canvas.
    im.paste(capture,(815,(800-capture.height)//2))
    text(d,(64,742),'qr.haking.tr',font=brand.font(16,True),fill='#f5f7ff')
    folder=out/'screenshots'/lang;folder.mkdir(parents=True,exist_ok=True)
    im.save(folder/('01-reader-1280x800.png' if mode=='reader' else '02-generator-1280x800.png'),optimize=True)
    return True

def export_assets():
    OUT.mkdir(exist_ok=True)
    store=Image.new('RGBA',(128,128));store.paste(brand.icon(96),(16,16))
    store.save(OUT/'store-icon-128x128.png',optimize=True)
    count=0
    for lang in LOCALES:
        for size in [(440,280),(1400,560)]:tile(lang,size)
        for mode in ['reader','generator']:count+=int(screenshot(lang,mode))
    print(f'Chrome assets: padded store icon, {len(LOCALES)*2} localized promotional tiles, {count} real-UI screenshot compositions.')
    if count==len(LOCALES)*2:
        (OUT/'screenshots/release.json').write_text(json.dumps({'version':brand.VERSION,'languages':list(LOCALES),'source':'Native Chromium extension UI, 390px; localized 1280x800 compositions'},indent=2),encoding='utf-8')

if __name__=='__main__':export_assets()
