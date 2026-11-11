# Security policy

Security fixes target the latest release (1.1.3). Please report vulnerabilities
privately through GitHub's private vulnerability reporting when enabled, or use
qr@haking.tr. Do not include secrets or personal
QR contents in public issues. Do not assume an HTTPS QR destination is safe.

No QR payload is sent to a server. The extension contacts qr.haking.tr only
for release metadata and opens its localized welcome/release page on install/update; standard network metadata can be visible to hosting
providers. Theme, language, cached release metadata and update state use local storage.
Desktop notifications are optional and do not contain QR contents. Support and
store review links navigate to external sites only when explicitly selected.
Files are limited to 15 MB and scanner canvas dimensions are bounded. Decoded
content is rendered as text; only explicit HTTP(S) links can be opened.
