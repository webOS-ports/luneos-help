# Shell group audit: basics, launcher, just-type

Sources: devices TouchPad (TouchPad) and MindPhone (MindPhone), luna-next-cardshell, webos-keyboard. Key shell QML and the keyboard keys match the repos by md5 on the devices; only CardsArea.qml and HardwareKeys.qml differ (lock-screen alarm alert, media keys).

## Shell vocabulary

Other groups should use exactly these names.

| Use | What it is | Never say |
|---|---|---|
| **Card view** | Screen of open applications as cards. Cards are *thrown* off the top. Cards form *stacks*. | card mode, multitasking view |
| **Launcher** | All applications, on fixed **tabs**: Apps, Android (optional), Downloads, Favorites, Prefs | pages, launcher pages, App Launcher |
| **Quick Launch** | Bar at the bottom in Card view and Launcher. Tablet 5 apps, phone 4, plus the **Launcher icon** at the right end | dock (the code's word, not the user's) |
| **Just Type** | The **Just type...** field, in Card view only, and the search screen it opens. Tabs All, Contacts, Content, Actions. Launcher > Prefs > **Just Type** for settings | Universal Search, Just Type in the Launcher |
| **status bar** | Strip at the top | title bar |
| **application menu** | Tap the app's name upper left, or flick down from the top edge over it. Default label "App Menu". None in Card view or Launcher | "the menu" alone |
| **system menu** | Tap the icons upper right, or flick down from the top at the right | connection menu, device menu |
| **power menu** | See below; labels differ | device menu |
| **gesture area** | Black strip on the screen below the app, hidden in fullscreen, can be turned off in Tweaks. Tap: app to and from Card view. Flick up: app to Card view, Card view to Launcher, Launcher to Card view. Flick left: back. Flick right: screenshot | gesture light, Center button |
| **back gesture** | Flick left on the gesture area | swipe back on the bezel |
| **notifications** | **Banner** (brief), **dashboard item** (expanded), **pop-up** (needs a response). Phone at the bottom, tablet in the status bar | notification area as a place name for users |
| **onscreen keyboard** | One word "onscreen" in text. The system menu's own label is "Show On-screen Keyboard" | virtual keyboard |
| **tap and hold / throw / flick / swipe / pinch out / pinch in** | Gesture verbs | long press, slide |

Power menu labels are not the same in the two places:

- Hold power (com.palm.systemui): **Airplane Mode** / **Turn off Airplane Mode**, **Restart**, **Luna Next restart**, **Shut Down**, **Cancel**.
- No power button, system menu > **Power** (shell PowerMenu): **Device Restart**, **Luna-Next Restart**, **Shut Down**, **Cancel**.

Hardware keys Back, Home and Menu only act when the Tweaks setting says so, or on auto with a hardware keyboard. Do not write "press Center" or "press Home" in any article.

## Device drawings

Device tours are generic across very different hardware. They describe one Palm device, not what a reader holds.

| Drawing | Fits LuneOS | Decision |
|---|---|---|
| front-view (Pre mrwr/slab, TouchPad to3g) | No: earpiece, Center, one device's shape | Drawing removed. Page kept as text only, "Buttons and gesture area", because it's in `featured` and is the one place explaining the gesture area |
| back-view | No | Page deleted |
| top-view | No: ringer switch, headset, one layout | Page deleted |
| keyboard (keyboard-mrwr) | No: one keyboard; Option key missing on most | Page deleted, merged into use-the-keyboard, no drawing |
| touchscreen-card-view (card_view_blank_callouts_mrwr, card_view_blank_towi) | Yes | Stay. Legend: 1 Just Type field, 2 Wallpaper, 3 Quick Launch. Status bar and gesture area are not drawn |
| touchscreen-the-launcher, tablet (launcher_to3g) | Yes, with a new legend | Stay. Legend: 1 "Launcher" in the status bar, 2 tabs, 3 icons, 4 Quick Launch, 5 system icons (system menu), 6 notification icons |
| touchscreen-the-launcher, phone (launcher_page1b_mrwr) | No: no Quick Launch | Image removed, text legend kept. Redraw needed. Proposed legend as tablet, with 6 at the bottom and an arrow at the end of the tab row |
| use-the-onscreen-keyboard, tablet (keyboard_US_towi) | Partly: no number row, shows .com | Kept for now with a legend for keys that exist. Redraw from Keyboard_en_tablet.qml, or drop the image |
| insert_usb_mrwr, connect_usb_towi, insert_SIM_to3g | No: one device's port | Removed from their articles |

