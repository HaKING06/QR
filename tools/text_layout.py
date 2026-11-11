"""Shape Arabic for Pillow builds without RAQM, preserving real RTL glyph order."""
import re

def display(value):
    if not re.search('[\u0600-\u06ff]',value):return value
    import arabic_reshaper
    from bidi.algorithm import get_display
    return get_display(arabic_reshaper.reshape(value))

def width(draw,value,font):return draw.textlength(display(value),font=font)

def text(draw,position,value,rtl_width=None,**kwargs):
    shaped=display(value)
    if rtl_width and re.search('[\u0600-\u06ff]',value):
        position=(position[0]+rtl_width-draw.textlength(shaped,font=kwargs.get('font')),position[1])
    draw.text(position,shaped,**kwargs)
