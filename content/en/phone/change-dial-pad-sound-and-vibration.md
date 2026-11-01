---
{
 "id": "phone/change-dial-pad-sound-and-vibration",
 "title": "Change dial pad sound and vibration",
 "section": [
  "Customize device settings"
 ],
 "order": 138.4,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/services/org.webosports.service.tweaks.prefs/preferences/org.webosports.app.phone.json",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/AppTweaks/AppTweaks.qml",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/DialerPage.qml:182-190",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/KeyTonePlayer.qml:36-52",
  "adb: /usr/palm/applications/org.webosports.app.tweaks/source/Main.js:10-19"
 ],
 "requires": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Tweaks** > tap **Phone**.
2. Tap **Dialpad Feedback** and choose **Vibrate & Sound**, **Vibrate Only**, **Sound Only**, or **None**.

The setting also decides whether you hear the keys you press during a call.