Recommendation: no per-device tour pages. If a tour returns, build it per device from the device's own photo.

## Articles

| Article | Status | What changed | Evidence |
|---|---|---|---|
| basics/1-throw-all-open-applications-off-the-top-of-the-screen | verified-device | Gesture area wording; dropped Center button | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardView/CardView.qml:330-345 tap and swipe up; qml/CardView/SwipeableCard.qml throw |
| basics/2-turn-your-device-completely-off-and-on | verified-device | Power menu labels per device; Device Info route removed | adb: com.palm.systemui app/PowerdAlerts/PowerdAlerts.js:81-84 Restart, Shut Down; qml/Notifications/PowerMenu.qml:51 Device Restart; qml/StatusBar/SystemMenu/PowerElement.qml:35, only without power button |
| basics/3-trigger-a-restart | needs-device-test | Triple toggle gone; power-hold restart only | adb: com.palm.systemui app/PowerdAlerts/PowerdAlerts.js:82 Luna Next restart; qml/Notifications/PowerMenu.qml:75 Luna-Next Restart; forced restart by holding power not established: firmware behaviour, per device |
| basics/4-top-off-the-battery | verified-source | Reworded, device-neutral | generic hardware step; adb: com.palm.systemui PowerdAlerts.js:42-46 Low Battery alert |
| basics/browse-all-of-help | verified-source | Describes this site; says no Help app on device | tools/build.py:279 search field, :48 device bar; adb: /usr/palm/applications has no com.palm.app.help; org.webosports.app.settings.help is the example page qml/General/HelpPage.qml:27-32 |
| basics/change-card-order-or-unstack-cards | verified-device | Hold, drag, drop per CardWindowWrapper | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardView/CardWindowWrapper.qml:175; qml/CardView/CardGroupListView.qml opacity 0.8, drag |
| basics/charge-the-battery | verified-device | Generic charger, USB popup labels | adb: /media/internal/screencaptures/20261007082944.png USB Connected popup on the TouchPad; adb: com.palm.systemui StoragedAlerts.js:45-62, PowerdAlerts.js:203; qml/StatusBar/SystemMenu/BatteryElement.qml:75 |
| basics/close-an-application-or-application-screen | verified-device | Merged close-an-application; throw, or back gesture for a screen | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardView/SwipeableCard.qml onFlickingChanged; qml/CardView/CardGroupListView.qml throwAway |
| basics/connect-to-a-network | verified-device | Real Wi-Fi and SIM labels, feature-split | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/StatusBar/SystemMenu/WiFiElement.qml:125,156; qml/Connectors/AirplaneModeService.qml:70 |
| basics/copy-files-between-your-device-and-your-computer | verified-device | USB popup File Transfer (MTP); USB mode dropped | adb: /media/internal/screencaptures/20261007082944.png, 20261007123138.png; adb: com.palm.systemui StoragedAlerts.js:22,45-62,160,208; adb: org.webosports.app.settings-common qml/Connectivity/UsbPage.qml:123,132-142 |
| basics/copy-music-photos-and-videos-between-your-computer-and-your-device | verified-device | Same MTP route | adb: ls /media/internal has music, DCIM, ringtones; adb: com.palm.systemui StoragedAlerts.js:58 |
| basics/copyright | verified-source | States origin of the text and the HP copyright | README.md: keep the notice on imported text; tools/build.py:29 NOTICE |
| basics/cut-copy-and-paste-information | verified-device | Pill overlay: Cut, Copy, Paste, Select, Select All | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/EditOverlay.qml:124-141 items; qml/CardsArea.qml:619-727 hold 700 ms, tap on selection |
| basics/delete-a-list-item | verified-source | Throw the item; fallback if a list does not support it | adb: org.webosports.app.settings-common qml/Common/SwipeRow.qml; enyo-1.0-ports SwipeableItem; varies per application |
| basics/delete-an-application | verified-device | Launcher edit mode Delete, no confirmation; App Catalog gone | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/LaunchBar/DraggableAppIcon.qml remove button; qml/LaunchBar/FullLauncher.qml:onRemoveAppLauncher, removeApplication, DONE |
| basics/delete-files-from-your-device | verified-device | Via computer over MTP | adb: com.palm.systemui StoragedAlerts.js:58 |
| basics/display-card-view-minimize-an-application | verified-device | Tap or flick up on gesture area | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardView/CardView.qml:330-345; qml/CardsArea.qml:295-300 onScreenEdgeFlickEdgeBottom, only while the gesture area is hidden |
| basics/drag-and-drop | verified-device | Generic steps; where it applies | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/LaunchBar/LaunchBar.qml:dragArea; qml/LaunchBar/FullLauncher.qml:dragArea |
| basics/enter-alternate-keyboard-characters | verified-source | Physical keyboards only: Alt, Sym, latch and lock | webos-keyboard/data/hwkeyboard/README.md altKeys, symKeys, lockOnDoubleTap; webos-keyboard/data/hwkeyboard/q25.json: driver owns Alt and Sym |
| basics/enter-information-in-a-field | verified-device | Tap field, keyboard appears | adb: md5sum /usr/share/maliit/plugins/org/luneos/keys matches webos-keyboard on MindPhone; webos-keyboard/qml/keys/ReturnKey.qml:24-28; webos-keyboard/plugins/en/qml/Keyboard_en_tablet.qml Tab |
| basics/enter-passwords | verified-source | Short: hidden input, Caps Lock reminder | webos-keyboard/qml/keys/ShiftKey.qml Caps Lock |
| basics/enter-symbols-and-alternate-characters | verified-device | Onscreen 123 / +=[] / hold for extended row | adb: /usr/share/maliit/plugins/org/luneos/keys md5 matches; webos-keyboard/plugins/en/qml/Keyboard_en_phone.qml 123; webos-keyboard/plugins/en/qml/Keyboard_en_tablet.qml |
| basics/enter-uppercase-letters | verified-device | Shift tap, double-tap, hold | adb: /usr/share/maliit/plugins/org/luneos/keys/ShiftKey.qml md5 matches webos-keyboard; webos-keyboard/qml/keys/ShiftKey.qml double tap and hold |
| basics/front-view | verified-device | Now text page Buttons and gesture area, no drawing | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardsArea.qml:285-300,712-760; qml/WindowManager/LunaGestureArea.qml |
| basics/go-to-another-open-application | verified-device | Swipe in Card view, tap card; Center button gone | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardView/CardGroupListView.qml internalListView |
| basics/go-up-one-level-in-an-app-back-gesture | verified-device | Flick left on gesture area | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardView/CardView.qml:327-333 swipe left sends Escape; qml/Connectors/HardwareKeys.qml:_sendBack |
| basics/icons-in-the-title-bar | verified-device | Retitled Icons in the status bar; real indicator list | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/StatusBar/SystemIndicators.qml; qml/StatusBar/Indicators/ |
| basics/insert-the-sim-card | verified-device | Merged SIM activation; points to manufacturer, drawing removed | adb: screencaptures/20261031100458.png carrier name in Card view on MindPhone; qml/StatusBar/StatusBar.qml carrierText; qml/SIMPinWindowArea.qml |
| basics/line-up-your-favorite-applications-in-quick-launch | needs-device-test | Fixed set of apps, reorder only | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/LaunchBar/LaunchBar.qml:102-178 no drop from the Launcher, :242-270,:335-354 fixed list; adb: /etc/palm/default-dock-positions.json |
| basics/maximize-battery-life | verified-source | Tips that apply, links to Screen & Lock | generic advice; links checked in content/en |
| basics/move-among-cards-and-stacks | verified-device | Swipe, arrow keys | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardView/CardGroupListView.qml Keys.onPressed |
| basics/move-the-cursor | verified-source | Tap, round control on tablet keyboard | webos-keyboard/qml/keys/TrackBall.qml; webos-keyboard/plugins/en/qml/Keyboard_en_tablet.qml TrackBall; phone layout has none |
| basics/open-an-application-in-quick-launch | verified-device | Available in Card view and Launcher only | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/LaunchBar/Launcher.qml states launchbar, fullLauncher keep launchBarInstance visible; adb: screencaptures/20261031075422.png |
| basics/open-an-application-in-the-launcher | verified-device | Tabs not pages; Prefs tab noted | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/LaunchBar/FullLauncher.qml tabs and grid; qml/LaunchBar/LauncherTabs.js:6-14 |
| basics/open-the-application-menu | verified-device | Merged use-the-application-menu; tap name or flick from top | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/StatusBar/AppMenu.qml toggleState; qml/StatusBar/StatusBar.qml:611-616 top edge flick |
| basics/open-the-connection-menu | verified-device | Retitled Open the system menu; slug kept | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/StatusBar/StatusBar.qml:216-234,611-622 |
| basics/open-the-launcher | verified-device | Launcher icon, flick up, keyboard keys; Center gone | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/LaunchBar/Launcher.qml onSwipeUpGesture, onToggleLauncherDisplay; qml/Connectors/HardwareKeys.qml:_defaultActions, navigationKeys |
| basics/place-the-cursor-in-a-text-field | verified-source | Simplified | qml/CardsArea.qml:133-167 keyboard focus; webos-keyboard |
| basics/reorder-quick-launch-icons | needs-device-test | Hold and drag; persistence unconfirmed | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/LaunchBar/LaunchBar.qml:147-176; does the order survive a restart: refreshConfig() rebuilds from /etc/palm/default-dock-positions.json, LaunchBar.qml:335-354 |
| basics/resize-panels-display-or-hide-levels-in-an-app | needs-device-test | Retitled; gesture hedged per app | core-apps-ports/com.palm.app.email/mail/source/Mail.js SlidingPane; not tried per application |
| basics/save-information | verified-source | Autosave statement narrowed | org.webosports.app.memos/source/views/memos.js; varies per application |
| basics/scroll-a-specific-amount | verified-source | Unchanged in meaning | generic gesture |
| basics/scroll-fast | verified-source | Unchanged in meaning | generic gesture; qml/LaunchBar/FullLauncher.qml flick |
| basics/search-for-information | verified-device | Just Type tabs, Card view only | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; adb: com.palm.launcher app/JustType.js:24,45-48; adb: com.palm.universalsearch getUniversalSearchList |
| basics/select-items-in-a-list | verified-source | Lists versus menus | luneos-components LabelAndPicker; enyo-1.0-ports ListSelector |
| basics/select-text | verified-device | Hold pill: Select / Select All; Shift-drag gone | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/EditOverlay.qml:124-141; qml/CardsArea.qml:619-727 |
| basics/shut-down-your-device | verified-device | Power menu per device; Device Info route gone | adb: com.palm.systemui PowerdAlerts.js:83-84; qml/Notifications/PowerMenu.qml:69,93,111; qml/StatusBar/SystemMenu/PowerElement.qml:35 |
| basics/stack-cards | verified-device | Hold, drop on card; tweak named | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardView/CardGroupListView.qml pinch to spread, drag; files/tweaks/luna-next-cardshell.json stackedCardSupport |
| basics/stop-scrolling | verified-source | Unchanged in meaning | generic gesture; qml/LaunchBar/FullLauncher.qml onMovementStarted |
| basics/support-site | verified-source | help.luneos.org and webos-ports.org | webOS-ports.github.io/CNAME webos-ports.org, devices/; README.md |
| basics/sync-personal-data-using-third-party-software | verified-device | Retitled Sync personal data; online accounts only | adb: listLaunchPoints has Accounts on both devices |
| basics/take-a-screenshot | verified-device | Flick right on gesture area; key combo gone; real path and album | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardsArea.qml:285-290; adb: ls /media/internal/screencaptures on both devices |
| basics/touchscreen-card-view | verified-device | 3-item legend, phone 4 + Launcher, tablet 5 + Launcher | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; adb: screencaptures/20261031100458.png, 20261007123151.png; adb: /etc/palm/default-dock-positions.json |
| basics/touchscreen-the-launcher | verified-device | New 6-item legend; phone drawing removed | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; adb: screencaptures/20261031075422.png phone Launcher; qml/StatusBar/StatusBar.qml launcher-visible |
| basics/turn-all-wireless-services-on-off-airplane-mode | verified-device | Real labels, system and power menu routes | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/Connectors/AirplaneModeService.qml:26-50; adb: PowerdAlerts.js:77,102 |
| basics/turn-the-screen-on-off | verified-device | Power button; slide-keyboard wake gone; lock types | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; luna-displaymanager/Src/DisplayStates.cpp DisplayEventPowerKeyPress; qml/LockScreen/PadLock.qml:130 Drag up to unlock |
| basics/use-the-keyboard | verified-source | Merged keyboard page; requires keyboard; drawing removed | webos-keyboard/data/hwkeyboard/README.md; qml/LaunchBar/JustTypeField.qml Keys.onPressed; qml/StatusBar/SystemMenu/OnScreenKeyboardElement.qml:42 |
| basics/use-the-onscreen-keyboard | verified-device | Both UIs; real keys. Tablet drawing kept but inaccurate, see drawings | adb: /usr/share/maliit/plugins/org/luneos/keys md5 matches; webos-keyboard/plugins/en/qml/Keyboard_en_phone.qml; webos-keyboard/plugins/en/qml/Keyboard_en_tablet.qml |
| basics/use-the-system-menu | verified-device | Real menu order and labels, per-feature | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/StatusBar/SystemMenu/SystemMenu.qml:165-460; qml/StatusBar/SystemMenu/MuteElement.qml |
| basics/view-and-work-with-notifications | verified-device | Phone bottom, tablet status bar; throw to remove | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/Notifications/NotificationArea.qml:113-124; qml/Notifications/NotificationAreaTablet.qml |
| basics/why-the-screen-goes-dark | verified-device | Real intervals; proximity only on modem devices | adb: settings-common qml/General/DisplayPage.qml:104 1, 2, 5, 10 minutes; luna-displaymanager/Src/DisplayManager.cpp proximity |
| basics/work-with-stacked-cards | verified-device | Child windows join stack; pinch out | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/CardView/CardGroupModel.qml:82-107 child window joins parent's group; qml/CardView/CardGroupListView.qml pinch to spread |
| basics/zoom-in-or-out-a-fixed-amount | needs-device-test | Atlas Web only, not tried | web runtime behaviour, not tried in Atlas Web |
| basics/zoom-in-to-increase-the-size-of-items-on-the-screen | verified-source | PDF Viewer, Maps named | org.webosports.app.pdf/qml/components/DocumentView.qml PinchArea; org.webosports.app.maps lib/leaflet; Atlas Web not tried |
| basics/zoom-out-to-decrease-the-size-of-items-on-the-screen | verified-source | PDF Viewer, Maps named | org.webosports.app.pdf/qml/components/DocumentView.qml PinchArea; org.webosports.app.maps lib/leaflet; Atlas Web not tried |
| just-type/create-a-new-item-such-as-a-message-calendar-event-or-memo | verified-device | Merged message-or-memo; real Quick Actions list | adb: com.palm.launcher pulled from both devices, identical; app/Actions.js:30,70-76,88; adb: luna-send com.palm.universalsearch/getUniversalSearchList ActionList |
| just-type/customize-just-type | verified-device | Prefs page Just Type groups; no Find More | adb: com.palm.launcher pulled from both devices, identical; adb: org.webosports.app.settings-common qml/General/SearchPreferencesPage.qml; adb: luna-send getAllSearchPreference, getUniversalSearchList on both devices |
| just-type/find-information-in-an-application-on-your-device | verified-device | Real content rows | adb: com.palm.launcher pulled from both devices, identical; app/DbSearch.js, app/ContentResults.js; adb: getUniversalSearchList DBSearchItemList |
| just-type/get-in-touch-with-a-contact | verified-device | Merged look-up-a-contact; IM and reminders gone | adb: com.palm.launcher pulled from both devices, identical; app/MainView.js MIN_SEARCH_LENGTH; app/ContactSearch.js |
| just-type/open-an-application | verified-device | Launch group | adb: com.palm.launcher pulled from both devices, identical; app/LaunchPointSearch.js:39 Launch, searchApps keyword; qml/LaunchBar/JustTypeField.qml Keys.onPressed |
| just-type/repeat-a-recent-search | verified-device | Five, in memory, X removes | adb: com.palm.launcher pulled from both devices, identical; app/HomeView.js:32,62-68 five, kept in memory; app/JustType.js justTypeDeactivated |
| just-type/search-the-web | verified-device | Real engines, Suggest, More; Maps and Google Maps gone | adb: com.palm.launcher pulled from both devices, identical; app/LaunchAndSearch.js:45-65,185-191; app/LaunchItems.js:Go to website |
| launcher/reorder-launcher-icons | verified-device | DONE button, tabs not pages | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/LaunchBar/FullLauncher.qml drop areas, turnLeftTimer, dragArea, DONE; qml/LaunchBar/LauncherTabConfig.qml saved in db8 |
| launcher/use-the-launcher | needs-device-test | Five fixed tabs described | adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices; qml/LaunchBar/LauncherTabs.js:6-14,60-78; qml/LaunchBar/FullLauncher.qml Keys.onPressed |

