---
{
 "id": "text-assist/use-another-keyboard-layout",
 "title": "Use another keyboard layout",
 "section": [],
 "order": 359.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: /usr/share/maliit/plugins/org/luneos/keys/LanguageKey.qml:47",
  "adb MindPhone: /usr/share/maliit/plugins/org/luneos/keys/KeyPad.qml:154",
  "adb MindPhone: /usr/share/maliit/plugins/org/luneos/lib/*/Keyboard_*_{tablet,phone}.qml alternativeLayouts",
  "adb: settings-common/qml/General/TextAssistPage.qml:129"
 ]
}
---

To change the layout for good, see [Customize Text Assist settings](/text-assist/customize-text-assist-settings). Some layouts are for phones or tablets only.

{if:tablet}To switch layout while you type:

1. {if:tablet}Make sure more than one keyboard language is set up, so that the language key appears ([learn how](/regional-settings/set-up-and-switch-among-multiple-onscreen-keyboard-layouts-and-languag)).
2. {if:tablet}Press and hold the language key.
3. {if:tablet}Tap a layout, such as **Thumb** or **Dvorak**. Tap **LuneOS** to go back to the standard layout.

{if:tablet}The layouts on offer depend on the language. Nothing appears if the language has only the standard layout.
