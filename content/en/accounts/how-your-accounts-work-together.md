---
{
 "id": "accounts/how-your-accounts-work-together",
 "title": "How your accounts work together",
 "section": [],
 "order": 154.7,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates '{}' (both devices, 37 templates, same ids)",
  "productivity-apps/mindphone/accounts-lib/source/accounts-list.js:136-143 (per-kind groups under the list title)",
  "/usr/palm/applications/com.palm.app.accounts/source/AccountManager.js:59 (SYNERGY ACCOUNTS)",
  "productivity-apps/mindphone/accounts-lib/source/modify.js:34 (USE ACCOUNT WITH)",
  "/usr/palm/applications/org.webosports.app.documents/source/services/CloudService.js (reads DOCUMENTS accounts)",
  "/usr/palm/services/com.palm.service.photos/lib/capabilities.js (PHOTO.UPLOAD accounts)"
 ],
 "review": []
}
---

You don't need a separate app for each online service. Add an account once, and its information shows up in the apps you already use, next to the information from your other accounts.

- **Email:** Read all your inboxes together ([**learn how**](/email/merged-inboxes-in-email)).
- **Calendar:** See the events from all your calendars in one view ([**learn how**](/calendar/layered-calendars)).
- **Contacts:** Entries for the same person from different accounts are linked into one contact ([**learn how**](/contacts/linked-contacts-in-contacts)).
- **Messaging:** Your conversations from chat accounts appear in Messaging ([**learn how**](/messaging/set-up-an-im-account)).
- **Documents and Photos & Videos:** Files and pictures from your cloud accounts appear in these apps.
- **Music:** Play music from your streaming accounts ([**learn how**](/music/stream-music)).

Accounts keeps all of this in one place. Your online accounts are listed under **SYNERGY ACCOUNTS**, sorted by kind. Tap an account to choose which apps use it under **USE ACCOUNT WITH** ([**learn how**](/accounts/use-the-accounts-application-to-edit-or-delete-an-online-account)).

See Also [**What kinds of accounts can I add?**](/accounts/what-kinds-of-accounts-can-i-add)
