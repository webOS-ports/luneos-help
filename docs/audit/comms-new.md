# comms-new: replacements and new features

25 new pages: 8 verified-device, 17 needs-device-test. 9 existing pages changed. Nothing was tapped or launched. "verified-device" means a file or read-only query on the device, not an observed behaviour. Full evidence is in each page's front matter; the table gives the first entry.

Device checks: both devices have Tweaks, Video Call, and the Telegram, WhatsApp, Discord, Teams, Google Chat and Facebook (E2EE) connectors. Emergency Broadcast is on the MindPhone only; its page has requires ["modem"]. The TouchPad's only account is com.palm.palmprofile, so no connector has been signed in there.

## New pages

| Page | Status | Evidence (first) |
|---|---|---|
| phone/see-your-phone-accounts | verified-device | `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhoneAppMenu.qml:67` |
| phone/choose-which-account-places-your-calls | needs-device-test | `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:274-301` |
| phone/check-or-turn-off-call-barring | verified-device | `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:394-415` |
| phone/change-dial-pad-sound-and-vibration | verified-device | `adb: /usr/palm/services/org.webosports.service.tweaks.prefs/preferences/org.webosports.app.phone.json` |
| phone/receive-emergency-alerts | verified-device | `adb: /usr/palm/applications/org.webosports.app.settings.cellbroadcast/appinfo.json` |
| phone/hide-your-caller-id-for-one-call | verified-device | `adb: /usr/palm/applications/org.webosports.app.phone/qml/services/DialStringParser.js:53` |
| phone/use-network-service-codes | needs-device-test | `adb: /usr/palm/applications/org.webosports.app.phone/qml/services/MmiCodes.js` |
| phone/use-your-provider-s-service-menus | needs-device-test | `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/IncomingUSSDAlert.qml:60-186` |
| phone/respond-to-a-missed-call | verified-device | `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/MissedCallAlert.qml:31-36` |
| messaging/react-to-a-message | needs-device-test | `adb: /usr/palm/applications/org.webosports.app.messaging/index.html (reaction-picker-popup, reactMore)` |
| messaging/reply-to-a-specific-message | needs-device-test | `adb: /usr/palm/applications/org.webosports.app.messaging/index.html (messageMenu, menuReply)` |
| messaging/open-pictures-files-and-voice-messages | needs-device-test | `org.webosports.messaging/app/src/views/ConversationItem.js:576-592` |
| messaging/see-whether-a-message-was-delivered | needs-device-test | `org.webosports.messaging/app/src/views/ConversationItem.js:181-189` |
| messaging/vote-in-a-poll | needs-device-test | `org.webosports.messaging/app/src/views/ConversationItem.js:480-516` |
| messaging/use-servers-and-channels | needs-device-test | `adb: /usr/palm/applications/org.webosports.app.messaging/index.html (Search servers, No servers yet)` |
| chat-apps/what-chat-services-can-i-use | verified-device | `adb: luna-send com.palm.service.accounts/listAccountTemplates (both devices' template lists)` |
| chat-apps/set-up-telegram | needs-device-test | `adb: /usr/palm/applications/com.palm.app.telegram/source/validator.js:53-74` |
| chat-apps/set-up-whatsapp | needs-device-test | `adb: /usr/palm/applications/com.palm.app.whatsapp/source/validator.js:55-100` |
| chat-apps/set-up-discord | needs-device-test | `adb: /usr/palm/applications/com.palm.app.discord/source/validator.js:104-146` |
| chat-apps/set-up-teams | needs-device-test | `adb: /usr/palm/applications/com.palm.app.teams/source/validator.js:81-119` |
| chat-apps/set-up-google-chat | needs-device-test | `adb: /usr/palm/applications/com.palm.app.googlechat/source/validator.js:31-35` |
| chat-apps/set-up-facebook | needs-device-test | `adb: /usr/palm/applications/com.palm.app.gometa/source/validator.js:28-64` |
| chat-apps/call-someone-over-a-chat-account | needs-device-test | `adb: listAccountTemplates: PHONE on com.palm.telegram, com.palm.whatsapp, com.palm.teams, videoFormat none` |
| video-calls/join-a-video-meeting | needs-device-test | `adb: /usr/palm/applications/com.webos.app.videocall/appinfo.json` |
| video-calls/what-kinds-of-video-calls-can-i-make | verified-device | `adb: listAccountTemplates: every PHONE provider has videoFormat none` |

