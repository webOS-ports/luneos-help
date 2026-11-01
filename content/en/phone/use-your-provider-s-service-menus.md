---
{
 "id": "phone/use-your-provider-s-service-menus",
 "title": "Use your provider's service menus",
 "section": [
  "Make calls"
 ],
 "order": 85.3,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/IncomingUSSDAlert.qml:60-186",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialHandler.qml:166-172",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialStringParser.js:134-136",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/TelephonyManager.qml:86-96"
 ],
 "requires": [
  "modem"
 ]
}
---

Many wireless service providers offer short codes for checking your balance, topping up, and other services. Your provider can tell you which codes to use.

1. **[Open](/basics/open-an-application-in-the-launcher) Phone**.
2. Enter the code. These codes usually end in `#`.
3. Tap the dial button.
4. Do one of the following:
   - If you see a message, read it and tap **OK**.
   - If the provider shows a menu, enter your choice under **Your reply** > tap **Send**, or tap **Cancel** to leave the menu.

If you see **The request could not be sent.**, try again when you have a network connection.
