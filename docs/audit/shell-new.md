# Shell group: replacements and new features

Sources: devices TouchPad (TouchPad, briefly offline, back during the work) and MindPhone (MindPhone) read-only; luna-next-cardshell at fb0afde; tweaks; org.webosports.app.settings; webOS-ports.github.io; live URLs checked with curl on 2026-11-01. Evidence per page is in its front matter. No step was performed on a device.

## New pages

| Page | Status | Evidence |
|---|---|---|
| basics/use-the-power-menu | verified-device | PowerdAlerts.js PowerOffAlert; qml/Notifications/PowerMenu.qml; PowerElement.qml; md5 matches both devices |
| basics/resize-cards | verified-device | qml/CardView/CardGroupListView.qml:39-41,131-157 |
| basics/lock-the-screen-rotation | verified-device | RotationLockElement.qml; SystemMenu.qml:363-395; SystemIndicators.qml:70 |
| basics/turn-sound-off-or-on | needs-device-test | MuteElement.qml; SystemMenu.qml; VolumeControl.qml:86. Which sounds it silences is unknown |
| basics/move-your-information-to-another-device | needs-device-test | com.palm.app.backup source/restore/*, BackupApp.js:95, BackupInfo.js:10 |
| basics/reinstall-luneos | verified-source | curl 200 for webos-ports.org, wiki Devices, luneos-testing releases; site #devices text |
| launcher/use-the-favorites-tab | verified-device | LauncherTabs.js, LauncherTabConfig.qml, TabApplicationModel.qml, default-launcher-page-layout.json |
| tweaks/use-tweaks | needs-device-test | luna-next-cardshell.json md5 on both devices; tweaks Main.js, Config.js |
| tweaks/use-the-new-device-menu | needs-device-test | NewDeviceMenu.qml; StatusBar.qml:637 |
| tweaks/turn-hardware-navigation-keys-on-or-off | needs-device-test | HardwareKeys.qml; CardShell.qml:239-241; hardware-keys.json `{}` on both |
| android-apps/about-android-applications | verified-device | Waydroid on MindPhone, absent on TouchPad; launch points; waydroid.cfg VANILLA |
| android-apps/set-up-android | verified-device | /usr/libexec/waydroid-luneos-download; download dashboard main.qml. Flow read, not run |
| android-apps/open-an-android-application | verified-device | /usr/libexec/waydroid-luneos-app; launch.sh per app. Read, not run |
| android-apps/turn-the-android-tab-on-or-off | needs-device-test | FullLauncher.qml:56,102-105; LauncherTabs.js; AppearancePage.qml:391 |

Counts: 7 verified-device, 1 verified-source, 6 needs-device-test.

## Pages changed for replacements

| Page | Change |
|---|---|
| basics/browse-all-of-help | Retitled "Get help", section "Get help". Says plainly there's no Help application, the site needs a connection, a Help menu item opens nothing |
| basics/support-site | Real links: help, project site, wiki, forums, issue tracker |
| launcher/use-the-launcher | Android line corrected (tab shows on every device, empty without Android); links to new pages |
| basics/use-the-system-menu | Links to rotation, mute, power, New Device Menu |
| basics/stack-cards | Link to Tweaks |

Order values only, because the site's rail splits a section whose pages aren't adjacent: resize-panels 22.5, close-an-application 32.5, use-the-onscreen-keyboard 40.5, enter-symbols 42.5, use-the-system-menu 51.5, copy-music 54.5, 2-turn-your-device 62.2, 3-trigger-a-restart 62.4. Basics now has no split section.

## Replacements

- webOS Doctor -> basics/reinstall-luneos. Confirmed.
- Data Transfer Assistant -> basics/move-your-information-to-another-device: Backup, accounts, MTP. Restore lists backups from other devices (ChooseBackupPage.js), and the app says backups can go onto a different device. The full route is untested.

Confirmed absent, staying deleted: Data Export Wizard for desktop organizers; Help application (get-help-for-a-specific-application, switch-between-help-and-another-open-application); Launcher pages (add, delete, rename, reorder): tabs are fixed.

## Features found but not documented

- Installing Android applications: no app store in the image, and no LuneOS handler for APK files found (no vnd.android.package match on the device). A route for ordinary users isn't established. `waydroid app install` is a command-line tool.
- Android notifications reaching LuneOS (notification_manager.py): behaviour not established from a device.
- Privacy kill switches (KillSwitchIndicator.qml): on the missing list, not assigned to me, no owner seen.
- Headset button presses: on the devices, HardwareKeys.qml has one press play/pause, two next, three previous. Not in the repo at fb0afde. Belongs with media if anyone documents it.
- Mute key: HardwareKeys uses com.palm.audio/setMuted and its own state, so it won't update the system menu's Mute Sound or the status bar icon. Left out of the page.

Not mine: Text Assist layouts and keyboard language key (settings), Exhibition, USB tethering and adb.

## Problems to look at

- MindPhone tweaks store is broken: `org.webosports.service.tweaks.prefs/get` answers "More than 1 preferences object found" for every owner (lib/prefs.js:231). TouchPad answers normally. So on the MindPhone, Appearance likely shows its retry state and Tweaks likely can't load. Cause not investigated; db8 wasn't read.
- New Device Menu has no Power item (showPowerMenu is never emitted). On a device with no power button, turning it on removes the only route to Restart and Shut Down in the menus. The page warns about it.
- New Device Menu always shows the phone tab, also on the wifi-only TouchPad.
- Backup's info text still says "webOS Doctor" (BackupInfo.js:10), and it's shown to users. Not a Help change.
- help.luneos.org doesn't resolve yet, so that link and the "Get help" text wait for publishing.
- The site's Devices list has no links to device pages; wiki/TouchPad and wiki/HP_TouchPad are 404. The reinstall page sends readers to wiki/Devices.
- Waydroid on MindPhone isn't in packagegroup-luneos-extended.bb lines 194-199. Where it comes from wasn't traced.
- The Android tab shows on devices with no Waydroid: only the tweak decides.

## Needs device test

1. MindPhone: open Tweaks and Appearance. Note any error. Then on the TouchPad open Tweaks > Luna, change Tab title case, see that it applies at once, and find the help button (compact layout on phone).
2. Mute Sound: play music, call the device, trigger an alarm. Note what stays audible.
3. Move data: back up on device A, copy webos-backups to device B over MTP, Backup menu > Restore a backup..., confirm it's listed, restores and restarts.
4. Android first start on a device without images: Waydroid > Download Android? > Not now, > Download, Stop download, then a full download. Confirm Android starts by itself.
5. Open an Android application, then throw its card. Confirm it closes.
6. Appearance > Launcher > Android Tab off: confirm Android icons move to Apps.
7. Resize cards: pinch out and in on a single card, confirm all resize and the limits. Restart Luna Next, confirm it resets.
8. New Device Menu: turn on, go through each icon on both devices, tap near each edge.
9. Hardware keys on a Q25 or similar: Automatic, On, Off.
10. Favorites: drag an icon in, restart Luna Next, confirm it stays.

## New topics

| id | title | home group | icon |
|---|---|---|---|
| tweaks | Tweaks | Preferences | /home/herrie/Documents/GitHub/tweaks/enyo-app/icon.png |
| android-apps | Android applications | Basics | /home/herrie/claude-scratch/help/shell-new/waydroid-icon.png (pulled from /usr/palm/applications/Waydroid/icon.png on MindPhone) |

## Links into other groups

Outgoing: backup/manually-back-up-information-to-your-luneos-account, system-updates/update-the-system-software-from-a-notification, plus the older ones in shell.md. If the system group adds a restore page, link it from move-your-information-to-another-device. If settings adds a Display page for Rotation Lock, link it from lock-the-screen-rotation.

For owners: calendar/how-do-i-get-events-into-calendar and contacts/get-contact-info-into-contacts can point to basics/move-your-information-to-another-device in place of the deleted DTA page. Settings' Appearance page and system's Tweaks and Waydroid items overlap tweaks/* and android-apps/*: don't write them twice.
