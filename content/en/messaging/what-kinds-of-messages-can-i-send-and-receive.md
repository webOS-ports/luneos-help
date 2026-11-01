---
{
 "id": "messaging/what-kinds-of-messages-can-i-send-and-receive",
 "title": "What kinds of messages can I send and receive?",
 "section": [],
 "order": 202,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/20729",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "org.webosports.messaging/app/src/views/ComposeView.js:221",
  "adb: grep in /usr/palm/applications/org.webosports.app.messaging/index.html: 'New MMS on your phone'",
  "adb: grep -l MESSAGING /usr/palm/public/accounts/*/*",
  "adb: luna-send com.palm.service.accounts/listAccountTemplates"
 ],
 "requires": []
}
---

- {if:modem}**Text messages:** Send and receive SMS messages.
- **Instant messages:** Chat using an online account that supports messaging, such as Telegram, WhatsApp, Discord, Teams, Google Chat, Matrix, or Jabber. Set up the account first ([see all services](/chat-apps/what-chat-services-can-i-use)).

You can't send multimedia messages.
