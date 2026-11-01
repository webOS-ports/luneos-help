---
{
 "id": "basics/turn-sound-off-or-on",
 "title": "Turn sound off or on",
 "section": [
  "Use the menus"
 ],
 "order": 51.7,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: md5sum of the cited QML on both devices matches luna-next-cardshell",
  "qml/StatusBar/SystemMenu/MuteElement.qml",
  "qml/StatusBar/SystemMenu/SystemMenu.qml:440-470 preferences.muteSound, volumeControl.setMute",
  "qml/StatusBar/SystemIndicators.qml:79 MuteSoundIndicator",
  "qml/LunaSysAPI/VolumeControl.qml:86 master/muteVolume: which sounds it silences is untested"
 ]
}
---

1. Open the [system menu](/basics/open-the-connection-menu).
2. Tap **Mute Sound**.

An icon in the status bar shows that the sound is off.

To turn sound back on: Open the system menu and tap **Unmute Sound**.
