---
{
 "id": "phone/respond-to-a-missed-call",
 "title": "Respond to a missed call",
 "section": [
  "Receive calls"
 ],
 "order": 88.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/MissedCallAlert.qml:31-36",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/MissedCallAlert.qml:66-78",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/MessageAlert.qml (showQuestion, Dismiss)",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/NotificationManager.qml:59-68",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/NotificationManager.qml:120-132"
 ],
 "requires": [
  "modem"
 ]
}
---

When you miss a call, the screen comes on and a **Missed call** alert shows who called and when. A call you ignored doesn't count as missed.

Do one of the following:

- Call the person back: Tap **Call back**.
- Close the alert: Tap **Dismiss**.

If you do nothing for a minute, the alert becomes a notification. Tap the notification to go to the call log ([learn more](/phone/view-your-call-history)).
