---
{
 "id": "chat-apps/set-up-google-chat",
 "title": "Set up Google Chat",
 "section": [
  "Set up a chat account"
 ],
 "order": 100006,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.googlechat/source/validator.js:31-35",
  "adb: /usr/palm/applications/com.palm.app.googlechat/source/validator.js:46-75",
  "adb: /usr/palm/public/accounts/com.palm.googlechat/com.palm.googlechat.json"
 ],
 "requires": []
}
---

Google Chat signs in with values copied from a web browser, so this is easier to do with a computer next to you.

1. On a computer, sign in to chat.google.com in a private or incognito window.
2. **[Open](/basics/open-an-application-in-the-launcher) Messaging** > **[Menu](/basics/open-the-application-menu)** (upper left) > **Preferences & Accounts** > **Add An Account** > tap **Google Chat**.
3. Under **EMAIL ADDRESS**, enter your Google email address.
4. From the browser's cookies for that page, copy the values into **COMPASS COOKIE**, **SSID COOKIE**, **SID COOKIE**, **OSID COOKIE**, and **HSID COOKIE**.
5. Tap **Sign In**.

These values give access to your Google account, so keep them private.
