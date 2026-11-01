---
{
 "id": "accounts/delete-data-kept-from-a-removed-account",
 "title": "Delete data kept from a removed account",
 "section": [],
 "order": 156.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.accounts/source/AccountManager.js:84,361-385 (menu item, only with kept data)",
  "/usr/palm/applications/com.palm.app.accounts/source/RetainedDataView.js:17-27,102 (labels, swipe rows)",
  "~/Documents/GitHub/imlibpurpleservice/src/IMServiceHandler.cpp:280-314 (only the messaging service writes the record)",
  "adb: luna-send com.palm.db/find com.palm.imretaineddata:1 returned no rows: nothing to see on the devices, labels only"
 ],
 "review": []
}
---

If you removed a messaging or chat account and checked **Keep this account's data on this device**, its messages, contacts, and media stay on your device. You can erase them later.

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **[Menu](/basics/open-the-application-menu)** > **Delete Account Data**.

   This menu item appears only when a removed account has data on your device.
2. Under **REMOVED ACCOUNTS**, swipe the account and tap **Delete**.
3. Tap **Done**.

If you add the same account again, it no longer appears in this list, because its data is back in use.

See Also [**Use the Accounts application to edit or delete an online account**](/accounts/use-the-accounts-application-to-edit-or-delete-an-online-account)
