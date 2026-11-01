---
{
 "id": "basics/use-the-onscreen-keyboard",
 "title": "Use the onscreen keyboard",
 "section": [
  "Enter information"
 ],
 "order": 40.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/40389",
 "status": "verified-device",
 "review": [],
 "requires": [
  "!keyboard"
 ],
 "evidence": [
  "adb: /usr/share/maliit/plugins/org/luneos/keys md5 matches",
  "webos-keyboard/plugins/en/qml/Keyboard_en_phone.qml",
  "webos-keyboard/plugins/en/qml/Keyboard_en_tablet.qml",
  "webos-keyboard/qml/keys/DismissKey.qml",
  "adb: settings-common qml/General/TextAssistPage.qml:235-243"
 ]
}
---

<!-- ui:phone -->

The onscreen keyboard appears when you tap a text field.

- **Shift:** Tap for a capital letter ([learn how](/basics/enter-uppercase-letters)).
- **123:** Tap for numbers and symbols, and **ABC** to go back ([learn how](/basics/enter-symbols-and-alternate-characters)).
- **Enter:** Tap to start a new line or accept what you entered. Some applications give this key another name.

To change the layout, [open](/basics/open-an-application-in-the-launcher) **Text Assist** on the **Prefs** tab.

<!-- ui:tablet -->

![image](/legacy/device_drawings/keyboard_US_towi.png)

1. **Tab:** Tap to move to the next field.
2. **Symbols:** Tap **+=[]** for the symbol keyboard, and **ABC** to go back.
3. **Enter:** Tap to start a new line or accept what you entered. Some applications give this key another name.
4. **Hide keyboard:** Tap to hide the keyboard. To resize the keys, tap and hold, and then tap a size.
5. **Space**

To change the layout, [open](/basics/open-an-application-in-the-launcher) **Text Assist** on the **Prefs** tab.
