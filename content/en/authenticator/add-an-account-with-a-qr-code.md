---
{
 "id": "authenticator/add-an-account-with-a-qr-code",
 "title": "Add an account with a QR code",
 "section": [],
 "order": 100003,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.authenticator/qml/AccountsPage.qml:214 (Scan QR code)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/main.qml:259,278 (Scan a QR code opens the Camera)",
  "/usr/palm/applications/org.webosports.app.camera/qml/components/CodeBanner.qml:78-110 (read on the TouchPad; Two-step verification, Codes for, Open)",
  "/usr/palm/applications/org.webosports.app.camera/qml/PreferencesModel.qml:55 (scanCodes on by default)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/EditAccountPage.qml:152 (From a link...)",
  "MindPhone has no org.webosports.app.camera, hence requires camera"
 ],
 "review": [],
 "requires": [
  "camera"
 ]
}
---

1. On the site, turn on two-step verification so that it shows a QR code.
2. **[Open](/basics/open-an-application-in-the-launcher) Authenticator** > **[Menu](/basics/open-the-application-menu)** > **Scan a QR code**. If you have no accounts yet, you can tap **Scan QR code** instead.
3. Point the camera at the QR code. A banner appears with **Two-step verification** and the name of the account.
4. Tap **Open**.
5. Check that this is the site you meant, and tap **Save**.
6. Enter the code from Authenticator on the site to finish.

If no banner appears, open **Camera**, and in its preferences turn on **Read QR codes and barcodes**.

See Also [**Add an account to Authenticator**](/authenticator/add-an-account-to-authenticator)
