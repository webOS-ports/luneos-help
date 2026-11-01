---
{
 "id": "basics/close-an-application-or-application-screen",
 "title": "Close an application or application screen",
 "section": [
  "Manage applications"
 ],
 "order": 32.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/40359",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/CardView/SwipeableCard.qml onFlickingChanged",
  "qml/CardView/CardGroupListView.qml throwAway"
 ]
}
---

- If a screen has a **Back** or **Done** button, tap it to leave the screen but stay in the application. You can also make the [back gesture](/basics/go-up-one-level-in-an-app-back-gesture).
- To close an application or a screen, [display Card view](/basics/display-card-view-minimize-an-application) and throw the card off the top of the screen. If cards are in a stack, you throw one card at a time.

If an application has more than one card open, throwing away one card may close only that screen, or the whole application. It depends on the application.

See also [Work with stacked cards](/basics/work-with-stacked-cards).
