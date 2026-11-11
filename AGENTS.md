# QR Scanner çalışma düzeni

- Çalışma kaynağı `C:/Users/halit/Desktop/WEB/QR` klasörüdür.
- Tamamlanan değişiklikleri `C:/Users/halit/OneDrive/Belgeler/GitHub/QR`
  klasörüne kopyala. Kullanıcının mevcut değişikliklerini ezmeden önce kontrol et.
- Otomatik commit, push, sürüm etiketi oluşturma veya public deployment yapma.
  Kullanıcı son kontrolü ve yayınlamayı kendisi yapar; bu işlemler için ilgili
  görevde açık talimat gerekir.
- Cloudflare/mağaza/hesap ayarlarını kendiliğinden değiştirme. Özel bir altyapı,
  yetki veya yayın işlemi gerektiğinde ne gerektiğini kullanıcıya bildir.
- `edge/` mağazaya yükleme klasörüdür. Güncel Edge ZIP'ini ve mağaza görsellerini
  burada hazır tut. `npm run build` Edge ZIP'ini de yeniler; logo değişirse
  `npm run build:edge-assets` ile görsel boyutlarını yeniden üret.
- `chrome/` Chrome Web Store yükleme klasörüdür. `npm run build` Chrome ZIP'ini
  ve sekiz dilde mağaza metinlerini de yeniler. Görseller için
  `npm run build:chrome-assets` kullan; arayüz değiştiyse gerçek ekranları yenile.
- Chrome mağaza adresini uydurma. Kullanıcının gerçek, herkese açık bağlantısını
  `store-links.json` içindeki `chrome` alanına ekleyince site düğmesi mağazaya gider.
- Her projede açık bir sürüm bulunmalı. Her tamamlanan değişiklik tesliminde
  uygun sürümü artır; aynı teslimin ara düzenlemelerinde gereksiz sürüm artışı yapma.
  Site, manifest, paketler ve sürüm notları aynı sürümü taşımalı.
- Son kullanıcı yanıtının son cümlesinde teslim edilen yeni sürümü belirt.
