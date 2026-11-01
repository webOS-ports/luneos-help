---
{
 "id": "basics/resize-cards",
 "title": "Resize cards",
 "section": [
  "Manage applications"
 ],
 "order": 38.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum of the cited QML on both devices matches luna-next-cardshell",
  "qml/CardView/CardGroupListView.qml:39-41 cardScale 0.6, not saved",
  "qml/CardView/CardGroupListView.qml:131-157 pinch to zoom, alone in group only, range 0.2 to 0.7"
 ]
}
---

1. In Card view, go to a card that isn't in a stack.
2. Pinch out to make the cards bigger, or pinch in to make them smaller.

All your cards change size together. They go back to their usual size when the shell restarts.

If the card in the middle is in a stack, a pinch [spreads out the stack](/basics/work-with-stacked-cards) instead.
