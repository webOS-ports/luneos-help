---
{
 "id": "basics/change-card-order-or-unstack-cards",
 "title": "Change card order or unstack cards",
 "section": [
  "Manage applications"
 ],
 "order": 38,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/40371",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/CardView/CardWindowWrapper.qml:175",
  "qml/CardView/CardGroupListView.qml opacity 0.8, drag",
  "files/tweaks/luna-next-cardshell.json stackedCardSupport"
 ]
}
---

1. In Card view, tap and hold the card you want to move. This can be a single card or a card in a stack.
2. When the card turns slightly transparent, drag it to another position. You can drag a stacked card to another position in the stack, or drag it out of the stack to unstack it.

This needs **Enable stacked cards**, which is on unless you turned it off in Tweaks.
