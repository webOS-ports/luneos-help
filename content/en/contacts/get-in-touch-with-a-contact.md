---
{
 "id": "contacts/get-in-touch-with-a-contact",
 "title": "Get in touch with a contact",
 "section": [],
 "order": 272,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/25161",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "org.webosports.app.contacts/src/util/details.js:133",
  "org.webosports.app.contacts/src/views/ContactDetails.js:153",
  "adb: grep in /usr/palm/applications/com.palm.app.contacts/index.html: 'Chat', 'Voice Call', 'Video Call'",
  "adb: luna-send com.palm.applicationManager/listAllHandlersForUrl tel:123 -> com.palm.app.phone (not installed)"
 ],
 "requires": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Contacts** > tap the contact.
2. Do any of the following:
   - {if:modem}Call the contact: Tap the phone number.
   - {if:modem}Send a text message: Tap the message button next to the phone number.
   - Send an email: Tap the email address.
   - Chat with the contact: Tap the IM address > **Chat**.
   - View an address on a map: Tap the address.
   - Open a web address: Tap the address.

You can also find a contact with Just Type ([learn how](/just-type/get-in-touch-with-a-contact)).