## Deleted articles

| Article | Reason |
|---|---|
| basics/2-turn-your-phone-completely-off-and-on | Duplicate of 2-turn-your-device-completely-off-and-on |
| basics/3-triple-toggle-to-restart | Needs ringer switch and Option key |
| basics/5-take-out-the-battery | Device-specific and last-resort hardware steps |
| basics/5-tether-your-device-to-your-computer-and-reinstall-luneos | webOS Doctor procedure; no such tool |
| basics/6-tether-your-device-to-your-computer-and-reinstall-luneos-software | Same |
| basics/back-view | Device tour, see drawings |
| basics/top-view | Device tour, see drawings |
| basics/keyboard | Merged into use-the-keyboard |
| basics/close-an-application | Merged into close-an-application-or-application-screen |
| basics/copy-music-photos-and-videos-using-third-party-software | Desktop software that doesn't apply; MTP covers this |
| basics/enter-characters-from-the-symbols-table | No symbols table found in webos-keyboard |
| basics/get-help-for-a-specific-application | No Help app: Just Type's Help opens a hidden demo page, and enyo HelpMenu targets com.palm.app.help, not installed. Restore when it ships |
| basics/switch-between-help-and-another-open-application | Same |
| basics/insert-the-sim-card-and-activate-data-services | Merged into insert-the-sim-card |
| basics/move-among-open-applications | Duplicate of go-to-another-open-application |
| basics/open-an-application-using-just-type | Duplicate of just-type/open-an-application |
| basics/printed-information-in-the-box | No box |
| basics/reorder-launcher-icons | Duplicate of launcher/reorder-launcher-icons |
| basics/see-all-open-applications-card-view | Duplicate of display-card-view-minimize-an-application |
| basics/use-the-application-menu | Merged into open-the-application-menu |
| basics/use-the-data-export-wizard-to-export-data-from-a-desktop-organizer-on- | No such tool |
| basics/use-the-data-transfer-assistant-dta | No such tool |
| basics/use-the-launcher | Duplicate of launcher/use-the-launcher |
| launcher/add-a-launcher-page | Launcher tabs are fixed (LauncherTabs.js) |
| launcher/delete-a-launcher-page | Same |
| launcher/rename-a-launcher-page | Same |
| launcher/reorder-launcher-pages | Same |
| just-type/create-a-new-item-such-as-a-message-or-memo | Merged into ...-message-calendar-event-or-memo |
| just-type/look-up-a-contact | Merged into get-in-touch-with-a-contact |

