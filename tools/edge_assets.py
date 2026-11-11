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

from chrome_assets import tile,screenshot,LOCALES
for language in LOCALES:
    for size in [(440,280),(1400,560)]:tile(language,size,OUT,'large-promo-1400x560.png')
    for mode in ['reader','generator']:screenshot(language,mode,OUT)
print('Exported Edge store assets for',len(LOCALES),'languages.')
(OUT/'screenshots/release.json').write_text(json.dumps({'version':VERSION,'languages':list(LOCALES),'source':'Native Chromium extension UI, 390px; localized 1280x800 compositions'},indent=2),encoding='utf-8')
