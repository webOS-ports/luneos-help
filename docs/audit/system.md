# Audit: group "system"

Topics: accounts, backup, exhibition, print-manager, software-manager, system-updates, device-info, sim-toolkit.
Devices used read-only: TouchPad (TouchPad), MindPhone (MindPhone). The MindPhone copies of the apps were pulled to
~/claude-scratch/help/audit/system-dev/ (tp/ and mp/). Device shell QML is in mp/shell-qml. It differs from the repo in many files, but DockMode is identical.
The rewrite script is ~/claude-scratch/help/audit/system-dev/tools/rewrite.py. Originals of deleted articles are in ~/claude-scratch/help/content-imported/en/.

Counts: 24 kept (14 verified-device, 6 verified-source, 4 needs-device-test), 17 deleted.
"verified-device" means the labels were read from files or query results on the device. Nothing was tapped, so see "Needs device test".

## Articles

| Article | Status | What changed | Evidence |
|---|---|---|---|
| accounts/accounts-overview | verified-device | Removed Synergy and App Catalog. Added the real list groups, Local Account, and "no online account of its own" | listAccountTemplates on both; AccountManager.js:48; add-account.js:88; com.palm.accountservices does not exist |
| accounts/use-the-accounts-application-to-set-up-an-online-account | verified-device | Add an Account (never "Add Account"), search box, no Find More, provider sign-in page, USE ACCOUNT WITH, Create Account. ui blocks merged | add-account.js:111; util.js:320-332; modify.js:34-44 |
| accounts/use-the-accounts-application-to-edit-or-delete-an-online-account | verified-device | Real labels. Added the keep-data checkbox and Delete Account Data. ui blocks merged | modify.js:31-43; remove-account.js:37-48; AccountManager.js:84 |
| backup/manually-back-up-information-to-your-luneos-account | verified-device | Retitled "Back up your device manually". Now describes the real local backup. Slug kept | BackupInfo.js:10; BackupProgress.js:9; BackupApp.js:96; listTargets |
| backup/erase-luneos-account-information-from-the-server | verified-device | Retitled "Turn Backup on or off". No server; it erases the on-device backups. Added delete one backup. Slug kept | BackupInfo.js:28-31,170; BackupListPage.js:64-76 |
| exhibition/customize-exhibition-settings | verified-device | Checkboxes only, Time fixed, no Find More | ExhibitionPage.qml:69-125; listDockModeLaunchPoints |
| exhibition/start-exhibition | verified-source | Start Exhibition button first. Inductive dock only, not USB. Not during a call | ExhibitionPage.qml:135; DisplayStates.cpp:331-338,518; DisplayManager.cpp:573-580 |
| exhibition/exit-exhibition | verified-source | Gesture area tap, {if:homebutton}, off the dock. Ends in Card view, not the last-used item | DockMode.qml:70,85; CardShell.qml:86-90; DisplayDockMode::handleEvent |
| exhibition/use-exhibition | verified-source | Page menu, swipe, last-used page. Dropped the notification and Secure Unlock claims (not established) | DockMode.qml:43-50; ExhibitionAppMenu.qml:68; AppMenu.qml:91-92 |
| exhibition/use-your-device-as-a-clock | verified-source | Added the three faces | Clocks.qml:42-50; ExhibitionAppMenu.qml:50 |
| exhibition/view-a-picture-slideshow | verified-source | Rewritten for org.webosports.app.photos. Must be ticked first. Legacy icons removed. Merged | SlideshowView.qml:35,200,226,252-285,294; listDockModeLaunchPoints |
| print-manager/add-a-printer | verified-device | Real form labels. devices now phone and tablet | PrintManagerPage.qml:247,287-319,335; listPrinters found a network printer on both |
| print-manager/cancel-printing | verified-device | Cancel button beside the job, Cancel All. devices now phone and tablet | PrintManagerPage.qml:168-235; listJobs |
| print-manager/remove-a-printer | verified-device | Swipe, Delete, manual printers only. devices now phone and tablet | PrintManagerPage.qml:335,422,445 |
| print-manager/what-printers-can-i-add | verified-device | IPP, IPP Everywhere, AirPrint instead of HP PCL. Print from Photos. devices now phone and tablet | luneos-print-adapter.bb:1-38; /usr/libexec/cups/filter (32 files on both); PictureView.qml:290; printmgr/printers/listActive |
| software-manager/manage-downloaded-applications | verified-device | Software Manager does not exist. Now Applications (list, details, swipe delete) and Preware 2 (install) | ApplicationsPage.qml:156,174,252,343; app.js strings; listLaunchPoints |
| software-manager/manually-check-for-application-updates | verified-device | Preware 2: Update Feeds, Package Updates, Update, Update All | preware source lines in the article; strings confirmed in device build/app.js |
| system-updates/update-the-system-software-from-a-notification | needs-device-test | Retitled "System update notifications". Says plainly that it cannot be installed from the device. Slug kept because basics links here | update.js:30,263-272; 24h activity; UpdatePage placeholder; updates visible:false |
| device-info/view-system-information | verified-device | No More Info. Real rows. Merged | DeviceInfoPage.qml:91-191; retrieveVersion |
| device-info/restart-your-device | verified-source | Power hold > Restart, {if:!powerbutton} System menu > Power > Device Restart. Device Info has no Reset Options. Ringer and Center key text removed; the forced restart was not provable | PowerdAlerts.js:81-84; PowerdService.js:204; ShutdownScreen.qml:36; SystemMenu.qml:469-476; PowerMenu.qml:69 |
| device-info/install-a-certificate-from-usb-drive-storage | needs-device-test | Rewritten for the real import popup, downloads folder only. States there is no Launcher icon | CertificatePage.qml:211,282-332; FilePickerPopup.qml:68-69; certificate visible:false |
| device-info/delete-a-certificate | needs-device-test | Swipe, Delete. States there is no Launcher icon | CertificatePage.qml:191; listAll answers |
| device-info/view-certificate-details | needs-device-test | No details screen; the list row shows name, issuer, expiry | CertificatePage.qml:104,155 |
| sim-toolkit/use-sim-toolkit | verified-device | requires modem. App is always in the Launcher, so "not in the Launcher" was wrong. Added the empty-menu case | appinfo.json; MenuPage.qml:44-55 |

