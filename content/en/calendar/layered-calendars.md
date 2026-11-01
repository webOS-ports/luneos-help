---
{
 "id": "calendar/layered-calendars",
 "title": "Layered calendars",
 "section": [],
 "order": 233,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26113",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.calendar/app/shared/CalendarsManager.js:284",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/header/CalendarList.js:43",
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates '{}'"
 ]
}
---

Suppose you use a calendar in both Google and iCloud. Your device's Calendar app shows the events from both in a single view: a layered calendar with events that are color-coded to identify which calendar they come from.

Individual events are stored separately with your different providers. The events are just assembled in one view on your device for your convenience.

If you change an event, the change is made in the appropriate calendar.

You can also look at the events of just one calendar at a time ([**learn how**](/calendar/change-the-calendar-display)).
