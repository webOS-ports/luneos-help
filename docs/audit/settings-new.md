# Audit: group "settings", replacements and new features

40 new pages: 26 verified-device, 11 verified-source, 3 needs-device-test. 4 new topics. 8 existing pages changed. No images added.

Device copies and scripts: ~/claude-scratch/help/audit/settings-new/ (mp, tp, settings-src, scripts/write_pages.py).
Evidence strings: `adb: settings-common/qml/...` is /usr/palm/applications/org.webosports.app.settings-common/qml/... (both devices unless a serial is given). `org.webosports.app.settings@b5d8ff4:` is the SRCREV in the wrynose recipe (herrie/integration-testing), newer than both devices. Pages only in that revision are verified-source.

"verified-device" means the file or query was seen on a device. Nothing was tapped or changed, so no connection, enrolment, or import was actually run.

What is installed:
- TouchPad (TouchPad): no Network Settings, Emergency Broadcast, NFC, Fingerprint, Face Unlock, eSIM.
- MindPhone (MindPhone): Network Settings and Emergency Broadcast, two SIMs active. No NFC, Fingerprint, Face Unlock, eSIM.
- NFC, Fingerprint, Face Unlock and eSIM were seen on neither device, so those pages are verified-source and say so in the first line. faceunlock is a machine feature only of halium-arm64.

## New pages

| Page | Status | Key evidence |
|---|---|---|
| wi-fi/view-wi-fi-network-details | verified-device | adb: settings-common/qml/Connectivity/WiFiNetworkInfoPopup.qml:346 |
| wi-fi/if-a-wi-fi-network-wont-connect | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/WiFiConnectProblemPopup.qml:94 |
| bluetooth/view-details-of-a-paired-device | verified-device | adb MindPhone: settings-common/qml/Connectivity/BluetoothDeviceInfoPopup.qml:126 |
| bluetooth/reconnect-headsets-automatically | verified-device | adb MindPhone: settings-common/qml/Connectivity/BluetoothPage.qml:349 |
| bluetooth/choose-where-calls-and-alerts-play | verified-device | adb MindPhone: settings-common/qml/Connectivity/BluetoothPage.qml:593 |
| vpn/import-a-vpn-profile | verified-device | adb: settings-common/qml/Connectivity/VPNPage.qml:226 |
| vpn/add-a-wireguard-vpn-profile | verified-device | adb: settings-common/qml/Connectivity/VpnProfilePopup.qml:214 |
| vpn/add-an-openvpn-vpn-profile | verified-device | adb: settings-common/qml/Connectivity/VpnProfilePopup.qml:214 |
| vpn/add-an-l2tp-vpn-profile | needs-device-test | adb: settings-common/qml/Connectivity/VpnProfilePopup.qml:214 |
| vpn/add-a-pptp-vpn-profile | verified-device | adb MindPhone: /usr/share/luneos-vpn-adapter/formfields/pptp.json |
| text-assist/enter-emoji | verified-device | adb: /usr/share/maliit/plugins/org/luneos/EmojiPanel.qml (both devices) |
| text-assist/use-another-keyboard-layout | verified-device | adb MindPhone: /usr/share/maliit/plugins/org/luneos/keys/LanguageKey.qml:47 |
| text-assist/set-hardware-keyboard-options | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/General/TextAssistPage.qml:293 |
| network/turn-mobile-data-and-data-roaming-on-off | verified-device | adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:149 |
| network/set-the-network-mode | verified-device | adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:167 |
| network/choose-a-mobile-network-manually | verified-device | adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:193 |
| network/lock-your-sim-card-with-a-pin | verified-device | adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:267 |
| network/edit-an-access-point | verified-device | adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:351 |
| network/use-two-sim-cards | verified-device | adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:424 |
| network/add-an-esim-profile | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimPage.qml:434 |
| network/manage-esim-profiles | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/EsimPage.qml:492 |
| network/receive-emergency-broadcasts | needs-device-test | adb MindPhone: settings-common/qml/Connectivity/CellBroadcastPage.qml:201 |
| network/use-nfc-tags | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:259 |
| network/write-copy-or-lock-an-nfc-tag | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:443 |
| network/read-an-id-card-or-passport | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:287 |
| network/connect-to-a-computer-with-usb | verified-device | adb: settings-common/qml/Connectivity/UsbPage.qml:96 |
| notifications/turn-notifications-from-an-app-on-off | verified-device | adb: settings-common/qml/General/NotificationsPage.qml:247 |
| notifications/choose-a-notification-light-color | verified-device | adb: settings-common/qml/General/NotificationsPage.qml:114 |
| notifications/manage-notifications-from-web-apps | verified-device | adb: settings-common/qml/General/NotificationsPage.qml:329 |
| appearance/change-the-status-bar | verified-device | adb: settings-common/qml/General/AppearancePage.qml:90 |
| appearance/change-how-cards-behave | verified-device | adb: settings-common/qml/General/AppearancePage.qml:269 |
| appearance/change-the-launcher-tabs | verified-device | adb: settings-common/qml/General/AppearancePage.qml:99 |
| appearance/lock-the-screen-rotation | verified-device | adb: settings-common/qml/General/DisplayPage.qml:215 |
| appearance/set-the-e-ink-refresh-speed | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/General/DisplayPage.qml:237 |
| security/set-up-fingerprint-unlock | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/General/FingerprintPage.qml:293 |
| security/set-up-face-unlock | verified-source | org.webosports.app.settings@b5d8ff4:src/qml/General/FaceUnlockPage.qml:294 |
| security/check-whether-your-device-is-encrypted | verified-device | adb: settings-common/qml/General/EncryptionPage.qml:135 |
| security/see-what-an-application-may-use | verified-device | adb: settings-common/qml/General/ApplicationsPage.qml:156 |
| security/use-hardware-privacy-switches | verified-source | luna-next-cardshell/qml/Connectors/KillSwitchService.qml |
| security/what-is-certificate-manager | needs-device-test | adb: settings-common/qml/General/CertificatePage.qml:104 |

