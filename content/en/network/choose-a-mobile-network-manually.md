---
{
 "id": "network/choose-a-mobile-network-manually",
 "title": "Choose a mobile network manually",
 "section": [
  "Mobile network"
 ],
 "order": 100003,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:193",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:232",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:598",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:507"
 ],
 "requires": [
  "modem"
 ]
}
---

Your device normally picks a mobile network by itself. **Carrier** shows the current **Operator**, **Technology**, **Strength**, and **Status**.

1. **[Open](/basics/open-an-application-in-the-launcher) Network Settings**.
2. Under **Carrier**, turn off **Automatic selection**.
3. Under **Choose a Network**, wait for the search to finish.
4. Tap a network. You can't choose one marked **Forbidden**. To search again, tap **Rescan**.

To pick another network later: Tap **Search networks...**.

To go back: Turn on **Automatic selection**.
