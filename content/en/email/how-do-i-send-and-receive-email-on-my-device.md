---
{
 "id": "email/how-do-i-send-and-receive-email-on-my-device",
 "title": "How do I send and receive email on my device?",
 "section": [],
 "order": 164,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/22109",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates '{}'",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/ManualConfig.js:57",
  "adb: /usr/palm/applications/com.palm.app.email/accounts/source/ManualConfig.js:59",
  "adb: ls /usr/share/luna-service2/services.d (com.palm.imap, com.palm.pop, com.palm.smtp present)"
 ]
}
---

Use the Email application on your device to read and send email from accounts that work with IMAP or POP, such as those from your internet provider or a web-based email service. You must create the account online before you can set it up on your device. There's no Microsoft Exchange or Microsoft 365 account type ([**see what you can add**](/accounts/what-kinds-of-accounts-can-i-add)).

You can set up your email accounts in either of these locations:

- The Accounts app ([**learn how**](/accounts/use-the-accounts-application-to-set-up-an-online-account))
- The Email app ([**learn how**](/email/set-up-email))

If you wish, you can also use your device's web browser to view your web-based email: just go to the email provider's website.
