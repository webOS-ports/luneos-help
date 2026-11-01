---
{
 "id": "just-type/get-in-touch-with-a-contact",
 "title": "Get in touch with a contact",
 "section": [],
 "order": 141,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42438",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: com.palm.launcher pulled from both devices, identical",
  "app/MainView.js MIN_SEARCH_LENGTH",
  "app/ContactSearch.js",
  "data/AppLauncher.js launchEmail, launchPhone, launchSMS"
 ]
}
---

1. [Display Card view](/basics/display-card-view-minimize-an-application) and tap the **Just type...** field.
2. Type at least two letters of the contact's name, or an email address.
3. To see only contacts, tap the **Contacts** tab.
4. Tap the contact to see ways to get in touch, and then tap one of them.
   - Tap an email address to write a message.
   - {if:modem}Tap a phone number to call it.
   - {if:modem}Tap the message icon next to a phone number to send a text message.
