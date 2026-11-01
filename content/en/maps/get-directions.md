---
{
 "id": "maps/get-directions",
 "title": "Get directions",
 "section": [],
 "order": 383,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/43655",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.maps/build/app.js contains 'Starting Location'",
  "/usr/palm/applications/org.webosports.app.maps/build/app.js contains 'Ending Location'",
  "/usr/palm/applications/org.webosports.app.maps/build/app.js contains 'Start voice guidance'",
  "/usr/palm/applications/org.webosports.app.maps/build/app.js contains 'Route from here'",
  "/usr/palm/applications/org.webosports.app.maps/build/app.js contains 'Add as stop'",
  "org.webosports.app.maps/source/engines/OsmEngine.js:20 (travelModes DRIVING, WALKING, BICYCLING)"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Maps**.
2. Tap the Directions button at the top right of the screen.
3. **Starting Location** is filled in with My Location if your device knows where it is. To start elsewhere, enter a place.
4. Tap **Ending Location** and enter your destination.

   To use a saved place, tap the bookmark button beside the field and choose it from the panel. To swap the two, tap the Swap button.
5. Tap **Go**.
6. To change how you travel, open the panel at the lower left of the screen and tap Directions. Then tap car, walking or bicycle. With the Google Maps engine, public transport is there as well.

From the same panel you can read the route step by step and tap **Start voice guidance**.

You can also start from any place on the map: tap its marker, tap the box that appears, and tap **Route from here**, **Route to here** or **Add as stop**.

To use your own position, turn on a location service ([learn how](/location-services/turn-location-service-providers-on-off)). Maps needs an internet connection for routes.
