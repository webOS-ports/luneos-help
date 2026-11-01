---
{
 "id": "regional-settings/select-a-default-country-code-for-phone-numbers",
 "title": "Select a default country code for phone numbers",
 "section": [],
 "order": 519,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/40303",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/LanguagePickerPage.qml:250",
  "adb: settings-common/qml/General/LanguagePickerPage.qml:267",
  "adb: settings-common/qml/General/LanguagePickerPage.qml:344",
  "adb: settings-common/qml/General/LanguagePickerPage.qml:428",
  "adb: settings-common/qml/General/LanguagePickerPage.qml:441"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Regional Settings**.
2. Under **Phone Numbers**, tap **Region** > tap a country.
3. Tap **Apply Changes and Restart** > **Apply and Restart**. To save the change without restarting, tap **Apply Only**. The change doesn't take effect everywhere until your device restarts.

This region is for contacts and phone numbers that don't carry a country code. The Phone app currently uses the region under **Formats** instead ([learn how](/regional-settings/change-the-display-formats)).
