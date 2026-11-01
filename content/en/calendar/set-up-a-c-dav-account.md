---
{
 "id": "calendar/set-up-a-c-dav-account",
 "title": "Set up a C+DAV account",
 "section": [],
 "order": 235.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates '{}' (both devices, 37 templates, same ids): validators and loc_usernameLabel AppleId, Yahoo ID",
  "/usr/palm/applications/org.webosports.app.cdav/CrossAppTarget/CrossAppTarget.js:23-62 (form labels)",
  "/usr/palm/applications/org.webosports.app.cdav/CrossAppTarget/CrossAppTarget.js:192-233,290 (error text)",
  "/usr/palm/applications/org.webosports.app.cdav/CrossAppTarget/urlschemes.js (Known Servers, needPrefix)",
  "/usr/palm/applications/org.webosports.app.cdav/GoogleOauth/CrossAppTarget.js:31 (header; TouchPad copy has unfilled client id placeholders)",
  "productivity-apps/mindphone/accounts-lib/source/credentials.js:56-63 (default sign-in screen)",
  "productivity-apps/mindphone/accounts-lib/source/modify.js:34-44"
 ],
 "review": []
}
---

C+DAV accounts add your online contacts and calendars to Contacts and Calendar. They work with services and servers that use CalDAV and CardDAV.

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account**. Under **CONTACTS & CALENDAR**, tap the account you want.
2. Do one of the following:
   - **iCloud C+DAV** or **Yahoo C+DAV:** Enter your **AppleId** or **Yahoo ID** and your password > **Sign In**.
   - **Google C+DAV:** Sign in on the Google page that opens.
   - **C+DAV Connector:** Follow the steps below to connect to any other server.
3. If the account offers a choice of apps, turn each one on or off under **USE ACCOUNT WITH**, and then tap **Create Account**.

To connect to another server with **C+DAV Connector**:

1. Under **Connection settings**, tap **Known Servers** and select your server. If it isn't listed, keep **Manual setup**.
2. In **Name**, enter a name for the account.
3. In **URL**, enter the address of your server. With some known servers, such as fruux.com or Mailbox.org, the address is already known and you can't enter one here.
4. Enter your **Username** and **Password**.
5. Check **Ignore SSL Certificate Errors** only if you trust the server and it can't be reached otherwise.
6. Tap **Check Credentials**.

If you see "Credentials were wrong or could not be checked.", check what you entered, and that the server address is right. To go back without adding the account, tap **Back**.

If Google C+DAV shows "Google sign-in is not available in this build.", you can't add this account on your device.

See Also [**Use the Accounts application to edit or delete an online account**](/accounts/use-the-accounts-application-to-edit-or-delete-an-online-account)
[**Check C+DAV sync**](/calendar/check-c-dav-sync)
