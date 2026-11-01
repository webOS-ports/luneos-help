---
{
 "id": "contacts/find-a-contact",
 "title": "Find a contact",
 "section": [],
 "order": 259,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/25319",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "org.webosports.app.contacts/src/util/search.js:5",
  "org.webosports.app.contacts/src/views/ContactsBar.js:7",
  "org.webosports.app.contacts/src/views/ContactsBar.js:65",
  "adb: grep in /usr/palm/applications/com.palm.app.contacts/index.html: 'Search Exchange'",
  "adb: grep -l REMOTECONTACTS /usr/palm/public/accounts/*/*.json: none on MindPhone, so the Search Exchange row cannot appear"
 ],
 "requires": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Contacts** > tap the search field > start typing.
2. Tap the contact.

Your search matches names, nicknames, companies, and the first part of email and IM addresses. Each word you type must match the start of one of these. Enter at least three digits to search phone numbers.
