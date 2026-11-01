---
{
 "id": "messaging/see-whether-a-message-was-delivered",
 "title": "See whether a message was delivered",
 "section": [
  "Use an instant messaging (IM) account"
 ],
 "order": 220.4,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "org.webosports.messaging/app/src/views/ConversationItem.js:181-189",
  "imlibpurpleservice/src/ReceiptHandler.cpp:152"
 ],
 "requires": []
}
---

In an IM conversation, a mark next to the time on a message you sent shows how far it got:

- One check mark: The message was delivered.
- Two check marks: The message was read.

No mark means the service hasn't reported anything. Not all services do.
