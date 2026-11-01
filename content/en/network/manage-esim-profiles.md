---
{
 "id": "network/manage-esim-profiles",
 "title": "Manage eSIM profiles",
 "section": [
  "eSIM"
 ],
 "order": 100008,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimPage.qml:492",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimPage.qml:528",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimPage.qml:572",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimPage.qml:619",
  "adb: org.webosports.app.settings.esim absent on both devices"
 ],
 "requires": [
  "modem"
 ]
}
---

eSIM isn't installed on every device. If there's no **eSIM** app, your device doesn't offer it.

1. **[Open](/basics/open-an-application-in-the-launcher) eSIM**. The **Profiles** tab shows the eSIM chip's **EID** and your profiles.
2. Under **Profiles**, do any of the following:

   - To start or stop using a profile: Tap **Enable** or **Disable**.
   - To remove a profile: Disable it and tap **Delete**.
   - To update the list: Tap **Refresh**.

If your device has more than one SIM slot, the eSIM can be reached only while its slot is in use. Under **SIM slot**, tap **Slot 1**, **Slot 2**, and so on. The eSIM is usually in the last slot.

If you see **No eUICC was found on this device**, your device has no eSIM chip that LuneOS can reach. An eSIM adapter card in the SIM slot also works.
