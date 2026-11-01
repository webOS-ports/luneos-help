# Productivity: replacements and new features

Topics: email, calendar, tasks, clock, memos, calculator, accounts, plus new topics authenticator and weather.
Devices read-only: MindPhone (MindPhone) and TouchPad (TouchPad). App copies pulled to ~/claude-scratch/help/audit/productivity-new/ (mp/, tp/). The page generator is write_pages.py in that folder.
"verified-device" has the same meaning as in productivity.md: labels and logic were read from the files or queries on the devices. Nothing was tapped.
Weather labels come from the repo source, each checked against build/app.js on both devices (minified, so no useful line numbers there).

25 new pages: 20 verified-device, 5 needs-device-test. 13 existing pages changed.

## New pages

| Page | Status | Evidence |
| --- | --- | --- |
| accounts/what-kinds-of-accounts-can-i-add | verified-device | listAccountTemplates on both (37 templates, same ids); add-account.js:71-88; util.js:25 |
| accounts/how-your-accounts-work-together | verified-device | Synergy replacement. accounts-list.js:136-143; AccountManager.js:59 |
| accounts/delete-data-kept-from-a-removed-account | verified-device | RetainedDataView.js; AccountManager.js:84; IMServiceHandler.cpp:280-314. com.palm.imretaineddata is empty on the MindPhone, so labels only |
| calendar/set-up-a-c-dav-account | needs-device-test | CrossAppTarget.js; urlschemes.js; template loc_usernameLabel |
| calendar/check-c-dav-sync | needs-device-test | CDavApp.js:77-92; listLaunchPoints |
| calendar/view-your-events-as-a-list | verified-device | DayViewFrame.js:42,46; WeekHeader.js:57; AgendaView.js; PreferencesView.js:162 |
| tasks/use-the-unfiled-list | verified-device | TasksDb.js:344; TasksView.js:115,129,350; TaskDetails.js |
| tasks/get-notified-about-tasks-that-are-due | verified-device | Launcher.js:20-30,221-256 |
| tasks/search-for-a-task | verified-device | TasksView.js:56,251-263; ListsView.js:48,100 |
| clock/change-the-clock-theme | verified-device | prefs.js:61-65,170; main.js:221-229 |
| clock/see-your-next-alarm-in-the-notification-area | needs-device-test | dashboardmanager.js, alarmdashstate.js, alarmDashboard.js (MindPhone); old dashboardmanager.js (TouchPad) |
| memos/give-a-memo-a-title | verified-device | build/app.js: Memo.setTitle, deriveTitle, isTitleAuto |
| calculator/use-formula-style | verified-device | build/app.js: FormulaEntry; Parser log is base 10, ln natural |
| email/select-several-messages-at-once | verified-device | Mail.js:49-52,109-121,744,1161,1224 |
| authenticator/about-authenticator | verified-device | appinfo.json; AccountStore.qml:315 (noexport) |
| authenticator/add-an-account-to-authenticator | verified-device | AccountsPage.qml; EditAccountPage.qml |
| authenticator/add-an-account-with-a-qr-code (requires camera) | verified-device | main.qml:259,278; TouchPad camera CodeBanner.qml:78; PreferencesModel.qml:55 |
| authenticator/use-a-code-to-sign-in | verified-device | AccountRow.qml:83-90,126,149; README for the red ring |
| authenticator/edit-or-delete-an-account-in-authenticator | verified-device | AccountsPage.qml:232-256; EditAccountPage.qml:187 |
| authenticator/change-the-order-of-your-accounts | verified-device | main.qml:283; AccountRow.qml:157-165 |
| authenticator/lock-authenticator | needs-device-test | main.qml:74,152-187,292-304; LockScreen.qml; README |
| weather/check-the-weather | verified-device | App.js:54-138; build/app.js strings |
| weather/add-or-remove-a-place | verified-device | App.js:142-155,380-437,498-510 |
| weather/change-weather-settings | verified-device | App.js:157-186,311 |
| weather/show-the-weather-in-the-notification-area | needs-device-test | App.js:191-197,254-300; Widget.js. The widget was not opened |

## Pages changed for replacements or links

- accounts/use-the-accounts-application-to-edit-or-delete-an-online-account: corrected. The keep-data box only has an effect for messaging and chat accounts (see Surprises). Long text moved to the new page.
- accounts/accounts-overview: links to the list of types and to how accounts work together (Synergy replacement).
- email/how-do-i-send-and-receive-email-on-my-device: says there is no Exchange or Microsoft 365 account type.
- email/delete-a-message: multi-select now points to the new page. It was also wrong for Delete Confirmation, because multi-delete always asks.
- Links to new pages only: calendar/set-up-an-online-account-in-calendar, calendar/how-do-i-get-events-into-calendar, calendar/change-the-calendar-display, clock/manage-clock, clock/set-an-alarm, memos/create-a-memo, calculator/use-calculator, tasks/create-a-task, tasks/view-tasks-that-are-due-today.

## Replacements

Confirmed: Synergy -> Accounts. The Accounts app still shows the heading SYNERGY ACCOUNTS, so the page uses that label.

