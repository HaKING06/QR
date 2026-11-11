"""Apply the complete eight-language QR Scanner 1.1.3 content update.

No writes occur on import. Run from any directory; only shared/locales.json changes.
"""
import json
from pathlib import Path

BASE = {
'ru': '''
navCreate|Создать QR
navRead|Считать QR
navExtension|Расширение
navAbout|О проекте
eyebrow|МАЛЕНЬКИЙ КОД. БЕСКОНЕЧНЫЕ ВОЗМОЖНОСТИ.
title|Один QR. Столько возможностей.
subtitle|Создавайте, считывайте и делитесь. Простые инструменты QR с заботой о конфиденциальности — прямо в браузере.
create|Создать QR-код
read|Считать QR-код
toolTitle|Создайте то, чем хочется поделиться.
toolDesc|Выберите тип и добавьте содержимое. Ваш QR-код будет готов за секунды.
url|Сайт
text|Текст
wifi|Wi-Fi
email|Электронная почта
content|Ваше содержимое
password|Пароль
subject|Тема письма
security|Защита
size|Размер экспорта
color|Цвет QR-кода
generate|Создать QR
preview|Ваш QR-код готов.
previewNote|Чёткий QR-код в высоком разрешении. Без регистрации и водяных знаков.
png|Скачать PNG
svg|Скачать SVG
copy|Копировать текст
clear|Очистить
local|Конфиденциальность по умолчанию
localDesc|Изображения и содержимое QR-кодов обрабатываются на вашем устройстве.
free|Полностью бесплатно
freeDesc|Без регистрации, подписки и водяных знаков.
export|Для любого размера
exportDesc|PNG для отправки. SVG для чёткой печати в любом размере.
extensionTitle|Ваши инструменты QR. В одном нажатии.
extensionDesc|Считывайте изображения, сканируйте текущую вкладку и создавайте QR-коды, не выходя из браузера.
edge|Установить для Edge
download|Скачать ZIP v1.1.3
install|Инструкция по установке
compat|Chrome, Edge, Brave и Opera: пакет Chromium. Firefox: отдельный пакет. Для Safari нужна сборка для Apple.
faqTitle|Ответы на ваши вопросы.
q1|Есть ли у QR-кодов срок действия?
a1|У статических QR-кодов нет срока действия. Сайт, на который ведёт код, должен оставаться доступным.
q2|Мои файлы отправляются на сервер?
a2|Нет. Изображения, текст и пароли Wi-Fi обрабатываются локально. Только проверка версии расширения обращается к qr.haking.tr.
q3|Можно ли настроить внешний вид QR-кода?
a3|Выберите цвет и размер экспорта. Файлы PNG и SVG включают белое поле шириной в четыре модуля для надёжного считывания.
q4|Какие браузеры поддерживаются?
a4|Сайт работает в современных браузерах. Расширение доступно в магазине Edge; ZIP-пакеты Chromium можно установить вручную. Для постоянной установки в Firefox требуется подпись.
aboutTitle|Полезные инструменты. Меньше хлопот.
aboutDesc|QR Scanner — проект с открытым исходным кодом от HaKING (Халит). Он делает повседневные задачи с QR-кодами быстрыми, доступными и конфиденциальными. Создавайте коды для сайтов, текста, Wi-Fi и электронной почты или считывайте код с изображения.
privacy|Конфиденциальность
privacyDesc|Содержимое QR-кодов не отправляется на наши серверы. Нет аналитики, отслеживающих cookie и истории QR-кодов. Настройки темы, языка, отзывов и обновлений хранятся на вашем устройстве. Хостинг-провайдеры могут обрабатывать обычные журналы соединений.
helpTitle|Установка QR Scanner
step1|Распакуйте скачанный ZIP в постоянную папку.
step2|Скопируйте адрес ниже и вставьте его в адресную строку новой вкладки.
step3|Нажмите «Загрузить распакованное расширение» и выберите папку с файлом manifest.json.
keepFolder|Сохраните эту папку. Для обновления замените файлы новой версией и нажмите «Перезагрузить». Firefox: about:debugging → Этот Firefox → Загрузить временное дополнение → manifest.json (до перезапуска). Для Safari требуются преобразование через Xcode, подпись и отдельный процесс распространения.
scanTitle|Узнайте, что внутри.
scanDesc|Загрузите, перетащите или вставьте изображение. Его содержимое останется на вашем устройстве.
choose|Выбрать изображение
drop|Перетащите изображение сюда или вставьте сочетанием Ctrl / ⌘ + V
result|Считанное содержимое
open|Открыть ссылку
linkNote|Проверьте адрес перед открытием. HTTPS не гарантирует надёжность сайта.
empty|Сначала введите содержимое.
invalid|Введите допустимое содержимое.
tooLong|Содержимое слишком длинное для QR-кода. Сократите его и повторите попытку.
notFound|QR-код не найден. Попробуйте более чёткое или крупное изображение.
badFile|Выберите изображение PNG, JPEG или WebP размером до 15 МБ.
copied|Скопировано.
copyError|Буфер обмена недоступен. Выделите и скопируйте текст вручную.
ready|Ваш QR-код готов.
scanning|Считывание изображения…
theme|Тема
language|Язык
latest|Последняя версия
update|Доступна новая версия. Скачайте последнее обновление.
screenshot|Сканировать текущую вкладку
screenError|Не удалось сделать снимок вкладки. Попробуйте обычную вкладку с сайтом.
fileError|Не удалось прочитать изображение.
privacyTitle|О конфиденциальности простыми словами.
faq|Частые вопросы
source|Исходный код
release|История изменений
auto|Системная
light|Светлая
dark|Тёмная
noExpiry|Остаётся у вас
noExpiryDesc|Статические QR-коды. Без срока действия и сервиса перенаправления.
skip|Перейти к инструментам
downloadNote|Версия в магазине Edge может отличаться. ZIP-пакеты содержат v1.1.3. До подписания ZIP для Firefox предназначен для временного тестирования.
footerTag|Считывайте. Создавайте. Двигайтесь дальше.
imageOnly|PNG, JPEG, WebP · до 15 МБ
heroLead|Любой QR.
heroAccent|В одном месте.
workspace|Ваше рабочее пространство QR
workspaceDesc|Поделитесь ссылкой, подключите сеть или узнайте содержимое кода.
tools|Инструменты
contact|Связаться
downloadTitle|Пусть всегда будет под рукой.
downloadDesc|Повседневные инструменты QR рядом с текущей вкладкой.
downloadZip|Скачать ZIP
browser|Браузер
phone|Телефон
sms|SMS
vcard|Карточка контакта
message|Сообщение
fullName|Имя и фамилия
organization|Организация
correction|Коррекция ошибок
hiddenNetwork|Скрытая сеть
copyImage|Копировать изображение
currentTab|QR-код этой вкладки
camera|Сканировать камерой
stopCamera|Остановить камеру
cameraError|Камера недоступна. Проверьте разрешение и убедитесь, что её не использует другое приложение.
working|Обработка…
sample|Пример QR-кода
contentHint|Введите ссылку или содержимое. Предпросмотр обновится автоматически.
contactTitle|Вместе — лучше.
contactDesc|Напишите нам, если нужна помощь, вы нашли ошибку или хотите предложить улучшение. Не отправляйте личное содержимое QR-кодов и пароли.
aboutMission|Делаем повседневные задачи с QR-кодами проще для всех.
aboutPrinciples|Конфиденциальность, понятные инструменты и контроль в ваших руках.
aboutOpen|Открытый код. Открытый подход.
aboutOpenDesc|Изучайте код, предлагайте улучшения или сообщайте об ошибках. QR Scanner разрабатывает HaKING.
installIntro|Скачайте пакет, выберите браузер и следуйте инструкции ниже.
downloadStarted|Запрос на скачивание отправлен вашему браузеру.
downloadAgain|Скачать ещё раз
copyAddress|Копировать адрес
stepExtract|Распакуйте пакет
stepOpen|Откройте страницу расширений
stepLoad|Загрузите расширение
stepReload|Для обновления замените файлы в той же папке и нажмите кнопку перезагрузки расширения.
firefoxIntro|До подписания пакет Firefox предназначен для временной установки в целях разработки.
firefoxStep|Откройте about:debugging → Этот Firefox → Загрузить временное дополнение → manifest.json. Временное дополнение удаляется при закрытии браузера.
safariInfo|В Safari можно пользоваться веб-инструментами. Расширение для Safari пока не выпущено.
troubleshoot|Что-то пошло не так?
troubleDesc|Выберите папку с файлом manifest.json. Распакуйте последний пакет, а не старый ZIP. После перезагрузки расширения закройте и снова откройте его окно.
engineError|Не удалось загрузить движок QR. Откройте страницу или расширение заново.
noHistory|История QR-кодов не сохраняется
readyScan|Готово к сканированию
readerHint|Выберите, перетащите или вставьте снимок экрана.
chooseBrowser|Выберите браузер
downloadFor|Скачать для
statusError|Проверьте выделенное поле.
noPassword|Открытая сеть
formatHint|Статический QR · PNG и SVG · Обработка на вашем устройстве
sendEmail|Написать письмо
latestBadge|Последний выпуск
step|Шаг
customize|Настроить
automaticPreview|Предпросмотр в реальном времени
autoLanguage|Автоматически (язык браузера)
chromeStore|Добавить в Chrome
''',
'ar': '''
navCreate|إنشاء QR
navRead|قراءة QR
navExtension|الإضافة
navAbout|عن المشروع
eyebrow|رمز صغير. إمكانات بلا حدود.
title|رمز واحد. إمكانات كثيرة.
subtitle|أنشئ وامسح وشارك. أدوات QR بسيطة تحترم خصوصيتك، مباشرة في متصفحك.
create|إنشاء رمز QR
read|مسح رمز QR
toolTitle|أنشئ شيئًا يستحق المشاركة.
toolDesc|اختر النوع وأضف المحتوى. يصبح رمزك جاهزًا خلال ثوانٍ.
url|موقع إلكتروني
text|نص
wifi|شبكة Wi-Fi
email|بريد إلكتروني
content|المحتوى
password|كلمة المرور
subject|الموضوع
security|الحماية
size|حجم التصدير
color|لون الرمز
generate|إنشاء الرمز
preview|رمزك جاهز للاستخدام.
previewNote|رمز واضح بدقة عالية. دون حساب أو علامة مائية.
png|تنزيل PNG
svg|تنزيل SVG
copy|نسخ النص
clear|مسح
local|الخصوصية أساس التصميم
localDesc|تُعالَج صورك ومحتويات الرموز على جهازك.
free|مجاني تمامًا
freeDesc|دون حساب أو اشتراك أو علامات مائية.
export|مناسب لكل الأحجام
exportDesc|PNG للمشاركة، وSVG لطباعة واضحة بأي حجم.
extensionTitle|أدوات QR على بُعد نقرة.
extensionDesc|اقرأ الصور وامسح علامة التبويب الحالية وأنشئ رموز QR دون مغادرة المتصفح.
edge|تثبيت على Edge
download|تنزيل ZIP للإصدار v1.1.3
install|دليل التثبيت
compat|Chrome وEdge وBrave وOpera: حزمة Chromium. Firefox: حزمة منفصلة. يتطلب Safari إصدارًا مخصصًا لأجهزة Apple.
faqTitle|إجابات توضح لك الأمور.
q1|هل تنتهي صلاحية رموز QR؟
a1|لا تنتهي صلاحية الرموز الثابتة. يجب أن يظل الموقع الذي يشير إليه الرمز متاحًا.
q2|هل تُرفَع ملفاتي إلى الخادم؟
a2|لا. تُعالَج الصور والنصوص وكلمات مرور Wi-Fi محليًا. يتصل فحص تحديث الإضافة فقط بموقع qr.haking.tr.
q3|هل يمكنني تخصيص رمز QR؟
a3|اختر اللون وحجم التصدير. تتضمن ملفات PNG وSVG هامشًا أبيض بعرض أربع وحدات لضمان سهولة المسح.
q4|ما المتصفحات المدعومة؟
a4|يعمل الموقع في المتصفحات الحديثة. الإضافة متاحة في متجر Edge، ويمكن تثبيت حزم Chromium بصيغة ZIP يدويًا. يتطلب التثبيت الدائم في Firefox توقيع الإضافة.
aboutTitle|أدوات مفيدة. خطوات أقل.
aboutDesc|QR Scanner مشروع مفتوح المصدر يطوره HaKING (Halit). يسهّل مهام QR اليومية مع التركيز على السرعة وإمكانية الوصول والخصوصية. أنشئ رموزًا للمواقع والنصوص وشبكات Wi-Fi والبريد الإلكتروني، أو اقرأ رمزًا من صورة.
privacy|الخصوصية
privacyDesc|لا تُرسَل محتويات الرموز إلى خوادمنا. لا تحليلات استخدام أو ملفات تعريف ارتباط للتتبع أو سجل للرموز. تبقى تفضيلات المظهر واللغة والمراجعات والتحديثات على جهازك. قد تعالج جهات الاستضافة سجلات الاتصال المعتادة.
helpTitle|تثبيت QR Scanner
step1|استخرج ملف ZIP الذي نزّلته إلى مجلد دائم.
step2|انسخ العنوان أدناه والصقه في شريط العنوان بعلامة تبويب جديدة.
step3|اختر «تحميل إضافة غير مضغوطة» وحدد المجلد المستخرج الذي يحتوي على manifest.json.
keepFolder|احتفظ بهذا المجلد. للتحديث، استبدل ملفاته بالحزمة الأحدث واضغط «إعادة التحميل». Firefox: افتح about:debugging ← هذا Firefox ← تحميل إضافة مؤقتة ← manifest.json (حتى إعادة التشغيل). يتطلب Safari تحويلًا عبر Xcode وتوقيعًا وآلية توزيع منفصلة.
scanTitle|اكتشف ما بداخله.
scanDesc|اختر صورة أو اسحبها أو الصقها. يبقى محتواها على جهازك.
choose|اختيار صورة
drop|أفلت صورة هنا أو الصقها باستخدام Ctrl / ⌘ + V
result|المحتوى المقروء
open|فتح الرابط
linkNote|تحقق من الوجهة قبل فتحها. لا يضمن HTTPS أن الموقع موثوق.
empty|أدخل المحتوى أولًا.
invalid|أدخل محتوى صالحًا.
tooLong|المحتوى أطول من سعة رمز QR. اختصره وحاول مجددًا.
notFound|لم يُعثَر على رمز QR. جرّب صورة أوضح أو أكبر.
badFile|اختر صورة PNG أو JPEG أو WebP لا يتجاوز حجمها 15 ميغابايت.
copied|تم النسخ.
copyError|الحافظة غير متاحة. حدد النص وانسخه يدويًا.
ready|رمز QR جاهز.
scanning|جارٍ قراءة الصورة…
theme|المظهر
language|اللغة
latest|أحدث إصدار
update|يتوفر إصدار أحدث. نزّل آخر إصدار.
screenshot|مسح علامة التبويب الحالية
screenError|تعذّر التقاط هذه الصفحة. جرّب علامة تبويب لموقع عادي.
fileError|تعذّرت قراءة الصورة.
privacyTitle|الخصوصية بلغة واضحة.
faq|الأسئلة الشائعة
source|الكود المصدري
release|ملاحظات الإصدار
auto|النظام
light|فاتح
dark|داكن
noExpiry|لك دائمًا
noExpiryDesc|رموز ثابتة دون انتهاء صلاحية أو خدمة إعادة توجيه.
skip|الانتقال إلى الأدوات
downloadNote|قد يختلف إصدار متجر Edge. تحتوي حزم ZIP على v1.1.3. حزمة Firefox مخصصة للاختبار المؤقت إلى حين توقيعها.
footerTag|امسح. أنشئ. واصل.
imageOnly|PNG وJPEG وWebP · حتى 15 ميغابايت
heroLead|كل رموز QR.
heroAccent|في مكان واحد.
workspace|مساحة عمل QR
workspaceDesc|شارك رابطًا أو اتصل بشبكة أو اكتشف محتوى رمز.
tools|الأدوات
contact|تواصل معنا
downloadTitle|اجعله جزءًا من متصفحك.
downloadDesc|أدوات QR اليومية بجوار علامة التبويب الحالية.
downloadZip|تنزيل ZIP
browser|المتصفح
phone|الهاتف
sms|رسالة نصية
vcard|بطاقة اتصال
message|الرسالة
fullName|الاسم الكامل
organization|المؤسسة
correction|تصحيح الأخطاء
hiddenNetwork|شبكة مخفية
copyImage|نسخ الصورة
currentTab|رمز لهذه الصفحة
camera|المسح بالكاميرا
stopCamera|إيقاف الكاميرا
cameraError|الكاميرا غير متاحة. تحقق من الإذن ومن عدم استخدامها في تطبيق آخر.
working|جارٍ المعالجة…
sample|رمز تجريبي
contentHint|أدخل رابطًا أو محتوى. تتحدث المعاينة تلقائيًا.
contactTitle|معًا نصنع الأفضل.
contactDesc|تواصل معنا للدعم أو الإبلاغ عن خطأ أو تقديم اقتراح. لا تحتاج إلى إرسال محتويات QR خاصة أو كلمات مرور.
aboutMission|نسهّل مهام QR اليومية للجميع.
aboutPrinciples|خصوصية وأدوات واضحة وتحكم يبقى بين يديك.
aboutOpen|مصدر مفتوح. نهج منفتح.
aboutOpenDesc|استكشف الكود أو ساهم في تحسينه أو أبلغ عن مشكلة. يطوّر HaKING مشروع QR Scanner.
installIntro|نزّل الحزمة واختر متصفحك واتبع الخطوات التالية.
downloadStarted|أُرسِل طلب التنزيل إلى متصفحك.
downloadAgain|التنزيل مجددًا
copyAddress|نسخ العنوان
stepExtract|استخراج الحزمة
stepOpen|فتح صفحة الإضافات
stepLoad|تحميل الإضافة
stepReload|للتحديث، استبدل الملفات في المجلد نفسه واضغط «إعادة التحميل» في صفحة الإضافة.
firefoxIntro|حزمة Firefox مخصصة للتثبيت المؤقت أثناء التطوير إلى حين توقيعها.
firefoxStep|افتح about:debugging ← هذا Firefox ← تحميل إضافة مؤقتة ← manifest.json. يُزال التثبيت المؤقت عند إغلاق المتصفح.
safariInfo|استخدم أدوات الموقع في Safari. لم يصدر امتداد Safari بعد.
troubleshoot|هل واجهت مشكلة؟
troubleDesc|اختر المجلد الذي يحتوي على manifest.json. استخرج أحدث حزمة بدلًا من ملف ZIP قديم. بعد إعادة تحميل الإضافة، أغلق نافذتها وافتحها مجددًا.
engineError|تعذّر تحميل محرك QR. أعد فتح الصفحة أو الإضافة.
noHistory|لا يُحفَظ سجل لرموز QR
readyScan|جاهز للمسح
readerHint|اختر لقطة شاشة أو اسحبها أو الصقها.
chooseBrowser|اختر متصفحك
downloadFor|تنزيل من أجل
statusError|تحقق من الحقل المحدد.
noPassword|شبكة مفتوحة
formatHint|رمز ثابت · PNG وSVG · معالجة على جهازك
sendEmail|إرسال بريد إلكتروني
latestBadge|أحدث إصدار
step|الخطوة
customize|تخصيص
automaticPreview|معاينة مباشرة
autoLanguage|تلقائي (لغة المتصفح)
chromeStore|إضافة إلى Chrome
'''
}

