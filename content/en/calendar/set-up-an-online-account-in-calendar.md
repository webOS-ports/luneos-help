---
{
 "id": "calendar/set-up-an-online-account-in-calendar",
 "title": "Set up an online account in Calendar",
 "section": [],
 "order": 235,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42231",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.calendar/app/prefs/PreferencesView.js:159",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/util.js:323",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/util.js:326",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/util.js:331",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/entry-first-launch.js:247",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/accounts/source/modify.js:35",
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates '{}'"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Calendar**.
2. Do one of the following:
   - Set up an online account the first time you use Calendar ([**learn how**](/calendar/use-calendar-for-the-first-time)).
   - To set up an online account any other time: **[Menu](/basics/open-the-application-menu)** > **Preferences & Accounts** > **Add an Account** > tap an account type: **Google C+DAV**, **iCloud C+DAV**, **Yahoo C+DAV**, or **C+DAV Connector** for another CalDAV server ([**learn how**](/calendar/set-up-a-c-dav-account)).
3. Enter the account information > **Sign In**.
4. Depending on the account, you may be presented with options for which apps should download data from that account. For each app, tap **On** or **Off**, and then tap **Create Account**.
