# Audit: group "settings"

Topics: wi-fi, bluetooth, vpn, tethering, screen-and-lock, sounds-and-ringtones, text-assist, date-and-time, regional-settings.
72 imported articles: 48 kept (42 verified-device, 1 verified-source, 5 needs-device-test), 24 deleted.

Evidence strings: `adb: settings-common/qml/...` means /usr/palm/applications/org.webosports.app.settings-common/qml/... on the device. Line numbers are from the MindPhone copy.
Copies pulled read-only from both devices: ~/claude-scratch/help/audit/settings-device/{tp,mp}. Pre-edit articles: ~/claude-scratch/help/audit/settings-work/before. Generator: ~/claude-scratch/help/audit/settings-work/apply.py.
All kept articles now list both phone and tablet in "devices", and all ui blocks were merged because no text differs. All legacy image refs were removed.

## Images differ between the two devices

The TouchPad and MindPhone run different builds of Settings and the shell, and the checked-out org.webosports.app.settings (herrie/bt-discovery-trust) matches neither.
- Bluetooth: the MindPhone has Forget device, device details, Search again, Reconnect headsets automatically and the Calls group. The TouchPad has none of these.
- Wi-Fi: only the TouchPad has the Private Wi-Fi address row (and WiFiMACRandomization in connman).
- VPN: only the MindPhone lists Cisco IPsec (vpnc.so) and has pptp.so.
Articles describe the newer behaviour. delete-a-device cannot be followed on the current TouchPad image.

## Articles

