---
{
 "id": "accounts/accounts-overview",
 "title": "Accounts overview",
 "section": [],
 "order": 154,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42478",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: luna-send com.palm.service.accounts/listAccountTemplates (both devices)",
  "/usr/palm/applications/com.palm.app.accounts/source/AccountManager.js:48 (Local Account row)",
  "/usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/add-account.js:88 (groups)",
  "/usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/modify.js:34 (USE ACCOUNT WITH)",
  "adb: luna-send com.palm.accountservices/getAccountToken: service does not exist"
 ]
}
---

An online account is a service, such as Google, iCloud, or an email provider, where you keep things like email, contacts, calendars, messages, files, or photos.

Use the Accounts app to add and manage your online accounts. After you add an account, you choose which apps on your device use it.

**Add an Account** lists the kinds of accounts you can add, grouped under headings such as **EMAIL**, **CONTACTS & CALENDAR**, **MESSAGING & CHAT**, **CLOUD & PHOTOS**, and **MUSIC**. The list depends on what is installed on your device ([**see what you can add**](/accounts/what-kinds-of-accounts-can-i-add)).

Everything from your accounts shows up together in the apps you already use ([**learn how**](/accounts/how-your-accounts-work-together)).

The **Local Account** at the top of the Accounts app belongs to your device. It is not an online account, and LuneOS has no online account of its own that you sign in to.
