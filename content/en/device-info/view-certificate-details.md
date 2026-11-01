---
{
 "id": "device-info/view-certificate-details",
 "title": "View certificate details",
 "section": [
  "Use certificate manager"
 ],
 "order": 435,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/23335",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: appinfo.json of org.webosports.app.settings.certificate (visible false)",
  "adb: luna-send com.webos.service.applicationManager/listLaunchPoints has no Certificate Manager on either device",
  "adb: luna-send org.webosports.service.certmgr/listAll (service answers)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/CertificatePage.qml:104 (Installed Certificates), :155 (issuer, expiry)"
 ]
}
---

Certificate Manager is installed, but it does not have an icon in the Launcher yet.

Certificate Manager lists each certificate you installed under **Installed Certificates**, with its name, its issuer, and the date it expires.