| Article | Status | What changed | Key evidence |
|---|---|---|---|
| wi-fi/turn-wi-fi-on-off | verified-device | Header switch; labels are "Turn on WiFi"/"Turn off WiFi" | WiFiPage.qml:45, WiFiElement.qml:125 |
| wi-fi/connect-to-a-new-open-network | verified-device | Removed Join network, which does nothing | WiFiPage.qml:64,172 |
| wi-fi/connect-to-a-new-secure-wi-fi-network | verified-device | Real popup: passphrase, Show passphrase, Connect. Removed Security field and Sign In | WiFiProvidePassphrasePopup.qml |
| wi-fi/connect-to-a-previously-used-wi-fi-network | verified-device | Removed Stored Profiles and "most recently used" ordering; added Connect automatically | WiFiPage.qml:219 |
| wi-fi/customize-wi-fi-connection-settings | verified-device | Touch and hold; real field names; need not be connected, only known | WiFiNetworkInfoPopup.qml:177,522,573 |
| wi-fi/disconnect-from-a-wi-fi-network | verified-device | Tap to disconnect; Forget network does not require being connected | WiFiPage.qml:176, popup:170 |
| wi-fi/connect-to-a-captive-portal | needs-device-test | No notification or certificate dialog exists; now "open Atlas Web" | wifi_service.c:4112, no consumer of captivePortal |
| bluetooth/turn-the-bluetooth-feature-on-off | verified-device | Header switch | BluetoothPage.qml:299, BluetoothElement.qml:53 |
| bluetooth/what-is-bluetooth-wireless-technology | verified-device | Removed Touch to Share | BluetoothManager.qml:85 |
| bluetooth/make-a-pairing-request-to-another-device | verified-device | Removed Add device, Type and car-kit steps; tap in Choose a device; real PIN popups | BluetoothManager.qml:93, Bluetooth*Popup.qml |
| bluetooth/accept-a-pairing-request-from-another-device | verified-device | Discoverable switch; Allow; app must stay open (agent lives in the page) | BluetoothPage.qml:39,331 |
| bluetooth/connect-with-a-paired-device | verified-device | Added system menu route; removed the computer claim | BluetoothPage.qml:516 |
| bluetooth/disconnect-from-a-device | verified-device | Removed OK step | BluetoothPage.qml:516 |
| bluetooth/delete-a-device | verified-device | Touch and hold > Forget device (MindPhone image only) | BluetoothDeviceInfoPopup.qml:216 |
| vpn/what-is-the-vpn-app | verified-device | Real connection types from the service; fixed typo | getAgents on both devices |
| vpn/add-a-cisco-anyconnect-vpn-profile | verified-device | Retitled OpenConnect (AnyConnect); real form; removed license step | openconnect.json, VpnProfilePopup.qml |
| vpn/add-a-vpnc-vpn-profile | verified-device | Retitled Cisco IPsec; real options; not on every device | vpnc.json, getAgents |
| vpn/connect-to-a-profile | verified-device | Removed system menu route: VpnElement is visible: false | VPNPage.qml:158, SystemMenu.qml |
| vpn/disconnect-from-a-profile | verified-device | Same | VPNPage.qml:292 |
| vpn/edit-a-profile | verified-device | Edit button; name and type are fixed | VPNPage.qml:195 |
| vpn/delete-a-profile | verified-device | Swipe > Delete Profile | VPNPage.qml:152 |
| tethering/what-is-tethering (was what-is-hp-mobile-hotspot) | verified-device | Rewritten for the Tethering app; removed range and five-device claims | TetheringPage.qml |
| tethering/use-tethering (was use-hp-mobile-hotspot) | verified-device | Wi-Fi, USB and Bluetooth switches | TetheringPage.qml:145,225,256 |
| tethering/create-a-secure-hotspot | verified-device | Name, Password, Share over Wi-Fi; requires modem | TetheringPage.qml:145-186 |
| tethering/change-your-secure-passphrase | verified-device | Password field; requires modem | TetheringPage.qml:185 |
| tethering/view-information-about-connected-devices | verified-device | Only a count exists, no per-device details | TetheringPage.qml:272 |
| screen-and-lock/adjust-the-screen-brightness | verified-device | Moved to Display; merged phone article; requires brightness | DisplayPage.qml:139 |
| screen-and-lock/turn-auto-dim-on-off | verified-device | Moved to Display | DisplayPage.qml:163 |
| screen-and-lock/set-the-interval-for-turning-the-screen-off-automatically | verified-device | Moved to Display; 1, 2, 5, 10 minutes | DisplayPage.qml:103 |
| screen-and-lock/change-your-wallpaper | verified-device | Moved to Appearance; no crop step, no New Photo | AppearancePage.qml:118, WallpaperPickerPopup.qml |
| screen-and-lock/set-options-for-unlocking-the-screen | needs-device-test | Unlock with: Pattern added; 4-digit PIN; lockout; removed remote reset. Lock After unconfirmed | ScreenLockPage.qml:109,253, Lockout.js |
| screen-and-lock/change-your-secure-unlock-password | verified-device | Continue/Save; Change Pattern added | ScreenLockPage.qml:235 |
| screen-and-lock/get-notifications-when-the-screen-is-locked-or-off | needs-device-test | Merged tablet article; retitled; effect unconfirmed | ScreenLockPage.qml:406 |
| screen-and-lock/turn-blink-notifications-on-off | verified-device | Any notification light, not gesture area or Center button | NotificationLed.qml:114 |
| screen-and-lock/turn-advanced-gestures-on-off | needs-device-test | Removed next/previous gestures; switch appears to do nothing | ScreenLockPage.qml:168, CardsArea.qml:295 |
| sounds-and-ringtones/add-ringtones-to-your-device | verified-device | Rewritten; removed App Catalog, Amazon, AMR, QCELP; real file filter | TonePickerPopup.qml:48-51 |
| sounds-and-ringtones/copy-a-ringtone-to-your-device | verified-device | USB app > Connect as media device (MTP) | UsbPage.qml:123 |
| sounds-and-ringtones/select-a-file-from-the-ringtones-folder-as-a-ringtone | verified-device | My ringtones / System sounds; Alert and Notification tones added | SoundsAndAlertsPage.qml:211 |
| sounds-and-ringtones/set-sound-options | verified-device | Merged phone article; added Mute Sound and the volume slider | SoundsAndAlertsPage.qml, MuteElement.qml:43 |
| sounds-and-ringtones/set-your-device-to-vibrate | needs-device-test | Vibrate group, Sounds on / Sounds off; effect unconfirmed | SoundsAndAlertsPage.qml:298,316 |
| text-assist/work-with-the-text-assist-feature | verified-source | Rewritten around the four real switches; removed orange/gray underlines, tones, shortcuts | TextAssistPage.qml:222, wordengine.cpp:276 |
| text-assist/customize-text-assist-settings | verified-device | Removed Alert; added Layout, Size, Hardware Keyboard | TextAssistPage.qml:146 |
| text-assist/add-your-own-words-and-shortcuts | verified-device | Words and Shortcuts tabs; no edit; states shortcuts do not expand | DictionaryPopup.qml |
| date-and-time/use-date-and-time | verified-device | Clock selector; Network Time Zone is modem only | DateAndTimePage.qml |
| regional-settings/change-the-display-language | verified-device | Merged phone article; Apply Changes and Restart dialog | LanguagePickerPage.qml |
| regional-settings/change-the-display-formats | verified-device | Merged phone article; Format Previews | LanguagePickerPage.qml:274 |
| regional-settings/select-a-default-country-code-for-phone-numbers | verified-device | Added: Phone app reads Formats region instead | LanguagePickerPage.qml:267 |
| regional-settings/set-up-and-switch-among-multiple-onscreen-keyboard-layouts-and-languag | verified-device | Add..., Default, Remove Keyboard, language key; retitled | LanguagePickerPage.qml:181, LanguageKey.qml |

