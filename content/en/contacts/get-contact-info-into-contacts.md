---
{
 "id": "contacts/get-contact-info-into-contacts",
 "title": "Get contact info into Contacts",
 "section": [],
 "order": 252,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42163",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: grep -l CONTACTS /usr/palm/public/accounts/*/* (cdav, Google, iCloud, Yahoo, Discord, Teams and others)",
  "org.webosports.app.contacts/src/views/FirstLaunch.js:47"
 ],
 "requires": []
}
---

Do any of the following:

- Add an online account that has contacts ([learn how](/contacts/set-up-an-online-account-in-contacts)). Contacts in the account appear in Contacts and stay in sync.
- Enter contacts yourself ([learn how](/contacts/create-a-contact)).
- Open a vCard ([learn how](/contacts/receive-vcards)).
