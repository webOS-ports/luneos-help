---
{
 "id": "contacts/delete-a-contact",
 "title": "Delete a contact",
 "section": [],
 "order": 273,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/25285",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "org.webosports.app.contacts/src/views/EditContact.js:278",
  "org.webosports.app.contacts/src/views/EditContact.js:521",
  "adb: grep in /usr/palm/applications/com.palm.app.contacts/index.html: 'Delete Contact', 'Delete All Profiles', 'profiles cannot be deleted'"
 ],
 "requires": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Contacts** > tap the contact.
2. Tap the edit button at the lower right.
3. Tap **Delete Contact** > **Delete**. If the contact is linked to several profiles, tap **Delete All Profiles** to delete all of them.

Some accounts don't allow deleting. If so, you see a message that those profiles cannot be deleted.
