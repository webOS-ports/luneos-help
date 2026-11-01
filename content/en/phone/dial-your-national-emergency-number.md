---
{
 "id": "phone/dial-your-national-emergency-number",
 "title": "Dial your national emergency number",
 "section": [
  "Make calls"
 ],
 "order": 84,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/19791",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/SimPinCard.qml:195",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/EmergencyDialerPage.qml:67",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialHandler.qml:222",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/CallMessages.js:52",
  "luna-next-cardshell/qml/LockScreen: no emergency-call control (grep -i emergency: no match)"
 ],
 "requires": [
  "modem"
 ]
}
---

To dial your national emergency number (such as 112 or 911):

1. {if:powerbutton}Press the **power** button to wake up the screen if needed.
2. Unlock the screen if needed. The lock screen has no emergency call button.
3. **[Open](/basics/open-an-application-in-the-launcher) Phone** > enter the number > tap the dial button.

If your device asks for your SIM PIN, you don't have to enter it: Tap **Emergency Call** > enter the number > tap the dial button.

If your device is in airplane mode, you don't have to turn the phone on. It turns the radio on, shows **Connecting to network to dial...**, and places the call.
