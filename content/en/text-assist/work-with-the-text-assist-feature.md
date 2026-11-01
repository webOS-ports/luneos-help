---
{
 "id": "text-assist/work-with-the-text-assist-feature",
 "title": "Work with the Text Assist feature",
 "section": [],
 "order": 357,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/17287",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/TextAssistPage.qml:222",
  "webos-keyboard/src/plugin/inputmethod_p.h:307",
  "webos-keyboard/src/lib/logic/wordengine.cpp:276",
  "webos-keyboard/qml/WordRibbon.qml:96",
  "webos-keyboard/src/lib/models/wordribbon.cpp:167",
  "adb: /etc/palm/defaultPreferences.txt keyboard"
 ]
}
---

Text Assist controls how the onscreen keyboard helps you type. Turn each feature on or off in the **Text Assist** app ([learn how](/text-assist/customize-text-assist-settings)).

**Auto-Capitalization:** Capitalizes the start of a sentence.

**Auto-Correction:** Fixes a word as you finish it.

**Spell Checking:** Underlines a misspelled word and offers corrections above the keyboard.

**Predictive Text:** Offers the next word above the keyboard. Tap a word to use it.
