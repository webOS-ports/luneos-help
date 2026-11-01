---
{
 "id": "appearance/change-the-status-bar",
 "title": "Change the status bar",
 "section": [],
 "order": 100201,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/AppearancePage.qml:90",
  "adb: settings-common/qml/General/AppearancePage.qml:141",
  "adb: settings-common/qml/General/AppearancePage.qml:202",
  "adb: settings-common/qml/General/AppearancePage.qml:225",
  "adb MindPhone: luna-send org.webosports.service.tweaks.prefs/get showBatteryPercentage"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Appearance**.
2. Under **Status Bar**, do any of the following:

   - **Clock:** Tap and choose **Date only**, **Time only**, or **Date and time**.
   - **Battery:** Tap and choose **Icon only**, **Percentage only**, or **Icon and percentage**.
   - **Percentage colour:** If the percentage is showing, tap and choose **White** or **By charge left**.
   - **Custom Carrier Name:** Turn on and enter your own text in **Shown instead**.

Changes appear straight away.