NEW = {
'en': '''
updates|Updates
supportDeveloper|Support the developer
supportDesc|Share feedback or leave an honest store review. It is optional, and every feature remains free.
reviewTitle|Enjoying QR Scanner?
reviewDesc|An honest review helps others discover the project and helps us improve it.
reviewChrome|Review on Chrome
reviewEdge|Review on Edge
reviewLater|Maybe later
updateAvailable|New version available
updatedTitle|QR Scanner has been updated
installedTitle|Welcome to QR Scanner
updateIntro|Version 1.1.3 is installed. Explore the improvements and continue with your QR tools.
installIntroTitle|Your QR toolkit is ready
releaseHighlights|Release highlights
featureMotion|A smoother interface with motion that respects reduced-motion preferences.
featureLanguages|Eight languages, including Russian and Arabic with right-to-left layout.
featureMultiScan|Find multiple QR codes in one image and choose the result you need.
featureUpdates|Clear release notes after a real extension update, with optional desktop notifications.
whatsNew|What’s new
continueTools|Continue to tools
updatePrivacy|Images, screenshots, tab URLs, QR contents, Wi-Fi passwords, contact cards and SMS data stay on your device. Version checks contact qr.haking.tr without sending this content.
reviewOpen|Open store review
scrollExplore|Scroll to explore
storyTitle|From a code to a possibility.
storyScan|See what is inside.
storyCreate|Make it yours.
storyShare|Ready to share.
storyScanDesc|Read an image, a screenshot or the current tab. Review every result before opening a link.
storyCreateDesc|Turn a link, text, Wi-Fi details, email, phone number, SMS or contact card into a QR code.
storyShareDesc|Export a crisp PNG or scalable SVG. Your static codes have no expiry.
storyPrivacy|Your data. Your device.
storyPrivacyDesc|QR processing stays local. No account, tracking or QR history.
allCodes|All QR codes
selectCode|Select a code
scanCount|QR codes found
notificationTitle|QR Scanner {version} is available
notificationBody|A newer version is ready. Open the release page to see how to update.
releaseNotes|Release notes
updateSettings|Update settings
autoUpdates|How updates work
autoUpdatesDesc|Store installations are updated by the browser. Unpacked ZIP installations must be replaced manually. The hosted version JSON only checks availability; it never installs or runs code.
updateNotice|A newer release is available. It is not installed yet.
lastVersion|Installed version
securityNoticeTitle|Check before you open
securityNoticeDesc|A QR code can point anywhere. Review the full destination; HTTPS alone does not prove a site is trustworthy.
noDataUploaded|QR contents, images, screenshots, tab URLs, Wi-Fi details, contact cards and SMS data are not uploaded.
notificationsEnable|Enable update notifications
notificationsEnabled|Update notifications enabled
notificationsDenied|Notifications are blocked. You can change this in your browser settings.
copyAll|Copy all results
notificationPermission|Optional desktop notifications let you know when a newer release is available. Allow them only if you want these alerts.
versionLabel|Version
updateInstalledBody|QR Scanner {version} is now installed. See what changed in this release.
compat|Chrome and Edge: official store listings. Brave and Opera: Chromium ZIP. Firefox: separate package for temporary testing until signed. A Safari extension has not been released.
downloadNote|Chrome and Edge store releases may differ from the ZIP. ZIP packages contain v1.1.3. Firefox ZIP is for temporary testing until signed.
a4|Use the website in modern browsers. Official Chrome and Edge store listings are available. Chromium ZIPs can be installed manually. Firefox needs signing for permanent installation; Safari currently uses the web tools.
''',
'tr': '''
updates|Güncellemeler
supportDeveloper|Geliştiriciye destek ol
supportDesc|Geri bildirim paylaş veya mağazada dürüst bir yorum bırak. Tamamen isteğe bağlı; tüm özellikler ücretsiz kalır.
reviewTitle|QR Scanner işine yarıyor mu?
reviewDesc|Dürüst bir yorum, başkalarının projeyi keşfetmesine ve bizim geliştirmemize yardımcı olur.
reviewChrome|Chrome’da yorum yap
reviewEdge|Edge’de yorum yap
reviewLater|Belki daha sonra
updateAvailable|Yeni sürüm mevcut
updatedTitle|QR Scanner güncellendi
installedTitle|QR Scanner’a hoş geldin
updateIntro|1.1.3 sürümü kuruldu. Yenilikleri keşfet, ardından QR araçlarını kullanmaya devam et.
installIntroTitle|QR araçların hazır
releaseHighlights|Bu sürümde öne çıkanlar
featureMotion|Hareketi azaltma tercihine uyan, daha akıcı bir arayüz.
featureLanguages|Sağdan sola arayüzüyle Arapça ve Rusça dahil sekiz dil.
featureMultiScan|Tek bir görselde birden fazla QR kod bul, istediğin sonucu seç.
featureUpdates|Gerçek uzantı güncellemesinden sonra anlaşılır sürüm notları ve isteğe bağlı masaüstü bildirimleri.
whatsNew|Neler yeni?
continueTools|Araçlara devam et
updatePrivacy|Görseller, ekran görüntüleri, sekme adresleri, QR içerikleri, Wi-Fi şifreleri, kişi kartları ve SMS verileri cihazında kalır. Sürüm kontrolü bu içerikleri göndermeden qr.haking.tr adresine bağlanır.
reviewOpen|Mağazada yorum sayfasını aç
scrollExplore|Keşfetmek için kaydır
storyTitle|Bir koddan yeni olasılıklara.
storyScan|İçinde ne olduğunu gör.
storyCreate|Kendininkini oluştur.
storyShare|Paylaşmaya hazır.
storyScanDesc|Görseli, ekran görüntüsünü veya açık sekmeyi oku. Bağlantıyı açmadan önce her sonucu incele.
storyCreateDesc|Bağlantı, metin, Wi-Fi bilgisi, e-posta, telefon, SMS veya kişi kartını QR koda dönüştür.
storyShareDesc|Net bir PNG veya ölçeklenebilir SVG indir. Statik kodlarının süresi dolmaz.
storyPrivacy|Verilerin. Kendi cihazın.
storyPrivacyDesc|QR işlemleri yerel kalır. Hesap, takip veya QR geçmişi yok.
allCodes|Tüm QR kodlar
selectCode|Bir kod seç
scanCount|Bulunan QR kodlar
notificationTitle|QR Scanner {version} sürümü mevcut
notificationBody|Daha yeni bir sürüm hazır. Nasıl güncelleyeceğini görmek için sürüm sayfasını aç.
releaseNotes|Sürüm notları
updateSettings|Güncelleme ayarları
autoUpdates|Güncellemeler nasıl çalışır?
autoUpdatesDesc|Mağazadan kurulan uzantıyı tarayıcı günceller. ZIP ile kurulan dosyalar elle yenilenmelidir. Sitedeki sürüm JSON’u yalnızca yeni sürümü kontrol eder; kod kurmaz veya çalıştırmaz.
updateNotice|Daha yeni bir sürüm mevcut. Henüz kurulmadı.
lastVersion|Kurulu sürüm
securityNoticeTitle|Açmadan önce kontrol et
securityNoticeDesc|QR kod herhangi bir adrese yönlendirebilir. Tam adresi incele; HTTPS tek başına güvenilirlik kanıtı değildir.
noDataUploaded|QR içerikleri, görseller, ekran görüntüleri, sekme adresleri, Wi-Fi bilgileri, kişi kartları ve SMS verileri yüklenmez.
notificationsEnable|Güncelleme bildirimlerini aç
notificationsEnabled|Güncelleme bildirimleri açık
notificationsDenied|Bildirimler engellenmiş. Tarayıcı ayarlarından değiştirebilirsin.
copyAll|Tüm sonuçları kopyala
notificationPermission|İsteğe bağlı masaüstü bildirimleri yeni sürüm çıktığında haber verir. Bu uyarıları istiyorsan izin ver.
versionLabel|Sürüm
updateInstalledBody|QR Scanner {version} artık kurulu. Bu sürümdeki değişiklikleri incele.
compat|Chrome ve Edge: resmi mağaza bağlantıları. Brave ve Opera: Chromium ZIP. Firefox: imzalanana kadar geçici test için ayrı paket. Safari uzantısı henüz yayımlanmadı.
downloadNote|Chrome ve Edge mağaza sürümleri ZIP’ten farklı olabilir. ZIP paketleri v1.1.3 içerir. Firefox ZIP, imzalanana kadar geçici test içindir.
a4|Siteyi güncel tarayıcılarda kullanabilirsin. Resmi Chrome ve Edge mağaza bağlantıları mevcut. Chromium ZIP paketleri elle kurulabilir. Firefox kalıcı kurulum için imza gerektirir; Safari’de şimdilik web araçları kullanılabilir.
''',
'de': '''
updates|Updates
supportDeveloper|Entwicklung unterstützen
supportDesc|Teile Feedback oder hinterlasse eine ehrliche Bewertung im Store. Das ist freiwillig; alle Funktionen bleiben kostenlos.
reviewTitle|Hilft dir QR Scanner?
reviewDesc|Eine ehrliche Bewertung hilft anderen, das Projekt zu entdecken, und uns, es zu verbessern.
reviewChrome|In Chrome bewerten
reviewEdge|In Edge bewerten
reviewLater|Vielleicht später
updateAvailable|Neue Version verfügbar
updatedTitle|QR Scanner wurde aktualisiert
installedTitle|Willkommen bei QR Scanner
updateIntro|Version 1.1.3 ist installiert. Entdecke die Verbesserungen und nutze deine QR-Werkzeuge weiter.
installIntroTitle|Deine QR-Werkzeuge sind bereit
releaseHighlights|Das bringt diese Version
featureMotion|Eine flüssigere Oberfläche, die deine Einstellung für reduzierte Bewegung berücksichtigt.
featureLanguages|Acht Sprachen, darunter Russisch und Arabisch mit Schreibrichtung von rechts nach links.
featureMultiScan|Finde mehrere QR-Codes in einem Bild und wähle das gewünschte Ergebnis.
featureUpdates|Übersichtliche Versionshinweise nach einem tatsächlichen Erweiterungsupdate und freiwillige Desktop-Benachrichtigungen.
whatsNew|Was ist neu?
continueTools|Weiter zu den Werkzeugen
updatePrivacy|Bilder, Screenshots, Tab-Adressen, QR-Inhalte, WLAN-Passwörter, Kontaktkarten und SMS-Daten bleiben auf deinem Gerät. Versionsprüfungen kontaktieren qr.haking.tr, ohne diese Inhalte zu senden.
reviewOpen|Bewertung im Store öffnen
scrollExplore|Zum Entdecken scrollen
storyTitle|Vom Code zur Möglichkeit.
storyScan|Entdecke den Inhalt.
storyCreate|Gestalte deinen eigenen Code.
storyShare|Bereit zum Teilen.
storyScanDesc|Lies ein Bild, einen Screenshot oder den aktuellen Tab. Prüfe jedes Ergebnis, bevor du einen Link öffnest.
storyCreateDesc|Verwandle Links, Texte, WLAN-Daten, E-Mails, Telefonnummern, SMS oder Kontaktkarten in QR-Codes.
storyShareDesc|Exportiere scharfe PNGs oder skalierbare SVGs. Deine statischen Codes laufen nicht ab.
storyPrivacy|Deine Daten. Dein Gerät.
storyPrivacyDesc|QR-Verarbeitung bleibt lokal. Ohne Konto, Tracking oder QR-Verlauf.
allCodes|Alle QR-Codes
selectCode|Code auswählen
scanCount|Gefundene QR-Codes
notificationTitle|QR Scanner {version} ist verfügbar
notificationBody|Eine neuere Version ist bereit. Öffne die Versionsseite und erfahre, wie du aktualisieren kannst.
releaseNotes|Versionshinweise
updateSettings|Update-Einstellungen
autoUpdates|So funktionieren Updates
autoUpdatesDesc|Store-Installationen aktualisiert der Browser. Entpackte ZIP-Installationen müssen manuell ersetzt werden. Die Versions-JSON prüft nur die Verfügbarkeit und installiert oder startet keinen Code.
updateNotice|Eine neuere Version ist verfügbar. Sie ist noch nicht installiert.
lastVersion|Installierte Version
securityNoticeTitle|Vor dem Öffnen prüfen
securityNoticeDesc|Ein QR-Code kann auf jede Adresse verweisen. Prüfe das vollständige Ziel; HTTPS allein beweist keine Vertrauenswürdigkeit.
noDataUploaded|QR-Inhalte, Bilder, Screenshots, Tab-Adressen, WLAN-Daten, Kontaktkarten und SMS-Daten werden nicht hochgeladen.
notificationsEnable|Update-Benachrichtigungen aktivieren
notificationsEnabled|Update-Benachrichtigungen aktiviert
notificationsDenied|Benachrichtigungen sind blockiert. Du kannst dies in den Browsereinstellungen ändern.
copyAll|Alle Ergebnisse kopieren
notificationPermission|Freiwillige Desktop-Benachrichtigungen informieren dich über neue Versionen. Erlaube sie nur, wenn du diese Hinweise möchtest.
versionLabel|Version
updateInstalledBody|QR Scanner {version} ist jetzt installiert. Sieh dir die Änderungen dieser Version an.
compat|Chrome und Edge: offizielle Store-Einträge. Brave und Opera: Chromium-ZIP. Firefox: eigenes Paket für temporäre Tests bis zur Signierung. Eine Safari-Erweiterung wurde noch nicht veröffentlicht.
downloadNote|Store-Versionen für Chrome und Edge können vom ZIP abweichen. ZIP-Pakete enthalten v1.1.3. Das Firefox-ZIP ist bis zur Signierung für temporäre Tests bestimmt.
a4|Die Webseite funktioniert in aktuellen Browsern. Offizielle Einträge im Chrome- und Edge-Store sind verfügbar. Chromium-ZIPs lassen sich manuell installieren. Firefox benötigt eine Signierung für dauerhafte Installationen; Safari nutzt derzeit die Web-Werkzeuge.
''',
'es': '''
updates|Actualizaciones
supportDeveloper|Apoya al desarrollador
supportDesc|Comparte tus comentarios o deja una reseña sincera en la tienda. Es opcional y todas las funciones siguen siendo gratuitas.
reviewTitle|¿Te resulta útil QR Scanner?
reviewDesc|Una reseña sincera ayuda a otras personas a descubrir el proyecto y a nosotros a mejorarlo.
reviewChrome|Opinar en Chrome
reviewEdge|Opinar en Edge
reviewLater|Quizá más tarde
updateAvailable|Nueva versión disponible
updatedTitle|QR Scanner se ha actualizado
installedTitle|Te damos la bienvenida a QR Scanner
updateIntro|La versión 1.1.3 está instalada. Descubre las mejoras y continúa con tus herramientas QR.
installIntroTitle|Tus herramientas QR están listas
releaseHighlights|Novedades destacadas
featureMotion|Una interfaz más fluida que respeta la preferencia de movimiento reducido.
featureLanguages|Ocho idiomas, incluidos ruso y árabe con diseño de derecha a izquierda.
featureMultiScan|Encuentra varios códigos QR en una imagen y elige el resultado que necesitas.
featureUpdates|Notas claras tras una actualización real de la extensión y notificaciones de escritorio opcionales.
whatsNew|Qué hay de nuevo
continueTools|Ir a las herramientas
updatePrivacy|Las imágenes, capturas, direcciones de pestañas, contenidos QR, contraseñas Wi-Fi, contactos y datos SMS permanecen en tu dispositivo. La comprobación de versiones contacta con qr.haking.tr sin enviar estos contenidos.
reviewOpen|Abrir reseña en la tienda
scrollExplore|Desplázate para descubrir más
storyTitle|De un código a una posibilidad.
storyScan|Descubre su contenido.
storyCreate|Hazlo tuyo.
storyShare|Listo para compartir.
storyScanDesc|Lee una imagen, una captura o la pestaña actual. Revisa cada resultado antes de abrir un enlace.
storyCreateDesc|Convierte enlaces, texto, datos Wi-Fi, correos, teléfonos, SMS o contactos en códigos QR.
storyShareDesc|Exporta un PNG nítido o un SVG escalable. Tus códigos estáticos no caducan.
storyPrivacy|Tus datos. Tu dispositivo.
storyPrivacyDesc|El procesamiento QR es local. Sin cuenta, rastreo ni historial QR.
allCodes|Todos los códigos QR
selectCode|Selecciona un código
scanCount|Códigos QR encontrados
notificationTitle|QR Scanner {version} está disponible
notificationBody|Hay una versión nueva. Abre la página de versiones para ver cómo actualizar.
releaseNotes|Notas de la versión
updateSettings|Ajustes de actualización
autoUpdates|Cómo funcionan las actualizaciones
autoUpdatesDesc|El navegador actualiza las instalaciones de la tienda. Las instalaciones desde ZIP se sustituyen manualmente. El JSON de versiones solo comprueba la disponibilidad; nunca instala ni ejecuta código.
updateNotice|Hay una versión más reciente. Todavía no está instalada.
lastVersion|Versión instalada
securityNoticeTitle|Comprueba antes de abrir
securityNoticeDesc|Un código QR puede apuntar a cualquier dirección. Revisa el destino completo; HTTPS por sí solo no demuestra que un sitio sea fiable.
noDataUploaded|No se suben contenidos QR, imágenes, capturas, direcciones de pestañas, datos Wi-Fi, contactos ni datos SMS.
notificationsEnable|Activar avisos de actualización
notificationsEnabled|Avisos de actualización activados
notificationsDenied|Las notificaciones están bloqueadas. Puedes cambiarlo en los ajustes del navegador.
copyAll|Copiar todos los resultados
notificationPermission|Las notificaciones de escritorio opcionales te avisan cuando hay una versión nueva. Permítelas solo si deseas recibir estos avisos.
versionLabel|Versión
updateInstalledBody|QR Scanner {version} ya está instalado. Consulta los cambios de esta versión.
compat|Chrome y Edge: tiendas oficiales. Brave y Opera: ZIP Chromium. Firefox: paquete independiente para pruebas temporales hasta su firma. Aún no se ha publicado una extensión para Safari.
downloadNote|Las versiones de las tiendas de Chrome y Edge pueden diferir del ZIP. Los paquetes ZIP contienen v1.1.3. El ZIP de Firefox es para pruebas temporales hasta su firma.
a4|Usa el sitio en navegadores modernos. Hay versiones oficiales en las tiendas de Chrome y Edge. Los ZIP Chromium se instalan manualmente. Firefox exige firma para instalaciones permanentes; en Safari puedes usar las herramientas web.
''',
'fr': '''
updates|Mises à jour
supportDeveloper|Soutenir le développeur
supportDesc|Partagez vos retours ou laissez un avis sincère sur la boutique. C’est facultatif et toutes les fonctions restent gratuites.
reviewTitle|QR Scanner vous est utile ?
reviewDesc|Un avis sincère aide d’autres personnes à découvrir le projet et nous aide à l’améliorer.
reviewChrome|Donner un avis sur Chrome
reviewEdge|Donner un avis sur Edge
reviewLater|Peut-être plus tard
updateAvailable|Nouvelle version disponible
updatedTitle|QR Scanner a été mis à jour
installedTitle|Bienvenue dans QR Scanner
updateIntro|La version 1.1.3 est installée. Découvrez les améliorations, puis retrouvez vos outils QR.
installIntroTitle|Vos outils QR sont prêts
releaseHighlights|Les nouveautés à retenir
featureMotion|Une interface plus fluide qui respecte votre préférence de réduction des animations.
featureLanguages|Huit langues, dont le russe et l’arabe avec une mise en page de droite à gauche.
featureMultiScan|Repérez plusieurs codes QR dans une image et choisissez le résultat souhaité.
featureUpdates|Des notes claires après une véritable mise à jour de l’extension et des notifications de bureau facultatives.
whatsNew|Quoi de neuf ?
continueTools|Accéder aux outils
updatePrivacy|Images, captures, adresses des onglets, contenus QR, mots de passe Wi-Fi, contacts et données SMS restent sur votre appareil. La vérification de version contacte qr.haking.tr sans envoyer ces contenus.
reviewOpen|Ouvrir les avis de la boutique
scrollExplore|Faites défiler pour découvrir
storyTitle|D’un code à une possibilité.
storyScan|Découvrez son contenu.
storyCreate|Créez le vôtre.
storyShare|Prêt à partager.
storyScanDesc|Lisez une image, une capture ou l’onglet actuel. Vérifiez chaque résultat avant d’ouvrir un lien.
storyCreateDesc|Transformez liens, textes, informations Wi-Fi, e-mails, téléphones, SMS ou contacts en codes QR.
storyShareDesc|Exportez un PNG net ou un SVG redimensionnable. Vos codes statiques n’expirent pas.
storyPrivacy|Vos données. Votre appareil.
storyPrivacyDesc|Le traitement QR reste local. Sans compte, suivi ni historique QR.
allCodes|Tous les codes QR
selectCode|Choisir un code
scanCount|Codes QR trouvés
notificationTitle|QR Scanner {version} est disponible
notificationBody|Une nouvelle version est prête. Ouvrez la page des versions pour savoir comment effectuer la mise à jour.
releaseNotes|Notes de version
updateSettings|Paramètres de mise à jour
autoUpdates|Fonctionnement des mises à jour
autoUpdatesDesc|Le navigateur met à jour les installations provenant des boutiques. Les installations ZIP sont à remplacer manuellement. Le JSON de version vérifie seulement la disponibilité ; il n’installe ni n’exécute de code.
updateNotice|Une version plus récente est disponible. Elle n’est pas encore installée.
lastVersion|Version installée
securityNoticeTitle|Vérifiez avant d’ouvrir
securityNoticeDesc|Un code QR peut mener à n’importe quelle adresse. Vérifiez la destination complète ; HTTPS seul ne prouve pas la fiabilité d’un site.
noDataUploaded|Aucun contenu QR, image, capture, adresse d’onglet, information Wi-Fi, contact ou donnée SMS n’est envoyé.
notificationsEnable|Activer les alertes de mise à jour
notificationsEnabled|Alertes de mise à jour activées
notificationsDenied|Les notifications sont bloquées. Vous pouvez modifier cela dans les paramètres du navigateur.
copyAll|Copier tous les résultats
notificationPermission|Les notifications de bureau facultatives signalent les nouvelles versions. Autorisez-les uniquement si vous souhaitez recevoir ces alertes.
versionLabel|Version
updateInstalledBody|QR Scanner {version} est maintenant installé. Découvrez les changements de cette version.
compat|Chrome et Edge : boutiques officielles. Brave et Opera : ZIP Chromium. Firefox : paquet distinct pour tests temporaires avant signature. Aucune extension Safari n’est encore publiée.
downloadNote|Les versions des boutiques Chrome et Edge peuvent différer du ZIP. Les paquets ZIP contiennent la v1.1.3. Le ZIP Firefox sert aux tests temporaires avant signature.
a4|Utilisez le site dans un navigateur récent. Des versions officielles sont disponibles dans les boutiques Chrome et Edge. Les ZIP Chromium s’installent manuellement. Firefox exige une signature pour une installation permanente ; Safari utilise actuellement les outils web.
''',
'pt': '''
updates|Atualizações
supportDeveloper|Apoie o desenvolvedor
supportDesc|Envie sugestões ou deixe uma avaliação sincera na loja. É opcional, e todos os recursos continuam gratuitos.
reviewTitle|Gostando do QR Scanner?
reviewDesc|Uma avaliação sincera ajuda outras pessoas a descobrir o projeto e nos ajuda a melhorá-lo.
reviewChrome|Avaliar no Chrome
reviewEdge|Avaliar no Edge
reviewLater|Talvez depois
updateAvailable|Nova versão disponível
updatedTitle|QR Scanner foi atualizado
installedTitle|Boas-vindas ao QR Scanner
updateIntro|A versão 1.1.3 está instalada. Conheça as melhorias e continue usando suas ferramentas QR.
installIntroTitle|Suas ferramentas QR estão prontas
releaseHighlights|Destaques da versão
featureMotion|Uma interface mais fluida que respeita a preferência de movimento reduzido.
featureLanguages|Oito idiomas, incluindo russo e árabe com layout da direita para a esquerda.
featureMultiScan|Encontre vários códigos QR em uma imagem e escolha o resultado desejado.
featureUpdates|Notas claras após uma atualização real da extensão e notificações opcionais na área de trabalho.
whatsNew|O que há de novo
continueTools|Ir para as ferramentas
updatePrivacy|Imagens, capturas, endereços de abas, conteúdos QR, senhas Wi-Fi, contatos e dados SMS ficam no seu dispositivo. A verificação de versão acessa qr.haking.tr sem enviar esses conteúdos.
reviewOpen|Abrir avaliação na loja
scrollExplore|Role para explorar
storyTitle|De um código a uma possibilidade.
storyScan|Descubra o conteúdo.
storyCreate|Crie do seu jeito.
storyShare|Pronto para compartilhar.
storyScanDesc|Leia uma imagem, uma captura ou a aba atual. Confira cada resultado antes de abrir um link.
storyCreateDesc|Transforme links, textos, dados Wi-Fi, e-mails, telefones, SMS ou contatos em códigos QR.
storyShareDesc|Exporte um PNG nítido ou um SVG escalável. Seus códigos estáticos não expiram.
storyPrivacy|Seus dados. Seu dispositivo.
storyPrivacyDesc|O processamento QR é local. Sem conta, rastreamento ou histórico QR.
allCodes|Todos os códigos QR
selectCode|Selecione um código
scanCount|Códigos QR encontrados
notificationTitle|QR Scanner {version} está disponível
notificationBody|Uma nova versão está pronta. Abra a página da versão para saber como atualizar.
releaseNotes|Notas da versão
updateSettings|Configurações de atualização
autoUpdates|Como as atualizações funcionam
autoUpdatesDesc|O navegador atualiza instalações feitas pela loja. Instalações por ZIP precisam ser substituídas manualmente. O JSON de versão só verifica a disponibilidade; nunca instala nem executa código.
updateNotice|Há uma versão mais recente disponível. Ela ainda não está instalada.
lastVersion|Versão instalada
securityNoticeTitle|Confira antes de abrir
securityNoticeDesc|Um código QR pode apontar para qualquer endereço. Confira o destino completo; HTTPS sozinho não garante que um site seja confiável.
noDataUploaded|Conteúdos QR, imagens, capturas, endereços de abas, dados Wi-Fi, contatos e dados SMS não são enviados.
notificationsEnable|Ativar avisos de atualização
notificationsEnabled|Avisos de atualização ativados
notificationsDenied|As notificações estão bloqueadas. Você pode mudar isso nas configurações do navegador.
copyAll|Copiar todos os resultados
notificationPermission|Notificações opcionais na área de trabalho avisam quando há uma nova versão. Permita apenas se quiser receber esses alertas.
versionLabel|Versão
updateInstalledBody|QR Scanner {version} já está instalado. Confira as mudanças desta versão.
compat|Chrome e Edge: lojas oficiais. Brave e Opera: ZIP Chromium. Firefox: pacote separado para testes temporários até ser assinado. A extensão para Safari ainda não foi publicada.
downloadNote|As versões nas lojas do Chrome e Edge podem diferir do ZIP. Os pacotes ZIP contêm a v1.1.3. O ZIP do Firefox é para testes temporários até ser assinado.
a4|Use o site em navegadores modernos. Há versões oficiais nas lojas do Chrome e Edge. Os ZIP Chromium podem ser instalados manualmente. O Firefox exige assinatura para instalação permanente; o Safari usa as ferramentas web por enquanto.
''',
'ru': '''
updates|Обновления
supportDeveloper|Поддержать разработчика
supportDesc|Поделитесь мнением или оставьте честный отзыв в магазине. Это необязательно; все функции остаются бесплатными.
reviewTitle|Вам нравится QR Scanner?
reviewDesc|Честный отзыв помогает другим найти проект, а нам — сделать его лучше.
reviewChrome|Отзыв в Chrome
reviewEdge|Отзыв в Edge
reviewLater|Может быть, позже
updateAvailable|Доступна новая версия
updatedTitle|QR Scanner обновлён
installedTitle|Добро пожаловать в QR Scanner
updateIntro|Версия 1.1.3 установлена. Узнайте об улучшениях и продолжайте пользоваться инструментами QR.
installIntroTitle|Ваши инструменты QR готовы
releaseHighlights|Главное в этом выпуске
featureMotion|Более плавный интерфейс с учётом настройки уменьшения движения.
featureLanguages|Восемь языков, включая русский и арабский с интерфейсом справа налево.
featureMultiScan|Находите несколько QR-кодов на одном изображении и выбирайте нужный результат.
featureUpdates|Понятные заметки после фактического обновления расширения и необязательные уведомления на рабочем столе.
whatsNew|Что нового
continueTools|Перейти к инструментам
updatePrivacy|Изображения, снимки экрана, адреса вкладок, содержимое QR, пароли Wi-Fi, карточки контактов и данные SMS остаются на вашем устройстве. Проверка версии обращается к qr.haking.tr без отправки этих данных.
reviewOpen|Открыть отзывы в магазине
scrollExplore|Прокрутите, чтобы узнать больше
storyTitle|От кода — к новым возможностям.
storyScan|Узнайте, что внутри.
storyCreate|Создайте свой код.
storyShare|Готово к отправке.
storyScanDesc|Считайте изображение, снимок экрана или текущую вкладку. Проверьте каждый результат перед открытием ссылки.
storyCreateDesc|Превратите ссылку, текст, данные Wi-Fi, письмо, номер телефона, SMS или карточку контакта в QR-код.
storyShareDesc|Скачайте чёткий PNG или масштабируемый SVG. Ваши статические коды не имеют срока действия.
storyPrivacy|Ваши данные. Ваше устройство.
storyPrivacyDesc|Обработка QR выполняется локально. Без регистрации, отслеживания и истории кодов.
allCodes|Все QR-коды
selectCode|Выберите код
scanCount|Найдено QR-кодов
notificationTitle|Доступен QR Scanner {version}
notificationBody|Готова новая версия. Откройте страницу выпуска, чтобы узнать, как обновить расширение.
releaseNotes|История изменений
updateSettings|Настройки обновлений
autoUpdates|Как работают обновления
autoUpdatesDesc|Установки из магазина обновляет браузер. Файлы распакованного ZIP нужно заменять вручную. JSON с версией только проверяет доступность — он не устанавливает и не запускает код.
updateNotice|Доступен новый выпуск. Он ещё не установлен.
lastVersion|Установленная версия
securityNoticeTitle|Проверьте перед открытием
securityNoticeDesc|QR-код может вести куда угодно. Проверьте полный адрес: сам по себе HTTPS не доказывает надёжность сайта.
noDataUploaded|Содержимое QR, изображения, снимки экрана, адреса вкладок, данные Wi-Fi, контакты и данные SMS не загружаются на сервер.
notificationsEnable|Включить уведомления об обновлениях
notificationsEnabled|Уведомления об обновлениях включены
notificationsDenied|Уведомления заблокированы. Это можно изменить в настройках браузера.
copyAll|Копировать все результаты
notificationPermission|Необязательные уведомления на рабочем столе сообщат о новой версии. Разрешите их, только если хотите получать такие сообщения.
versionLabel|Версия
updateInstalledBody|QR Scanner {version} установлен. Узнайте, что изменилось в этом выпуске.
compat|Chrome и Edge: официальные магазины. Brave и Opera: ZIP Chromium. Firefox: отдельный пакет для временного тестирования до подписания. Расширение для Safari пока не выпущено.
downloadNote|Версии в магазинах Chrome и Edge могут отличаться от ZIP. ZIP-пакеты содержат v1.1.3. Пакет Firefox предназначен для временного тестирования до подписания.
a4|Сайт работает в современных браузерах. Доступны официальные страницы в магазинах Chrome и Edge. ZIP Chromium можно установить вручную. Для постоянной установки Firefox нужна подпись; в Safari пока доступны веб-инструменты.
''',
'ar': '''
updates|التحديثات
supportDeveloper|ادعم المطوّر
supportDesc|شارك ملاحظاتك أو اترك تقييمًا صادقًا في المتجر. الأمر اختياري، وتبقى جميع الميزات مجانية.
reviewTitle|هل أعجبك QR Scanner؟
reviewDesc|يساعد التقييم الصادق الآخرين على اكتشاف المشروع ويساعدنا على تحسينه.
reviewChrome|التقييم في Chrome
reviewEdge|التقييم في Edge
reviewLater|ربما لاحقًا
updateAvailable|يتوفر إصدار جديد
updatedTitle|تم تحديث QR Scanner
installedTitle|مرحبًا بك في QR Scanner
updateIntro|تم تثبيت الإصدار 1.1.3. اكتشف التحسينات ثم تابع استخدام أدوات QR.
installIntroTitle|أدوات QR جاهزة
releaseHighlights|أبرز مستجدات الإصدار
featureMotion|واجهة أكثر سلاسة تراعي تفضيل تقليل الحركة.
featureLanguages|ثماني لغات، منها الروسية والعربية مع تخطيط من اليمين إلى اليسار.
featureMultiScan|اعثر على عدة رموز QR في صورة واحدة واختر النتيجة المطلوبة.
featureUpdates|ملاحظات واضحة بعد التحديث الفعلي للإضافة، مع إشعارات سطح مكتب اختيارية.
whatsNew|ما الجديد؟
continueTools|الانتقال إلى الأدوات
updatePrivacy|تبقى الصور ولقطات الشاشة وعناوين الصفحات ومحتويات QR وكلمات مرور Wi-Fi وبطاقات الاتصال وبيانات الرسائل النصية على جهازك. يتصل فحص الإصدار بموقع qr.haking.tr دون إرسال هذه المحتويات.
reviewOpen|فتح صفحة التقييم في المتجر
scrollExplore|مرّر لاستكشاف المزيد
storyTitle|من رمز إلى إمكانات جديدة.
storyScan|اكتشف ما بداخله.
storyCreate|أنشئ رمزك الخاص.
storyShare|جاهز للمشاركة.
storyScanDesc|اقرأ صورة أو لقطة شاشة أو الصفحة الحالية. راجع كل نتيجة قبل فتح أي رابط.
storyCreateDesc|حوّل رابطًا أو نصًا أو معلومات Wi-Fi أو بريدًا أو رقم هاتف أو رسالة نصية أو بطاقة اتصال إلى رمز QR.
storyShareDesc|صدّر PNG واضحًا أو SVG قابلًا للتحجيم. لا تنتهي صلاحية رموزك الثابتة.
storyPrivacy|بياناتك. جهازك.
storyPrivacyDesc|تُعالَج الرموز محليًا. دون حساب أو تتبع أو سجل للرموز.
allCodes|جميع رموز QR
selectCode|اختر رمزًا
scanCount|رموز QR التي عُثر عليها
notificationTitle|يتوفر QR Scanner {version}
notificationBody|إصدار أحدث جاهز. افتح صفحة الإصدار لمعرفة طريقة التحديث.
releaseNotes|ملاحظات الإصدار
updateSettings|إعدادات التحديث
autoUpdates|كيف تعمل التحديثات؟
autoUpdatesDesc|يحدّث المتصفح الإضافات المثبتة من المتجر. يجب استبدال ملفات التثبيت من ZIP يدويًا. يفحص ملف JSON توفر إصدار جديد فقط، ولا يثبت أي كود أو يشغله.
updateNotice|يتوفر إصدار أحدث، لكنه لم يُثبَّت بعد.
lastVersion|الإصدار المثبّت
securityNoticeTitle|تحقق قبل الفتح
securityNoticeDesc|قد يشير رمز QR إلى أي عنوان. راجع الوجهة كاملة؛ لا يثبت HTTPS وحده أن الموقع موثوق.
noDataUploaded|لا تُرفَع محتويات QR أو الصور أو لقطات الشاشة أو عناوين الصفحات أو معلومات Wi-Fi أو بطاقات الاتصال أو بيانات الرسائل النصية.
notificationsEnable|تفعيل إشعارات التحديث
notificationsEnabled|إشعارات التحديث مفعّلة
notificationsDenied|الإشعارات محظورة. يمكنك تغيير ذلك في إعدادات المتصفح.
copyAll|نسخ جميع النتائج
notificationPermission|تنبهك إشعارات سطح المكتب الاختيارية عند توفر إصدار أحدث. اسمح بها فقط إذا أردت تلقي هذه التنبيهات.
versionLabel|الإصدار
updateInstalledBody|تم تثبيت QR Scanner {version}. تعرّف على تغييرات هذا الإصدار.
compat|Chrome وEdge: المتاجر الرسمية. Brave وOpera: حزمة Chromium بصيغة ZIP. Firefox: حزمة منفصلة للاختبار المؤقت إلى حين توقيعها. لم تصدر إضافة Safari بعد.
downloadNote|قد تختلف إصدارات متجري Chrome وEdge عن ZIP. تحتوي حزم ZIP على v1.1.3. حزمة Firefox للاختبار المؤقت إلى حين توقيعها.
a4|يعمل الموقع في المتصفحات الحديثة. تتوفر صفحات رسمية في متجري Chrome وEdge. يمكن تثبيت ZIP الخاص بـChromium يدويًا. يتطلب Firefox توقيعًا للتثبيت الدائم، وتتوفر حاليًا أدوات الموقع لمستخدمي Safari.
'''
}

