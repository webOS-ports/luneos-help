---
{
 "id": "tweaks/use-the-new-device-menu",
 "title": "Use the New Device Menu",
 "section": [],
 "order": 100002,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/services/org.webosports.service.tweaks.prefs/preferences/luna-next-cardshell.json md5 matches files/tweaks/luna-next-cardshell.json on both devices",
  "adb: NewDeviceMenu.qml md5 matches repo on TouchPad; on MindPhone differs only in Bluetooth disconnect",
  "qml/StatusBar/SystemMenu/NewDeviceMenu.qml:376-410 tabs, :99 tap collapses, :416-775 labels, :781-797 edges",
  "qml/StatusBar/StatusBar.qml:637 Loader picks the menu from the tweak, value false by default",
  "NewDeviceMenu.qml has no mute, VPN, SIM or Power entry; signal showPowerMenu never emitted"
 ]
}
---

The New Device Menu replaces the [system menu](/basics/use-the-system-menu) with a menu in the middle of the screen, with one tab for each subject. It's off until you turn it on.

**Turn it on**

1. Open [Tweaks](/tweaks/use-tweaks), and tap **Luna**.
2. Under **Status Bar**, set **Use New Device Menu** to **Yes**.

To go back to the system menu, set it to **No**.

**Use it**

[Open it](/basics/open-the-connection-menu) the way you open the system menu. The date is at the top, with a row of icons below it. Tap an icon to show its tab, and tap it again to hide the tab. You can also tap near the left or right edge of the menu to go to another tab.

- Wi-Fi icon: **Wi-Fi**, the networks in range and **Wi-Fi Preferences**.
- Bluetooth icon: **Bluetooth**, your devices and **Bluetooth Preferences**.
- Location icon: **GPS**, **Network Location** and **Location Preferences**.
- Sound icon: **Ringtone**, **Media** and **System** volume.
- Screen icon: **Brightness**, **Rotation Lock** and **Flashlight**.
- Phone icon: **Airplane Mode**.
- {if:modem}Also under the phone icon: **Phone Radio**, **Data Usage**, **Data Network** and **Data Roaming**.
- {if:keyboard}Also under the phone icon: **On-screen Keyboard**.

**What it doesn't have**

There's no VPN, SIM or mute item in this menu.

{if:!powerbutton}There's also no **Power** item, so keep the system menu if you need it to shut down or restart.