## Deleted articles

| Article | Reason (proof) |
|---|---|
| accounts/create-a-skype-account-in-accounts | No Skype template in listAccountTemplates on either device |
| accounts/sign-in-to-a-skype-account-in-accounts | Same |
| backup/update-your-luneos-account-settings | No such account: com.palm.accountservices "Service does not exist" on both devices. The Accounts row stays disabled without it (AccountManager.js:294-310) |
| backup/what-is-a-luneos-account | Same. Remote erase, hpwebos.com and server backup are all gone |
| exhibition/view-your-day-s-agenda | No Agenda page: listDockModeLaunchPoints has only Music, Photos & Videos. Calendar appinfo has no exhibitionMode |
| software-manager/update-a-downloaded-application-from-a-notification | Preware has no notification code (AppPanels.js:543-549 are TODOs). Nothing else notifies |
| system-updates/get-help-if-a-software-update-fails | LuneOS Doctor does not exist; the article also relied on server backups |
| system-updates/manually-check-for-system-updates | System Updates is visible:false, its title is "(placeholder)", and UpdatePage.qml is the fake example page. No app calls checkUpdate, downloadUpdate or initiateUpdate (grep on device) |
| device-info/change-default-applications | No UI in Settings or any app. Option key text was wrong too |
| device-info/erase-data-and-reset-your-device | No erase or reset UI anywhere (grep of all settings QML) |
| device-info/install-a-certificate-from-an-email-attachment | /etc/palm/command-resource-handlers.json sends .pem, .p12, .crt etc. to org.webosports.app.settings, which is not installed. No Trust Certificate UI |
| device-info/rename-your-device | Name is a read-only row, generated at boot from the adaptation (DeviceInfoPage.qml) |
| device-info/run-a-custom-application | No such item. Device Info has no menu |
| device-info/run-automated-diagnostics | No Diagnostics in any app |
| device-info/run-interactive-diagnostics | Same |
| device-info/run-interactive-tests | Same |
| device-info/run-quick-tests | Same |

## Bugs and decisions for the owner