## Pages changed for replacements

| Page | Change |
|---|---|
| messaging/send-and-receive-im-messages | Removed a false claim that attach sends a file and mic sends a voice note |
| messaging/what-kinds-of-messages-can-i-send-and-receive | Lists the chat services, links to chat-apps |
| messaging/set-up-an-im-account | Links to the per-service sign-in pages |
| messaging/use-emoticons-in-a-message | Emoji panel steps: tabs and **ABC** |
| messaging/work-with-conversations | Added reactions |
| messaging/switch-between-conversations-buddies-and-favorites-lists | devices now phone and tablet; the four tabs are not tablet-only |
| contacts/find-a-contact | Removed **Search Exchange**: it cannot appear on these devices |
| phone/turn-call-forwarding-on-off | Links to service codes for conditional forwarding |
| phone/turn-my-caller-id-on-off | Links to the one-call page |

Replacement mapping confirmed:

- All 18 phone Skype pages and contacts/messaging Skype pages: chat-apps/call-someone-over-a-chat-account and the set-up pages. Voice only, Telegram, WhatsApp and Teams.
- messaging/chat-with-a-group: partly replaced by messaging/use-servers-and-channels. Group chats arrive from the service; there is still no way to start one here.
- contacts/where-are-the-contacts-i-transferred-using-the-data-transfer-assistant: stays deleted. contacts/get-contact-info-into-contacts already covers online accounts, and Backup is the backup group's.

## Replacements confirmed absent

- **Video in Phone**: not real today. The Video tab appears only if an account declares a video format (PhoneTabView.qml:69-70, 92-94). Every PHONE provider in listAccountTemplates has videoFormat "none". VideoCallPage.qml:30-32 says nothing in the stack produces a stream. No page describes the tab; video-calls/what-kinds-of-video-calls-can-i-make says so.
- **com.webos.app.videocall**: not a calling app. It is two buttons that open Webex or Teams web pages in Atlas. Documented as that. Its window title is "Video Call App".
- **RCS**: not real. Only a feasibility report in ~/webos/LuneOS/rcs. Nothing in Messaging or on the device. No page.
- **Visual voicemail**: not real. TODO lists it as deliberately not ported; ~/webos/LuneOS/vvm and phonecalls are empty. phone/use-visual-voicemail stays deleted.
- **Global address lookup**: the code is on the device (`GLOBAL ADDRESS LOOKUP`, `Search Exchange` in Contacts) but needs a REMOTECONTACTS account. No template on the MindPhone has one, and listAccountTemplates on it shows no Exchange account. No Exchange connector turned up in the meta-luneos recipes. No page, and the old sentence is gone.
- **SIM contacts**: com.palm.sim template exists, but its service com.palm.service.contacts.sim is not installed. contacts/copy-a-contact-to-the-sim-card stays deleted.
- messaging/forward-a-message, phone/dial-using-a-speed-dial, restricted dialing (FDN has no editing UI): stay deleted.

## Features found but not documented, and why

- **Sending attachments**: the attach button calls palm://com.palm.filepicker, which is not installed, and attachmentChosen has no caller. The page says you can't send files yet.
- **Sending voice notes**: startVoiceNote and stopVoiceNote only run a timer. No recording or send exists in the app, though the transport has an Opus encoder. The page says you can't send them yet.
- **View location**: launches com.palm.app.maps; getAppInfo says invalid on the MindPhone. Left out of messaging/open-pictures-files-and-voice-messages. Bug for the Messaging app.
- **Messaging header call and video buttons**: use `tel:` and com.palm.app.phone, and getAppInfo says that app id is invalid. Left out of the call page; Phone is the documented route. Probably the same fault as tel: in the earlier needs-device-test list.
- **Emergency alerts**: nothing but the settings page listens. No matches for CellBroadcast in luna-next-cardshell/qml, org.webosports.app.phone/qml or webos-telephonyd/src. A real alert with that page closed is seen by nobody. The page warns about it. This is a safety gap worth fixing before the page is softened.
- **Call barring display**: PhonePrefsPage shows oFono's raw value, so "disabled" may appear instead of **Not barred**. The page avoids quoting either.
- **Dialpad Feedback default mismatch**: the Tweaks file says "noFeedback", the app's default is "vibrateSound". Tweaks may show **None** while the phone beeps and buzzes until the value is first set. The page states no default.
- **Dial pad pauses** (`,` `p` `;` `w`): parsed, but I found no way to type them on the keypad. Not documented.
- **Phone Preferences hint**: the service chooser says the preference is in Preferences & Accounts; it is in Phone Preferences. The page gives the real place.
- **Hand-set contact search**: still unreachable (Dial on empty reopens the keypad), so call-someone-over-a-chat-account uses dial and Favorites, with Enter Name under {if:tablet}.
- **Headset takes calls**: a Bluetooth setting, left to settings. **Emoji panel**: covered by the messaging page edit; text-assist may want its own.
- `HP webOS Account` (com.palm.palmprofile) declares PHONE and exists on both devices. If its transport is added, Phone Accounts could list an extra row. Check on device.

