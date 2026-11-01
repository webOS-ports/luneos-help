---
{
 "id": "messaging/open-pictures-files-and-voice-messages",
 "title": "Open pictures, files, and voice messages",
 "section": [
  "Use an instant messaging (IM) account"
 ],
 "order": 220.3,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "org.webosports.messaging/app/src/views/ConversationItem.js:576-592",
  "org.webosports.messaging/app/src/views/ConversationItem.js:700-760",
  "org.webosports.messaging/app/src/views/ConversationList.js:941-986",
  "org.webosports.messaging/app/src/views/ConversationList.js:1215-1275",
  "adb: getAppInfo com.palm.app.photos ok; com.palm.app.maps invalid",
  "adb: /usr/palm/applications/org.webosports.app.messaging/index.html (attachmentChosen has no caller; startVoiceNote only runs a timer)"
 ],
 "requires": []
}
---

In an IM conversation, what people send you appears in the message. **[Open](/basics/open-an-application-in-the-launcher) Messaging** > tap the conversation, then do any of the following:

- Picture: It appears in the message. Tap it to open it in Photos.
- Voice message: Tap the play button in the message. Tap it again to pause.
- Video: Tap it to play it.
- Document or other file: Tap its name to open it in an application that can show it.
- Contact card: Tap **Contact card** to add it to Contacts.
- Event: Tap **Add to Calendar**.

You can't send files or voice messages yet. The attach and mic buttons are there, but nothing you pick or record is sent.
