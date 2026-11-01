---
{
 "id": "basics/use-the-system-menu",
 "title": "Use the system menu",
 "section": [
  "Use the menus"
 ],
 "order": 51.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/40326",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/StatusBar/SystemMenu/SystemMenu.qml:165-460",
  "qml/StatusBar/SystemMenu/MuteElement.qml",
  "qml/StatusBar/SystemMenu/SimElement.qml"
 ]
}
---

[Open the system menu](/basics/open-the-connection-menu), and then do any of the following:

- See the date and the **Battery** level at the top.
- {if:brightness}To adjust the screen brightness: Drag the slider.
- {if:!volumebutton}To adjust the volume: Drag the slider.
- {if:modem}To choose which SIM card to use: Tap **SIM**.
- To use Wi-Fi, VPN or Bluetooth: Tap the item to see what's available. Tap **Wi-Fi Preferences**, **VPN Preferences** or **Bluetooth Preferences** for more.
- To turn all wireless features on or off: Tap **Turn on Airplane Mode** or **Turn off Airplane Mode**.
- To stop the screen turning with your device ([learn how](/appearance/lock-the-screen-rotation)): Tap **Turn on Rotation Lock** or **Turn off Rotation Lock**.
- {if:keyboard}To show or hide the onscreen keyboard: Tap **Show On-screen Keyboard** or **Hide On-screen Keyboard**.
- To turn sound off or on ([learn how](/basics/turn-sound-off-or-on)): Tap **Mute Sound** or **Unmute Sound**.
- {if:!powerbutton}To restart or shut down ([learn how](/basics/use-the-power-menu)): Tap **Power**.

If the menu is longer than the screen, scroll it to see more items.

You can replace this menu with the [New Device Menu](/tweaks/use-the-new-device-menu).
