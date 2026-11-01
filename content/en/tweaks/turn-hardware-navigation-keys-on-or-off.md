---
{
 "id": "tweaks/turn-hardware-navigation-keys-on-or-off",
 "title": "Turn hardware navigation keys on or off",
 "section": [],
 "order": 100003,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/services/org.webosports.service.tweaks.prefs/preferences/luna-next-cardshell.json md5 matches files/tweaks/luna-next-cardshell.json on both devices",
  "qml/AppTweaks/AppTweaks.qml hardwareNavigationKeys \"auto\"",
  "qml/CardShell.qml:239-241 on, or auto with hardware keyboard",
  "qml/Connectors/HardwareKeys.qml:_defaultActions, navigationKeys, actionFor, _overridden, _sendBack",
  "adb: /etc/luneos/hardware-keys.json is {} on both devices: no device override",
  "adb: HardwareKeys.qml on both devices differs from the repo only by added media keys",
  "the keys themselves and the setting were not tried"
 ]
}
---

Some devices have **Back**, **Home** and **Menu** keys. You can choose whether LuneOS uses them.

1. Open [Tweaks](/tweaks/use-tweaks), and tap **Luna**.
2. Under **ui**, tap **Hardware navigation keys**.
3. Tap one of these:

- **Automatic:** The keys work only on a device with a hardware keyboard.
- **On:** The keys always work.
- **Off:** The keys do nothing.

When the keys work, **Back** does the same as the [back gesture](/basics/go-up-one-level-in-an-app-back-gesture), and **Home** and **Menu** show or hide the Launcher.

On some devices a key has been given another job, and this setting doesn't change that key.
