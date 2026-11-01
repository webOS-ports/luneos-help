# LuneOS Help: replacements and new features

Read docs/audit/BRIEF.md first. Its sources of truth, forbidden device actions, voice, feature syntax and status rules all apply here. Evidence stays mandatory: no page from memory or from what a feature "should" do. Read the code behind every label.
Owner's request: update the pages with LuneOS's replacements where that isn't done yet, and add new LuneOS features too, including music streaming in the Music app.

## Your two jobs
1. Replacements. Go through your group's "Deleted articles" in docs/audit/<group>.md and every topic you own. Where LuneOS has a different way of doing what the old page did, write that page or fix the existing page to point to it. Known replacements to confirm: App Catalog -> Preware; HP Play -> copying over USB/MTP and streaming; Skype -> Phone video calls, com.webos.app.videocall and chat apps (Telegram, WhatsApp, Discord, Teams, Google Chat); Quickoffice -> Documents; Adobe Reader -> PDF Viewer; Synergy -> Accounts; Palm Profile backup -> local Backup; webOS Doctor -> reinstalling from webos-ports.org; Data Transfer Assistant -> Backup, accounts or MTP, whichever is true. Do not assume a replacement exists: confirm it. If none exists, leave the page deleted.
2. New features. Write every item in your group's "Missing articles" list that really exists, plus anything else in your area that you find. One task per page, short numbered steps, plain words for ordinary users. Use real labels.

Items that belong to another group are listed under its name below. Skip items not in your list unless you find them inside your own topics.

## New article format
Path: content/en/<topic>/<slug>.md, slug from the title. Copy the front matter shape from a neighbouring page:
id, title, section (list with one heading), order, devices ["phone","tablet"] unless UI-specific, origin "luneos", status, evidence, requires, review [].
"order": a neighbour's order + a fraction to sit beside it, otherwise 100000 + a running number. Pages in one section must have adjacent order values.
Do not add images: no drawing exists for new pages. Log it if a page really needs one.
Apps differ per device and some are only added later. If an app is not on every device, say so plainly in the article's first line, like "Documents isn't installed on every device." Check both devices.
Do not fill pages with unverifiable behaviour: for network services nobody can reach from here (Spotify sign-in, say), describe what the UI offers and use "needs-device-test".
Project notes in ~/webos/LuneOS/<subject>/ and each repo's README/CLAUDE.md help find features, but they can be stale: code and devices win.

## Do not touch
tools/, static/, content/en/toc.json, other groups' topics. Do not run builds. Edit existing pages only in your own topics.
List any new topic in your report with: id, title, which home group, and the path of a real icon.png for it. I add them to toc.json.

## Deliverable
docs/audit/<group>-new.md: new pages table (page, status, evidence), pages changed for replacements, replacements confirmed absent, features found but not documented and why, needs-device-test steps, new topics, links into other groups.
Reply with counts and top surprises, under 150 words.