Order values: fractions beside neighbours in existing topics. New topics use 100001+ (network), 100101+ (notifications), 100201+ (appearance), 100301+ (security). Sections in existing topics stay empty, like their neighbours; network and security use headings.

## Pages changed

| Page | Change |
|---|---|
| vpn/what-is-the-vpn-app | Links to import; PPTP added to "some devices" |
| regional-settings/set-up-and-switch-among-multiple-onscreen-keyboard-layouts-and-languag | Removed "press and hold the language key" as a general claim: phones have no alternative layouts. Links to the new layout page |
| text-assist/customize-text-assist-settings | Hardware Keyboard sentence now links to the new page |
| screen-and-lock/set-options-for-unlocking-the-screen | Links to fingerprint and face unlock |
| screen-and-lock/turn-blink-notifications-on-off | Color sentence links to the new page |
| wi-fi/customize-wi-fi-connection-settings | Related link to network details |
| wi-fi/connect-to-a-new-secure-wi-fi-network | Link to the won't-connect page |
| tethering/use-tethering | Link to the USB page |

Pre-edit copies: ~/claude-scratch/help/audit/settings-new/before-edit/.

## Replacements

No page in my topics still mentions App Catalog, Touch to Share, Synergy, or Palm/HP services, so job 1 produced only the pages above.

