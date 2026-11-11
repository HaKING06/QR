<p align="center"><img src="assets/brand/logo.png" width="100" alt="QR Scanner logo"></p>
<h1 align="center">QR Scanner</h1>
<p align="center">Scan. Create. Carry on.<br>A private QR toolkit for the web and your browser.</p>
<p align="center"><a href="https://qr.haking.tr/">Website</a> · <a href="https://qr.haking.tr/#extension">Download</a> · <a href="https://qr.haking.tr/help.html">Installation</a> · <a href="https://qr.haking.tr/privacy.html">Privacy</a></p>

![QR Scanner toolkit](assets/brand/social-card.png)

## Türkçe

QR Scanner; ücretsiz QR kod oluşturma, QR kod okuma ve tarayıcı uzantısını
bir araya getiren açık kaynaklı bir projedir. Web sitesi, metin, Wi-Fi,
e-posta, telefon, SMS ve kişi kartı QR kodları oluşturur. PNG/SVG dışa aktarma, sürükleyip bırakma,
görsel yapıştırma, otomatik dil, açık/koyu/sistem temaları desteklenir.
QR içeriği ve görseller cihazda işlenir. Hesap ve filigran yoktur.

**Sürüm: 1.1.3.** Kaydırmaya bağlı hareketli anlatım, sekiz dil (Arapça RTL dahil),
çoklu QR okuma ve güncelleme sonrası sürüm notları.
İletişim: [qr@haking.tr](mailto:qr@haking.tr).

## Features

- Seven QR types, UTF-8, live preview, error correction and hidden Wi-Fi support.
- PNG (512/1024/2048px) and scalable SVG; four-module quiet zone.
- Local PNG/JPEG/WebP image scanning, paste and drag/drop (15 MB maximum).
- Scan active browser tab in the extension with a user gesture.
- Create a QR for the current tab; copy generated images to the clipboard.
- On-demand local camera scanning on the website; camera stops after a result.
- Every ZIP download opens the matching browser installation guide automatically.
- Automatic browser language, manual language choice, persistent theme.
- Static localized HTML, canonical/hreflang links, sitemap, structured data.
- Extension only shows the update notice when the release is newer.
- A genuine installed-version update opens localized release notes once; same-version reloads do not.
- Optional desktop notifications, a dismissible review prompt and [developer support](https://buymeacoffee.com/haking).
- Up to six distinct QR results per image, with a result picker and copy-all.
- English, Turkish, German, Spanish, French, Portuguese, Russian and Arabic (RTL).
- Native scroll-driven storytelling and reduced-motion support.
- No analytics, server-side QR processing, tracking cookies or QR history.

## Browser availability

| Platform | Installation/status |
| --- | --- |
| Edge | [Existing store listing](https://microsoftedge.microsoft.com/addons/detail/qr-scanner/klblmhlgnbnclpdhddadkbbccmdjknmf); submitting 1.1.3 requires the owner's store account. |
| Chrome | [Chrome Web Store](https://chromewebstore.google.com/detail/qr-scanner/pmhjjnijononbcfddpimpegdobibhijo); the owner submits updates. |
| Brave / Opera | Load the Chromium ZIP unpacked in Developer mode. |
| Firefox 142+ | Separate MV3 package with Gecko ID and no-data declaration. Temporary installation via about:debugging; Mozilla signing is required for permanent installation. |
| Safari | Website works in modern Safari. Native extension conversion/signing with Xcode and Apple distribution is still required. No Safari package is claimed. |

The extension requests `storage` for preferences/release state and `activeTab` for explicitly initiated screenshots and
`https://qr.haking.tr/*` for version checks. Optional `notifications` is requested only when the user enables update notifications. No content scripts or broad
browsing permissions. Version checks run on popup opening at most once per
hour, send no QR contents, and silently tolerate being offline. Checks
cannot be retroactively added to older installed versions.

## Development

Requires Node.js 20+ and Python 3.10+. Runtime is plain HTML/CSS/JS.

```sh
npm ci
npm test
npm run build
python -m http.server 4173
```

Open `http://localhost:4173`. `tools/build.py` renders all localized HTML,
copies shared runtime into `extension/`, and creates Chromium/Firefox ZIPs
and SHA-256 checksums in `downloads/`. `shared/locales.json` is the source
for translations. `tools/templates.py` contains website and compact popup layouts.
`shared/ui.css` holds design tokens/controls; `style.css` is website-only and
`popup.css` fixes actual browser-popup geometry without viewport-relative shrinking.
Branding can be rebuilt with its documented
asset script. For localized artwork install `pip install -r requirements-assets.txt`
(Pillow, Arabic shaping and bidi text support).

## Release and deployment

The assistant prepares local files and copies them into the existing GitHub
checkout. The owner performs final review, Git push and public publication.
No automatic commit, push, release tag or deployment is authorized.

For Edge submission use [edge/README.md](edge/README.md). `npm run build`
refreshes the Edge ZIP in that folder; `npm run build:edge-assets` regenerates
the 300×300 store logo, icon variants and 440×280 / 1400×560 promotional assets.

For Chrome submission use [chrome/README.md](chrome/README.md). The folder
contains the Chrome ZIP, eight localized descriptions/listings/privacy justifications,
128px store icon, 440×280 / 1400×560 artwork and real-UI screenshot compositions.
`npm run build:chrome-assets` refreshes artwork from native brand assets and
locally captured UI. `npm run build` refreshes both store packages.
`store-links.json` contains the published Chrome and Edge URLs. Brave/Opera/Firefox
ZIP buttons continue to open their matching installation guide.

Read [RELEASING.md](RELEASING.md). This repository retains root `index.html`
compatibility with the existing site and local preview. The actual production
host is the GitHub-connected Cloudflare Worker named `qr`.
No new hosting service, account, database or Cloudflare project is required.
`_headers` supplies CSP, MIME protection, referrer policy and no-cache release
metadata. Pushes to the existing production branch use the existing
GitHub → Cloudflare integration. Review the actual deployment result.

Cloudflare build command: `npm run build:static`. Deploy command:
`npx wrangler deploy --name qr --assets ./dist --compatibility-date 2026-10-19`.
This preserves the existing Wrangler-based Git deployment without adding a
new CLI configuration file. `dist/` contains only public site assets and
download packages. Python builds the committed release locally, not on hosting.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md),
[CHANGELOG.md](CHANGELOG.md), [third-party notices](THIRD_PARTY_NOTICES.md).
MIT © 2026 Halit (HaKING). [haking.tr](https://haking.tr/).

## Verification for 1.1.3

Website primary QR interactions, two-code image decoding, scroll phases and overflow
at 390px and 768px; native Chromium extension rendering in all eight languages
with real runtime APIs. Update lifecycle/deduplication and optional notification
branches have automated mock-API tests; operating-system notification appearance
and signed-store automatic updates require verification after store publication.
Store submission and Safari conversion remain separate distribution steps.
