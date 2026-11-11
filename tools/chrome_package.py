"""Build a local Chrome Web Store submission; never uploads or publishes."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT=Path(__file__).resolve().parents[1]
INTRO={
'tr':'QR Scanner, QR kodlarını tarayıcınızdan ayrılmadan okumanız ve oluşturmanız için hazırlanmış bir araçtır. Bir görsel seçin, sürükleyin veya ekran görüntüsünü yapıştırın; kodun içeriğini cihazınızda görüntüleyin. Kendi içeriğinizden QR kodu oluşturun, rengini ve çıktı boyutunu seçin, PNG veya SVG olarak indirin.',
'en':'QR Scanner lets you read and create QR codes without leaving your browser. Choose an image, drag it in or paste a screenshot to decode its contents on your device. Create a code from your own content, choose its color and output size, and download it as PNG or SVG.',
'de':'Mit QR Scanner kannst du QR-Codes direkt im Browser lesen und erstellen. Wähle ein Bild, lege es ab oder füge einen Screenshot ein, um den Inhalt auf deinem Gerät auszulesen. Erstelle Codes aus eigenen Inhalten, wähle Farbe und Ausgabegröße und lade sie als PNG oder SVG herunter.',
'es':'QR Scanner permite leer y crear códigos QR sin salir del navegador. Elige una imagen, arrástrala o pega una captura para descifrar su contenido en tu dispositivo. Crea códigos con tu propio contenido, elige el color y el tamaño de salida y descárgalos en PNG o SVG.',
'fr':'QR Scanner permet de lire et de créer des codes QR sans quitter le navigateur. Choisissez une image, déposez-la ou collez une capture pour lire son contenu sur votre appareil. Créez un code avec votre propre contenu, choisissez sa couleur et sa taille, puis téléchargez-le en PNG ou SVG.',
'pt':'O QR Scanner permite ler e criar códigos QR sem sair do navegador. Escolha uma imagem, arraste-a ou cole uma captura para decodificar o conteúdo no seu dispositivo. Crie códigos com seu próprio conteúdo, escolha a cor e o tamanho de saída e baixe em PNG ou SVG.'}

PRIVACY={
'tr':[
'QR Scanner’ın tek amacı, tarayıcıda QR kodlarını cihaz üzerinde okumak ve oluşturmaktır. Görsel veya etkin sekmedeki QR okunabilir; bağlantı, metin, Wi-Fi, e-posta, telefon, SMS ve kişi kartı için QR oluşturulup indirilebilir.',
'activeTab, kullanıcı uzantıyı açıp ilgili düğmeye bastığında etkin sekmenin görünen alanındaki QR kodunu yerel olarak okumak ve etkin sekmenin adresinden QR oluşturmak için kullanılır. Arka planda sekmeler ya da gezinme geçmişi izlenmez. Ekran görüntüleri ve sekme adresleri sunucuya gönderilmez.',
'https://qr.haking.tr/* yalnızca https://qr.haking.tr/version.json üzerinden yeni sürüm bilgisini almak ve daha yeni sürüm varsa bağlantısını göstermek için kullanılır. İstek QR içeriği, görsel, ekran görüntüsü veya etkin sekmenin adresini içermez. Buradan kod indirilmez ya da çalıştırılmaz.',
'Hayır. JavaScript ve QR kütüphaneleri ZIP içindedir. Harici JavaScript veya WebAssembly yüklenmez. Uzaktaki sürüm JSON’u yalnızca veri olarak okunur; kod olarak çalıştırılmaz.'],
'en':[
'QR Scanner has one purpose: reading and creating QR codes locally in the browser. It reads images or the active tab and creates QR codes for links, text, Wi-Fi, email, phone, SMS and contact cards.',
'activeTab is used only after the user opens the extension and selects the corresponding action, to scan the visible area of the active tab locally or create a QR for its URL. The extension does not monitor tabs or browsing history in the background. Screenshots and tab URLs are not sent to a server.',
'https://qr.haking.tr/* is used only to fetch https://qr.haking.tr/version.json and show an update link when a newer version exists. The request contains no QR contents, images, screenshots or active-tab URL. No code is downloaded or executed from this host.',
'No. All JavaScript and QR libraries are bundled in the ZIP. No external JavaScript or WebAssembly is loaded. The remote release JSON is read as data only and never executed as code.'],
'de':[
'QR Scanner hat einen Zweck: QR-Codes lokal im Browser lesen und erstellen. Die Erweiterung liest Bilder oder den aktiven Tab und erzeugt QR-Codes für Links, Text, WLAN, E-Mail, Telefon, SMS und Kontaktkarten.',
'activeTab wird nur nach dem Öffnen der Erweiterung und der Auswahl der jeweiligen Aktion verwendet, um den sichtbaren Bereich des aktiven Tabs lokal zu scannen oder einen QR-Code für dessen Adresse zu erstellen. Tabs und Browserverlauf werden nicht im Hintergrund überwacht. Screenshots und Tab-Adressen werden nicht an Server gesendet.',
'https://qr.haking.tr/* dient ausschließlich zum Abrufen von https://qr.haking.tr/version.json und zum Anzeigen eines Update-Links bei einer neueren Version. Die Anfrage enthält keine QR-Inhalte, Bilder, Screenshots oder Adresse des aktiven Tabs. Es wird kein Code heruntergeladen oder ausgeführt.',
'Nein. JavaScript und QR-Bibliotheken sind im ZIP enthalten. Externes JavaScript oder WebAssembly wird nicht geladen. Die entfernte Versions-JSON wird nur als Daten gelesen und niemals als Code ausgeführt.'],
'es':[
'QR Scanner tiene un único propósito: leer y crear códigos QR localmente en el navegador. Lee imágenes o la pestaña activa y crea códigos para enlaces, texto, Wi-Fi, correo, teléfono, SMS y contactos.',
'activeTab se utiliza únicamente cuando el usuario abre la extensión y elige la acción correspondiente, para leer localmente el área visible de la pestaña activa o crear un QR de su dirección. No se vigilan pestañas ni el historial en segundo plano. Las capturas y direcciones no se envían a un servidor.',
'https://qr.haking.tr/* se usa solo para consultar https://qr.haking.tr/version.json y mostrar un enlace de actualización si existe una versión más reciente. La solicitud no incluye contenido QR, imágenes, capturas ni la dirección de la pestaña activa. No se descarga ni ejecuta código desde ese sitio.',
'No. Todo el JavaScript y las bibliotecas QR están incluidos en el ZIP. No se carga JavaScript ni WebAssembly externo. El JSON de versión remoto se lee solo como datos y nunca se ejecuta como código.'],
'fr':[
'QR Scanner a un seul objectif : lire et créer des codes QR localement dans le navigateur. L’extension lit les images ou l’onglet actif et crée des codes pour liens, textes, Wi-Fi, e-mail, téléphone, SMS et contacts.',
'activeTab est utilisé uniquement lorsque l’utilisateur ouvre l’extension et choisit l’action correspondante, pour lire localement la zone visible de l’onglet actif ou créer un QR de son adresse. Les onglets et l’historique ne sont pas surveillés en arrière-plan. Les captures et adresses ne sont pas envoyées à un serveur.',
'https://qr.haking.tr/* sert uniquement à consulter https://qr.haking.tr/version.json et à afficher un lien de mise à jour si une version plus récente existe. La requête ne contient aucun contenu QR, image, capture ou adresse de l’onglet actif. Aucun code n’est téléchargé ou exécuté depuis cet hôte.',
'Non. Le JavaScript et les bibliothèques QR sont inclus dans le ZIP. Aucun JavaScript ou WebAssembly externe n’est chargé. Le JSON de version distant est uniquement lu comme des données et jamais exécuté comme du code.'],
'pt':[
'O QR Scanner tem um único objetivo: ler e criar códigos QR localmente no navegador. Ele lê imagens ou a aba ativa e cria códigos para links, textos, Wi-Fi, e-mail, telefone, SMS e contatos.',
'activeTab é usado apenas quando o usuário abre a extensão e escolhe a ação correspondente, para ler localmente a área visível da aba ativa ou criar um QR do seu endereço. Não há monitoramento de abas ou histórico em segundo plano. Capturas e endereços não são enviados a um servidor.',
'https://qr.haking.tr/* é usado somente para consultar https://qr.haking.tr/version.json e mostrar um link de atualização quando houver uma versão mais recente. A solicitação não inclui conteúdo QR, imagens, capturas ou endereço da aba ativa. Nenhum código é baixado ou executado desse host.',
'Não. Todo JavaScript e as bibliotecas QR estão incluídos no ZIP. Nenhum JavaScript ou WebAssembly externo é carregado. O JSON de versão remoto é lido apenas como dados e nunca executado como código.']}

def prepare_chrome():
    version=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))['version']
    out=(ROOT/'chrome').resolve();assert out.is_relative_to(ROOT) and out!=ROOT
    out.mkdir(exist_ok=True)
    source=ROOT/'downloads'/f'qr-scanner-{version}-chromium.zip'
    icon=out/'store-icon-128x128.png'
    assert icon.is_file(),'Run npm run build:chrome-assets first'
    name=f'qr-scanner-{version}-chrome.zip'
    for previous in out.glob('qr-scanner-*-chrome.zip'):
        if previous.name!=name:previous.unlink()
    with zipfile.ZipFile(source) as original,zipfile.ZipFile(out/name,'w',zipfile.ZIP_DEFLATED) as target:
        manifest=json.loads(original.read('manifest.json'));assert manifest['version']==version
        icon_path=manifest['icons']['128']
        assert manifest['manifest_version']==3 and not manifest.get('browser_specific_settings')
        for item in original.infolist():target.writestr(item,icon.read_bytes() if item.filename==icon_path else original.read(item.filename))
    digest=hashlib.sha256((out/name).read_bytes()).hexdigest()
    (out/'SHA256SUMS.txt').write_text(f'{digest}  {name}\n',encoding='utf-8')
    (out/'release.json').write_text(json.dumps({'version':version,'package':name,'sha256':digest,'source':source.relative_to(ROOT).as_posix(),'automatic_publication':False,'adaptation':'128px icon with 96px artwork and 16px transparent padding'},indent=2),encoding='utf-8')
    locales=json.loads((ROOT/'shared/locales.json').read_text(encoding='utf-8'))
    extra=json.loads((ROOT/'tools/store_copy_extra.json').read_text(encoding='utf-8'))
    for lang,copy in extra.items():
        INTRO[lang]=copy['intro']
        PRIVACY[lang]=[copy['purpose'],copy['activeTab'],copy['host'],copy['remote']]
    for folder in ['store-listings','privacy-forms']:(out/folder).mkdir(exist_ok=True)
    for lang,s in locales.items():
        types=', '.join(s[key] for key in ['url','text','wifi','email','phone','sms','vcard'])
        features='\n'.join('• '+s[key] for key in ['currentTab','screenshot','featureMultiScan','featureLanguages','featureUpdates','exportDesc','noExpiryDesc','free'])
        description='\n\n'.join([INTRO[lang],types+'.',features,s['privacyDesc'],s['linkNote']])
        assert len(description)>250
        content=f'QR Scanner — v{version}\n\nName: QR Scanner\n\nSummary / Short description:\n{s["extensionDesc"]}\n\nDetailed description:\n{description}\n\nWebsite: https://qr.haking.tr/\nPrivacy policy: https://qr.haking.tr/{lang}/privacy.html\nSupport: qr@haking.tr\n{s["supportDeveloper"]}: https://buymeacoffee.com/haking\n'
        (out/'store-listings'/f'{lang}.txt').write_text(content,encoding='utf-8')
        purpose,active,host,remote=PRIVACY[lang]
        assert all(len(value)<=1000 for value in PRIVACY[lang])
        storage={
          'en':'storage saves language/theme preferences, cached release metadata and the last opened/notified version locally. It prevents repeated update pages and notifications. QR contents, images and browsing history are never stored.',
          'tr':'storage, dil/tema tercihlerini, önbelleğe alınan sürüm bilgisini ve son açılan/bildirilen sürümü yerel olarak saklar. Güncelleme sayfasının ve bildirimlerin tekrarlanmasını önler. QR içerikleri, görseller ve gezinme geçmişi saklanmaz.',
          'de':'storage speichert Sprache, Design, zwischengespeicherte Versionsdaten und die zuletzt angezeigte/gemeldete Version lokal. So werden wiederholte Update-Seiten und Benachrichtigungen vermieden. QR-Inhalte, Bilder und Browserverlauf werden nicht gespeichert.',
          'es':'storage guarda localmente el idioma, tema, metadatos de versión en caché y la última versión mostrada o notificada. Evita páginas y avisos repetidos. No guarda contenidos QR, imágenes ni historial.',
          'fr':'storage conserve localement la langue, le thème, les métadonnées de version et la dernière version affichée ou notifiée. Cela évite les pages et notifications répétées. Aucun contenu QR, image ou historique de navigation n’est conservé.',
          'pt':'storage guarda localmente idioma, tema, metadados de versão em cache e a última versão aberta ou notificada. Evita páginas e notificações repetidas. Não guarda conteúdo QR, imagens ou histórico.',
          'ru':'storage локально сохраняет язык, тему, кеш метаданных версии и последнюю показанную версию. Это предотвращает повторное открытие страницы обновления и уведомлений. Содержимое QR, изображения и история браузера не сохраняются.',
          'ar':'يحفظ إذن storage اللغة والمظهر وبيانات الإصدار المؤقتة وآخر إصدار تم عرضه أو إرسال إشعار به محليًا، لمنع تكرار صفحات التحديث والإشعارات. لا تُحفظ محتويات QR أو الصور أو سجل التصفح.'
        }[lang]
        fields=f'Single purpose description:\n{purpose}\n\nactiveTab justification:\n{active}\n\nHost permission justification:\n{host}\n\nstorage justification:\n{storage}\n\nnotifications (optional) justification:\n{s["notificationPermission"]}\n\nRemote code: NO\nExplanation:\n{remote}\n\nPrivacy policy: https://qr.haking.tr/{lang}/privacy.html\nSupport: qr@haking.tr\n'
        (out/'privacy-forms'/f'{lang}.txt').write_text(fields,encoding='utf-8')
        descriptions=out/'descriptions';descriptions.mkdir(exist_ok=True)
        (descriptions/f'{lang}.txt').write_text(description,encoding='utf-8')
    print(f'Prepared chrome/{name} and {len(locales)} localized listing/privacy files; not published.')

if __name__=='__main__':prepare_chrome()
