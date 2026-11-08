"""Export existing vector branding at Microsoft Edge Add-ons asset sizes."""
from pathlib import Path
import importlib.util
import json
import shutil
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'edge'
VERSION=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))['version']
spec=importlib.util.spec_from_file_location('qr_brand',ROOT/'assets/brand/build-brand.py')
brand=importlib.util.module_from_spec(spec)
spec.loader.exec_module(brand)
OUT.mkdir(exist_ok=True)
(OUT/'icons').mkdir(exist_ok=True)
(OUT/'promotional').mkdir(exist_ok=True)

for size in [16,19,24,32,38,48,64,128,256,300,512,1024]:
    brand.icon(size).save(OUT/'icons'/f'icon-{size}.png',optimize=True)
brand.icon(300).save(OUT/'logo-300x300.png',optimize=True)
for name,color in [('white','#ffffff'),('dark','#11162b')]:
    canvas=Image.new('RGB',(300,300),color)
    mark=brand.icon(240)
    canvas.paste(mark,(30,30),mark)
    canvas.save(OUT/'icons'/f'logo-300x300-{name}.png',optimize=True)
shutil.copy2(ROOT/'assets/brand/logo.svg',OUT/'icons/logo.svg')

def tile(language,size):
    w,h=size
    small=w==440
    canvas=Image.new('RGB',size,'#11162b')
    draw=ImageDraw.Draw(canvas)
    margin=24 if small else 64
    logo_size=40 if small else 60
    mark=brand.icon(logo_size)
    canvas.paste(mark,(margin,24 if small else 38),mark)
    draw.text((margin+logo_size+10,30 if small else 46),'QR Scanner',font=brand.font(18 if small else 27,True),fill='#f5f7ff')
    if small:
        lines=['Her QR.','Bir tık ötede.'] if language=='tr' else ['Every QR.','One click away.']
        font=brand.font(27,True)
        for index,line in enumerate(lines):
            assert draw.textlength(line,font=font)<236,line
            draw.text((24,102+index*36),line,font=font,fill='#f5f7ff')
        mark=brand.icon(132)
        canvas.paste(mark,(284,102),mark)
        draw.line((24,244,416,244),fill='#303957')
        draw.text((24,253),'qr.haking.tr',font=brand.font(11),fill='#acb6d4')
    else:
        for x in range(960,w,40):draw.line((x,0,x,h),fill='#1b2342')
        for y in range(0,h,40):draw.line((960,y,w,y),fill='#1b2342')
        lines=['Her QR için','tek bir uzantı.'] if language=='tr' else ['Every QR.','One extension.']
        for index,line in enumerate(lines):draw.text((60,161+index*78),line,font=brand.font(62,True),fill='#f5f7ff')
        subtitle='Oku, oluştur ve paylaş. Tarayıcından ayrılmadan.' if language=='tr' else 'Scan, create and share. Without leaving your browser.'
        draw.text((64,355),subtitle,font=brand.font(23),fill='#acb6d4')
        mark=brand.icon(310)
        canvas.paste(mark,(1020,123),mark)
        draw.line((64,464,1336,464),fill='#303957')
        draw.text((64,491),'qr.haking.tr',font=brand.font(20,True),fill='#f5f7ff')
    name=('small-promo-440x280' if small else 'large-promo-1400x560')
    canvas.save(OUT/'promotional'/f'{name}-{language}.png',optimize=True)
    if language=='tr':shutil.copy2(OUT/'promotional'/f'{name}-{language}.png',OUT/f'{name}.png')

for language in ['tr','en']:
    for size in [(440,280),(1400,560)]:tile(language,size)
print('Exported Edge store logo, icon variants and correctly sized promotional tiles.')
