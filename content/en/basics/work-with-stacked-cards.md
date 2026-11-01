---
{
 "id": "basics/work-with-stacked-cards",
 "title": "Work with stacked cards",
 "section": [
  "Manage applications"
 ],
 "order": 34,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27693",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/CardView/CardGroupModel.qml:82-107 child window joins parent's group",
  "qml/CardView/CardGroupListView.qml pinch to spread"
 ]
}
---

If an application opens another window, such as a new email message from your inbox, the new card joins a stack with the card that opened it. Each card in a stack is still its own window.

You can also stack and unstack cards yourself ([learn how](/basics/stack-cards)).

To see the cards in a stack better, pinch out on it in Card view. To close a stack, throw its cards off the top of the screen one at a time.
