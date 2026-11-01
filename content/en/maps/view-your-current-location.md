---
{
 "id": "maps/view-your-current-location",
 "title": "View your current location",
 "section": [],
 "order": 386,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/43978",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.maps/build/app.js contains 'Current location found'",
  "/usr/palm/applications/org.webosports.app.maps/build/app.js contains 'Location error: '",
  "org.webosports.app.maps/source/views/main.js:44,595,637 (myLocation button)",
  "adb: luna-send -n 1 -f luna://com.webos.service.location/getAllLocationHandlers {} (gps and network both off on both devices)"
 ]
}
---

Turn on a location service first ([learn how](/location-services/turn-location-service-providers-on-off)).

In Maps, tap the My Location button at the top right of the screen. It stays dim until your device knows where it is. The map then moves to your position and follows you. Tap the button again to stop following.

If your position cannot be found, Maps shows a **Location error** message.
