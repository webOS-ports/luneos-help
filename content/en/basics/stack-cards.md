---
{
 "id": "basics/stack-cards",
 "title": "Stack cards",
 "section": [
  "Manage applications"
 ],
 "order": 37,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/40368",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/CardView/CardGroupListView.qml pinch to spread, drag",
  "files/tweaks/luna-next-cardshell.json stackedCardSupport"
 ]
}
---

1. In Card view, tap and hold a card.
2. When the card turns slightly transparent, drag it on top of another card, and lift your finger.

To spread out a stack so you can see its cards, pinch out on it.

This needs **Enable stacked cards**, which is on unless you turned it off in [Tweaks](/tweaks/use-tweaks).
