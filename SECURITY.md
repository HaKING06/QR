# Security policy

Security fixes target the latest release (1.1.1). Please report vulnerabilities
privately through GitHub's private vulnerability reporting when enabled, or use
the contact channels on https://haking.tr/. Do not include secrets or personal
QR contents in public issues. Do not assume an HTTPS QR destination is safe.

No QR payload is sent to a server. The extension contacts qr.haking.tr only
for release metadata; standard network metadata can be visible to hosting
providers. Theme, language and cached release metadata use local storage.
Files are limited to 15 MB and scanner canvas dimensions are bounded. Decoded
content is rendered as text; only explicit HTTP(S) links can be opened.
