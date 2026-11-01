---
{
 "id": "messaging/receive-and-view-text-messages",
 "title": "Receive and view text messages",
 "section": [
  "Get and send text/multimedia messages"
 ],
 "order": 478,
 "devices": [
  "tablet"
 ],
 "origin": "palm/d500-01/35651",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: grep in /usr/palm/applications/org.webosports.app.messaging/index.html: 'New MMS on your phone'",
  "adb: ps on MindPhone: mmsd, webos-telephonyd"
 ],
 "requires": [
  "modem"
 ]
}
---

When a message arrives, a notification appears. Tap it to open the conversation, or **[Open](/basics/open-an-application-in-the-launcher) Messaging** > tap the conversation.

Multimedia messages aren't shown yet. A message with pictures or other media appears as **New MMS on your phone**.
