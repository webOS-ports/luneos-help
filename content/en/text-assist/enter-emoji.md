---
{
 "id": "text-assist/enter-emoji",
 "title": "Enter emoji",
 "section": [],
 "order": 359.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/share/maliit/plugins/org/luneos/EmojiPanel.qml (both devices)",
  "adb MindPhone: /usr/share/maliit/plugins/org/luneos/WordRibbon.qml emojiButton",
  "adb MindPhone: /usr/share/maliit/plugins/org/luneos/Keyboard.qml:141",
  "webos-keyboard/src/lib/logic/wordengine.cpp:175",
  "webos-keyboard/src/plugin/t9multitap.h:80",
  "adb: getPreferences keyboard (predictiveText true on MindPhone, false on TouchPad)"
 ]
}
---

1. In a text field, tap the smiley face at the right end of the strip above the keys.
2. To change the type of emoji, tap a tab above the emoji. Flick up or down to see more emoji.
3. Tap an emoji to enter it.
4. To go back to the keys, tap **ABC**.

If you don't see the smiley face, the strip is hidden. It appears only when **Predictive Text** or **Spell Checking** is on ([learn how](/text-assist/customize-text-assist-settings)). It never appears in password, number, phone number, email address, or web address fields.

Some physical keyboards have a key that opens emoji.
