---
{
 "id": "device-info/delete-a-certificate",
 "title": "Delete a certificate",
 "section": [
  "Use certificate manager"
 ],
 "order": 436,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/23321",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: appinfo.json of org.webosports.app.settings.certificate (visible false)",
  "adb: luna-send com.webos.service.applicationManager/listLaunchPoints has no Certificate Manager on either device",
  "adb: luna-send org.webosports.service.certmgr/listAll (service answers)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/CertificatePage.qml:191 (Delete)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/CertificatePage.qml:220"
 ]
}
---

Certificate Manager is installed, but it does not have an icon in the Launcher yet.

In Certificate Manager, swipe the certificate sideways > **Delete**.
