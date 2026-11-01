---
{
 "id": "email/set-up-email-when-automatic-setup-fails",
 "title": "Set up email when automatic setup fails",
 "section": [
  "Set up email"
 ],
 "order": 167,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42327",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/SimpleConfig.js:75",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/ManualConfig.js:49",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/ManualConfig.js:75",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/ManualConfig.js:127",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/ManualConfig.js:135",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/ManualConfig.js:182",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/ManualConfig.js:190"
 ]
}
---

Follow these steps only if automatic setup ([**learn how**](/email/set-up-email)) does not work for your email account.

Before You Begin

Get this info from your email provider or system administrator:

- Account type (POP or IMAP)
- Incoming and outgoing mail server names
- Incoming mail server username and password
- Incoming and outgoing server port numbers
- Any SSL or TLS requirements for incoming and outgoing mail
- Any authentication requirements for outgoing mail
- Root folder (IMAP accounts only)

1. If you have already started account setup and sign-in failed, tap **Manual Setup**, and skip to step 5. Otherwise, start at step 2.
2. **[Open](/basics/open-an-application-in-the-launcher) Email**.
3. Do one of the following:
   - The first time you open Email, tap **Email Account**.
   - Any other time: **[Menu](/basics/open-the-application-menu)** > **Preferences & Accounts** > **Add Account** > **Email Account**.
4. Enter your email address and password > **Sign In**. When the sign-in fails, tap **Manual Setup**.
5. Tap the field under **Account Type** > tap **IMAP** or **POP**.
6. Enter info for the incoming and outgoing mail server, based on the server information you got from your email provider or system administrator.
7. Tap **Sign In**.
8. Tap **Create Account**.
