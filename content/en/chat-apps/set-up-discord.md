---
{
 "id": "chat-apps/set-up-discord",
 "title": "Set up Discord",
 "section": [
  "Set up a chat account"
 ],
 "order": 100004,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.discord/source/validator.js:104-146",
  "adb: /usr/palm/applications/com.palm.app.discord/source/validator.js:298-334",
  "adb: /usr/palm/public/accounts/com.palm.discord/com.palm.discord.json"
 ],
 "requires": []
}
---

You approve the sign-in with the Discord app on another phone, so you need that phone with you.

1. **[Open](/basics/open-an-application-in-the-launcher) Messaging** > **[Menu](/basics/open-the-application-menu)** (upper left) > **Preferences & Accounts** > **Add An Account** > tap **Discord**.
2. Under **USERNAME**, enter your Discord handle or email address. Leave **AUTH TOKEN** blank.
3. Tap **Sign In**. A QR code appears. If Discord asks you to prove you're human, complete the box first.
4. On your other phone, open Discord > **Settings** > **Scan QR Code**, and scan the code.
5. Approve the sign-in on your other phone.

The code lasts about two minutes. If it expires, tap **Get a new code**.

If you have your Discord web auth token, you can enter it under **AUTH TOKEN** instead of scanning a code. Keep your token private, because it gives full access to your account.
