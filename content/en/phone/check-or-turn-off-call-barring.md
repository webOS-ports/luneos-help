---
{
 "id": "phone/check-or-turn-off-call-barring",
 "title": "Check or turn off call barring",
 "section": [
  "Customize device settings"
 ],
 "order": 138.3,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:394-415",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:594-625",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:654-667",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/SimPinCard.qml:195-209"
 ],
 "requires": [
  "modem"
 ]
}
---

Call barring blocks calls on your account at the network. Check with your wireless service provider about availability, and for your barring password.

1. **[Open](/basics/open-an-application-in-the-launcher) Phone** > **[Menu](/basics/open-the-application-menu)** (upper left) > **Phone Preferences**.
2. Under **Call Barring**, see what is set for **Outgoing calls** and **Incoming calls**.
3. To remove all barring, tap **Turn all barring off** > enter your four-digit barring password > tap **Done**. If you see **Could not turn barring off**, the password may be wrong or the network may have refused the change.

To turn barring on, or to change your barring password, use a [network service code](/phone/use-network-service-codes).
