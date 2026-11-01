---
{
 "id": "location-services/manage-location-information-passed-to-applications",
 "title": "Manage location information passed to applications",
 "section": [],
 "order": 378,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42732",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.settings.location/qml/General/LocationPage.qml:293",
  "/usr/palm/applications/org.webosports.app.settings.location/qml/General/LocationPage.qml:318",
  "/usr/palm/applications/org.webosports.app.settings.location/qml/General/LocationPage.qml:332",
  "/usr/palm/applications/org.webosports.app.settings.location/qml/General/LocationPage.qml:361",
  "/usr/palm/applications/org.webosports.app.settings.location/qml/General/LocationPage.qml:276"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Location Services**.
2. Under **For Applications**, turn **Location** on or off.

   When it is on, applications are asked before they can use your location. When it is off, they cannot use it.
3. Under **Application Access**, change the answer for an application. The list shows the ones that have asked. Your answers are kept while **Location** is off.

{if:camera}**Geotag Photos:** Turn this on to store your location in the photos you take. It appears only while **Location** under For Applications is on.

To have every application asked again next time, tap **Clear My Location Data** > **Clear**.

Applications that use the location service directly do not appear in the list. Their access was set when they were installed.
