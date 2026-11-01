---
{
 "id": "utilities/test-your-sensors-with-messwerk",
 "title": "Test your sensors with Messwerk",
 "section": [],
 "order": 100111,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.messwerk/qml/pages/*.qml (Accelerometer, Gyroscope, Light & Proximity, Magnetometer, Position, Pressure, Rotation, GNSS Satellites)",
  "/usr/palm/applications/org.webosports.app.messwerk/qml/Common/LoggingGroup.qml (Logging)",
  "adb: listLaunchPoints (Messwerk on both)"
 ],
 "review": []
}
---

Messwerk shows what the sensors in your device measure. It is handy for checking that a sensor works.

1. **[Open](/basics/open-an-application-in-the-launcher) Messwerk**.
2. Tap a sensor to see its readings: **Accelerometer**, **Gyroscope**, **Light & Proximity**, **Magnetometer**, **Position**, **Pressure**, **Rotation** or **GNSS Satellites**.

Your device does not have all of these sensors.
