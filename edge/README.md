# Edge mağazasına yükleme — QR Scanner

Bu klasör yerel hazırlık içindir. Otomatik mağaza gönderimi veya public yayın yapılmaz.

| Partner Center alanı | Seçeceğin dosya |
| --- | --- |
| Packages / Paket | `qr-scanner-<sürüm>-edge.zip` — klasördeki güncel sürüm |
| Extension logo | `logo-300x300.png` — önerilen 300×300 logo |
| Small promotional tile | `small-promo-440x280.png` — 440×280, isteğe bağlı |
| Large promotional tile | `large-promo-1400x560.png` — 1400×560, isteğe bağlı |

`icons/` içinde 16, 19, 24, 32, 38, 48, 64, 128, 256, 300, 512 ve 1024px
PNG'ler, SVG kaynak logosu, ayrıca beyaz ve koyu zeminli 300×300 alternatifler var.
Mağaza logosu olarak ana dizindeki dosyayı kullan; diğer boyutlar uyumluluk ve
farklı kullanım alanları içindir. Uzantının kendi ikonları ZIP'e zaten dahil.

`promotional/` klasöründe Türkçe ve İngilizce tanıtım görselleri bulunur.
Ana dizindeki iki tanıtım görseli Türkçedir. Mağazada aynı logoyu diğer dillere
Duplicate seçeneğiyle kopyalayabilirsin. Görselleri ZIP'in içine koyma;
Partner Center'daki ilgili görsel alanlarına ayrı yükle.

`store-listings/` altındaki altı dil dosyası, açıklamalar ve bağlantılar için
kopyalanabilir metinler içerir. Göndermeden önce gözden geçir.

## Sonraki güncellemeler

- `package.json` sürümünü güncelle ve `npm run build` çalıştır: güncel paket
  bu klasöre otomatik kopyalanır, önceki Edge ZIP'i kaldırılır ve sağlama dosyası yenilenir.
- Logo veya afiş değiştiyse `npm run build:edge-assets` çalıştır.
  Bu görsel dışa aktarma komutu Python/Pillow ve Windows Segoe UI kullanır.
- GitHub klasörüne kopyalama, commit/push, web yayını ve mağazaya gönderim ayrı
  işlemlerdir; son kontrolü ve public yayını kullanıcı yapar.
- Bu klasör web sitesinin `dist/` yayın paketine dahil edilmez.

Sürüm numarası daha önce mağazada kullanıldıysa aynı sürümle yeni kod
gönderme; `package.json` içinden sürümü artırıp yeniden paketle.

Kaynak: https://learn.microsoft.com/en-us/microsoft-edge/extensions/publish/publish-extension

Microsoft'un belirttiği logo: 1:1, önerilen 300×300, en az 128×128.
Tanıtım görselleri: 440×280 ve 1400×560. İsteğe bağlı gerçek ekran görüntüleri
640×480 veya 1280×800 olmalı; tanıtım afişleri ekran görüntüsü alanına yüklenmemeli.
