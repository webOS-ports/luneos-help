---
{
 "id": "phone/use-dialing-shortcuts",
 "title": "Use dialing shortcuts",
 "section": [
  "Customize device settings"
 ],
 "order": 134,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/19689",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:322",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:367",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:474",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:484",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialingShortcuts.qml:34",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialHandler.qml:275"
 ],
 "requires": [
  "modem"
 ]
}
---

Dialing shortcuts add a prefix at the beginning of a number, so you can dial an extension instead of the whole number.

1. **[Open](/basics/open-an-application-in-the-launcher) Phone** > **[Menu](/basics/open-the-application-menu)** (upper left) > **Phone Preferences** > under **Dialing Shortcuts**, tap **+ Add a number**.
2. Set the following:

   **Number length:** Under **When I Dial**, choose how many digits you dial: 4, 5, 6, or 7.

   **Enter Number:** Under **Use This Dialing Prefix**, enter the prefix to add at the beginning of the number you dial. The prefix and the digits you dial must add up to a complete phone number.
3. Tap **Done**.

To delete a shortcut, drag it sideways > **Delete**.

**Example:** A complete phone number in your company's phone system is 1-408-555-1122, and from inside the system you dial only the last five digits. Choose **5 digits** and enter 140855 as the prefix. When you dial 51122, your device dials 14085551122.
