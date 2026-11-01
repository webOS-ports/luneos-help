---
{
 "id": "phone/add-a-phone-number-to-a-favorite",
 "title": "Add a phone number to a favorite",
 "section": [
  "Work with favorites"
 ],
 "order": 120,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/18943",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/FavouritePage.qml:142",
  "org.webosports.app.contacts/src/views/EditContact.js:47",
  "adb: grep in /usr/palm/applications/com.palm.app.contacts/index.html: 'New phone number', 'Favourites', 'Save'"
 ],
 "requires": [
  "modem"
 ]
}
---

A favorite with no number shows **TAP TO ADD NUMBER** on the **Favorites** tab. Numbers belong to the contact, so you add them in Contacts.

1. **[Open](/basics/open-an-application-in-the-launcher) Contacts** > **Favourites** > tap the contact.
2. Tap the edit button at the lower right of the contact.
3. Tap **New phone number** > enter the number > choose a label from the list beside it, such as mobile or work.
4. Tap **Save**.
