---
{
 "id": "basics/insert-the-sim-card",
 "title": "Insert the SIM card",
 "section": [],
 "order": 7,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42739",
 "status": "verified-device",
 "review": [],
 "requires": [
  "modem"
 ],
 "evidence": [
  "adb: screencaptures/20261031100458.png carrier name in Card view on MindPhone",
  "qml/StatusBar/StatusBar.qml carrierText",
  "qml/SIMPinWindowArea.qml"
 ]
}
---

Where the SIM card goes depends on your device, so check the instructions from the manufacturer. Shut down the device first ([learn how](/basics/shut-down-your-device)).

After you start the device again, the name of your wireless service provider appears in the upper-left corner of the screen in Card view. If your SIM card has a PIN, you're asked to enter it.

If the name doesn't appear, check that airplane mode is off ([learn how](/basics/turn-all-wireless-services-on-off-airplane-mode)), and then contact your wireless service provider.
