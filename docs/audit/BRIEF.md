# LuneOS Help text audit: shared brief

Repo: ~/Documents/GitHub/luneos-help. Articles: content/en/<topic>/<slug>.md, one Markdown file each,
JSON front matter between --- lines. Untouched imports are in ~/claude-scratch/help/content-imported/.
This text was imported from Palm/HP webOS 3.0-era Help. Goal: every sentence must describe what LuneOS
actually does today. Owner's words: "cross check all text with the actual behavior on device and in
luna next cardshell, we dont have an option key, ringer switch in most cases etc."

## Sources of truth (in this order)
1. The running devices, READ-ONLY over adb. Serials: TouchPad (HP TouchPad, tablet UI, wifi only)
   and MindPhone (MindPhone "mindset", phone UI, no camera). Allowed: ls, cat, grep, ps,
   luna-send read-only queries (get/query/list methods), reading app files in /usr/palm/applications
   and /media/cryptofs/apps/usr/palm/applications. FORBIDDEN: any write, tap, input event, setting change, app launch,
   install, reboot, set/put/del methods. BusyBox on the MindPhone: `head -n 5`, not `head -5`.
2. Source in ~/Documents/GitHub: luna-next-cardshell (the shell), org.webosports.app.* (phone, messaging is
   org.webosports.messaging, camera, memos, maps, music, photos, pdf, settings, videoplayer...), core-apps-ports
   (com.palm.app.accounts, calculator, calendar, clock, contacts, email, notes, tasks), core-apps, webos-keyboard
   (the onscreen keyboard), luneos-components, luna-sysservice, luna-sysmgr. Search with grep, and read the code, not just names.
   Layers: /media/herrie/LuneOS/wrynose/webos-ports/meta-webos-ports and meta-smartphone.
   Installed apps may be newer or different from a repo: the file on the device wins.
3. Shell facts already established are in FACTS below; verify anything else you rely on.

Never invent. If you cannot establish that something works, do not assert it. Remove the claim or mark the
article as described in Status. Do not guess from what webOS did.

## What to do for each article
Read it, find the code or on-device file behind every step, label and menu name, then:
- Correct it: real labels, real menu paths, real gestures, exactly as the UI spells them.
- Rewrite in the same plain, second-person voice. Keep it short. Steps stay numbered lists.
- Remove references to things LuneOS lacks (Palm/HP Profile, HP App Catalog, Synergy marketing, Touch to Share, Skype etc.)
  unless the code shows they exist. If a whole article describes something that doesn't exist, delete the file and log it.
- Where it differs per device, use the feature syntax below instead of writing "if your device has".
- Keep the front matter and add/change fields:
  - "status": "verified-device" only if you saw it on a device (file or query result, not just the repo);
    "verified-source" if confirmed from source; "needs-device-test" if the steps could not be confirmed.
  - "evidence": short list of "path:line" or "adb: <query>" strings backing it.
  - "requires": optional, list of features the whole article needs, e.g. ["modem"] or ["!keyboard"].
  - "review": empty it as you resolve terms.
- Keep `<!-- ui:phone -->` / `<!-- ui:tablet -->` blocks only where the phone and tablet UI really differ
  (Settings.tabletUi in the shell, or app layout). Merge them to a single body if the text is now the same.
- Keep image refs `![image](/legacy/...)` when still accurate, delete them when not. Do not edit tools/.
- Links are `/topic/slug`. Only link to articles that exist in the repo. Other groups may delete theirs, so log any
  link into another group's topic under "Cross-group links".
- Never use: "smartphone" (say "device" or "phone"), HP, Palm, webOS in user-facing steps unless it's the real label.

## Feature syntax
Features come from each machine's deviceinfo adaptation, and the page shows only what applies.
  tablet        tablet UI (deviceinfo_tablet_ui). Prefer ui blocks for large differences.
  keyboard      physical keyboard (deviceinfo_keyboard_layout)
  modem         cellular modem (deviceinfo_modem): calls, SMS, mobile data, SIM
  camera        device has a camera (deviceinfo_has_camera)
  homebutton    physical home button (deviceinfo_has_home_button)
  volumebutton  physical volume buttons (deviceinfo_has_volume_button)
  powerbutton   physical power button (deviceinfo_has_power_button)
  brightness    display brightness can be controlled (deviceinfo_has_brightness_control)
Put `{if:feature}` at the very start of a paragraph, list item or heading to show it only with that feature.
`{if:!feature}` is the opposite; commas mean AND: `{if:modem,!tablet}`.
  - {if:keyboard}Press **Sym** ...
  {if:!homebutton}Flick up from the bottom edge of the screen.
No inline conditions inside a sentence: use two list items or paragraphs instead.
Only these eight features exist. There is NO feature for a ringer switch or Option key.

## FACTS (shell, established from source and devices)
- deviceinfo keys: most are unset on most devices; shell defaults HasHomeButton=false, HasVolumeButton=true, HasPowerButton=true.
- Ringer switch: no deviceinfo field and no shell handling. Key_VolumeMute maps to audio.mute. System menu has a Mute element
  (luna-next-cardshell/qml/StatusBar/SystemMenu/MuteElement.qml). Do not mention a ringer switch.
- Physical keyboards are rare (only Q25 sets keyboard_layout). Check webos-keyboard for what the onscreen keyboard really does. Option/Sym/orange-key instructions are wrong unless proven for a physical keyboard, and there is no Option key in general.
- Gesture area: not hardware. It's an on-screen strip at the bottom (qml/WindowManager/LunaGestureArea.qml, height gu(4)) that a Tweak can switch off (qml/AppTweaks), hidden for fullscreen cards. A flick up from the screen's bottom edge also works (CardsArea.qml onScreenEdgeFlickEdgeBottom). Read those files for exactly what each gesture does.
- "Center button" is only the home button feature.
- Hardware keys defaults: qml/Connectors/HardwareKeys.qml. Launcher/Quick Launch: qml/LaunchBar. Status bar and system menu: qml/StatusBar. Lock screen: qml/LockScreen. Card stacks: qml/CardView. Notifications: qml/Notifications. Exhibition: qml/DockMode.
- Installed on both devices include com.palm.app.{accounts,backup,calendar,clock,contacts,email,tasks}, org.webosports.app.{atlas,calculator,documents,maps,memos,messaging,music,pdf,phone,photos,...}, com.palm.stark.files, Preware (com.palm.app.preware2); apps differ by device, so check. Settings is split into org.webosports.app.settings.* entries.

## Deliverables
- Edited files in your topics only. Touch nothing else, and do not run tools/import_archive.py or tools/build.py.
- ~/claude-scratch/help/audit/<group>.md with: a table of article, status, what changed, evidence; "Deleted articles" with reason;
  "Cross-group links"; "Missing articles": LuneOS features in your area with no help page yet (list only, don't write them);
  "Needs device test": exact steps a person must try.
- Reply with counts per status and the top surprises, under 150 words.
