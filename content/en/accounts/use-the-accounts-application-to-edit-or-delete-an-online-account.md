---
{
 "id": "accounts/use-the-accounts-application-to-edit-or-delete-an-online-account",
 "title": "Use the Accounts application to edit or delete an online account",
 "section": [],
 "order": 156,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/28923",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/modify.js:31-43",
  "/usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/util.js:328-353",
  "/usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/remove-account.js:37-48",
  "/usr/palm/applications/com.palm.app.accounts/source/AccountManager.js:84 (Delete Account Data)",
  "/usr/palm/applications/com.palm.app.accounts/build.js (Swipe an entry and tap Delete)",
  "~/Documents/GitHub/imlibpurpleservice/src/IMServiceHandler.cpp:280-314 (keepData honoured)",
  "adb: grep keepData: none in /usr/bin/mojomail-imap, mojomail-pop, /usr/palm/services/_cloudcore; none in org.webosports.service.cdav"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > tap the account name.
2. Do one of the following:
   - To change the account display name: Under **ACCOUNT NAME**, tap the current name and enter the new name.
   - To change which apps use the account: Under **USE ACCOUNT WITH**, turn each app on or off.
   - To change your sign-in details: Tap **Change Login Settings** > enter the new details > **Sign In**.
   - To delete the account: Tap **Remove Account**. To keep a messaging or chat account's messages, contacts, and media on your device, check **Keep this account's data on this device**. Tap **Remove Account**.

The box appears for every account, but only messaging and chat accounts keep their data. Email, C+DAV, and cloud accounts lose theirs from your device even if you check it.

If you kept the data of a removed account, you can erase it later ([**learn how**](/accounts/delete-data-kept-from-a-removed-account)).