The slugs vpn/add-a-cisco-anyconnect-vpn-profile and vpn/add-a-vpnc-vpn-profile no longer match their titles. Only the two tethering files with HP in the slug were renamed; nothing linked to them from other groups.

## Deleted articles

| Article | Reason |
|---|---|
| wi-fi/put-wi-fi-to-sleep-when-the-screen-is-off | No Sleep Settings in the Wi-Fi app |
| bluetooth/rename-a-device | No rename in the app |
| bluetooth/forward-contact-phone-numbers-or-text-messages-to-a-car-kit | No per-device settings in the app |
| bluetooth/manage-luneos-device-connection-preferences | Same |
| bluetooth/manage-luneos-tablet-connection-preferences | Same |
| bluetooth/what-is-touch-to-share | Touch to Share absent (no code; qml/NFC is tag dispatch only) |
| bluetooth/pair-with-a-luneos-device-using-touch-to-share | Same |
| bluetooth/pair-with-a-luneos-tablet-using-touch-to-share | Same |
| bluetooth/share-a-web-page-using-touch-to-share | Same |
| bluetooth/delete-a-touch-to-share-connection | Same |
| bluetooth/disconnect-a-touch-to-share-connection | Same |
| vpn/view-statistics-for-a-connected-profile | No statistics view; the row shows only the state |
| tethering/install-hp-mobile-hotspot | Tethering is built in; no App Catalog |
| tethering/create-an-open-hotspot | The page has no open/secure choice (see Needs device test) |
| screen-and-lock/change-screen-brightness | Merged into adjust-the-screen-brightness |
| screen-and-lock/get-notifications-when-the-screen-is-locked | Merged into the -or-off article |
| screen-and-lock/use-voice-dialing-when-the-screen-is-locked | No voice dialing in Settings, the shell or the Phone app |
| sounds-and-ringtones/select-a-song-as-a-ringtone | No add-song control; a song is added by copying it (see add-ringtones) |
| sounds-and-ringtones/set-ringer-switch-settings | No ringer switch; the options moved to set-your-device-to-vibrate |
| sounds-and-ringtones/set-system-sound-options | Merged into set-sound-options |
| sounds-and-ringtones/turn-beats-audio-on-off | Removed from LuneOS (SoundsAndAlertsPage.qml header) |
| sounds-and-ringtones/use-the-ringer-switch | No ringer switch; Mute Sound is in set-sound-options |
| regional-settings/formats | Merged into change-the-display-formats |
| regional-settings/language | Merged into change-the-display-language |

## Cross-group links

Broken by these deletions, to be fixed by the owning group:
- messaging/connect-your-device-to-a-luneos-device.md links to bluetooth/pair-with-a-luneos-device-using-touch-to-share
- clock/set-an-alarm.md links to sounds-and-ringtones/select-a-song-as-a-ringtone

