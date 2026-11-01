---
{
 "id": "security/see-what-an-application-may-use",
 "title": "See what an application may use",
 "section": [
  "Protect your data"
 ],
 "order": 100304,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/ApplicationsPage.qml:156",
  "adb: settings-common/qml/General/ApplicationsPage.qml:270",
  "adb: settings-common/qml/General/ApplicationsPage.qml:294",
  "adb: settings-common/qml/General/ApplicationsPage.qml:305"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Applications**.
2. Tap an application. **May use** lists what it is allowed to do.

To include the parts of the system, turn on **Show System Apps**.

You can't change this list. To stop an application from using something, remove the application ([learn how](/software-manager/manage-downloaded-applications)).

Web applications ask before they use your location or show notifications. To change your answer, see [Manage location information passed to applications](/location-services/manage-location-information-passed-to-applications) and [Manage notifications from web applications](/notifications/manage-notifications-from-web-apps).
