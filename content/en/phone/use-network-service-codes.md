---
{
 "id": "phone/use-network-service-codes",
 "title": "Use network service codes",
 "section": [
  "Make calls"
 ],
 "order": 85.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/MmiCodes.js",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialStringParser.js:114-165",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/SupplementaryServices.qml:218-357",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialHandler.qml:318-322",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhoneWindow.qml:330",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/CallMessages.js (mmi messages)"
 ],
 "requires": [
  "modem"
 ]
}
---

You can change some network settings by dialing a code. What works depends on your wireless service provider.

1. **[Open](/basics/open-an-application-in-the-launcher) Phone**.
2. Enter the code.
3. Tap the dial button. You see **Sending your request...**, and then the result.

In these codes, replace **number** with a phone number, **password** with your four-digit barring password, and **old** and **new** with the old and new password or PIN.

**Call forwarding**

- See whether calls are forwarded: `*#21#`
- Forward all calls: `**21*number#`
- Forward calls when you're busy: `**67*number#`
- Forward calls you don't answer: `**61*number#`
- Forward calls when you can't be reached: `**62*number#`
- Stop forwarding: `##21#`, `##67#`, `##61#`, or `##62#`, or `##002#` for all of them

**Call waiting**

- See whether it's on: `*#43#`
- Turn it on: `*43#`
- Turn it off: `#43#`

**Call barring**

- See whether calls are barred: `*#33#` for outgoing calls, `*#35#` for incoming calls
- Bar all outgoing calls: `*33*password#`
- Bar international calls: `*331*password#`
- Bar international calls except to your home country: `*332*password#`
- Bar all incoming calls: `*35*password#`
- Bar incoming calls when roaming: `*351*password#`
- Turn off all barring: `#330*password#`
- Change your barring password: `**03*330*old*new*new#`

**Your device and SIM card**

- Show your IMEI number: `*#06#`
- Change your SIM PIN: `**04*old*new*new#`
- Unlock your SIM with the PUK code: `**05*PUK*new*new#`

A code the device doesn't recognize goes to your provider ([learn more](/phone/use-your-provider-s-service-menus)). If airplane mode is on, only the PIN and PUK codes work.