def parse(block):
    entries = [line.split('|', 1) for line in block.strip().splitlines()]
    result = dict(entries)
    if len(entries) != len(result) or any(not value.strip() for value in result.values()):
        raise ValueError('Duplicate key or empty translation')
    return result

def apply(data):
    base_keys = set(data['en']) - (set(parse(NEW['en'])) - set(parse(BASE['ru'])))
    for language, block in BASE.items():
        translated = parse(block)
        missing, extra = base_keys - translated.keys(), translated.keys() - base_keys
        if missing or extra:
            raise ValueError(f'{language}: missing={sorted(missing)}, extra={sorted(extra)}')
        data[language] = translated
    for language, block in NEW.items():
        data[language].update(parse(block))
        data[language] = {key: value.replace('1.1.2', '1.1.3') for key, value in data[language].items()}
    expected = set(data['en'])
    for language, values in data.items():
        if set(values) != expected or any(not isinstance(v, str) or not v.strip() for v in values.values()):
            raise ValueError(f'{language}: incomplete or blank translation')
        if '{version}' not in values['notificationTitle']:
            raise ValueError(f'{language}: missing notification version placeholder')
        data[language] = {key: values[key] for key in data['en']}
    return data

def main():
    path = Path(__file__).resolve().parents[1] / 'shared' / 'locales.json'
    data = apply(json.loads(path.read_text(encoding='utf-8-sig')))
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Prepared {len(data)} complete locales, {len(data["en"])} keys each, version 1.1.3.')

if __name__ == '__main__':
    main()
