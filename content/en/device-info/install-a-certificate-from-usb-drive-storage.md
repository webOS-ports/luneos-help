---
{
 "id": "device-info/install-a-certificate-from-usb-drive-storage",
 "title": "Install a certificate from USB Drive storage",
 "section": [
  "Use certificate manager"
 ],
 "order": 433,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/23291",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: appinfo.json of org.webosports.app.settings.certificate (visible false)",
  "adb: luna-send com.webos.service.applicationManager/listLaunchPoints has no Certificate Manager on either device",
  "adb: luna-send org.webosports.service.certmgr/listAll (service answers)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/CertificatePage.qml:211 (Import Certificate...)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/CertificatePage.qml:282-332 (popup)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/Common/FilePickerPopup.qml:68-69 (/media/internal/downloads)"
 ]
}
---

Certificate Manager is installed, but it does not have an icon in the Launcher yet.

1. Copy the certificate to the **downloads** folder on your device ([**learn how**](/basics/copy-files-between-your-device-and-your-computer)).
2. In Certificate Manager, tap **Import Certificate...** > **Choose file...** > the certificate.
3. If the certificate has a passphrase, enter it.
4. Tap **Import**.

Certificates are digital documents that are used to authenticate and exchange information on networks. Certificate Manager can import .p12, .pfx, .pem, .crt, and .cer files.
