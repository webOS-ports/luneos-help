---
{
 "id": "phone/set-roaming-and-data-usage-preferences",
 "title": "Set roaming and data usage preferences",
 "section": [
  "Customize device settings"
 ],
 "order": 137,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/19553",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:155",
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:162",
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:175",
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:232",
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:256"
 ],
 "requires": [
  "modem"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Network Settings**.
2. Under **Mobile Data**, set any of the following:

   **Mobile data:** Turn data services on or off.

   **Data roaming:** Set whether to allow data services when you are roaming.

   **Network mode:** Choose **Automatic**, **2G (GSM)**, **3G (UMTS)**, or **4G (LTE)**. This setting appears only if your device supports it.
3. Under **Carrier**, set **Automatic selection** to choose whether your device selects a network automatically. If you turn it off, tap **Search networks...** > tap the network to use.
