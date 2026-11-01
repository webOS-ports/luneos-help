---
{
 "id": "photos/print-pictures",
 "title": "Print pictures",
 "section": [],
 "order": 500,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/41191",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.photos/qml/PictureView.qml:290",
  "/usr/palm/applications/org.webosports.app.photos/qml/Printer.qml:50",
  "/usr/palm/applications/org.webosports.app.photos/qml/Printer.qml:68",
  "adb: luna-send -n 1 luna://com.palm.printmgr/printers/listActive {} (returns Lexmark MC2425adw on both devices)"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Photos & Videos** > tap the album > tap the picture.
2. If the bar at the top is hidden, tap the picture.
3. Tap the Print button.
4. Tap a printer in the list.

The message **Sent to the printer** tells you the picture is on its way. If you see **No printers found**, add one in Print Manager ([learn how](/print-manager/add-a-printer)).

There are no copy, size or color options here, and you print one picture at a time. To follow or cancel a job, use Print Manager ([learn how](/print-manager/cancel-printing)).
