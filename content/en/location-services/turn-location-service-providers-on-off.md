---
{
 "id": "location-services/turn-location-service-providers-on-off",
 "title": "Turn location service providers on/off",
 "section": [],
 "order": 380,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/21467",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.settings.location/qml/General/LocationPage.qml:400",
  "/usr/palm/applications/org.webosports.app.settings.location/qml/General/LocationPage.qml:425",
  "/usr/palm/applications/org.webosports.app.settings.location/qml/General/LocationPage.qml:447",
  "/usr/palm/applications/org.webosports.app.settings.location/qml/General/LocationPage.qml:194",
  "adb: luna-send -n 1 -f luna://com.webos.service.location/getAllLocationHandlers {}"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Location Services**.
2. Under **Locate Me Using**, turn on or off:

   **GPS:** Accurate outdoors, but uses more battery.

   **Network Location:** Works indoors and is quicker, but is only as precise as the nearby cell towers and Wi-Fi access points allow.
3. (Optional) Under **Network Lookup**, choose what Network Location asks: **beaconDB**, an open database, or **Google**, which needs a key installed on the device.

You can turn on both. To check that it works, turn on **Show My Location** under **GPS Status**. Your position appears when the device has a fix.
