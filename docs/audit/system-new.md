# Audit: group "system", replacements and new features

Devices read-only: TouchPad (TouchPad), MindPhone (MindPhone). The TouchPad dropped off adb for a while, then came back. Pulled app copies are in ~/claude-scratch/help/audit/system-dev/ (tp2, mp2, mp-svc). The page generator is tools/new_pages.py there; full evidence is in each page's front matter.
Nothing was tapped. "verified-device" means labels and behaviour were read from device files and query results.

## New pages (29: 21 verified-device, 6 needs-device-test, 2 verified-source)

| Page | Status | First evidence |
|---|---|---|
| backup/back-up-your-saved-passwords | verified-device | com.palm.app.backup/source/UserDataPage.js:114-128 (Saved passwords, note) |
| backup/choose-what-to-back-up | verified-device | com.palm.app.backup/source/UserDataPage.js:54-130,134-137 (rows, Done) |
| backup/do-i-need-a-luneos-account | verified-device | adb: com.palm.accountservices: Service does not exist (both devices) |
| backup/manage-your-backups | verified-device | com.palm.app.backup/source/BackupInfo.js:86-90 (Manage backups row) |
| backup/restore-a-backup | verified-device | com.palm.app.backup/source/BackupApp.js:95 (Restore a backup...) |
| backup/what-does-backup-save | verified-device | com.palm.app.backup/source/UserDataPage.js:36-48 (Always included) |
| backup/what-does-limited-backup-mean | verified-source | com.palm.app.backup/source/BackupInfo.js:21-22,69-73 (Limited backup box) |
| exhibition/show-music-in-exhibition | verified-device | org.webosports.app.music/appinfo.json (exhibitionMode) |
| exhibition/which-apps-work-in-exhibition | verified-device | adb: luna-send com.palm.applicationManager/listDockModeLaunchPoints (Music, Photos & Videos on both) |
| software-manager/find-and-install-apps-with-preware-2 | needs-device-test | com.palm.app.preware2/build/app.js (strings below confirmed) |
| software-manager/install-a-package-from-a-file-or-link | needs-device-test | com.palm.app.preware2/build/app.js (Package Location, Browse, Get Info, Install) |
| software-manager/manage-software-feeds | needs-device-test | com.palm.app.preware2/build/app.js (New Feed, Name, URL, Compressed, Add Feed, Third-party Feed, Delete, Close) |
| software-manager/set-preware-2-preferences | verified-device | com.palm.app.preware2/build/app.js (all labels) |
| software-manager/use-luna-manager | needs-device-test | com.palm.app.preware2/build/app.js (Luna Manager, Rescan, Restart Luna, Restart Java) |
| software-manager/use-the-saved-package-list | verified-device | com.palm.app.preware2/build/app.js (Saved Package List, Remove from Saved or Uninstall?, Saved Only, Uninstall, savedPackagesTaken) |
| system-updates/update-luneos-to-a-newer-version | verified-source | ~/webos/LuneOS/OTA/NOTES.md (no working updater; status update 2026-10-14: updater stack unchanged, no feeds, no update page) |
| storage/check-how-much-storage-is-in-use | verified-device | org.webosports.app.settings-common/qml/General/StoragePage.qml:158 (box per volume), :208-240 (Used, Free, Filesystem, Device), :260 (note), :272 (Encryption) |
| storage/turn-developer-mode-on-or-off | verified-device | org.webosports.app.settings-common/qml/General/DeveloperOptionsPage.qml (Developer Mode, Debugging, USB Debugging, explanation texts) |
| utilities/add-an-account-to-authenticator | verified-device | org.webosports.app.authenticator/qml/AccountsPage.qml:59,196-219 |
| utilities/browse-files-with-luneos-explorer | verified-device | com.palm.stark.files/source/App.js:46-62 (toolbar), :82-84, :101-104 (menu) |
| utilities/check-the-weather | needs-device-test | org.webosports.app.weather/build/app.js (labels) |
| utilities/check-your-device-with-system-monitor | verified-device | org.webosports.app.sysmonitor/qml/OverviewPage.qml:37-322 (sections) |
| utilities/get-a-code-from-authenticator | verified-device | org.webosports.app.authenticator/qml/AccountsPage.qml:51,239-248 |
| utilities/lock-authenticator | verified-device | org.webosports.app.authenticator/qml/main.qml:176-183,292-299 |
| utilities/record-sound | verified-device | org.webosports.app.soundrecorder/qml/RecordingsPage.qml:40,202-208,246,330-342 |
| utilities/test-your-sensors-with-messwerk | verified-device | org.webosports.app.messwerk/qml/pages/*.qml (Accelerometer, Gyroscope, Light & Proximity, Magnetometer, Position, Pressure, Rotation, GNSS Satellites) |
| utilities/use-fingerterm | needs-device-test | org.mer.app.fingerterm/Main.qml:261-272 (menu button, upper right) |
| utilities/use-the-terminal | verified-device | org.webosports.app.terminal/qml/KeyboardRows/Layouts.js (Scroll, Cmds, Fx, Nano, Ctrl) |
| utilities/use-your-device-as-a-torch | verified-device | org.webosports.app.torch/qml/main.qml (Tap to turn on/off, Torch unavailable; closing the card turns it off) |

## Pages changed for replacements

- backup/manually-back-up-information-to-your-luneos-account: links to what it saves and to restore.
- software-manager/manage-downloaded-applications: says Preware 2 takes the place of the app catalog; links the new install page and security/see-what-an-application-may-use.
- system-updates/update-the-system-software-from-a-notification: links the real way to update.
- print-manager/what-printers-can-i-add: links photos/print-pictures; says Photos & Videos is the only app that prints.
- exhibition/use-exhibition, exhibition/customize-exhibition-settings: link which-apps-work-in-exhibition.

## Replacements confirmed

- Palm Profile -> local Backup, no account: backup/do-i-need-a-luneos-account, backup/what-does-backup-save.
- App Catalog -> Preware 2: confirmed, 6 pages.
- Software update -> reinstall from a computer: confirmed by OTA notes (updater stack still unchanged on 2026-10-14) and webos-ports.org.
- webOS Doctor -> reinstall: basics/reinstall-luneos already exists (shell group). I link to it instead of writing a second page.
- Data Transfer Assistant -> Backup and MTP: basics/move-your-information-to-another-device already exists (shell group). Mine removed.
- App permissions: security/see-what-an-application-may-use already exists (settings group). Mine removed.
- Printing from Photos: photos/print-pictures already exists (media group). Not rewritten.

## Replacements confirmed absent (stay deleted)

- system-updates/manually-check-for-system-updates: no update page; settings.updates visible false.
- system-updates/get-help-if-a-software-update-fails: nothing to fail on the device.
- software-manager/update-a-downloaded-application-from-a-notification: Preware has no notification.
- backup/update-your-luneos-account-settings: no such account.
- device-info: change-default-applications, erase-data-and-reset, rename, diagnostics: no replacement found.
- Remote erase and locate: none. The account page says so.

## Features found, not documented

- Waydroid: covered by the android-apps topic (shell group).
- Tweaks: tweaks topic. Encryption: security topic. USB: network topic. Not repeated.
- Documents: not in my list.
- Testr, SDL2 OpenGLES 1 Test, SDL2 OpenGLES 2 Test, Youtube (com.webos.app.test.youtube), Video Proto, Documents (test): test apps, left out on purpose.
- LuneOS Explorer: Share Over FTP, network addresses (ftp, sftp, smb, davs), Google Drive, compress and extract have no page of their own. Only named in the browse page.
- Backup: Back up to dialog has one choice, so no page. Cancelling a running backup: button exists, not separately described.

## Bugs and decisions for the owner

- basics/reinstall-luneos says "To get a newer version of LuneOS without reinstalling, see System update notifications". There is no such way. It should link /system-updates/update-luneos-to-a-newer-version.
- Storage: the "Internal storage" name is never used on either device, because the list has /userdata, not /media/internal. It shows "userdata". The MindPhone lists many technical partitions (/android/vendor, /mnt/vendor/nvdata...), the TouchPad /uboot. The page text stays general for this reason.
- Exhibition: both devices answer enabled false for all apps. ~/webos/LuneOS/exhibition/TESTING.md says the choice is not saved across restarts. Not confirmed, so not in the text. See test 2.
- Exhibition settings still show the stale note about clocks. The new page tells users it is out of date; remove that line when the note goes.
- Exhibition list has two Photos & Videos on the MindPhone (a com.palm.app.photos in cryptofs as well).
- Restore: a row of an app that was not reinstalled opens com.palm.app.enyo-findapps, which does not exist (RestoringPage.js openAppDetails). The article does not say to tap it.
- Backup: deviceName is empty on the MindPhone, so restore rows read "webOS device (this device)". The "Cannot Restore" dialog says "webOS", the info box says "webOS Doctor", and the Limited box says to install with Preware or WebOS Quick Install, which does not apply.
- Backup builds differ with the same version 3.1.1: only the TouchPad has Reinstall apps when restoring. The article says "On some devices".
- Preware 2: Restart Java runs killall java, and neither device has java. Use App Tuckerbox is a leftover too. getConfigs is empty on both, so the default feeds have never been added there. Most feeds use plain http and date from the old devices.
- ~/webos/LuneOS/exhibition/TESTING.md notes appinstalld failing on the MindPhone ("Failed to extract package"). That would break Install on that device.
- Torch: appinfo is visible false on the MindPhone, yet torch service getStatus says available true and /sys/class/leds has no flash there. On that device the Flashlight button may do nothing.
- Fingerterm uses qsTrId; if its fingerterm_eng_en.qm is not loaded, the menu shows ids instead of the labels I used. See test 8.

## Needs device test

1. Preware 2, first start with Internet: are the feeds added, does Available Packages fill, do type > category > package > Install, Launch and Remove work on both devices? Is Search usable from the first screen? What buttons does Restart Required show?
2. Exhibition: check Music, restart the device, open Exhibition settings. Is it still checked? Does the Music page show as "Music" in the page menu, with the clock, Shuffle All and the three buttons?
3. Manage Feeds: add a feed, Third-party Feed warning buttons, Compressed, On/Off, swipe Delete.
4. Install Package: Browse to an .ipk on the device, Get Info, Install, and by URL. On the MindPhone, does it fail with "Failed to extract package"?
5. Luna Manager: Rescan, Restart Luna (does it restart the shell and close the cards?), Restart Java (error or nothing?).
6. Weather: place search, × to remove, tap icon to refresh, Widget Compact and Hourly (network service).
7. Saved Package List: first load makes the list; Remove > Saved Only and Uninstall.
8. Fingerterm: menu button, labels spelled as in the page, keyboard shows.
9. Backup: passphrase flow with Saved passwords on; Restore a backup... with and without passphrase; Restart button; Reinstall apps when restoring on the TouchPad.
10. Limited backup: does the box ever appear on a LuneOS build?
11. Sound Recorder: record, pause, stop, hold a row for the menu.
12. Authenticator: Scan a QR code on a device with a camera (the app hands off to Camera?); Lock with fingerprint or passcode on a device with no fingerprint reader.
13. Torch on the TouchPad: does a light come on?
14. Flash a newer image on one device following basics/reinstall-luneos: does a restore of the old backup work?

## New topics

| id | title | home group | icon |
|---|---|---|---|
| storage | Storage | Maintenance | ~/Documents/GitHub/org.webosports.app.settings/src/qml/images/icons/icon-storage.png |
| utilities | Utilities | Maintenance | ~/Documents/GitHub/org.webosports.app.sysmonitor/icon.png |

## Links into other groups

- /basics/open-an-application-in-the-launcher, /basics/open-the-application-menu, /basics/copy-files-between-your-device-and-your-computer, /basics/reinstall-luneos
- /accounts/accounts-overview (backup/do-i-need-a-luneos-account)
- /photos/print-pictures, /security/see-what-an-application-may-use, /tweaks/use-the-new-device-menu
- /screen-and-lock/set-options-for-unlocking-the-screen, /location-services/turn-location-service-providers-on-off
