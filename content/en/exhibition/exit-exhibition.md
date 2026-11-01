---
{
 "id": "exhibition/exit-exhibition",
 "title": "Exit Exhibition",
 "section": [],
 "order": 158,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/35282",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "/usr/lib/qml/WebOSCompositor/qml/DockMode/DockMode.qml:70 (gesture area tap undocks)",
  "/usr/lib/qml/WebOSCompositor/qml/DockMode/DockMode.qml:85 (switchToCardView)",
  "/usr/lib/qml/WebOSCompositor/qml/CardShell.qml:86-90 (home key taps gesture area)",
  "luna-displaymanager/Src/DisplayStates.cpp DisplayDockMode::handleEvent (off puck, home key)"
 ]
}
---

Do any of the following:

- Tap the gesture area at the bottom of the screen.
- {if:homebutton}Press the home button.
- If your device is on a charging dock, take it off the dock.

When you exit Exhibition, the apps Exhibition opened close, and you see Card view.
