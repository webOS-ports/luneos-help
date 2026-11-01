---
{
 "id": "chat-apps/what-chat-services-can-i-use",
 "title": "What chat services can I use?",
 "section": [],
 "order": 100001,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: luna-send com.palm.service.accounts/listAccountTemplates (both devices' template lists)",
  "adb: ls /usr/palm/public/accounts on TouchPad and MindPhone",
  "adb: ls /usr/lib/purple-2 (libtelegram-tdlib, libwhatsmeow, libdiscord, libteams, libgooglechat, libmatrix)",
  "adb: /usr/palm/applications/com.palm.app.telegram/appinfo.json (\"visible\": false)",
  "adb: /usr/palm/applications/com.palm.app.gometa/appinfo.json"
 ],
 "requires": []
}
---

Chat services work inside Messaging. They have no icons of their own in the Launcher: you add an account, and your chats appear in Messaging alongside your other conversations.

- [Telegram](/chat-apps/set-up-telegram)
- [WhatsApp](/chat-apps/set-up-whatsapp)
- [Discord](/chat-apps/set-up-discord)
- [Teams](/chat-apps/set-up-teams)
- [Google Chat](/chat-apps/set-up-google-chat)
- [Facebook (E2EE)](/chat-apps/set-up-facebook)
- [Jabber and Matrix](/messaging/set-up-an-im-account)

Once an account is set up, you use it as you do any IM account ([learn how](/messaging/send-and-receive-im-messages)). To remove one, see [Delete an IM account](/messaging/delete-an-im-account).

Telegram, WhatsApp, and Teams can also make voice calls ([learn how](/chat-apps/call-someone-over-a-chat-account)).
