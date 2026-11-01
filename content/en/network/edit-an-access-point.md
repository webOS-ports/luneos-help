---
{
 "id": "network/edit-an-access-point",
 "title": "Edit an access point",
 "section": [
  "Mobile network"
 ],
 "order": 100005,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:351",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:860",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:507"
 ],
 "requires": [
  "modem"
 ]
}
---

An access point (APN) tells your device how to reach your operator's mobile data network. Change it only if your operator tells you to.

1. **[Open](/basics/open-an-application-in-the-launcher) Network Settings**.
2. Under **Access Point Names**, tap an access point.
3. Change the **Name**, **APN**, **Username**, **Password**, or **Protocol**.
4. Tap **Save**.

You can't add or delete an access point. The list comes from your SIM's operator.
