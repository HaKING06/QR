# Yellow Argon — açıklama düzeltmesi ve yeniden gönderim

## Tespit

Ret maili, uzantının çalışmasına ilişkin bir hata bildirmiyor; Rusça, Fransızca,
İspanyolca ve Arapça mağaza açıklamalarındaki bağlamsız tür listelerini gösteriyor.
Bu satırlar `tools/chrome_package.py` tarafından arayüz etiketlerinden otomatik
üretiliyordu. Aynı üretim kalıbı diğer dört dilde ve Edge metinlerinde de vardı.

Sekiz dilin tamamı doğal paragraflarla yeniden yazıldı. Tür listesi ve gereksiz
özellik tekrarları çıkarıldı. Metinler yalnızca uzantıda bulunan işlevleri, yerel
işlemeyi, sürüm kontrolünü ve isteğe bağlı bildirimleri anlatıyor. Başlıklar,
paket özetleri ve afiş üretim metinleri de gözden geçirildi; bunlar ret mailinde
işaretlenen listeyi içermiyor. E-posta başka bir ihlal bildirmiyor; bu tespit
gelecek incelemede başka bir konu çıkmayacağının garantisi değildir.

## Panelde yapacakların

1. Mevcut `pmhjjnijononbcfddpimpegdobibhijo` öğesini aç; yeni öğe oluşturma.
2. Reddedilen taslağın **Mağaza girişi** bölümüne git.
3. Dil seçiminden aşağıdaki sekiz dili sırayla seç. O dilin dosyasındaki metnin
   tamamını **Açıklama** alanına yapıştır; eski metnin üstüne ekleme.

| Dil | Açıklama dosyası |
| --- | --- |
| İngilizce | `descriptions/en.txt` |
| Türkçe | `descriptions/tr.txt` |
| Almanca | `descriptions/de.txt` |
| İspanyolca | `descriptions/es.txt` |
| Fransızca | `descriptions/fr.txt` |
| Portekizce | `descriptions/pt.txt` |
| Rusça | `descriptions/ru.txt` |
| Arapça | `descriptions/ar.txt` |

4. Her dili kaydet. Panelde ayrıca eklediğin başka bir yerelleştirme varsa onun
   açıklamasında da eski virgüllü tür listesinin bulunmadığını kontrol et.
5. Gizlilik ve izin gerekçelerini tanıtım açıklamasına yapıştırma; bunların yeri
   **Gizlilik** bölümüdür. Bu ret, mevcut izinleri kaldırmayı gerektirmiyor.
6. **Durum** bölümünden düzeltilen taslağı yeniden incelemeye gönder. Yalnızca
   mağaza metni değiştiği için yeni ZIP veya yeni sürüm numarası gerekmiyor.
   Daha önce hazırlanan paketlerden hangisini bu taslağa yüklediysen o kalabilir.

Bu işlem metni düzelterek yeniden gönderim içindir. Kararın hatalı olduğunu
iddia eden bir itiraz hazırlamak yerine önce belirtilen içeriği düzeltmek uygundur.
Hesabından kaydetme/gönderme işlemleri otomatik yapılmadı. GitHub'a push etmek
Chrome panelindeki açıklamaları kendiliğinden güncellemez.

## İnceleme ekibine not alanı varsa

```text
We removed the standalone comma-separated QR-type lists identified in the
Yellow Argon rejection, including the Russian, French, Spanish and Arabic
descriptions. We also rewrote the remaining localized descriptions to use
contextual prose without those lists or unnecessary feature repetition.
The updated descriptions describe existing extension functionality only.
This submission changes listing metadata; the extension package and
permissions are unchanged.
```

Bu notu herkese açık ürün açıklamasına ekleme; yalnızca inceleme ekibine not
gönderebildiğin bir alan varsa kullan. Böyle bir alan yoksa ayrıca bir şey ekleme.

## Sonraki hazırlamalar

Kaynak `tools/store-descriptions.json` dosyasıdır. `npm run build:store-copy`
iki mağazanın metinlerini yeniler; `npm run check` dilleri, eski liste kalıbını
ve üretilmiş dosyaların güncelliğini denetler. Mağaza metni düzeltmesinde paket
sürümüne dokunulmadı ve mevcut ZIP dosyaları değiştirilmedi.

Kaynaklar:

- [Yellow Argon / Keyword stuffing](https://developer.chrome.com/docs/webstore/troubleshooting/#keyword-stuffing)
- [Spam politikası SSS](https://developer.chrome.com/docs/webstore/program-policies/spam-faq#keyword-spam)
- [Mağaza metadatasını güncelleme](https://developer.chrome.com/docs/webstore/update#update-the-listing-metadata)
