---
{
 "id": "network/turn-mobile-data-and-data-roaming-on-off",
 "title": "Turn mobile data and data roaming on/off",
 "section": [
  "Mobile network"
 ],
 "order": 100001,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:149",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:155",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:162"
 ],
 "requires": [
  "modem"
 ]
}
---

**[Open](/basics/open-an-application-in-the-launcher) Network Settings** > under **Mobile Data**, turn these on or off:

- **Mobile data:** Connects your device to the internet over your mobile network.
- **Data roaming:** Uses mobile data on other networks when you are away from your own. Check with your operator about what this costs.