## Needs device test

On the MindPhone unless noted.

1. Telegram: add the account, reply to the Telegram chat with the code. Does the chat appear?
2. WhatsApp: Sign In, scan the QR code, and try the pairing code. Which labels really appear?
3. Discord: Sign In with a blank token. Does the human check come up? Does the QR code work?
4. Teams: Sign In window, then Use device code instead. Does the code arrive in Messaging?
5. Google Chat: paste five cookies. Does sign-in work?
6. Facebook (E2EE): sign in, with two-factor if possible. Where does the prompt appear?
7. After any of these, does Accounts add a confirm step after Sign In?
8. With a calling account signed in: does Phone Accounts list it, with the right second line? Do Domestic Calls and International Calls appear?
9. With two calling accounts: dial a number, check the chooser, **Always use this service for these calls**, and that the call connects. Then Favorites > arrow > the account's line. TouchPad: does tablet **Enter Name** list the account? Does Cellular appear with no modem?
10. Type `*#06#`, `*#21#`, `*#43#`. Do the results appear? `**21*number#` then `##21#`. `*#33#`, then `#330*password#` on a SIM that allows it.
11. Your provider's balance code. Does the alert show? Reply, Send, Cancel.
12. `#31#` and a number, to a phone that shows caller ID.
13. Let a call ring out: alert, **Call back**, **Dismiss**, then wait a minute: does a notification appear and open Call Log?
14. Tweaks > Phone > Dialpad Feedback: try all four, in and out of a call. Does Tweaks show the phone's real value before you first change it?
15. Emergency Broadcast: are all switches off by default? With the page closed during a test broadcast, does anything appear?
16. IM conversation: react by tap and by a short right drag, remove by tapping. Does the other side see it? Try in an SMS conversation: does the row open, and what happens?
17. **Reply** in IM: does the quote show on the other side?
18. Receive a picture, voice message, mp4, PDF, vCard, event, location. Does each open? Does location fail?
19. Attach and mic: confirm nothing is sent.
20. Delivery ticks on Telegram or WhatsApp. Are one and two checks seen?
21. Poll on a service that sends them: does voting work?
22. Servers tab with Discord: list, search, a channel, tapping a sender's name.
23. Video Call: **Open with Webex** and **Open with Teams** on both devices. Does Atlas open? On the TouchPad, does the camera work in a meeting?
24. Messaging conversation header call button on a calling account: does Phone open?

## New topics

| id | Title | Home group | Icon |
|---|---|---|---|
| chat-apps | Chat Apps | Communication | ~/claude-scratch/help/comms-new/dev/messaging/icon.png (org.webosports.app.messaging/icon.png from the device) |
| video-calls | Video Calls | Communication | ~/claude-scratch/help/comms-new/dev/videocall-icon.png (com.webos.app.videocall/icon.png from the device) |

The Telegram, WhatsApp and other connectors have only images/icon-256x256.png, not an icon.png.

## Links into other groups

- /basics/open-an-application-in-the-launcher
- /basics/open-the-application-menu

All other links stay inside phone, messaging, contacts, chat-apps and video-calls, and all exist. Delivered to settings: Headset takes calls is left to them. eSIM, dual SIM and Network Settings were not touched. phone/receive-emergency-alerts covers the Emergency Broadcast app; settings should link to it, not duplicate it.