Outgoing links from my articles that depend on other groups keeping these:
- /basics/open-an-application-in-the-launcher (46)
- /basics/open-the-connection-menu (8). LuneOS has one System Menu, so that article's "connection menu" wording and its VPN mention need fixing. /basics/use-the-system-menu also exists.
- /basics/copy-files-between-your-device-and-your-computer (2)
- /contacts/add-a-ringtone-to-a-contact (1)

For the clock group: clock/manage-clock describes ringer-switch alarm behaviour that was removed from this group's articles.
For the basics group: the Appearance page's Gesture Area switch also has no help page.

## Missing articles

- Import a VPN profile (WireGuard .conf, OpenVPN .ovpn, ConnMan .config; files from the downloads folder)
- Add WireGuard, OpenVPN and L2TP/IPsec profiles
- Display app: Rotation Lock and E Ink settings
- Appearance app: status bar, cards and launcher settings
- Notifications app: per-app switches and LED colors
- Bluetooth: Discoverable, Reconnect headsets automatically, Headset takes calls, Alerts on phone speaker
- Bluetooth: device details popup
- Fingerprint and Face Unlock
- Wi-Fi network details (signal, channel, IP Address, Interface)
- Network Settings, eSIM, Emergency Broadcast, NFC, USB
- Airplane mode and Rotation Lock in the system menu
- Hardware Keyboard settings, including Type on the Keypad
- Keyboard: emoji panel and alternative layouts menu
- Certificate Manager

## Needs device test

Nothing below was tried: the devices are read-only for this audit.

1. Captive portal: join a network with a portal, open Atlas Web, load an http page. Does the sign-in page appear? Does anything notify you? (The adapter publishes onInternet "captivePortal"; nothing consumes it.)
2. Lock After: set a lock mode, set Lock After to 5 minutes, turn the screen off, turn it on after 10 seconds. Is the PIN asked for? lockTimeout is read only by libLunaSysMgrCommon, and not by LunaDisplayManager or the shell.
3. Show When Locked: turn it off, lock, send a notification. Does anything change? No consumer in the shell.
4. Enable Gestures: turn it off, swipe up from the bottom edge. Does it still card the app? sysUiEnableNextPrevGestures has no consumer, so expect no change. If so, remove the switch or implement it.
5. Vibrate group: set Sounds on to Sound, then Sound & Vibrate, and receive a call and a notification. Repeat for Sounds off. VibrateWhenRingerOn/Off have no consumer. Does the TouchPad have a vibrator?
6. Hotspot with an empty Password: is the network open? Name unset (no TetheringIdentifier on the MindPhone): does Share over Wi-Fi fail silently? A password cannot be cleared from the page once set.
7. Wi-Fi tethering on a Wi-Fi-only TouchPad: is anything shared? Hence requires ["modem"].
8. Ringtone Volume: does it change the real ringer volume? The page header says audiod only remembers the number.
9. Mute Sound and the Sounds switch: do they silence music and video as well? The shell calls master/muteVolume on muteSound, while the page's comment says the intent was to spare them.
10. Display language: does choosing one change the UI? Settings and shell strings are hard-coded English. The spelling errors in the language list ("Croation", "Lithunian", "Ukranian", "NorwegiaBokmal") come from the service.
11. Spell Checking underline, and whether tapping your own typed word in the ribbon adds it to the dictionary (wordribbon.cpp:167). The second is left out of the text until confirmed.
12. Wi-Fi system-menu password: tapping a secure network there launches Settings; does the passphrase popup appear? Only the app route is documented.

## Product bugs found

- Wi-Fi app: the Join Network row has no handler, so hidden networks cannot be joined.
- Text Assist: Shortcuts are stored in db8, but neither webos-keyboard nor meta-webos-ports reads that kind. The dictionary's empty-state text promises expansion.
- System menu: the VPN element is permanently visible: false.
- ScreenLockPage says "The center button blinks", which is wrong on devices without one.
- Bluetooth pairing requests from other devices are only answered while the Bluetooth app is open.
