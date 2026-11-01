---
{
 "id": "network/add-an-esim-profile",
 "title": "Add an eSIM profile",
 "section": [
  "eSIM"
 ],
 "order": 100007,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimPage.qml:434",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimPage.qml:708",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimPage.qml:766",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimQrScanner.qml:148",
  "meta-luneos/.../org.webosports.app.settings-qml.bb PACKAGES ${PN}-esim",
  "adb: org.webosports.app.settings.esim absent on both devices"
 ],
 "requires": [
  "modem"
 ]
}
---

eSIM isn't installed on every device. If there's no **eSIM** app, your device doesn't offer it.

Downloading a profile needs a working internet connection. An activation code can normally be used only once, so check it before you tap **Download profile**.

**Use a QR code**

1. **[Open](/basics/open-an-application-in-the-launcher) eSIM** > **Scan QR**.
2. Fit the whole QR code from your operator inside the square. The details are filled in on the **Add profile** tab.
3. Check them and tap **Download profile**.

**Enter the details yourself**

1. **[Open](/basics/open-an-application-in-the-launcher) eSIM** > **Add profile**.
2. Enter the **SM-DP+ address** and **Activation code** from your operator, and the **Confirmation code** if you have one. You can also paste the whole LPA:1$... string from the QR code into the address field.
3. Tap **Download profile**.

To start using the profile, see [Manage eSIM profiles](/network/manage-esim-profiles).
