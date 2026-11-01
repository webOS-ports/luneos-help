---
{
 "id": "contacts/view-edit-or-delete-contact-information",
 "title": "View, edit, or delete contact information",
 "section": [],
 "order": 263,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/25305",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "org.webosports.app.contacts/src/views/ContactHeader.js:85",
  "org.webosports.app.contacts/src/views/EditContact.js:310",
  "org.webosports.app.contacts/src/views/EditContact.js:394",
  "adb: grep in /usr/palm/applications/com.palm.app.contacts/index.html: 'Edit Contact', 'Grayed entries come from accounts'"
 ],
 "requires": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Contacts** > tap the contact.
2. To change the information, tap the edit button at the lower right.
3. Do any of the following:
   - Change an entry: Tap it and type.
   - Add an entry: Tap a **New** field, such as **New phone number**.
   - Remove an entry: Tap the **×** next to it.
4. Tap **Save**.

Grayed entries come from accounts that cannot be changed here.

To delete the whole contact, see [Delete a contact](/contacts/delete-a-contact).