## Cross-group links

Outgoing, all exist now. If an owner deletes one, the link here must change:

- contacts/set-up-an-online-account-in-contacts
- calendar/how-do-i-get-events-into-calendar
- screen-and-lock/adjust-the-screen-brightness
- screen-and-lock/set-the-interval-for-turning-the-screen-off-automatically
- screen-and-lock/turn-blink-notifications-on-off
- system-updates/update-the-system-software-from-a-notification
- email/enter-advanced-account-settings
- text-assist/work-with-the-text-assist-feature

Incoming links that now point at a deleted article, to be fixed by the owning group:

- calendar/how-do-i-get-events-into-calendar -> basics/use-the-data-transfer-assistant-dta
- contacts/get-contact-info-into-contacts -> basics/use-the-data-transfer-assistant-dta

Removed from my pages because the target doesn't apply: phone/turn-the-phone-on-and-off, messaging/sign-out-of-an-im-account, contacts/assign-a-reminder-message-to-a-contact, messaging/connect-your-device-to-a-luneos-device.

## Missing articles

- Reinstall or flash LuneOS (per device, on webos-ports.org)
- Android tab and Android applications
- Exhibition
- New Device Menu tweak
- Tweaks: the shell options
- Resize cards by pinching in Card view
- Favorites tab
- Hardware navigation keys
- Privacy kill switches
- Rotation lock and mute
- Text Assist keyboard layouts (Dvorak, Thumb, Pre Orange, Pre White)
- Onscreen keyboard language key
- USB tethering and adb

## Needs device test

1. Quick Launch order: hold an icon, drag it to a new place, restart Luna Next, see if the order stays. Code rebuilds from /etc/palm/default-dock-positions.json, and db8 could not be read.
2. Adding to Quick Launch: try dragging a Launcher icon onto Quick Launch. Code shows no way.
3. Forced restart: on each device, hold power for a long time and note the seconds. Basics 3-trigger-a-restart depends on it.
4. TouchPad Center button: press it in an app, Card view and Launcher. No Key_Home handler found; hardware-keys.json is `{}`.
5. Hold power on both devices: note the exact popup items and order.
6. Launcher: put an icon in edit mode, tap Delete on a downloaded app. Confirm there's no confirmation.
7. Downloads tab: install an app from Preware, note which tab it lands on.
8. Panels: in Email, Tasks and one other, swipe and drag panels; say which works.
9. Double-tap zoom in Atlas Web, plus pinch.
10. Just Type: type a word on each device and check tabs and group order against just-type/*.
11. Physical keyboard: Sym and Alt latch on a Pre or Q25.
