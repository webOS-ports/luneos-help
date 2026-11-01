---
{
 "id": "basics/use-the-power-menu",
 "title": "Use the power menu",
 "section": [
  "Turn your device on/off"
 ],
 "order": 12.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: com.palm.systemui app/PowerdAlerts/PowerdAlerts.js PowerOffAlert labels, both devices",
  "adb: md5sum of the cited QML on both devices matches luna-next-cardshell",
  "qml/Notifications/PowerMenu.qml:51,69,75,93,111",
  "qml/StatusBar/SystemMenu/PowerElement.qml:35",
  "qml/StatusBar/SystemMenu/SystemMenu.qml visible: !Settings.hasPowerButton"
 ]
}
---

1. {if:powerbutton}Press and hold the **power** button.
1. {if:!powerbutton}Open the [system menu](/basics/open-the-connection-menu) and tap **Power**.
2. Tap what you want to do:

- {if:powerbutton}**Airplane Mode** or **Turn off Airplane Mode:** Turns all wireless features off or on ([learn more](/basics/turn-all-wireless-services-on-off-airplane-mode)).
- {if:powerbutton}**Restart:** Restarts your device.
- {if:!powerbutton}**Device Restart:** Restarts your device.
- {if:powerbutton}**Luna Next restart:** Restarts only the screens you work with. Your device stays on, but open applications close.
- {if:!powerbutton}**Luna-Next Restart:** Restarts only the screens you work with. Your device stays on, but open applications close.
- **Shut Down:** Turns your device off ([learn more](/basics/shut-down-your-device)).
- **Cancel:** Closes the menu.
