---
{
 "id": "basics/delete-an-application",
 "title": "Delete an application",
 "section": [
  "Manage applications"
 ],
 "order": 32,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27585",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/LaunchBar/DraggableAppIcon.qml remove button",
  "qml/LaunchBar/FullLauncher.qml:onRemoveAppLauncher, removeApplication, DONE",
  "adb: listLaunchPoints removable false for system apps"
 ]
}
---

1. [Open the Launcher](/basics/open-the-launcher).
2. Tap and hold any icon until all icons get a frame.
3. Tap the delete button in the corner of the application's icon. The application is deleted right away, without asking.
4. Tap **DONE**.

The delete button appears only on applications you can remove. The applications that come with the system can't be deleted.
