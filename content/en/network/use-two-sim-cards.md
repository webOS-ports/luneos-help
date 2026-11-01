---
{
 "id": "network/use-two-sim-cards",
 "title": "Use two SIM cards",
 "section": [
  "Mobile network"
 ],
 "order": 100006,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:424",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:477",
  "adb MindPhone: luna-send com.palm.telephony/simListQuery simCount 2"
 ],
 "requires": [
  "modem"
 ]
}
---

**Dual SIM** appears when your device has two SIMs.

1. **[Open](/basics/open-an-application-in-the-launcher) Network Settings**.
2. Under **Dual SIM**, do any of the following:

   - To turn a SIM on or off: Tap the switch beside it. Each SIM shows its operator and signal strength.
   - To choose which SIM to use: Tap **Calls**, **Messages**, or **Mobile data** and tap a SIM.
