---
{
 "id": "chat-apps/set-up-facebook",
 "title": "Set up Facebook (E2EE)",
 "section": [
  "Set up a chat account"
 ],
 "order": 100007,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.gometa/source/validator.js:28-64",
  "adb: /usr/palm/applications/com.palm.app.gometa/appinfo.json",
  "adb: luna-send com.palm.service.accounts/listAccountTemplates: com.palm.gometa Facebook (E2EE)"
 ],
 "requires": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Messaging** > **[Menu](/basics/open-the-application-menu)** (upper left) > **Preferences & Accounts** > **Add An Account** > tap **Facebook (E2EE)**.
2. Under **EMAIL ADDRESS**, enter the email address, phone number, or username for your Facebook account. If you like, enter a **DISPLAY NAME**.
3. Under **PASSWORD**, enter your password.
4. Tap **Sign In**.

If your account uses two-factor authentication, you're asked for a code the first time you connect.
