---
{
 "id": "chat-apps/call-someone-over-a-chat-account",
 "title": "Call someone over a chat account",
 "section": [
  "Make calls with chat accounts"
 ],
 "order": 100008,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "org.webosports.app.phone/qml/views/PhoneTabView.qml:87,70 (Video tab only when a service has video)",
  "org.webosports.app.phone/qml/views/PhoneWindow.qml:448 (Switch to video? prompt)",
  "luneos-synergy-connectors 165229c, d3cdd93, 09f53a9 (videoFormat both for Signal, WhatsApp, Telegram; Teams already both)",
  "org.webosports.app.phone ffc85f8 (Call log: call back with video from the camera icon)",
  "adb: listAccountTemplates: PHONE on com.palm.telegram, com.palm.whatsapp, com.palm.teams, videoFormat none",
  "adb: ls /usr/share/luna-service2/services.d: com.palm.{teams,telegram,whatsapp}.call.service",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/ContactCallOptions.js",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/FavouritePage.qml:79",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/FavouritePage.qml:144",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PreferredServiceAlert.qml",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialProxy.qml:55-70",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/ContactLookupPage.qml:216"
 ],
 "requires": []
}
---

You can make voice and video calls over Telegram, WhatsApp, Teams, and Signal from Phone. Set up the account first ([learn how](/chat-apps/what-chat-services-can-i-use)), and make sure you have an internet connection.

Do one of the following:

- Dial a number: **[Open](/basics/open-an-application-in-the-launcher) Phone** > enter the number > tap the dial button. If Phone asks **Which service would you like to use?**, tap the account ([choose one to always use](/phone/choose-which-account-places-your-calls)).
- Call a favorite: **[Open](/basics/open-an-application-in-the-launcher) Phone** > **Favorites** > tap the arrow at the right of the favorite > tap the line for the account. The favorite's contact must have an address for that account.

{if:tablet}You can also search on the **Phone** tab: tap **Enter Name**, enter a name, and tap the line for the account.

**Video:** Phone shows a **Video** tab when one of your accounts can make video calls. To switch a voice call to video, use the video button on the call screen. If the other person switches to video, Phone asks **Switch to video?**. To call someone back with video, tap the camera icon in the **Call Log**.

To see which accounts can place calls, see [See your phone accounts](/phone/see-your-phone-accounts).
