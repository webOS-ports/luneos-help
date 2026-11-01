---
{
 "id": "sounds-and-ringtones/set-sound-options",
 "title": "Set sound options",
 "section": [],
 "order": 510,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/40032",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/SoundsAndAlertsPage.qml:99",
  "adb: settings-common/qml/General/SoundsAndAlertsPage.qml:145",
  "adb: settings-common/qml/General/SoundsAndAlertsPage.qml:170",
  "adb: settings-common/qml/General/SoundsAndAlertsPage.qml:191",
  "adb: /usr/lib/qml/WebOSCompositor/qml/StatusBar/SystemMenu/SystemMenu.qml MuteElement",
  "adb: /usr/lib/qml/WebOSCompositor/qml/StatusBar/SystemMenu/MuteElement.qml:43",
  "adb: /usr/lib/qml/WebOSCompositor/qml/StatusBar/SystemMenu/SystemMenu.qml VolumeElement visible: !Settings.hasVolumeButton"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Sounds & Ringtones**.
2. Do any of the following:
   - To turn sounds on or off: Tap the switch at the top of the screen. The sound settings are hidden while sounds are off.
   - To set the volume: Drag the **Volume** slider.
   - To turn sounds for actions on your device on or off: Turn **System Sounds** on or off.
   - To turn the sound of keys on the onscreen keyboard on or off: Turn **Keyboard Clicks** on or off.

To mute your device from any screen: Open the [system menu](/basics/open-the-connection-menu) > **Mute Sound**. To turn sound back on, tap **Unmute Sound**.

{if:!volumebutton}To set the volume from any screen: Open the [system menu](/basics/open-the-connection-menu) > drag the volume slider.
