---
{
 "id": "email/set-up-email",
 "title": "Set up email",
 "section": [
  "Set up email"
 ],
 "order": 165,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42312",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates '{}'",
  "adb: /usr/palm/applications/com.palm.app.email/mail/source/settings/Preferences.js:113",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/SimpleConfig.js:50",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/SimpleConfig.js:74",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/SimpleConfig.js:75",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/util.js:331",
  "adb: cat /usr/palm/public/accounts/com.palm.imap/*.json (hidden: true)"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Email**.
2. Do one of the following:
   - The first time you open Email, tap **Email Account**.
   - Any other time you open Email: **[Menu](/basics/open-the-application-menu)** > **Preferences & Accounts** > **Add Account** > **Email Account**.
3. Enter your email address and password > tap **Sign In**.
4. Tap **Create Account**.

**NOTE:** If automatic setup fails for your email account, an error message appears. Tap **Manual Setup** and enter the account settings ([**learn how**](/email/set-up-email-when-automatic-setup-fails)).
