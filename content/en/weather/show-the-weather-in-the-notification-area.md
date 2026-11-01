---
{
 "id": "weather/show-the-weather-in-the-notification-area",
 "title": "Show the weather in the notification area",
 "section": [],
 "order": 100014,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "~/Documents/GitHub/org.webosports.app.weather/source/App.js:191-197 (Widget, Off, Compact, Hourly)",
  "~/Documents/GitHub/org.webosports.app.weather/source/App.js:254-300 (widget opens as a dashboard, reopens when the app starts)",
  "~/Documents/GitHub/org.webosports.app.weather/source/Widget.js:22-52,133-170 (tap, icon refresh, 30 min)",
  "strings checked in /usr/palm/applications/org.webosports.app.weather/build/app.js, identical on both devices",
  "Widget not opened on a device: forbidden to launch"
 ],
 "review": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Weather**. Swipe left until you see **Menu**.
2. Under **Settings**, tap the current setting next to **Widget** > **Compact** or **Hourly**.

   **Compact** shows the temperature, place, conditions, and today's high and low. **Hourly** also shows the next six hours.

- To open Weather: Tap the widget.
- To update the forecast: Tap the icon in the widget.

To remove the widget, set **Widget** to **Off**.

If the widget is gone, for example after you restart your device, open Weather and it comes back.
