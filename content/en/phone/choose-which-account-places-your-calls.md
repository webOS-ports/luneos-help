---
{
 "id": "phone/choose-which-account-places-your-calls",
 "title": "Choose which account places your calls",
 "section": [
  "Customize device settings"
 ],
 "order": 138.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:274-301",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PreferredServiceAlert.qml:66-102",
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialProxy.qml:55-85"
 ],
 "requires": []
}
---

You make this choice only if you have a chat account that can make calls ([learn more](/chat-apps/call-someone-over-a-chat-account)).

1. **[Open](/basics/open-an-application-in-the-launcher) Phone** > **[Menu](/basics/open-the-application-menu)** (upper left) > **Phone Preferences**.
2. Under **Domestic Calls** and **International Calls**, tap **Use** and choose an account, or **Always Ask**.
3. Tap **Done**.

If you choose **Always Ask**, Phone asks **Which service would you like to use?** each time you dial. Tap an account. To skip this question next time, first select **Always use this service for these calls**.

Service codes and emergency numbers always go over your SIM card.
