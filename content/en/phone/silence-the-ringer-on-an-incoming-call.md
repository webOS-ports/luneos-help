---
{
 "id": "phone/silence-the-ringer-on-an-incoming-call",
 "title": "Silence the ringer on an incoming call",
 "section": [
  "Receive calls"
 ],
 "order": 87,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/19231",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "luna-next-cardshell/qml/StatusBar/SystemMenu/MuteElement.qml:43",
  "luna-next-cardshell/qml/StatusBar/SystemMenu/SystemMenu.qml:441",
  "webos-audiod-port/audiod-pro/src/services/systemmanager.cpp:234 setRingerOn(!muteSound)",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/VoiceCallMgrWrapper.qml:648 (no caller)"
 ],
 "requires": [
  "modem"
 ]
}
---

Do one of the following:

- Answer the call or ignore it. Either one stops the ringing.
- Open the [system menu](/basics/use-the-system-menu) > **Mute Sound**. Sounds stay off until you tap **Unmute Sound**.
