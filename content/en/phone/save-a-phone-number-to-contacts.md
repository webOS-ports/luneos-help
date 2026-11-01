---
{
 "id": "phone/save-a-phone-number-to-contacts",
 "title": "Save a phone number to Contacts",
 "section": [],
 "order": 123,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/18791",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/CallGroupDetails.qml:347",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/CallLineDelegate.qml:191",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/CallGroupDetails.qml:382",
  "org.webosports.app.contacts/src/util/launch.js:107"
 ],
 "requires": [
  "modem"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Phone** > **Call Log**.
2. Tap the arrow at the right of the call > **Add to Contacts**. Contacts opens.
3. If the number is not filled in for you, tap the add button at the lower right of the contact list and enter it ([learn how](/contacts/create-a-contact)).

When you have two calls in progress, the line of a caller who isn't in Contacts has an add contact button too.
