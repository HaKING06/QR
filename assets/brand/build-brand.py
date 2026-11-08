"""Build QR Scanner v1.1.2 cobalt identity; requires Pillow and Segoe UI."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from html import escape
import json
ROOT = Path(__file__).resolve().parent
VERSION = json.loads((ROOT.parents[1]/'package.json').read_text(encoding='utf-8'))['version']
BLUE, NAVY, ICE, MUTED = '#4864ff', '#11162b', '#f5f7ff', '#acb6d4'
FONTS = Path('C:/Windows/Fonts')
def font(size,bold=False):
    return ImageFont.truetype(str(FONTS/('segoeuib.ttf' if bold else 'segoeui.ttf')),size)
MARK='''<rect width="128" height="128" rx="29" fill="#11162b"/><rect x="29" y="25" width="70" height="76" rx="21" fill="#f5f7ff"/><rect x="40" y="36" width="48" height="54" rx="11" fill="#11162b"/><g fill="#4864ff"><rect x="50" y="47" width="11" height="11" rx="2"/><rect x="67" y="47" width="11" height="11" rx="2"/><rect x="50" y="64" width="11" height="11" rx="2"/><rect x="67" y="64" width="11" height="11" rx="2"/><rect x="85" y="87" width="21" height="21" rx="4"/></g>'''
def icon(size=1024):
    s=size*4/128
    im=Image.new('RGBA',(size*4,size*4)); d=ImageDraw.Draw(im)
    def box(bounds,radius,fill):
        d.rounded_rectangle(tuple(round(v*s) for v in bounds),radius=radius*s,fill=fill)
    box((0,0,128,128),29,NAVY); box((29,25,99,101),21,ICE); box((40,36,88,90),11,NAVY)
    for x,y in [(50,47),(67,47),(50,64),(67,64)]: box((x,y,x+11,y+11),2,BLUE)
    box((85,87,106,108),4,BLUE)
    return im.resize((size,size),Image.Resampling.LANCZOS)
def export_icons():
    (ROOT/'logo.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-label="QR Scanner">'+MARK+'</svg>',encoding='utf-8')
    icon().save(ROOT/'logo.png')
    for n in (16,32,48,128,192,512): icon(n).save(ROOT/f'icon-{n}.png')
    icon(256).save(ROOT/'favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])
def banner(name,headline,subline,badge):
    im=Image.new('RGB',(1200,630),NAVY); d=ImageDraw.Draw(im)
    for x in range(756,1200,44): d.line((x,0,x,630),fill='#1b2342')
    for y in range(14,630,44): d.line((756,y,1200,y),fill='#1b2342')
    d.rounded_rectangle((64,49,116,101),radius=14,fill=ICE); im.paste(icon(48),(66,51),icon(48))
    d.text((131,53),'QR Scanner',font=font(28,True),fill=ICE)
    d.text((1040,63),'v'+VERSION,font=font(18,True),fill='#aab7ff')
    d.text((64,165),badge,font=font(15,True),fill='#aab7ff')
    for i,line in enumerate(headline): d.text((59,216+79*i),line,font=font(62,True),fill=ICE)
    for i,line in enumerate(subline): d.text((64,407+31*i),line,font=font(21),fill=MUTED)
    d.rounded_rectangle((804,173,1130,499),radius=49,fill='#202a55',outline='#35447d',width=2)
    d.rounded_rectangle((824,193,1110,479),radius=39,fill=BLUE)
    im.paste(icon(278),(828,197),icon(278))
    d.line((64,535,1136,535),fill='#303957',width=1)
    d.text((64,557),'qr.haking.tr',font=font(20,True),fill=ICE)
    d.text((1025,560),'by HaKING',font=font(17),fill=MUTED)
    im.save(ROOT/f'{name}.png',optimize=True)
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="{NAVY}"/>'
    for x in range(756,1200,44): svg+=f'<path d="M{x} 0v630" stroke="#1b2342"/>'
    for y in range(14,630,44): svg+=f'<path d="M756 {y}h444" stroke="#1b2342"/>'
    svg+=f'<g transform="translate(64 49) scale(.40625)">{MARK}</g><g font-family="Segoe UI, Arial, sans-serif"><text x="131" y="84" fill="{ICE}" font-size="28" font-weight="700">QR Scanner</text><text x="1040" y="84" fill="#aab7ff" font-size="18" font-weight="700">v{VERSION}</text><text x="64" y="183" fill="#aab7ff" font-size="15" font-weight="700">{escape(badge)}</text>'
    for i,line in enumerate(headline): svg+=f'<text x="59" y="{274+79*i}" fill="{ICE}" font-size="62" font-weight="700">{escape(line)}</text>'
    for i,line in enumerate(subline): svg+=f'<text x="64" y="{430+31*i}" fill="{MUTED}" font-size="21">{escape(line)}</text>'
    svg+=f'<text x="64" y="580" fill="{ICE}" font-size="20" font-weight="700">qr.haking.tr</text><text x="1025" y="580" fill="{MUTED}" font-size="17">by HaKING</text></g><rect x="804" y="173" width="326" height="326" rx="49" fill="#202a55" stroke="#35447d" stroke-width="2"/><rect x="824" y="193" width="286" height="286" rx="39" fill="{BLUE}"/><g transform="translate(828 197) scale(2.171875)">{MARK}</g><path d="M64 535h1072" stroke="#303957"/></svg>'
    (ROOT/f'{name}.svg').write_text(svg,encoding='utf-8')
if __name__=='__main__':
    export_icons()
    banner('social-card',['Every QR.','One place.'],['Create, scan and share in your browser.','Free to use. Your data stays yours.'],'THE QR TOOLKIT · REIMAGINED')
    banner('promo-extension',['Your browser.','Upgraded.'],['Scan the current tab. Read images.','Create QR codes without switching apps.'],'QR SCANNER · BROWSER EXTENSION')
    banner('promo-website-tr',['Her QR.','Tek bir yerde.'],['Tarayıcında QR oluştur, oku ve paylaş.','Ücretsiz. Verilerin seninle kalır.'],'QR SCANNER · YENİDEN TASARLANDI')
    print('QR Scanner v'+VERSION+' brand exports:',ROOT)
