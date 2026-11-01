---
{
 "id": "phone/dial-by-contact-name-in-the-phone-application",
 "title": "Dial by contact name in the Phone application",
 "section": [
  "Make calls"
 ],
 "order": 80,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/19759",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/ContactLookupPage.qml:216",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhoneTabView.qml:148",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/DialerPage.qml:237",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/DialerPage.qml:406"
 ],
 "requires": [
  "modem"
 ]
}
---

<!-- ui:phone -->

The keypad fills the Phone tab, so you find a contact from what you dial:

1. **[Open](/basics/open-an-application-in-the-launcher) Phone**.
2. Enter at least three digits of the contact's number. The matching contact, or the number of matching contacts, appears above the keys.
3. Tap the contact's name to fill in the number > tap the dial button.

To find someone by name, use Just Type ([learn how](/phone/dial-by-contact-name-using-just-type)).

<!-- ui:tablet -->

1. **[Open](/basics/open-an-application-in-the-launcher) Phone**.
2. On the **Phone** tab, tap **Enter Name** and type a name until the contact you want appears.
3. Tap the phone number.

See also [Create a contact](/contacts/create-a-contact)
