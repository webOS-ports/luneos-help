---
{
 "id": "phone/lock-or-unlock-the-sim-card",
 "title": "Lock or unlock the SIM card",
 "section": [
  "Customize device settings"
 ],
 "order": 135,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/19463",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:380",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:389",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:724",
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:322"
 ],
 "requires": [
  "modem"
 ]
}
---

Get your default PIN from your wireless service provider first.

1. **[Open](/basics/open-an-application-in-the-launcher) Phone** > **[Menu](/basics/open-the-application-menu)** (upper left) > **Phone Preferences**.
2. Under **Security**, do any of the following:
   - To lock the SIM card: **Lock SIM Card** > enter the PIN > **Done**. To use the SIM card after you restart your device, you must then enter the PIN.
   - To change the PIN of a locked SIM card: **Change SIM Card PIN** > enter the old PIN > enter a new PIN of 4 to 8 numbers twice.
   - To turn off SIM lock: **Unlock SIM Card** > enter the PIN > **Done**.

You can also do this in Network Settings, under **SIM PIN**.
