---
{
 "id": "phone/manually-select-network-settings",
 "title": "Manually select network settings",
 "section": [
  "Customize device settings"
 ],
 "order": 138,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/19483",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:351",
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:860",
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:509"
 ],
 "requires": [
  "modem"
 ]
}
---

Get the settings for the access point from your wireless service provider first.

1. **[Open](/basics/open-an-application-in-the-launcher) Network Settings**.
2. Under **Access Point Names**, tap the access point.
3. Enter the **Name**, **APN**, **Username**, **Password**, and **Protocol** > **Save**.

You can edit the access points your SIM card's provider set up, but you can't add or remove one here.
