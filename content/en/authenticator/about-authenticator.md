---
{
 "id": "authenticator/about-authenticator",
 "title": "About Authenticator",
 "section": [],
 "order": 100001,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.authenticator/appinfo.json (title, version 1.0.0, otpauth scheme; identical on both devices)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/AccountsPage.qml:205 (site shows a QR code and a key)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/AccountStore.qml:315,377,451 (noexport)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/main.qml:30 (time-based and counter-based)",
  "TouchPad getAppInfo runs the /usr/palm/applications copy; an older copy also sits in /media/cryptofs"
 ],
 "review": []
}
---

Many websites let you protect your account with two-step verification: after your password, the site asks for a short code that changes all the time. Authenticator makes these codes on your device, without needing a connection.

When you turn on two-step verification on a site, the site shows a QR code and a key. Add either one to Authenticator once, and it makes codes for that site from then on.

**Keep your recovery codes.** Your Authenticator accounts stay on this device and aren't part of a backup. If you lose or replace your device, you'll need the recovery codes from each site, and then you add each account again.

See Also [**Add an account to Authenticator**](/authenticator/add-an-account-to-authenticator)
[**Use a code to sign in**](/authenticator/use-a-code-to-sign-in)
