---
{
 "id": "chat-apps/set-up-signal",
 "title": "Set up Signal",
 "section": [
  "Set up a chat account"
 ],
 "order": 100003.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "luneos-synergy-connectors/im/signal/apps/com.palm.app.signal/source/validator.js:4-15 (device-link QR sign-in)",
  "luneos-synergy-connectors/im/signal/apps/com.palm.app.signal/source/validator.js:59-60,80-83 (on-screen wording, Get a new code)",
  "luneos-synergy-connectors/im/signal/account/com.palm.signal/com.palm.signal.json (templateId com.palm.signal, PHONE NUMBER label)"
 ],
 "requires": []
}
---

You link your device to Signal on another phone, so you need that phone with you.

1. **[Open](/basics/open-an-application-in-the-launcher) Messaging** > **[Menu](/basics/open-the-application-menu)** (upper left) > **Preferences & Accounts** > **Add An Account** > tap **Signal**.
2. Under **PHONE NUMBER**, enter your number in international format, such as +15551234567.
3. Tap **Sign In**. A QR code appears.
4. On your other phone, open Signal > **Settings** > **Linked Devices** > **Link New Device**, and scan the QR code.

If the code expires, tap **Get a new code**.

You can make voice and video calls over Signal ([learn how](/chat-apps/call-someone-over-a-chat-account)).
