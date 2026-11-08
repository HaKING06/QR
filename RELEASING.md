# Release procedure

1. Increment `V` in `tools/build.py` and version in `package.json` together.
   Update release date in build output, changelog and translated download labels/links.
   Never decrease a published extension manifest version.
2. Edit shared runtime/translations; never manually patch generated extension copies.
3. `npm ci`, `npm test`, `npm run build`, `npm run check`.
4. Test the website at 390px and 768px. Install Chromium ZIP unpacked and Firefox
   ZIP temporarily. Check generation, image scanning, screenshots, permissions,
   language/theme persistence and offline behavior.
5. Verify `downloads/SHA256SUMS.txt`. ZIP root must contain `manifest.json`.
6. Commit source and generated static pages/packages to the production branch.
   Existing GitHub/Cloudflare Workers integration publishes the site; verify live version.
7. Upload Chromium package through the owner's Edge dashboard and separately
   submit to Chrome Web Store if desired. Firefox needs Mozilla signing. Safari
   needs an Apple development environment. Website publication does not publish stores.

`version.json` is the public release authority, fetched by 1.1.1+ popups only.
Older installs without this feature need one manual/store update first.
During a staged deployment publish the ZIP packages together with the metadata;
do not advertise a version without its corresponding download. `_headers`
prevents stale release metadata in browsers/CDNs supporting Pages headers.

## Local folders

- `C:/Users/halit/Desktop/WEB/QR`: working site and shared extension source.
- `C:/Users/halit/OneDrive/Belgeler/GitHub/QR`: existing deployment Git checkout.
- `C:/Users/halit/Desktop/WEB/QR-Scanner-v1`: requested unpacked release location.
- `C:/Users/halit/Desktop/WEB/QR-Scanner`: original 1.1.0 source; preserve as baseline.

Root `QR-Scanner-v1.zip` is the original 1.1.0 artifact and is not the latest.
The site points to versioned `downloads/qr-scanner-1.1.1-*.zip` assets.
