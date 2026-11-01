---
{
 "id": "calendar/create-an-event",
 "title": "Create an event",
 "section": [],
 "order": 236,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42237",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.calendar/app/CalendarView.js:54",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/DetailView.js:87",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/EditView.js:215",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/day/DayEventGroup.js:77",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/EditView.js:128",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/EditView.js:130",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/EditView.js:138",
  "adb: /usr/palm/applications/com.palm.app.calendar/appinfo.json:16",
  "adb: /usr/palm/applications/com.palm.launcher/app/JustType.js:26",
  "adb: /usr/palm/applications/com.palm.launcher/app/Actions.js:35",
  "adb: /usr/palm/applications/com.palm.launcher/app/Actions.js:72",
  "adb: luna-send -n 1 luna://com.palm.universalsearch/getUniversalSearchList '{}'"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Calendar**.
2. Tap **New event**. Or, in Day view, go to the day you want ([**learn how**](/calendar/move-around-in-calendar)) and tap a blank time slot.
3. Tap **Event Name** > enter the event name.
4. Tap the calendar name below **Event Location** > tap the calendar you want to use for this event.

   If a calendar doesn't appear in the list, you can't add events to it from your device.
5. Under **From** and **To**, tap the start and finish dates and times for the event.
6. Tap **Done**.

To use Just Type to create an event: In Card view, tap **Just type...** > start typing the event text. Under **Quick Actions**, tap **New Event** (tap **More...** if you don't see it). Calendar opens at a new event, with the text you entered in the event name.

If you add an event to one of your online calendars, the event is also synchronized to your provider's server. If you add the event to your LuneOS calendar, it stays on your device.
