---
{
 "id": "contacts/receive-vcards",
 "title": "Receive vCards",
 "section": [],
 "order": 278,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/25115",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: luna-send com.palm.applicationManager/listAllHandlersForMime text/x-vcard -> com.palm.app.contacts",
  "org.webosports.app.contacts/src/views/AddToContactsPrompt.js:1",
  "adb: grep in /usr/palm/applications/com.palm.app.contacts/index.html: 'Add New Contact', 'Add To Existing', 'contacts?'"
 ],
 "requires": []
}
---

Open a vCard (a **.vcf** file), for example from an email. Contacts opens.

- If the file has one contact, tap **Add New Contact** or **Add To Existing**. If you tap **Add To Existing**, tap the contact to add it to.
- If the file has several contacts, tap **Import**.
