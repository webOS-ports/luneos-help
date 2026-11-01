---
{
 "id": "calendar/delete-an-online-account-from-calendar",
 "title": "Delete an online account from Calendar",
 "section": [],
 "order": 251,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26243",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/util.js:329",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/remove-account.js:43",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/remove-account.js:138",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/util.js:353",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/modify.js:38"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Calendar** > **[Menu](/basics/open-the-application-menu)** > **Preferences & Accounts**.
2. Under **Accounts**, tap the account name > **Remove Account** > **Remove Account**.

If other apps also use that account, this stops synchronization of calendar events only, and the other apps continue to synchronize. If only Calendar uses the account, the whole account is removed from your device.

The events are not deleted from the online account.

To restart synchronization with an account you removed from Calendar: Open the **Accounts** app > tap the account name > turn on Calendar.
