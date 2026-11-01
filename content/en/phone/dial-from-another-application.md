---
{
 "id": "phone/dial-from-another-application",
 "title": "Dial from another application",
 "section": [
  "Make calls"
 ],
 "order": 85,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/19821",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "org.webosports.app.contacts/src/util/details.js:133",
  "adb: luna-send com.palm.applicationManager/listAllHandlersForUrl tel:123 -> com.palm.app.phone",
  "adb: luna-send com.webos.service.applicationManager/getAppInfo com.palm.app.phone -> Invalid appId"
 ],
 "requires": [
  "modem"
 ]
}
---

Applications open a phone number in Phone. For example, tap a phone number in a contact entry to call it.

If nothing happens when you tap a number, **[Open](/basics/open-an-application-in-the-launcher) Phone** and dial it from there.
