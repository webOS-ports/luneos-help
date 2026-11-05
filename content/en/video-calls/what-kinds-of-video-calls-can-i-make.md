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
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "org.webosports.app.phone/qml/views/PhoneTabView.qml:87,70 (Video tab only when a service has video)",
  "luneos-synergy-connectors 165229c, d3cdd93, 09f53a9 (videoFormat both for Signal, WhatsApp, Telegram; Teams already both)",
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

You can make video calls in Phone over Telegram, WhatsApp, Teams, and Signal accounts ([learn how](/chat-apps/call-someone-over-a-chat-account)). Phone shows a **Video** tab when one of your accounts can make video calls. Regular phone calls over your mobile network are voice only.
