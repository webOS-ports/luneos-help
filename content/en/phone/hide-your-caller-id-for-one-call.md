---
{
 "id": "phone/hide-your-caller-id-for-one-call",
 "title": "Hide your caller ID for one call",
 "section": [
  "Make calls"
 ],
 "order": 85.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialStringParser.js:53",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialStringParser.js:238-240",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialHandler.qml:156-159",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:256-264"
 ],
 "requires": [
  "modem"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Phone**.
2. Enter `#31#` and then the number, with no spaces.
3. Tap the dial button.

If you've turned **Show My Caller ID** off, enter `*31#` before the number to show your caller ID for this one call ([change the setting for all calls](/phone/turn-my-caller-id-on-off)).
