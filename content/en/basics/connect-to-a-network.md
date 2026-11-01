---
{
 "id": "basics/connect-to-a-network",
 "title": "Connect to a network",
 "section": [],
 "order": 60,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26579",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/StatusBar/SystemMenu/WiFiElement.qml:125,156",
  "qml/Connectors/AirplaneModeService.qml:70",
  "adb: org.webosports.app.settings-common qml/Connectivity/NetworkSettingsPage.qml:155,162",
  "adb: listLaunchPoints has Network Settings on MindPhone only",
  "adb: com.palm.systemui app/CaptivePortalAlerts"
 ]
}
---

**Connecting with Wi-Fi**

- Is airplane mode on? Open the [system menu](/basics/open-the-connection-menu) and tap **Turn off Airplane Mode**.
- Is Wi-Fi off? Open the system menu, tap **Wi-Fi**, and then tap **Turn on WiFi**.
- Do you need to pick a network? Open the system menu and tap **Wi-Fi**, then tap a network in the list. For more choices, tap **Wi-Fi Preferences**.
- Do you have a signal? If it's weak, move to a location with a stronger signal.
- Do you need to sign in on a web page? [Open](/basics/open-an-application-in-the-launcher) Atlas Web and enter the information there.

{if:modem}**Connecting with your phone network**

- {if:modem}Is airplane mode on? Turn it off as described above.
- {if:modem}Do you have a signal? Check the signal bars in the upper-right corner of the screen. If there are none, move to a location with a stronger signal.
- {if:modem}Is mobile data on? Open the Launcher, tap the **Prefs** tab, and then tap **Network Settings**. Turn on **Mobile data**.
- {if:modem}Are you roaming? In **Network Settings**, turn on **Data roaming**.
