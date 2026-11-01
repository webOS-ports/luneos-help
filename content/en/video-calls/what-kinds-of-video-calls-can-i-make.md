---
{
 "id": "video-calls/what-kinds-of-video-calls-can-i-make",
 "title": "What kinds of video calls can I make?",
 "section": [],
 "order": 100102,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: listAccountTemplates: every PHONE provider has videoFormat none",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhoneTabView.qml:69-70",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhoneTabView.qml:92-94",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/VideoCallPage.qml:30-32",
  "adb: /usr/palm/applications/com.webos.app.videocall/main.js"
 ],
 "requires": []
}
---

You can join video meetings on the web with Video Call ([learn how](/video-calls/join-a-video-meeting)).

You can't make a video call in Phone. Calls over [chat accounts](/chat-apps/call-someone-over-a-chat-account) are voice only, so Phone has no **Video** tab.
