# comms audit: phone, messaging, contacts

86 articles kept, 46 deleted. Device source of truth: MindPhone MindPhone (read only). Nothing was tapped or launched, so every "verified-device" means a file or query on the device, not an observed behaviour.

| Article | Status | What changed | Evidence |
|---|---|---|---|
| contacts/add-or-change-a-contact-photo | verified-device | Retitled Contact photos: no way to add one on the device, only Remove Photo | 2 refs in front matter; first: `org.webosports.app.contacts/src/views/EditContact.js:234` |
| contacts/create-a-contact | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 4 refs in front matter; first: `org.webosports.app.contacts/src/views/EditContact.js:326` |
| contacts/create-a-favorite | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `org.webosports.app.contacts/src/views/ContactHeader.js:59` |
| contacts/customize-contacts | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `org.webosports.app.contacts/src/views/Preferences.js:50` |
| contacts/delete-a-contact | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `org.webosports.app.contacts/src/views/EditContact.js:278` |
| contacts/delete-an-online-account-from-contacts | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.app.contacts/src/views/Preferences.js:1` |
| contacts/find-a-contact | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 4 refs in front matter; first: `org.webosports.app.contacts/src/util/search.js:5` |
| contacts/get-contact-info-into-contacts | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `adb: grep -l CONTACTS /usr/palm/public/accounts/*/* (cdav, Google, iCloud, Yahoo, Discord, Teams and others)` |
| contacts/get-in-touch-with-a-contact | needs-device-test | Modem items conditional; tel: handler untested | 4 refs in front matter; first: `org.webosports.app.contacts/src/util/details.js:133` |
| contacts/link-a-contact | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.app.contacts/src/views/ContactHeader.js:85` |
| contacts/linked-contacts-in-contacts | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.app.contacts/src/views/ContactHeader.js:85` |
| contacts/manually-synchronize-contacts-with-your-online-accounts | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.app.contacts/src/views/Preferences.js:5` |
| contacts/receive-vcards | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `adb: luna-send com.palm.applicationManager/listAllHandlersForMime text/x-vcard -> com.palm.app.contacts` |
| contacts/remove-a-contact-from-favorites | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.app.contacts/src/views/ContactHeader.js:59` |
| contacts/set-up-an-online-account-in-contacts | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.app.contacts/src/views/Preferences.js:4` |
| contacts/unlink-a-contact | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.app.contacts/src/views/ContactDetails.js:161` |
| contacts/use-contacts-for-the-first-time | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `org.webosports.app.contacts/src/views/FirstLaunch.js:74` |
| contacts/view-edit-or-delete-contact-information | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 4 refs in front matter; first: `org.webosports.app.contacts/src/views/ContactHeader.js:85` |
| messaging/add-a-buddy | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/AddBuddyDialog.js:48` |
| messaging/add-a-favorite | needs-device-test | Fallback through Contacts; pickPerson launch not handled | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/FavoriteItem.js:12` |
| messaging/block-a-message-sender | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationList.js:91` |
| messaging/change-an-im-account-username-or-password | verified-source | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 1 refs in front matter; first: `org.webosports.messaging/app/src/views/PreferencesView.js:2` |
| messaging/change-your-custom-message | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/ImStatus.js:77` |
| messaging/change-your-online-status | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/MainView.js:117` |
| messaging/copy-messages | verified-device | Copy Text puts text in the message box, not the clipboard | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationList.js:184` |
| messaging/create-and-send-a-text-message | verified-device | Requires modem; one recipient; no MMS | 4 refs in front matter; first: `org.webosports.messaging/app/src/views/MsgAddrSearchList.js:42` |
| messaging/customize-messaging-notifications | needs-device-test | Real preference names; ringtone picker launches an app that is not installed | 4 refs in front matter; first: `org.webosports.messaging/app/src/views/PreferencesView.js:69` |
| messaging/delete-a-buddy | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/BuddyList.js:292` |
| messaging/delete-a-conversation | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationList.js:95` |
| messaging/delete-a-message | verified-source | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 1 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationList.js:184` |
| messaging/delete-an-im-account | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/PreferencesView.js:2` |
| messaging/dial-a-number-from-a-conversation | needs-device-test | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 1 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationList.js:609` |
| messaging/receive-a-buddy-request | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationItem.js:83` |
| messaging/receive-and-view-text-messages | verified-device | Says MMS shows only a placeholder | 2 refs in front matter; first: `adb: grep in /usr/palm/applications/org.webosports.app.messaging/index.html: 'New MMS on your phone'` |
| messaging/resend-a-failed-message | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationList.js:1309` |
| messaging/search-for-conversations-or-buddies | verified-source | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 1 refs in front matter; first: `org.webosports.messaging/app/src/views/BuddyList.js:47` |
| messaging/send-and-receive-im-messages | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/ComposeView.js:222` |
| messaging/set-up-an-im-account | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `org.webosports.messaging/app/src/views/PreferencesView.js:140` |
| messaging/sign-in-to-an-im-account | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 1 refs in front matter; first: `adb: grep in /usr/palm/applications/org.webosports.app.messaging/index.html: 'Available', 'INDIVIDUAL ACCOUNTS'` |
| messaging/sign-out-of-an-im-account | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 1 refs in front matter; first: `adb: grep in /usr/palm/applications/org.webosports.app.messaging/index.html: 'Offline', 'INDIVIDUAL ACCOUNTS'` |
| messaging/switch-between-conversations-buddies-and-favorites-lists | verified-source | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/Messaging.js:126` |
| messaging/switch-between-messaging-accounts-in-a-conversation | verified-source | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 1 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationList.js:545` |
| messaging/use-emoticons-in-a-message | verified-source | Replaced smiley table with the keyboard emoji button | 1 refs in front matter; first: `webos-keyboard/qml/WordRibbon.qml:127 emojiButton` |
| messaging/view-a-contact-s-information-from-a-message | needs-device-test | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 1 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationList.js:536` |
| messaging/what-kinds-of-messages-can-i-send-and-receive | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `org.webosports.messaging/app/src/views/ComposeView.js:221` |
| messaging/work-with-conversations | verified-source | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.messaging/app/src/views/ConversationList.js:95` |
| phone/add-a-phone-number-to-a-favorite | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/FavouritePage.qml:142` |
| phone/answer-a-call | verified-device | Removed gesture and legacy icons; answer is on the left; added headset button | 4 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/IncomingCallStrip.qml:82` |
| phone/answer-a-second-call-call-waiting | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhoneWindow.qml:217` |
| phone/change-your-voicemail-number | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:306` |
| phone/create-a-favorite | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/FavouritePage.qml:350` |
| phone/dial-a-favorite | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/FavouritePage.qml:186` |
| phone/dial-by-contact-name-in-the-phone-application | needs-device-test | Handset and tablet differ; handset contact search is unreachable | 4 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/ContactLookupPage.qml:216` |
| phone/dial-by-contact-name-using-just-type | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 5 refs in front matter; first: `luna-next-cardshell/qml/LaunchBar/JustTypeField.qml:89` |
| phone/dial-from-another-application | needs-device-test | tel: handler points at an app that is not installed; added fallback | 3 refs in front matter; first: `org.webosports.app.contacts/src/util/details.js:133` |
| phone/dial-using-the-keyboard | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/DialerPage.qml:120` |
| phone/dial-using-the-onscreen-dial-pad | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhoneTabView.qml:148` |
| phone/dial-your-national-emergency-number | verified-device | Removed lock-screen emergency path, which does not exist; added SIM PIN Emergency Call and airplane behaviour | 5 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/SimPinCard.qml:195` |
| phone/end-a-call | verified-device | Added closing the Phone card and headset button | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/ActiveCallPage.qml:516` |
| phone/ignore-a-call | verified-device | Removed power-button reject, which does not exist; added headset long press | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/IncomingCallStrip.qml:95` |
| phone/listen-to-voicemail-messages | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 4 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/DialerPage.qml:459` |
| phone/lock-or-unlock-the-sim-card | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 4 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:380` |
| phone/make-a-conference-call | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 5 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/CallLineDelegate.qml:257` |
| phone/make-a-second-call | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/ActiveCallPage.qml:606` |
| phone/manage-a-call | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 5 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/AudioRouteButton.qml:72` |
| phone/manually-select-network-settings | verified-device | Moved to Network Settings APN editing | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:351` |
| phone/redial-the-last-number-dialed | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 1 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/DialerPage.qml:218` |
| phone/remove-a-contact-from-the-favorites-list | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `org.webosports.app.contacts/src/views/ContactHeader.js:59` |
| phone/save-a-phone-number-to-contacts | needs-device-test | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 4 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/CallGroupDetails.qml:347` |
| phone/set-roaming-and-data-usage-preferences | verified-device | Moved to Network Settings | 5 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/NetworkSettingsPage.qml:155` |
| phone/set-up-and-use-a-bluetooth-hands-free-device | needs-device-test | Rewritten; HFP handling is listed as unfinished in the app TODO | 5 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/services/AudioRouteManager.qml:62` |
| phone/set-up-voicemail | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/DialerPage.qml:459` |
| phone/set-your-domestic-dialing-method | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 5 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:278` |
| phone/set-your-international-dialing-method | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 5 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:291` |
| phone/silence-the-ringer-on-an-incoming-call | needs-device-test | Removed power/volume silencing and ringer switch; left answer, ignore, Mute Sound | 4 refs in front matter; first: `luna-next-cardshell/qml/StatusBar/SystemMenu/MuteElement.qml:43` |
| phone/switch-between-two-calls | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/ActiveCallPage.qml:579` |
| phone/turn-call-forwarding-on-off | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 3 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:221` |
| phone/turn-call-waiting-on-off | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:268` |
| phone/turn-my-caller-id-on-off | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:260` |
| phone/turn-the-phone-on-and-off | verified-source | Reduced to a link to airplane mode | 1 refs in front matter; first: `luna-next-cardshell/qml/Connectors/AirplaneModeService.qml:247` |
| phone/use-a-wired-headset | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 4 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/services/AudioRouteManager.qml:72` |
| phone/use-another-application-while-on-a-call | verified-device | Warns that closing Phone ends the call | 1 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhoneWindow.qml:148` |
| phone/use-dialing-shortcuts | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 6 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:322` |
| phone/view-favorite-details | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/FavouritePage.qml:192` |
| phone/view-your-call-history | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 7 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/HistoryPage.qml:102` |
| phone/what-s-my-number | verified-device | Rewritten to real labels and paths; legacy icons and Preferences & Accounts paths replaced | 2 refs in front matter; first: `adb: /usr/palm/applications/org.webosports.app.phone/qml/views/PhonePrefsPage.qml:194` |

## Deleted articles

- phone/answer-a-skype-call: Skype is not ported (app TODO)
- phone/create-a-skype-account-in-the-phone-application: Skype is not ported (app TODO)
- phone/dial-a-skype-contact: Skype is not ported (app TODO)
- phone/edit-or-delete-a-skype-account: Skype is not ported (app TODO)
- phone/end-a-skype-call: Skype is not ported (app TODO)
- phone/ignore-an-incoming-skype-call: Skype is not ported (app TODO)
- phone/make-a-skype-to-skype-video-or-audio-call-in-the-phone-application: Skype is not ported (app TODO)
- phone/make-a-skype-to-skype-video-or-audio-call-using-just-type: Skype is not ported (app TODO)
- phone/manage-a-skype-to-skype-video-call: Skype is not ported (app TODO)
- phone/manage-a-skype-to-skype-voice-call: Skype is not ported (app TODO)
- phone/redial-the-last-skype-contact-or-number-dialed: Skype is not ported (app TODO)
- phone/set-skype-calling-preferences: Skype is not ported (app TODO)
- phone/silence-the-ringer-on-an-incoming-skype-call: Skype is not ported (app TODO)
- phone/use-an-existing-skype-account-in-the-phone-application: Skype is not ported (app TODO)
- phone/use-skype-to-dial-an-international-number: Skype is not ported (app TODO)
- phone/use-skype-to-dial-a-phone-number: Skype is not ported (app TODO)
- phone/what-can-i-do-during-a-skype-to-skype-voice-call: Skype is not ported (app TODO)
- phone/what-kinds-of-calls-can-i-make-and-receive-with-skype: Skype is not ported (app TODO)
- phone/change-your-voicemail-greeting: no voicemail greeting menu; set by the provider system
- phone/use-visual-voicemail: visual voicemail deliberately not ported (app TODO)
- phone/dial-using-a-speed-dial: no speed dial in Phone or Contacts
- phone/set-or-change-the-default-number-for-a-favorite: no UI in the current app
- phone/turn-contact-match-display-on-off: Phone Preferences deliberately omits this
- phone/turn-hac-on-off: Phone Preferences deliberately omits this
- phone/turn-tty-tdd-on-off: Phone Preferences deliberately omits this
- phone/turn-the-international-dialing-auto-prefix-feature-on-off: Phone Preferences deliberately omits this
- phone/use-restricted-dialing: no UI in the current app
- contacts/add-a-contact-entry-to-the-launcher: no such command
- contacts/add-a-ringtone-to-a-contact: no ringtone field
- contacts/assign-a-reminder-message-to-a-contact: no reminder field
- contacts/assign-a-speed-dial-to-a-contact: no speed dial in Phone or Contacts
- contacts/call-or-chat-with-a-skype-contact: Skype is not ported (app TODO)
- contacts/copy-a-contact-as-text: no such command
- contacts/copy-a-contact-to-the-sim-card: no SIM copy
- contacts/create-a-skype-account: Skype is not ported (app TODO)
- contacts/send-contacts: no send command
- contacts/where-are-the-contacts-i-transferred-using-the-data-transfer-assistant: no Data Transfer Assistant
- messaging/add-a-contact-from-a-message: no such command
- messaging/chat-with-a-group: no group chat flow
- messaging/connect-your-device-to-a-luneos-device: Touch to Share
- messaging/create-a-skype-account: Skype is not ported (app TODO)
- messaging/create-and-send-a-text-or-multimedia-message: duplicate, no MMS send
- messaging/dial-a-number-from-a-message: numbers not linkified
- messaging/forward-a-message: no Forward
- messaging/read-text-multimedia-messages: duplicate
- messaging/switch-between-conversations-view-and-buddies-view: duplicate

## Cross-group links

Dead link for the owning group to fix:

- sounds-and-ringtones/select-a-file-from-the-ringtones-folder-as-a-ringtone -> /contacts/add-a-ringtone-to-a-contact (deleted; Contacts has no ringtone field). Other imported inbound links to deleted slugs were already gone at last check; only this one remains.

Outbound links from comms into other topics, all existing today:

- /accounts/use-the-accounts-application-to-edit-or-delete-an-online-account
- /accounts/use-the-accounts-application-to-set-up-an-online-account
- /basics/display-card-view-minimize-an-application
- /basics/open-an-application-in-the-launcher
- /basics/open-the-application-menu
- /basics/turn-all-wireless-services-on-off-airplane-mode
- /basics/use-the-system-menu
- /bluetooth/make-a-pairing-request-to-another-device
- /bluetooth/turn-the-bluetooth-feature-on-off
- /just-type/get-in-touch-with-a-contact

## Missing articles

- Phone Accounts page
- Video tab and video calls
- Call barring
- USSD and MMI codes
- Messaging servers and channels tab
- Attachments and voice notes in IM
- Message reactions and Reply
- Cell broadcast
- SIM toolkit (a sim-toolkit topic exists; not checked by comms)
- eSIM
- Dual SIM
- Headset takes calls
- Network Settings overview
- Emoji panel
- Dialpad Feedback tweak
- Missed call alert
- Global address lookup details

## Needs device test

On the MindPhone with a working SIM unless noted.

1. Contacts > a contact > tap a phone number. Expected from files: tel: goes to com.palm.app.phone, which is not installed. Does Phone open and dial?
2. Messaging > a conversation on a voice-capable transport > call button. Same tel: path.
3. Phone > Favorites > expand a favorite > message button; Call Log > expand > message button. These launch com.palm.app.messaging, not installed.
4. Phone > Call Log > expand a call > View Contact. Passes personId; Contacts parses only id or launchType. Does the person open?
5. Phone > Call Log > unknown number > Add to Contacts. Is the number filled in?
6. Messaging > a conversation with a linked contact > tap the name. Does that contact open?
7. Messaging > favorites tab > Add Favorite. Launch type pickPerson is not handled by Contacts.
8. Messaging > Preferences & Accounts > Alert: Ringtone > Tap to pick a ringtone. Launches com.palm.app.musicplayer, not installed.
9. Phone UI, Phone tab: is there any way to reach the contact search (Enter Name)? syncDialpad reopens the keypad.
10. Incoming call: press power, press volume, each alone. Does ringing stop? Then set Mute Sound in the system menu and call again: does it ring?
11. During a call, go to Card view and throw the Phone card away. Does the call end?
12. Pair a Bluetooth headset. Does call audio route? Does Audio step through routes? Do answer and hang up on the headset work?
13. Send an MMS to the device. Does Messaging show only "New MMS on your phone"?
14. Headset button: press to answer, long press to reject, press in call to hang up.
