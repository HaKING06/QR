"""Rebuild vector-authored brand exports (Pillow required). No remote assets."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html

ROOT = Path(__file__).resolve().parent
TEAL, CREAM, INK, MUTED = '#087f73', '#f7f8f4', '#142724', '#60746d'
FONT = Path('C:/Windows/Fonts')

def font(size, bold=False):
    return ImageFont.truetype(str(FONT / ('segoeuib.ttf' if bold else 'segoeui.ttf')), size)

def icon(size=1024):
    scale = 4
    im = Image.new('RGBA', (size*scale, size*scale))
    d = ImageDraw.Draw(im)
    def box(bounds, radius, fill):
        d.rounded_rectangle(tuple(round(v*size*scale/128) for v in bounds), radius=radius*size*scale/128, fill=fill)
    box((0,0,128,128),28,TEAL)
    for x,y in [(25,25),(73,25),(25,73)]:
        box((x,y,x+30,y+30),6,CREAM)
        box((x+7,y+7,x+23,y+23),2,TEAL)
    box((73,73,84,84),2,CREAM)
    box((92,92,103,103),2,CREAM)
    s=size*scale/128
    d.line([(77*s,103*s),(103*s,77*s)], fill=CREAM, width=round(8*s))
    for x,y in [(77,103),(103,77)]:
        d.ellipse(((x-4)*s,(y-4)*s,(x+4)*s,(y+4)*s),fill=CREAM)
    return im.resize((size,size), Image.Resampling.LANCZOS)

MARK = '''<rect width="128" height="128" rx="28" fill="#087f73"/><g fill="none" stroke="#f7f8f4" stroke-width="7"><rect x="28.5" y="28.5" width="23" height="23" rx="3"/><rect x="76.5" y="28.5" width="23" height="23" rx="3"/><rect x="28.5" y="76.5" width="23" height="23" rx="3"/></g><g fill="#f7f8f4"><rect x="73" y="73" width="11" height="11" rx="2"/><rect x="92" y="92" width="11" height="11" rx="2"/></g><path d="M77 103 103 77" stroke="#f7f8f4" stroke-width="8" stroke-linecap="round"/>'''
(ROOT/'logo.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-label="QR Scanner">'+MARK+'</svg>',encoding='utf-8')
icon(1024).save(ROOT/'logo.png')
for size in (16,32,48,128,192,512):
    icon(size).save(ROOT/f'icon-{size}.png')
icon(256).save(ROOT/'favicon.ico', sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])

def banner(name, title, subtitle, badge, width=1200, height=630):
    im=Image.new('RGB',(width,height),CREAM)
    d=ImageDraw.Draw(im)
    # restrained drafting grid on the right; all content is decorative brand art.
    for x in range(width//2,width,32):
        for y in range(24,height,32): d.ellipse((x,y,x+2,y+2), fill='#dce7e0')
    im.paste(icon(52),(64,54),icon(52))
    d.text((132,57),'QR Scanner',font=font(29,True),fill=INK)
    badge_width = round(d.textlength(badge,font=font(16,True)))+32
    d.rounded_rectangle((64,155,64+badge_width,193),radius=19,fill='#deeee5')
    d.text((80,161),badge,font=font(16,True),fill=TEAL)
    for i,line in enumerate(title): d.text((60,224+i*78),line,font=font(65,True),fill=INK)
    for i,line in enumerate(subtitle): d.text((64,410+i*31),line,font=font(21),fill=MUTED)
    d.text((64,height-79),'qr.haking.tr',font=font(21,True),fill=TEAL)
    d.text((width-166,height-79),'by HaKING',font=font(18),fill=MUTED)
    # A large mark, not a misleading non-functional QR.
    marksize=256
    x,y=width-358,190
    d.rounded_rectangle((x-30,y-30,x+marksize+30,y+marksize+30),radius=38,fill='white',outline='#dce7e0',width=2)
    im.paste(icon(marksize),(x,y),icon(marksize))
    im.save(ROOT/f'{name}.png', optimize=True)
    esc=html.escape
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="{CREAM}"/><g transform="translate(64 54) scale(.40625)">{MARK}</g><g font-family="Segoe UI, Arial, sans-serif"><text x="132" y="87" fill="{INK}" font-size="29" font-weight="700">QR Scanner</text><rect x="64" y="155" width="{badge_width}" height="38" rx="19" fill="#deeee5"/><text x="80" y="180" fill="{TEAL}" font-size="16" font-weight="700">{esc(badge)}</text>'
    for i,line in enumerate(title): svg+=f'<text x="60" y="{285+i*78}" fill="{INK}" font-size="65" font-weight="700">{esc(line)}</text>'
    for i,line in enumerate(subtitle): svg+=f'<text x="64" y="{432+i*31}" fill="{MUTED}" font-size="21">{esc(line)}</text>'
    svg+=f'<text x="64" y="{height-55}" fill="{TEAL}" font-size="21" font-weight="700">qr.haking.tr</text><text x="{width-166}" y="{height-57}" fill="{MUTED}" font-size="18">by HaKING</text></g><rect x="{x-30}" y="{y-30}" width="316" height="316" rx="38" fill="white" stroke="#dce7e0" stroke-width="2"/><g transform="translate({x} {y}) scale(2)">{MARK}</g></svg>'
    (ROOT/f'{name}.svg').write_text(svg,encoding='utf-8')

banner('social-card',['One tool.','Every QR.'],['Create. Scan. Share.','Private by design. Free to use.'],'QR READER & GENERATOR')
banner('promo-extension',['Your browser.','QR ready.'],['Read images. Create QR codes.','Keep your data on your device.'],'BROWSER EXTENSION')
banner('promo-website-tr',['QR dünyanız,','tek bir yerde.'],['QR kod oluşturun, görselleri okuyun.','Ücretsiz. Gizlilik odaklı.'],'QR OKUYUCU & OLUŞTURUCU')
print('Brand exports written:',ROOT)
