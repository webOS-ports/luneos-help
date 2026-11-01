---
{
 "id": "messaging/reply-to-a-specific-message",
 "title": "Reply to a specific message",
 "section": [
  "Use an instant messaging (IM) account"
 ],
 "order": 220.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.messaging/index.html (messageMenu, menuReply)",
  "org.webosports.messaging/app/src/views/ConversationList.js:127-137",
  "org.webosports.messaging/app/src/views/ConversationList.js:182-188",
  "org.webosports.messaging/app/src/views/ConversationList.js:703-713",
  "org.webosports.messaging/app/src/views/ConversationList.js:1196-1211"
 ],
 "requires": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Messaging** > tap the conversation > tap the message.
2. Tap **•••** > **Reply**. The message you're replying to appears above the message box.
3. Enter your message > tap the send button.

To cancel the reply, tap the X next to the quoted message.