Confirmed absent, left deleted:
| Deleted article | Checked |
|---|---|
| wi-fi/put-wi-fi-to-sleep-when-the-screen-is-off | No such row in Wi-Fi or Battery |
| bluetooth/rename-a-device | No rename in BluetoothPage; DeviceInfoPage only shows the name |
| bluetooth/forward-contact-phone-numbers-or-text-messages-to-a-car-kit | No PBAP or MAP setting in Settings or Phone. obexd is on the MindPhone but nothing in the UI uses it |
| bluetooth/*touch-to-share* (6 pages) | No equivalent. qml/NFC only acts on tags. NFC tag pages are documented as their own feature, not as a replacement |
| vpn/view-statistics-for-a-connected-profile | Row shows only the state |
| tethering/create-an-open-hotspot | No open/secure choice |
| tethering/install-hp-mobile-hotspot | Tethering is built in |
| screen-and-lock/use-voice-dialing-when-the-screen-is-locked | No voice dialing |
| sounds-and-ringtones/turn-beats-audio-on-off | No equalizer in Sounds & Ringtones or Accessibility |
| sounds-and-ringtones ringer switch pages | Replacement already in set-sound-options (Mute Sound) and set-your-device-to-vibrate |

Already replaced in the earlier pass: Mobile Hotspot -> Tethering; brightness, Auto Dim and screen timeout -> Display; wallpaper -> Appearance.

## Features found but not documented

- Tweaks app and its Disable animations, Hardware navigation keys, Use New Device Menu: developer-facing editor, not in Settings.
- Developer Mode, Battery, Storage, Accessibility, Print Manager, Just Type: other groups' areas.
- VPN split routing: the service has setSplitRouting, there is no UI.
- VPN entry in the system menu: VpnElement is visible: false. basics/use-the-system-menu still says "VPN".
- Tap a tag with a vCard, Wi-Fi or Bluetooth record: readable in NFC, not acted on. Left out of the action list.
- Physical keyboard Alt, Sym and multi-tap behaviour: belongs with basics/enter-alternate-keyboard-characters.
- Emoji key on a physical keyboard: one sentence only, it depends on each keyboard's profile in hwkeyboard/*.json.
- Airplane mode in the system menu: basics/turn-all-wireless-services-on-off-airplane-mode already covers it.

## Needs device test

Nothing below was tried.

1. Import: put a .conf and a .ovpn in downloads, import each, connect. Does a file in a subfolder really stay hidden? Does a ConnMan .config import show no Edit button?
2. WireGuard on the TouchPad: add any profile and connect. The kernel has no CONFIG_WIREGUARD and there is no wireguard-go, so expect failure with no message (VPNPage only logs a connect error). The MindPhone has /sys/module/wireguard.
3. L2TP/IPsec: connect to a real L2TP/IPsec server. Neither device has an ipsec binary and the form has no pre-shared key field, so expect plain L2TP at best. Page marked needs-device-test.
4. OpenVPN with Username / password auth: is the prompt shown, and does Send connect?
5. Certificate Import... for an OpenVPN profile with the name typed first: does the path fill in, and is it kept when the profile is saved?
6. Emergency Broadcast: send a test alert on a test network, with the app closed. Does anything appear? OfonoCellBroadcast is bound only in CellBroadcastPage, so expect nothing outside the open app. The page tells people not to rely on it.
7. Certificate Manager: no launcher icon (visible: false). Can it be opened at all? main.qml lists it, but neither device installs that window as an app.
8. Wi-Fi won't-connect popup: only in the recipe revision. Check each message after updating an image.
9. Notification light: on a device with an LED, does every color show, and does a per-app color override the default? Neither test device lists a color LED under /sys/class/leds.
10. Emoji: turn Predictive Text and Spell Checking off. Does the strip vanish, as WordEngine::isEnabled says? This is the TouchPad's current state.
11. Rotation Lock in Display: the switch writes angle 0, the system menu writes the live angle. Does the Display switch lock at the current orientation as the page says?
12. Fingerprint and Face Unlock: enrol and unlock on a device that has them. Confirm passcode prompt and five-try lockout text.
13. eSIM and NFC: run through both pages on a device with the hardware.
14. Hardware Keyboard group: check on a Q25 (Type on the Keypad is shown only when no layout is identified) and with a USB keyboard.

## New topics (for toc.json)

Icons are in ~/Documents/GitHub/org.webosports.app.settings/src/qml/images/icons/.

| id | title | Home group | Icon |
|---|---|---|---|
| network | Network | Web and Wireless | icon-networksettings.png |
| notifications | Notifications | Preferences | icon-notifications.png |
| appearance | Appearance | Preferences | icon-appearance.png |
| security | Security | Preferences | icon-encryption.png |

## Links into other groups

- /basics/open-an-application-in-the-launcher (all pages)
- /basics/open-the-connection-menu (2 new)
- /basics/copy-files-between-your-device-and-your-computer (3 new)
- /basics/stack-cards (appearance/change-how-cards-behave)
- /basics/turn-all-wireless-services-on-off-airplane-mode (wi-fi/if-a-wi-fi-network-wont-connect)
- /device-info/install-a-certificate-from-usb-drive-storage, /device-info/view-certificate-details, /device-info/delete-a-certificate (security/what-is-certificate-manager)
- /software-manager/manage-downloaded-applications (security/see-what-an-application-may-use)
- /location-services/manage-location-information-passed-to-applications (same)

For the basics group: basics/use-the-onscreen-keyboard still says "Text Assist on the **Prefs** tab" and does not mention emoji; link /text-assist/enter-emoji. basics/use-the-system-menu lists VPN, which is hidden.

## Product bugs found

- L2TP/IPsec is offered, but neither device has an ipsec binary and the form has no pre-shared key field.
- WireGuard is offered on the TouchPad, whose kernel has no WireGuard. A failed connect is only logged, so the user sees nothing.
- Emergency alerts reach only the open Settings page. Nothing raises them on screen, which defeats their purpose.
- The emoji button lives on the suggestion strip, so it vanishes when Predictive Text and Spell Checking are both off.
- Certificate Manager has no launcher icon and no route from another page.
- Two Hardware Keyboard spellings: "On-Screen Keyboard" in Text Assist, "On-screen Keyboard" in the system menu.
- NfcAutoDispatch opens geo: links in Atlas, not Maps.
