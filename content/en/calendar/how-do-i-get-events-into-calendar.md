---
{
 "id": "calendar/how-do-i-get-events-into-calendar",
 "title": "How do I get events into Calendar?",
 "section": [],
 "order": 232,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42213",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates '{}'",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/prefs/PreferencesView.js:214",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/EditView.js:130",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/modify.js:35"
 ]
}
---

You have two options for getting events to show up in Calendar:

- Connect to an online calendar: Calendar can synchronize with Google, iCloud, and Yahoo calendars, and with other servers that use CalDAV ([**learn how**](/calendar/set-up-a-c-dav-account)). Events you enter online show up automatically in Calendar. Events you enter on your device sync to the online account, provided the account allows it.

  You can set up your calendar accounts in the Accounts app ([**learn how**](/accounts/use-the-accounts-application-to-set-up-an-online-account)) or in the Calendar app ([**learn how**](/calendar/set-up-an-online-account-in-calendar)). During setup you can also choose other apps to use the same account, such as Contacts.
- Enter an event directly in Calendar ([**learn how**](/calendar/create-an-event)): You can assign the event to one of your online calendars, and it synchronizes with that calendar. Or you can create the event in your LuneOS calendar, which means it shows up on your device only.
