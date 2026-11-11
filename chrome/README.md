# Chrome Web Store yükleme klasörü

Bu klasörden yalnızca `qr-scanner-<sürüm>-chrome.zip` dosyasını **Yeni öğe → Dosya seç** ile yükle.
ZIP, mevcut Chromium paketinin Chrome sürümüdür; 128px ikonu mağaza için 96px
çizim ve dört yanda 16px şeffaf boşlukla hazırlanmıştır. Çalışan kod ve izinler değişmez.
Diğer klasörleri ZIP'e ekleme veya klasör olarak yükleme.

## Mağaza alanları

| Alan | Kullanılacak dosya |
| --- | --- |
| Paket | Ana klasördeki güncel `qr-scanner-<sürüm>-chrome.zip` |
| Mağaza simgesi | `store-icon-128x128.png` |
| Küçük tanıtım görseli | `small-promo-440x280.png` |
| Marquee / büyük afiş | `marquee-1400x560.png` |
| Ekran görüntüleri | `screenshots/tr/` içindeki iki 1280×800 PNG |
| Açıklamalar | `descriptions/tr.txt` |
| Gizlilik / izin gerekçeleri | `privacy-forms/tr.txt` |

8 dil hazır: `tr`, `en`, `de`, `es`, `fr`, `pt`, `ru`, `ar`. Mağazada üstteki dil seçimini
değiştirerek aynı dilin `store-listings` açıklamasını ve `screenshots` ekranlarını ekle.
`privacy-forms` metinleri Gizlilik bölümündeki ilgili alanlar içindir; mağaza
açıklamasına yapıştırma. `store-listings` dosyasından yalnızca Detailed description
başlığı altındaki tanıtım metnini Açıklama alanına kopyala.
Chrome'da küçük/büyük tanıtım afişleri dil bazında değil, ortaktır. `promotional`
klasöründeki diğer yedi dilin sürümleri alternatiflerdir; tüm diller için İngilizce afişleri
kullanabilirsin. Ana klasördeki afişler Türkçedir. Logo da tüm diller için aynıdır.
Gizlilik/veri kullanımı beyanlarını göndermeden önce kontrol et; burada hesap üzerinden
otomatik seçim veya gönderim yapılmaz.

Ekran görüntüleri çalışan uzantının gerçek 390px arayüzünü, değiştirmeden ve
ölçeklemeden, 1280×800 sunum zemininde gösterir. Okuyucu ve oluşturucu ayrı
görsellerdir; afişleri ekran görüntüsü alanına yükleme.

## Siteyi Chrome mağazasına bağlamak

Gerçek Chrome mağaza bağlantısı `store-links.json` içinde tanımlı. Chrome için indir
düğmesi artık mağazaya gider. Yayınlamadan önce bağlantıyı kontrol et.

## Sonraki sürümler

- `package.json` sürümünü artır ve `npm run build` çalıştır; Chrome ve Edge
  klasörlerindeki güncel ZIP ve açıklamalar hazırlanır.
- Logo veya afiş değişirse `npm run build:chrome-assets` çalıştır (Python/Pillow).
- Arayüz değişirse gerçek uzantı ekran görüntülerini yeniden al. Ham yakalamalar
  yerel `test-results/chrome-captures/` içindedir; bu test klasörü Git'e eklenmez.
- Bu klasör web sitesinin `dist/` paketine dahil edilmez.
- Otomatik commit/push/yükleme/public yayın yapılmaz. Son kontrol ve gönderim kullanıcıdadır.

Resmî kaynaklar:
- https://developer.chrome.com/docs/webstore/images
- https://developer.chrome.com/docs/webstore/cws-dashboard-listing
- https://developer.chrome.com/docs/webstore/publish

## 1.1.3 teslim notu

Önce web sitesini yayınla; `/updates.html` açıldıktan sonra mağaza paketini yükle.
Yeni öğe oluşturma; mevcut öğenin paketini güncelle. Sekiz dilin düz açıklamaları
`descriptions/`, izin gerekçeleri `privacy-forms/`, gerçek uzantı ekranları
`screenshots/<dil>/` içinde. Yeni `storage` ve isteğe bağlı `notifications`
izinlerini hazırlanan metinlere göre beyan et. Sistem bildirimi kullanıcı
uzantıdaki zil düğmesinden izin verirse görünür.

Chrome Gelişmiş Güvenli Tarama yeni geliştiricilere güven geçmişi oluşana kadar
uyarı gösterebilir; bu uyarının hemen kalkacağı garanti edilemez.
Kaynak: https://support.google.com/chrome/answer/2664769
