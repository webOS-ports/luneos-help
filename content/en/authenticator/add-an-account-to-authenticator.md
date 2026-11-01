---
{
 "id": "authenticator/add-an-account-to-authenticator",
 "title": "Add an account to Authenticator",
 "section": [],
 "order": 100002,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.authenticator/qml/AccountsPage.qml:59,196-219 (Add, No accounts yet, Enter a key)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/EditAccountPage.qml:162-200 (Site, Name, Key, Save)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/EditAccountPage.qml:228-280 (More settings)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/EditAccountPage.qml:198-200 (a whole link fills in the rest)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/js/Base32.js:46,60,62; qml/js/Accounts.js:72 (messages)"
 ],
 "review": []
}
---

Use this when a site shows you a key to type in.

1. On the site, turn on two-step verification and find the key.
2. **[Open](/basics/open-an-application-in-the-launcher) Authenticator** > **Add**. If you have no accounts yet, you can tap **Enter a key** instead.
3. Enter the name of the site in **Site**, and your user name or email address in **Name**.
4. Enter the site's key in **Key**. Spaces and lowercase letters are fine.
5. Tap **Save**.
6. Enter the code from Authenticator on the site to finish.

If the site gives you a link starting with `otpauth://`, paste the whole link into **Key**. Authenticator fills in the rest.

Most sites don't need anything else. If a site tells you to use other settings, turn on **More settings** and set **Codes**, **Algorithm**, **Digits**, and **Seconds per code** (or **Counter**) as the site says.

{if:camera}If the site shows a QR code, you can scan it instead ([**learn how**](/authenticator/add-an-account-with-a-qr-code)).
