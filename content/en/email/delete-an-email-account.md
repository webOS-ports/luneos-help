---
{
 "id": "email/delete-an-email-account",
 "title": "Delete an email account",
 "section": [
  "Set up email"
 ],
 "order": 171,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/22447",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.email/mail/source/MailApp.js:89",
  "adb: /usr/palm/applications/com.palm.app.email/mail/source/settings/AccountSettings.js:247",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/util.js:329",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/util.js:353"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Email**.
2. **[Menu](/basics/open-the-application-menu)** > **Preferences & Accounts** > tap the account name.
3. Tap **Remove Account** > **Remove Account**. To keep the messages on your device, first tap **Keep this account's data on this device**.

When you delete an email account from your device, it removes the account information from your device only. It does not affect your account with the email provider.