Confirmed absent, pages stay deleted:
- Exchange: no template on either device, no EAS service in /usr/share/luna-service2/services.d (only imap, pop, smtp), EAS commented out in ManualConfig.js:57. ~/webos/LuneOS/exchange is an empty folder, o365 holds only a probe script for a tenant, and synergy only a log. The db kinds com.palm.task.eas and com.palm.tasklist.eas exist but nothing fills them. email/set-up-email-microsoft-exchange-and-lotus-notes stays deleted.
- Microsoft 365 or Outlook mail, contacts and calendars: no template. mojomail has no XOAUTH (grep of the binaries is 0). OneDrive and Teams are the only Microsoft account types.
- calendar/invite-others-to-an-event, email/format-email-text, email/reorder-accounts, email/reply-to-meeting-invitations, email/sort-email-in-a-folder: nothing new; the productivity.md reasons still hold.

The other replacements in BRIEF-new are not in this group's topics.

## Features found but not documented

- Calendar: Missed reminders. Not reachable. Nothing ever sets AppMenu.missedReminders, MissedRemindersView is not in any view, and AppView has no showReminders function. Marked TODO in AppMenu.js:62. Replaces item 13 in productivity.md's test list: the menu item cannot appear.
- Email: All Unread. Not reachable. Folders.js:346 reads showAllUnread, but Preferences has no switch and the default set does not include it. All Flagged has a switch.
- Calendar: New menu, Show today, Jump to... menu items: hidden in every view, as productivity.md says.
- Accounts: connectors in the layer recipes but not on either device (Immich, PhotoPrism, SmugMug, WebDAV, and Signal and YouTube in the connectors repo): no template on the devices, so not listed.
- Authenticator: otpauth:// links from other apps open the same screen as the QR path; not a separate page.
- Authenticator on a device without a camera: the Scan buttons stay visible and fail with "Could not open the Camera". The article is hidden by requires camera, but the app does not hide them.

## Surprises and bugs for the owner

- Keep this account's data on this device appears for every account, but only imlibpurple honours keepData. mojomail-imap, mojomail-pop, _cloudcore and the C+DAV service have no such code, so a user with a Google or email account who ticks it still loses the data, against the dialog's text. The articles say so. The checkbox should be hidden for those accounts.
- TouchPad build lacks OAuth client ids: GoogleOauth/CrossAppTarget.js and the config.js of box, dropbox, gdrive, hidrive, kdrive, koofr, onedrive, pcloud, yandexdisk still hold PLACEHOLDER values for the id (the service says a package built this way cannot sign in). On the TouchPad, Google C+DAV shows "Google sign-in is not available in this build." The MindPhone has real ids. The page mentions the Google message in one line. The rest is a build issue, so listAccountTemplates over-promises there.
- The Email Account table for Hotmail, Live and MSN uses POP with basic password login (AccountWizard.js:1722-1724); not established whether Microsoft still accepts it. Not documented; see test 7.
- The TouchPad has an older Authenticator in /media/cryptofs next to /usr/palm/applications. getAppInfo uses the /usr/palm copy (has the lock). It should be removed.
- Clock on the TouchPad: onMessageTap points at messageTap, which is not defined, so tapping its alarm notification may do nothing.
- Tasks: the due notification only follows due dates, no reminder time. Written that way.

## New topics (for toc.json)

| id | title | home group | icon |
| --- | --- | --- | --- |
| authenticator | Authenticator | Personal Information | ~/Documents/GitHub/org.webosports.app.authenticator/icon.png |
| weather | Weather | Personal Information | ~/Documents/GitHub/org.webosports.app.weather/icon.png |

## Links into other groups

- /contacts/linked-contacts-in-contacts, /messaging/set-up-an-im-account, /music/stream-music: from accounts/how-your-accounts-work-together.
- /screen-and-lock/set-options-for-unlocking-the-screen: from authenticator/lock-authenticator.
- /location-services/turn-location-service-providers-on-off: from weather/add-or-remove-a-place.
- /date-and-time/use-date-and-time: from weather/change-weather-settings.
- /basics/go-up-one-level-in-an-app-back-gesture, /basics/cut-copy-and-paste-information, /basics/open-an-application-in-the-launcher, /basics/open-the-application-menu.

## Needs device test

1. calendar/set-up-a-c-dav-account: add Google, iCloud, Yahoo and one Manual setup server. Confirm the screens and order, that USE ACCOUNT WITH appears, and whether iCloud needs an app-specific password (not stated in the article). Pick a known server with and without URL.
2. calendar/check-c-dav-sync: open C+DAV Sync App, confirm the account picker and that each of the three buttons does what the page says.
3. clock/see-your-next-alarm-in-the-notification-area: on both devices, set two alarms, leave Clock, snooze one, tap the text, tap the icon, throw it away.
4. authenticator/lock-authenticator: turn on the lock, leave for over a minute, come back. Try passcode and fingerprint on a device with a sensor, and face where enrolled.
5. authenticator/add-an-account-with-a-qr-code: on the TouchPad, scan a real QR code, tap Open, confirm Save and a working code at a real site.
6. weather/show-the-weather-in-the-notification-area: Compact and Hourly, tap the widget, tap its icon, restart the device and check when the widget returns.
7. Email Account with an outlook.com or hotmail.com address: does it sign in?
8. Remove a messaging account with the box ticked and confirm Delete Account Data as written; remove an email account with the box ticked and confirm the data goes.
9. tasks/get-notified-about-tasks-that-are-due: set a task due today, confirm the notification, the two taps, and that throwing it away keeps it away.
