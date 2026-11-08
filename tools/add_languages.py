"""Add complete German, Spanish, French and Portuguese translations."""
import json
from pathlib import Path

TRANSLATIONS = {
'de': '''
navCreate|QR erstellen
navRead|QR lesen
navExtension|Erweiterung
navAbout|Über uns
eyebrow|KLEINER CODE. UNENDLICHE MÖGLICHKEITEN.
title|Ein QR. So viele Möglichkeiten.
subtitle|Erstellen, scannen und teilen. Deine einfachen, datensparsamen QR-Werkzeuge direkt im Browser.
create|QR-Code erstellen
read|QR-Code scannen
toolTitle|Mach etwas teilbar.
toolDesc|Wähle einen Typ und füge deinen Inhalt hinzu. Dein QR-Code ist in Sekunden fertig.
url|Webseite
text|Text
wifi|WLAN
email|E-Mail
content|Dein Inhalt
password|Passwort
subject|Betreff
security|Verschlüsselung
size|Exportgröße
color|QR-Farbe
generate|QR erstellen
preview|Dein QR-Code ist bereit.
previewNote|Gestochen scharf und hochauflösend. Ohne Konto. Ohne Wasserzeichen.
png|PNG herunterladen
svg|SVG herunterladen
copy|Text kopieren
clear|Leeren
local|Datenschutz von Anfang an
localDesc|Bilder und QR-Inhalte werden auf deinem Gerät verarbeitet.
free|Völlig kostenlos
freeDesc|Ohne Konto, Abo oder Wasserzeichen.
export|Für jede Größe gemacht
exportDesc|PNG zum Teilen. SVG für scharfe Ausdrucke in jeder Größe.
extensionTitle|Deine QR-Werkzeuge. Nur einen Klick entfernt.
extensionDesc|Lies Bilder, scanne den aktuellen Tab und erstelle QR-Codes, ohne den Browser zu verlassen.
edge|Für Edge installieren
download|ZIP v1.1.1 herunterladen
install|Installationsanleitung
compat|Chrome, Edge, Brave und Opera: Chromium-Paket. Firefox: eigenes Paket. Safari benötigt eine Apple-Version.
faqTitle|Gut zu wissen.
q1|Laufen meine QR-Codes ab?
a1|Statische QR-Codes haben kein Ablaufdatum. Die Zielwebseite muss weiterhin erreichbar sein.
q2|Werden meine Dateien hochgeladen?
a2|Nein. Bilder, Texte und WLAN-Passwörter werden lokal verarbeitet. Nur die Update-Prüfung der Erweiterung verbindet sich mit qr.haking.tr.
q3|Kann ich meinen QR-Code anpassen?
a3|Wähle Farbe und Exportgröße. PNG- und SVG-Dateien enthalten für zuverlässiges Scannen einen weißen Rand von vier Modulen.
q4|Welche Browser werden unterstützt?
a4|Die Webseite funktioniert in aktuellen Browsern. Ein Eintrag im Edge-Store ist verfügbar; Chromium-ZIP-Pakete lassen sich manuell installieren. Für die dauerhafte Installation in Firefox ist eine Signierung nötig.
aboutTitle|Nützliche Werkzeuge. Weniger Aufwand.
aboutDesc|QR Scanner ist ein Open-Source-Projekt von HaKING (Halit). Es macht alltägliche QR-Aufgaben schnell, zugänglich und datensparsam. Erstelle QR-Codes für Webseiten, Texte, WLAN und E-Mails oder lies einen Code aus einem Bild.
privacy|Datenschutz
privacyDesc|QR-Inhalte werden niemals an unsere Server gesendet. Keine Analyse, Tracking-Cookies oder QR-Verläufe. Design- und Spracheinstellungen bleiben auf deinem Gerät. Hosting-Anbieter können übliche Verbindungsprotokolle verarbeiten.
helpTitle|QR Scanner installieren
step1|Entpacke die heruntergeladene ZIP-Datei in einen dauerhaften Ordner.
step2|Öffne chrome://extensions (Edge: edge://extensions) und aktiviere den Entwicklermodus.
step3|Wähle „Entpackte Erweiterung laden“ und den entpackten Ordner mit manifest.json.
keepFolder|Bewahre diesen Ordner auf. Ersetze für Updates die Dateien durch das neuere Paket und klicke auf „Neu laden“. Firefox: about:debugging → Dieser Firefox → Temporäres Add-on laden → manifest.json (bis zum Neustart). Safari benötigt eine Xcode-Konvertierung, Signierung und einen eigenen Vertriebsprozess.
scanTitle|Entdecke den Inhalt.
scanDesc|Lade ein Bild hoch, ziehe es hierher oder füge es ein. Der Inhalt bleibt auf deinem Gerät.
choose|Bild auswählen
drop|Bild hier ablegen oder mit Strg / ⌘ + V einfügen
result|Gelesener Inhalt
open|Link öffnen
linkNote|Prüfe das Ziel vor dem Öffnen. HTTPS garantiert keine vertrauenswürdige Webseite.
empty|Gib zuerst deinen Inhalt ein.
invalid|Gib eine gültige Web- oder E-Mail-Adresse ein.
tooLong|Dieser Inhalt ist für einen QR-Code zu lang. Kürze ihn und versuche es erneut.
notFound|Kein QR-Code gefunden. Versuche ein schärferes oder größeres Bild.
badFile|Wähle ein PNG-, JPEG- oder WebP-Bild mit höchstens 15 MB.
copied|Kopiert.
copyError|Zwischenablage nicht verfügbar. Markiere und kopiere den Text manuell.
ready|Dein QR-Code ist fertig.
scanning|Bild wird gelesen…
theme|Design
language|Sprache
latest|Neueste Version
update|Eine neuere Version ist verfügbar. Lade die aktuelle Version herunter.
screenshot|Aktuellen Tab scannen
screenError|Dieser Tab lässt sich nicht aufnehmen. Versuche es auf einer normalen Webseite.
fileError|Das Bild konnte nicht gelesen werden.
privacyTitle|Datenschutz, klar erklärt.
faq|Häufige Fragen
source|Quellcode
release|Versionshinweise
auto|System
light|Hell
dark|Dunkel
noExpiry|Dauerhaft deins
noExpiryDesc|Statische QR-Codes. Ohne Ablaufdatum und Weiterleitungsdienst.
skip|Zu den Werkzeugen springen
downloadNote|Die Version im Edge-Store kann abweichen. ZIP-Pakete enthalten v1.1.1. Das Firefox-ZIP ist bis zur Signierung nur für vorübergehende Tests bestimmt.
footerTag|Scannen. Erstellen. Weitermachen.
imageOnly|PNG, JPEG, WebP · bis zu 15 MB
''',
'es': '''
navCreate|Crear QR
navRead|Leer QR
navExtension|Extensión
navAbout|Acerca de
eyebrow|UN CÓDIGO PEQUEÑO. INFINITAS POSIBILIDADES.
title|Un QR. Muchas posibilidades.
subtitle|Crea, escanea y comparte. Herramientas QR sencillas y privadas, directamente en tu navegador.
create|Crear un código QR
read|Escanear un código QR
toolTitle|Crea algo para compartir.
toolDesc|Elige un tipo y añade tu contenido. Tu QR estará listo en segundos.
url|Sitio web
text|Texto
wifi|Wi-Fi
email|Correo electrónico
content|Tu contenido
password|Contraseña
subject|Asunto
security|Seguridad
size|Tamaño de exportación
color|Color del QR
generate|Generar QR
preview|Tu QR, listo para usar.
previewNote|Un QR nítido y de alta resolución. Sin cuenta. Sin marca de agua.
png|Descargar PNG
svg|Descargar SVG
copy|Copiar texto
clear|Borrar
local|Privacidad desde el diseño
localDesc|Tus imágenes y contenidos QR se procesan en tu dispositivo.
free|Totalmente gratis
freeDesc|Sin cuenta, suscripción ni marcas de agua.
export|Para cualquier tamaño
exportDesc|PNG para compartir. SVG para impresiones nítidas a cualquier tamaño.
extensionTitle|Tus herramientas QR. A un clic.
extensionDesc|Lee imágenes, escanea la pestaña actual y crea códigos QR sin salir del navegador.
edge|Instalar en Edge
download|Descargar ZIP v1.1.1
install|Guía de instalación
compat|Chrome, Edge, Brave y Opera: paquete Chromium. Firefox: paquete independiente. Safari requiere una compilación para Apple.
faqTitle|Resolvemos tus dudas.
q1|¿Caducan mis códigos QR?
a1|Los códigos QR estáticos no caducan. El sitio web de destino debe seguir disponible.
q2|¿Se suben mis archivos?
a2|No. Las imágenes, los textos y las contraseñas Wi-Fi se procesan localmente. Solo la comprobación de actualizaciones de la extensión se conecta a qr.haking.tr.
q3|¿Puedo personalizar mi código QR?
a3|Elige el color y el tamaño de exportación. Los archivos PNG y SVG incluyen un margen blanco de cuatro módulos para facilitar la lectura.
q4|¿Qué navegadores son compatibles?
a4|Usa el sitio web en navegadores modernos. La extensión está disponible en la tienda de Edge; los paquetes ZIP de Chromium pueden instalarse manualmente. Firefox requiere una firma para la instalación permanente.
aboutTitle|Herramientas útiles. Menos complicaciones.
aboutDesc|QR Scanner es un proyecto de código abierto de HaKING (Halit). Hace que las tareas QR cotidianas sean rápidas, accesibles y privadas. Crea códigos QR para sitios web, texto, Wi-Fi y correo electrónico, o lee un código desde una imagen.
privacy|Privacidad
privacyDesc|El contenido de los QR nunca se envía a nuestros servidores. Sin analítica, cookies de seguimiento ni historial de QR. Las preferencias de tema e idioma permanecen en tu dispositivo. Los proveedores de alojamiento pueden procesar registros habituales de conexión.
helpTitle|Instalar QR Scanner
step1|Extrae el ZIP descargado en una carpeta permanente.
step2|Abre chrome://extensions (Edge: edge://extensions) y activa el modo de desarrollador.
step3|Elige «Cargar descomprimida» y selecciona la carpeta extraída que contiene manifest.json.
keepFolder|Conserva esta carpeta. Para actualizar, sustituye sus archivos por el paquete nuevo y pulsa «Recargar». Firefox: about:debugging → Este Firefox → Cargar complemento temporal → manifest.json (hasta reiniciar). Safari necesita conversión con Xcode, firma y un proceso de distribución independiente.
scanTitle|Descubre lo que contiene.
scanDesc|Sube, arrastra o pega una imagen. Su contenido permanece en tu dispositivo.
choose|Elegir una imagen
drop|Arrastra aquí una imagen o pégala con Ctrl / ⌘ + V
result|Contenido leído
open|Abrir enlace
linkNote|Revisa el destino antes de abrirlo. HTTPS no garantiza que un sitio sea fiable.
empty|Primero introduce tu contenido.
invalid|Introduce una dirección web o de correo electrónico válida.
tooLong|Este contenido es demasiado largo para un código QR. Acórtalo y vuelve a intentarlo.
notFound|No se encontró ningún código QR. Prueba con una imagen más nítida o más grande.
badFile|Elige una imagen PNG, JPEG o WebP de hasta 15 MB.
copied|Copiado.
copyError|El portapapeles no está disponible. Selecciona y copia el texto manualmente.
ready|Tu QR está listo.
scanning|Leyendo imagen…
theme|Tema
language|Idioma
latest|Última versión
update|Hay una versión nueva. Descarga la versión más reciente.
screenshot|Escanear pestaña actual
screenError|No se puede capturar esta pestaña. Prueba con una pestaña de un sitio web normal.
fileError|No se pudo leer la imagen.
privacyTitle|La privacidad, sin complicaciones.
faq|Preguntas frecuentes
source|Código fuente
release|Notas de la versión
auto|Sistema
light|Claro
dark|Oscuro
noExpiry|Tuyo para siempre
noExpiryDesc|Códigos QR estáticos. Sin caducidad ni servicio de redirección.
skip|Ir a las herramientas
downloadNote|La versión de la tienda de Edge puede ser diferente. Los paquetes ZIP contienen v1.1.1. El ZIP de Firefox es para pruebas temporales hasta que se firme.
footerTag|Escanea. Crea. Continúa.
imageOnly|PNG, JPEG, WebP · hasta 15 MB
''',
'fr': '''
navCreate|Créer un QR
navRead|Lire un QR
navExtension|Extension
navAbout|À propos
eyebrow|UN PETIT CODE. UNE INFINITÉ DE POSSIBILITÉS.
title|Un QR. Tant de possibilités.
subtitle|Créez, scannez et partagez. Des outils QR simples et respectueux de votre vie privée, dans votre navigateur.
create|Créer un code QR
read|Scanner un code QR
toolTitle|Créez quelque chose à partager.
toolDesc|Choisissez un type, ajoutez votre contenu. Votre QR est prêt en quelques secondes.
url|Site web
text|Texte
wifi|Wi-Fi
email|E-mail
content|Votre contenu
password|Mot de passe
subject|Objet
security|Sécurité
size|Taille d’exportation
color|Couleur du QR
generate|Générer le QR
preview|Votre QR, prêt à l’emploi.
previewNote|Un QR net en haute résolution. Sans compte. Sans filigrane.
png|Télécharger le PNG
svg|Télécharger le SVG
copy|Copier le texte
clear|Effacer
local|La confidentialité dès la conception
localDesc|Vos images et contenus QR sont traités sur votre appareil.
free|Entièrement gratuit
freeDesc|Sans compte, abonnement ni filigrane.
export|Pour toutes les tailles
exportDesc|Le PNG pour partager. Le SVG pour des impressions nettes à toute taille.
extensionTitle|Vos outils QR. À portée de clic.
extensionDesc|Lisez des images, scannez l’onglet actuel et créez des codes QR sans quitter votre navigateur.
edge|Installer sur Edge
download|Télécharger le ZIP v1.1.1
install|Guide d’installation
compat|Chrome, Edge, Brave et Opera : paquet Chromium. Firefox : paquet distinct. Safari nécessite une version pour Apple.
faqTitle|Quelques réponses utiles.
q1|Mes codes QR expirent-ils ?
a1|Les codes QR statiques n’expirent pas. Le site web de destination doit rester accessible.
q2|Mes fichiers sont-ils envoyés en ligne ?
a2|Non. Les images, textes et mots de passe Wi-Fi sont traités localement. Seule la vérification des mises à jour de l’extension contacte qr.haking.tr.
q3|Puis-je personnaliser mon code QR ?
a3|Choisissez la couleur et la taille d’exportation. Les fichiers PNG et SVG incluent une marge blanche de quatre modules pour une lecture fiable.
q4|Quels navigateurs sont compatibles ?
a4|Utilisez le site dans un navigateur récent. L’extension est disponible sur la boutique Edge ; les paquets ZIP Chromium s’installent manuellement. Firefox exige une signature pour une installation permanente.
aboutTitle|Des outils utiles. Moins de complications.
aboutDesc|QR Scanner est un projet open source de HaKING (Halit). Il simplifie les tâches QR du quotidien en privilégiant la rapidité, l’accessibilité et la confidentialité. Créez des codes QR pour sites web, textes, Wi-Fi et e-mails, ou lisez un code dans une image.
privacy|Confidentialité
privacyDesc|Le contenu des QR n’est jamais envoyé à nos serveurs. Aucune analyse d’audience, aucun cookie de suivi ni historique QR. Vos préférences de thème et de langue restent sur votre appareil. Les hébergeurs peuvent traiter les journaux de connexion habituels.
helpTitle|Installer QR Scanner
step1|Décompressez le ZIP téléchargé dans un dossier permanent.
step2|Ouvrez chrome://extensions (Edge : edge://extensions) et activez le mode développeur.
step3|Choisissez « Charger l’extension non empaquetée » et sélectionnez le dossier extrait contenant manifest.json.
keepFolder|Conservez ce dossier. Pour une mise à jour, remplacez ses fichiers par le nouveau paquet et cliquez sur « Actualiser ». Firefox : about:debugging → Ce Firefox → Charger un module complémentaire temporaire → manifest.json (jusqu’au redémarrage). Safari nécessite une conversion avec Xcode, une signature et une distribution distincte.
scanTitle|Découvrez ce qu’il contient.
scanDesc|Importez, déposez ou collez une image. Son contenu reste sur votre appareil.
choose|Choisir une image
drop|Déposez une image ici ou collez-la avec Ctrl / ⌘ + V
result|Contenu décodé
open|Ouvrir le lien
linkNote|Vérifiez la destination avant de l’ouvrir. HTTPS ne garantit pas la fiabilité d’un site.
empty|Saisissez d’abord votre contenu.
invalid|Saisissez une adresse web ou e-mail valide.
tooLong|Ce contenu est trop long pour un code QR. Raccourcissez-le et réessayez.
notFound|Aucun code QR trouvé. Essayez une image plus nette ou plus grande.
badFile|Choisissez une image PNG, JPEG ou WebP de 15 Mo maximum.
copied|Copié.
copyError|Presse-papiers indisponible. Sélectionnez et copiez le texte manuellement.
ready|Votre QR est prêt.
scanning|Lecture de l’image…
theme|Thème
language|Langue
latest|Dernière version
update|Une nouvelle version est disponible. Téléchargez la dernière version.
screenshot|Scanner l’onglet actuel
screenError|Impossible de capturer cet onglet. Essayez un onglet de site web classique.
fileError|Impossible de lire l’image.
privacyTitle|La confidentialité, en toute clarté.
faq|Questions fréquentes
source|Code source
release|Notes de version
auto|Système
light|Clair
dark|Sombre
noExpiry|À vous, durablement
noExpiryDesc|Des codes QR statiques. Sans expiration ni service de redirection.
skip|Aller aux outils
downloadNote|La version de la boutique Edge peut différer. Les paquets ZIP contiennent la v1.1.1. Le ZIP Firefox est réservé aux tests temporaires jusqu’à sa signature.
footerTag|Scannez. Créez. Continuez.
imageOnly|PNG, JPEG, WebP · 15 Mo maximum
''',
'pt': '''
navCreate|Criar QR
navRead|Ler QR
navExtension|Extensão
navAbout|Sobre
eyebrow|UM CÓDIGO PEQUENO. POSSIBILIDADES INFINITAS.
title|Um QR. Tantas possibilidades.
subtitle|Crie, leia e compartilhe. Ferramentas QR simples e privadas, direto no seu navegador.
create|Criar um código QR
read|Ler um código QR
toolTitle|Crie algo para compartilhar.
toolDesc|Escolha um tipo e adicione seu conteúdo. Seu QR fica pronto em segundos.
url|Site
text|Texto
wifi|Wi-Fi
email|E-mail
content|Seu conteúdo
password|Senha
subject|Assunto
security|Segurança
size|Tamanho de exportação
color|Cor do QR
generate|Gerar QR
preview|Seu QR, pronto para usar.
previewNote|Um QR nítido e em alta resolução. Sem conta. Sem marca-d’água.
png|Baixar PNG
svg|Baixar SVG
copy|Copiar texto
clear|Limpar
local|Privacidade desde o início
localDesc|Suas imagens e conteúdos QR são processados no seu dispositivo.
free|Totalmente grátis
freeDesc|Sem conta, assinatura ou marcas-d’água.
export|Feito para qualquer tamanho
exportDesc|PNG para compartilhar. SVG para impressões nítidas em qualquer tamanho.
extensionTitle|Suas ferramentas QR. A um clique.
extensionDesc|Leia imagens, capture a aba atual e crie códigos QR sem sair do navegador.
edge|Instalar no Edge
download|Baixar ZIP v1.1.1
install|Guia de instalação
compat|Chrome, Edge, Brave e Opera: pacote Chromium. Firefox: pacote separado. Safari exige uma compilação para Apple.
faqTitle|Tire suas dúvidas.
q1|Meus códigos QR expiram?
a1|Códigos QR estáticos não expiram. O site de destino precisa continuar disponível.
q2|Meus arquivos são enviados?
a2|Não. Imagens, textos e senhas de Wi-Fi são processados localmente. Apenas a verificação de atualizações da extensão se conecta a qr.haking.tr.
q3|Posso personalizar meu código QR?
a3|Escolha a cor e o tamanho de exportação. Os arquivos PNG e SVG incluem uma margem branca de quatro módulos para uma leitura confiável.
q4|Quais navegadores são compatíveis?
a4|Use o site em navegadores modernos. A extensão está disponível na loja do Edge; os pacotes ZIP Chromium podem ser instalados manualmente. O Firefox exige assinatura para instalação permanente.
aboutTitle|Ferramentas úteis. Menos complicação.
aboutDesc|QR Scanner é um projeto de código aberto de HaKING (Halit). Ele torna as tarefas QR do dia a dia rápidas, acessíveis e privadas. Crie códigos QR para sites, textos, Wi-Fi e e-mails ou leia um código em uma imagem.
privacy|Privacidade
privacyDesc|O conteúdo dos códigos QR nunca é enviado aos nossos servidores. Sem análise de uso, cookies de rastreamento ou histórico de QR. As preferências de tema e idioma ficam no seu dispositivo. Os provedores de hospedagem podem processar registros normais de conexão.
helpTitle|Instalar QR Scanner
step1|Extraia o ZIP baixado para uma pasta permanente.
step2|Abra chrome://extensions (Edge: edge://extensions) e ative o modo de desenvolvedor.
step3|Escolha «Carregar sem compactação» e selecione a pasta extraída que contém manifest.json.
keepFolder|Mantenha essa pasta. Para atualizar, substitua os arquivos pelo pacote mais recente e clique em «Recarregar». Firefox: about:debugging → Este Firefox → Carregar extensão temporária → manifest.json (até reiniciar). O Safari precisa de conversão no Xcode, assinatura e um processo separado de distribuição.
scanTitle|Descubra o conteúdo.
scanDesc|Envie, arraste ou cole uma imagem. O conteúdo fica no seu dispositivo.
choose|Escolher imagem
drop|Solte uma imagem aqui ou cole com Ctrl / ⌘ + V
result|Conteúdo lido
open|Abrir link
linkNote|Confira o destino antes de abrir. HTTPS não garante que o site seja confiável.
empty|Primeiro, insira seu conteúdo.
invalid|Insira um endereço de site ou e-mail válido.
tooLong|O conteúdo é longo demais para um código QR. Reduza o texto e tente novamente.
notFound|Nenhum código QR encontrado. Tente uma imagem maior ou mais nítida.
badFile|Escolha uma imagem PNG, JPEG ou WebP de até 15 MB.
copied|Copiado.
copyError|Área de transferência indisponível. Selecione e copie o texto manualmente.
ready|Seu QR está pronto.
scanning|Lendo imagem…
theme|Tema
language|Idioma
latest|Versão mais recente
update|Há uma nova versão disponível. Baixe a versão mais recente.
screenshot|Ler aba atual
screenError|Não foi possível capturar esta aba. Tente uma aba de um site comum.
fileError|Não foi possível ler a imagem.
privacyTitle|Privacidade, sem complicação.
faq|Perguntas frequentes
source|Código-fonte
release|Notas da versão
auto|Sistema
light|Claro
dark|Escuro
noExpiry|Seu para sempre
noExpiryDesc|Códigos QR estáticos. Sem expiração nem serviço de redirecionamento.
skip|Ir para as ferramentas
downloadNote|A versão na loja do Edge pode ser diferente. Os pacotes ZIP contêm a v1.1.1. O ZIP do Firefox é para testes temporários até ser assinado.
footerTag|Leia. Crie. Siga em frente.
imageOnly|PNG, JPEG, WebP · até 15 MB
'''
}

def main():
    path = Path(__file__).resolve().parents[1] / 'shared' / 'locales.json'
    data = json.loads(path.read_text(encoding='utf-8-sig'))
    expected = set(data['en'])
    for language, lines in TRANSLATIONS.items():
        entries = [line.split('|', 1) for line in lines.strip().splitlines()]
        translated = dict(entries)
        if len(entries) != len(translated):
            raise ValueError(f'{language}: duplicate translation key')
        missing, extra = expected - set(translated), set(translated) - expected
        if missing or extra:
            raise ValueError(f'{language}: missing={sorted(missing)}, extra={sorted(extra)}')
        if any(not value.strip() for value in translated.values()):
            raise ValueError(f'{language}: empty translation')
        data[language] = {key: translated[key] for key in data['en']}
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Added {", ".join(TRANSLATIONS)}: {len(expected)} translated keys per language.')

if __name__ == '__main__':
    main()
