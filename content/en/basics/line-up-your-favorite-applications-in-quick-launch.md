---
{
 "id": "basics/line-up-your-favorite-applications-in-quick-launch",
 "title": "Line up your favorite applications in Quick Launch",
 "section": [
  "Manage applications"
 ],
 "order": 39,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27519",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/LaunchBar/LaunchBar.qml:102-178 no drop from the Launcher, :242-270,:335-354 fixed list",
  "adb: /etc/palm/default-dock-positions.json"
 ]
}
---

Quick Launch comes with a fixed set of applications. You can't add or remove them yet, but you can change their order ([learn how](/basics/reorder-quick-launch-icons)).

For quick access to other applications, drag them to the **Favorites** tab of the Launcher ([learn how](/launcher/reorder-launcher-icons)).
