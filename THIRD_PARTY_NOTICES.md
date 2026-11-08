# Third-party software

All runtime libraries ship locally; no CDN or remote JavaScript is used.

| Package | Version | License | Source |
| --- | --- | --- | --- |
| qrcode-generator | 1.4.4 | MIT | https://github.com/kazuhikoarase/qrcode-generator |
| jsQR | 1.4.0 | Apache-2.0 | https://github.com/cozmo/jsQR |
| Font Awesome Free brand SVGs | 7.3.1 | CC BY 4.0 (icons) | https://fontawesome.com/license/free |

Full upstream license text is retained in `vendor/qrcode-LICENSE.txt` and
`vendor/jsQR-LICENSE.txt`. The generator also retains its embedded copyright
header. Brand assets are part of this project's MIT distribution.

Browser marks in `assets/browsers/` are Font Awesome Free brand icons by
Fonticons, Inc., licensed under CC BY 4.0. Browser names and marks belong
to their respective owners. No endorsement is implied. Playwright 1.65.0
(Apache-2.0) is a development-only browser verification dependency.
