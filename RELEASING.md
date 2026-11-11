# Release procedure

1. Increment `version` in `package.json` (the single version source).
   Update release date, changelog and any version-specific translation copy.
   Never decrease a published extension manifest version.
2. Edit shared runtime/translations; never manually patch generated extension copies.
3. `npm ci`, `npm test`, `npm run build`, `npm run check`.
4. Test the website at 390px and 768px. Install Chromium ZIP unpacked and Firefox
   ZIP temporarily. Check generation, image scanning, screenshots, permissions,
   language/theme persistence and offline behavior.
5. Verify `downloads/SHA256SUMS.txt`. ZIP root must contain `manifest.json`.
6. Copy source and generated pages/packages to the user's existing GitHub checkout.
   Stop before commit/push/tag/deployment. The user performs the final review and public
   publication. Existing GitHub/Cloudflare integration runs when the user pushes.
7. The user uploads `edge/qr-scanner-<version>-edge.zip` through the Edge dashboard and `chrome/qr-scanner-<version>-chrome.zip` through Chrome Web Store. Firefox needs Mozilla signing. Safari
   needs an Apple development environment. Website publication does not publish stores.

`version.json` is the public release authority, fetched by 1.1.1+ popups only.
Older installs without this feature need one manual/store update first.
During a staged deployment publish the ZIP packages together with the metadata;
do not advertise a version without its corresponding download. `_headers`
prevents stale release metadata in Cloudflare Workers Static Assets.

## Local folders

- `C:/Users/halit/Desktop/WEB/QR`: working site and shared extension source.
- `C:/Users/halit/OneDrive/Belgeler/GitHub/QR`: existing deployment Git checkout.
- `C:/Users/halit/Desktop/WEB/QR-Scanner-v1`: requested unpacked release location.

Only the current version's packages belong in `downloads/`.
Legacy archives, old root icons and obsolete standalone extension scripts were
removed in 1.1.2. Git history retains release history. When updating the loaded
extension folder, remove stale files that are absent from generated `extension/`
and reload it on the browser's extensions page.

`edge/` is the store submission handoff folder. Every build refreshes its ZIP
and checksums. `npm run build:edge-assets` regenerates the store-sized logo
and promotional images when the brand changes. Do not include this folder in
the public website build. No automatic publishing is authorized.

`chrome/` provides the equivalent Chrome Web Store handoff. First generate
its assets with `npm run build:chrome-assets`; ordinary builds then refresh
the Chrome ZIP and eight localized text files. The Chrome ZIP differs from
the Chromium ZIP only in the 128px icon's transparent store padding.
Update actual UI captures when appearance changes. Neither store handoff
folder belongs in `dist/`. The published Chrome URL is configured in `store-links.json`.

## 1.1.3 publication order

Publish the website first and confirm `/updates.html` and the eight localized
release pages are available. Then upload the two store ZIPs. The extension
opens release notes only after a genuine installed-version increase. A version.json
check advertises a newer version; it never installs code itself. Manual ZIP
users must replace/reload their unpacked extension.

Store privacy fields now also explain `storage` and optional `notifications`.
Use each language's `descriptions/<lang>.txt` for the listing description;
`privacy-forms/<lang>.txt` belongs in the privacy form. Review prompts are
dismissible, never required and never tied to rewards or support payments.

Regenerate native UI captures before building store screenshots. Install
`requirements-assets.txt`, then run both asset build commands. Test real signed
store updating and optional OS notifications after publication; mock tests alone
do not prove these deployment-dependent behaviors.
