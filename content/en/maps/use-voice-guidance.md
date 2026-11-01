---
{
 "id": "maps/use-voice-guidance",
 "title": "Use voice guidance",
 "section": [],
 "order": 100001,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "org.webosports.app.maps/source/data/Pullout.js:699",
  "org.webosports.app.maps/source/views/main.js:1601",
  "org.webosports.app.maps/source/data/Guidance.js:176",
  "org.webosports.app.maps/source/views/main.js:1641",
  "/usr/palm/applications/org.webosports.app.maps/build/app.js contains 'Start voice guidance'",
  "/usr/palm/applications/org.webosports.app.maps/build/app.js contains 'Stop voice guidance'"
 ],
 "review": []
}
---

1. Get a route ([learn how](/maps/get-directions)). Your location must be on ([learn how](/location-services/turn-location-service-providers-on-off)).
2. Tap the handle at the lower left of the screen to open the panel, and tap Directions.
3. Tap **Start voice guidance**.

Maps follows your position and says what comes next. If you leave the route, it finds a new one. The screen stays on.

To stop, open the panel and tap **Stop voice guidance**.

If your device has no speech voice, you see the instructions but hear nothing.
