"""Scroll storytelling and release-page templates; all copy comes from locales."""
import templates as ui

COFFEE='https://buymeacoffee.com/haking'
CHROME='https://chromewebstore.google.com/detail/qr-scanner-%E2%80%94-read-qr-crea/pmhjjnijononbcfddpimpegdobibhijo'
EDGE='https://microsoftedge.microsoft.com/addons/detail/qr-scanner/klblmhlgnbnclpdhddadkbbccmdjknmf'

def support():
    t,icon=ui.t,ui.icon
    return f'''<section class="support-section" id="support" data-reveal><div class="support-mark" aria-hidden="true">{icon('coffee')}</div><div><span class="eyebrow">HAKING / INDEPENDENT SOFTWARE</span><h2>{t('supportDeveloper')}</h2><p>{t('supportDesc')}</p></div><a class="button primary" href="{COFFEE}" target="_blank" rel="noopener noreferrer">Buy Me a Coffee {icon('arrow')}</a></section>'''

def story(version):
    t,icon=ui.t,ui.icon
    stages=[('scan','storyScan','storyScanDesc'),('qr','storyCreate','storyCreateDesc'),('arrow','storyShare','storyShareDesc')]
    scenes=''.join(f'<article class="story-scene" data-story-scene="{i}"><span class="eyebrow">0{i+1} / QR SCANNER</span><h3>{t(title)}</h3><p>{t(description)}</p></article>' for i,(_,title,description) in enumerate(stages))
    controls=''.join(f'<button type="button" data-story-goto="{i}" aria-pressed="{str(i==0).lower()}">{icon(glyph)}{t(title)}</button>' for i,(glyph,title,_) in enumerate(stages))
    return f'''<section class="scroll-story" data-scroll-story aria-label="QR Scanner workflow"><div class="story-pin"><div class="story-heading"><span class="eyebrow">QR SCANNER / v{version}</span><h2>{t('storyTitle')}</h2></div><div class="story-grid"><div class="story-visual" aria-hidden="true"><div class="signal-orbit orbit-one"></div><div class="signal-orbit orbit-two"></div><div class="signal-card card-back"></div><div class="signal-card card-front"><img src="/assets/brand/logo.svg" width="140" height="140" alt=""><span class="signal-line"></span></div><span class="signal-number" data-story-number>01</span><span class="signal-point point-one"></span><span class="signal-point point-two"></span></div><div class="story-scenes">{scenes}</div></div><div class="story-controls">{controls}</div><div class="story-track" aria-hidden="true"><span></span></div><p class="story-assurance">{icon('shield')}{t('storyPrivacyDesc')}</p></div></section>'''

def review_dialog():
    t,icon=ui.t,ui.icon
    return f'''<dialog id="review-dialog" aria-labelledby="review-title" aria-describedby="review-description"><form method="dialog"><button class="dialog-close" value="dismiss" aria-label="Close">{icon('close')}</button><img src="/assets/brand/logo.svg" width="48" height="48" alt=""><span class="eyebrow">QR SCANNER</span><h2 id="review-title">{t('reviewTitle')}</h2><p id="review-description">{t('reviewDesc')}</p><div class="review-actions"><a class="button primary review-link" href="{CHROME}" target="_blank" rel="noopener noreferrer">{t('reviewChrome')}{icon('arrow')}</a><a class="button secondary review-link" href="{EDGE}" target="_blank" rel="noopener noreferrer">{t('reviewEdge')}{icon('arrow')}</a></div><button class="text-button review-later" value="later">{t('reviewLater')}</button></form></dialog>'''

def updates(version,date):
    t,icon=ui.t,ui.icon
    features=[('scan','featureMultiScan'),('globe','featureLanguages'),('qr','featureMotion'),('bell','featureUpdates')]
    cards=''.join(f'<article class="update-feature" data-reveal>{icon(glyph)}<span>0{i+1}</span><h3>{t(key)}</h3></article>' for i,(glyph,key) in enumerate(features))
    return f'''<main id="main" class="container updates-page"><section class="update-hero"><div class="release-orbit" aria-hidden="true"><img src="/assets/brand/logo.svg" width="86" height="86" alt=""></div><span class="release-chip"><span class="live-dot"></span>v{version} · {date}</span><h1 id="update-heading">{t('whatsNew')}</h1><p id="update-intro">{t('updateIntro')}</p><div class="update-transition" id="update-transition" hidden><span id="previous-version"></span>{icon('arrow')}<strong dir="ltr">v{version}</strong></div><div class="hero-links"><a class="button primary" href="./#toolkit">{t('continueTools')}{icon('arrow')}</a><button class="button secondary" id="open-review" type="button">{t('reviewOpen')}{icon('arrow')}</button></div></section><section class="release-content"><div class="section-heading"><div><span class="eyebrow">RELEASE NOTES / v{version}</span><h2>{t('releaseHighlights')}</h2></div><a href="https://github.com/HaKING06/QR/blob/main/CHANGELOG.md" class="text-button">{t('releaseNotes')}{icon('arrow')}</a></div><div class="update-grid">{cards}</div><div class="update-privacy">{icon('shield')}<p>{t('updatePrivacy')}</p></div></section>{support()}<section class="contact-card"><div>{icon('email')}<h2>{t('contactTitle')}</h2><p>{t('contactDesc')}</p></div><a href="mailto:qr@haking.tr" class="button secondary">qr@haking.tr {icon('arrow')}</a></section></main>{review_dialog()}'''
