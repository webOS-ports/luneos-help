---
{
 "id": "utilities/check-your-device-with-system-monitor",
 "title": "Check your device with System Monitor",
 "section": [],
 "order": 100101,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.sysmonitor/qml/OverviewPage.qml:37-322 (sections)",
  "/usr/palm/applications/org.webosports.app.sysmonitor/qml/main.qml:126-130 (menu)",
  "/usr/palm/applications/org.webosports.app.sysmonitor/qml/ProcessesPage.qml:104,113-114,142",
  "/usr/palm/applications/org.webosports.app.sysmonitor/qml/PreferencesPage.qml:53-81",
  "adb: listLaunchPoints (System Monitor on both)"
 ],
 "review": []
}
---

System Monitor shows how busy your device is. Use it if your device feels slow or the battery runs down quickly.

1. **[Open](/basics/open-an-application-in-the-launcher) System Monitor**.
2. Scroll through **CPU**, **Memory**, **System**, **Network**, **Storage**, **Battery** and **Temperatures**.

**See what is running**

1. Tap **Processes**. The list is sorted by **CPU**; tap **Memory**, **Name** or **PID** to sort another way.
2. To find something, type in the search box.
3. Tap a process to see its details.

**Change how often it updates**

1. **[Menu](/basics/open-the-application-menu)** (upper left) > **Preferences**.
2. Tap **Update every** and choose a time. To include parts of the system itself in the list of processes, turn on **Show kernel threads**.

System Monitor reads nothing while it is in the background.
