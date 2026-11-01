---
{
 "id": "video-calls/join-a-video-meeting",
 "title": "Join a video meeting",
 "section": [],
 "order": 100101,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.webos.app.videocall/appinfo.json",
  "adb: /usr/palm/applications/com.webos.app.videocall/main.js (handleClick, \"Open with Webex\", \"Open with Teams\")",
  "adb: ls /usr/palm/applications on both devices"
 ],
 "requires": []
}
---

Video Call opens a meeting service in Atlas Web, where you sign in and join as you would on a computer. You need an internet connection.

1. **[Open](/basics/open-an-application-in-the-launcher) Video Call**.
2. Tap **Open with Webex** or **Open with Teams**.
3. In Atlas Web, sign in and join your meeting.

{if:!camera}Your device has no camera, so others can't see you.