- Certificate Manager works (certmgr answers listAll) but appinfo has visible:false, so it is not in listLaunchPoints and has no entry anywhere. Setting visible:true in org.webosports.app.settings/data/appinfo.certificate.json would make the three articles usable; then remove their first line. If you do not want it visible, delete the three articles.
- System updates have a backend but no UI. The toast opens org.webosports.app.settings, which is not installed on either device, with a page that does not exist (update README B12).
- TouchPad: retrieveVersion fails, "Could not parse version", because /etc/luneos-release has build tree "<unknown>". Device Info version rows and the update check are affected on that build.
- The Exhibition settings page still says the shell shows only clocks and that ticked apps "will appear once the shell hosts them" (ExhibitionPage.qml:128). The device shell does host them. The on-screen text is stale; the articles follow the shell.
- Certificate handlers and update.js still name org.webosports.app.settings. The same applies to the Accounts template "HP webOS Account" (com.palm.palmprofile) and accounts strings naming hpwebos.com; also the Help menu items in Backup and Accounts point to webosarchive.org and help.palm.com.
- Backup differs per device: the TouchPad build has "Reinstall apps when restoring" and the MindPhone build has not, with the same version number 3.1.1. Not documented in the articles for that reason.
- The Backup screen says "webOS Doctor" (BackupInfo.js:10); there is no such LuneOS tool.
- Photos is the only app found that prints.
- com.webos.service.print/printers/listActive did not answer within 30 s on the MindPhone; the same call on com.palm.printmgr answered, and that is what Photos uses.

## Cross-group links

- All my articles link /basics/open-an-application-in-the-launcher.
- /basics/open-the-application-menu: used by accounts edit, backup manual, software-manager updates. Its front matter says devices phone only and it mentions the gesture area light; these apps run on tablets too.
- /basics/copy-files-between-your-device-and-your-computer: backup manual, certificate install.
- /screen-and-lock/set-the-interval-for-turning-the-screen-off-automatically: exhibition start.
- Inbound: basics/maximize-battery-life links /system-updates/update-the-system-software-from-a-notification to say "download system updates", plus "LuneOS App Catalog". There is no download from the device, so that bullet needs to go. The page itself is kept.
- basics/2-turn-your-phone-completely-off-and-on says Power > Restart; the real labels are the power button menu Restart, or System menu Power > Device Restart (Power only appears without a power button).

## Missing articles

- Backup: what Backup saves and where (Back up to, What to back up, media, passphrase for passwords, Limited backup box)
- Backup: restore a backup (menu Restore a backup..., Manage backups, passphrase, restart)
- Exhibition: Now Playing page (Music)
- Accounts: list of supported account types; delete data kept from a removed account as its own page
- Preware 2: Manage Feeds, Install Package, Saved Package List, Luna Manager, Preferences
- Applications: permissions shown per app
- Storage, Encryption, Developer Mode, USB, Tethering pages if no other group has them
- Power menu: Airplane Mode, Luna Next restart, Shut Down
- Printing a picture from Photos
- Emergency Broadcast, eSIM, Network Settings if no other group has them
- Authenticator, Torch, System Monitor, Terminal, Tweaks, Weather if no other group has them
- Waydroid (present on the MindPhone)

## Needs device test

Exhibition
1. Settings Exhibition > Start Exhibition on each device: does Time show, and does the status bar show "Time" at the upper left?
2. Tick Photos & Videos and Music, start Exhibition, tap the title: is there a "Choose an App" list? Does swiping work between app pages? Can you swipe off the Time page, or do the clock faces take the swipe?
3. Exit: tap the gesture area; on a device with the gesture area off in Tweaks, what exits Exhibition? Press the home button on a device that has one. Does the screen land on Card view?
4. With a screen lock passcode set, does exiting Exhibition ask for it?
5. TouchPad on a real Touchstone: starts with screen off? After the inactivity time with screen on? Leaves when lifted?
6. Slideshow: controls for five seconds, Select Album, shuffle, Show Each Photo For. Does a swipe change the picture rather than the Exhibition page?

Accounts
7. Add an account with a password and one with a provider sign-in: is the order of screens as written? Does an OAuth account show Change Login Settings?
8. Remove with the keep-data box, then Menu > Delete Account Data: swipe and Delete as written? Does the Accounts menu open on the tablet?

Backup
9. Turn Backup on, Back Up Now, turn off with Turn Off and Erase, delete one backup. Confirm "webos-backups" is what a computer sees over USB.

Printing
10. Add a printer by address; tap to make default; swipe and Delete; print from Photos; cancel a job. Do AirPrint-only printers work?

System and devices
11. Hold the power button on each device: which menu appears, and after how long? On a device without one: System menu > Power > Device Restart. Is there a forced restart to document?
12. If a real update toast appears, what does tapping it do?
13. Launch Certificate Manager (luna-send launch) and try import, swipe delete, and whether a row can be tapped.
14. Preware 2: Available Packages path (type, category, package) on phone and tablet; Update All.
15. Applications: swipe and Delete on an app that can be removed.
16. SIM Toolkit with a SIM that has a menu, and on the TouchPad (no modem) to see the message shown.
