---
{
 "id": "calendar/enter-the-event-location",
 "title": "Enter the event location",
 "section": [],
 "order": 237,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26071",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.calendar/app/CalendarView.js:54",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/DetailView.js:87",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/EditView.js:215",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/EditView.js:129",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/DetailView.js:321",
  "adb: luna-send -n 1 luna://com.webos.service.applicationManager/getAppInfo '{\"id\":\"com.palm.app.maps\"}'"
 ]
}
---

1. To create a new event, tap **New event**. To change an event you already created, tap the event name > **Edit**.
2. Tap **Event Location** > enter the location > **Done**.

The location appears in the event details.
