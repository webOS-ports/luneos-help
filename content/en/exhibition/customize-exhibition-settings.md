---
{
 "id": "exhibition/customize-exhibition-settings",
 "title": "Customize Exhibition settings",
 "section": [],
 "order": 163,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/35287",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/ExhibitionPage.qml:69-125 (list, Time checkbox)",
  "adb: luna-send com.palm.applicationManager/listDockModeLaunchPoints (Music, Photos & Videos)",
  "/usr/lib/qml/WebOSCompositor/qml/DockMode/ExhibitionCarousel.qml:25 (one page per enabled app)"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Exhibition**.
2. Under **Applications**, check or uncheck each app. You cannot uncheck **Time**.

Each app you check gets its own page in Exhibition. Only apps made for Exhibition are listed, such as **Music** and **Photos & Videos**. See [Which apps work in Exhibition?](/exhibition/which-apps-work-in-exhibition)
