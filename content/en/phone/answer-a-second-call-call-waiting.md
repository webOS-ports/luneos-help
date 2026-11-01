---
{
 "id": "phone/answer-a-second-call-call-waiting",
 "title": "Answer a second call (call waiting)",
 "section": [
  "What can I do during a call?"
 ],
 "order": 113,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/20019",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhoneWindow.qml:217",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/RingManager.qml:70",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/VoiceCallMgrWrapper.qml:538"
 ],
 "requires": [
  "modem"
 ]
}
---

When a second call arrives you hear a short tone instead of the ringtone, and an incoming call strip appears over the call screen. Tap the answer button on the left of the strip. The first call is put on hold.

To decline the second call, tap the ignore button on the right of the strip.
