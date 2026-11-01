---
{
 "id": "calendar/view-meeting-participants",
 "title": "View meeting participants",
 "section": [],
 "order": 248,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26275",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/DetailView.js:74",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/DetailView.js:362",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/AttendeesView.js:49",
  "adb: /usr/palm/applications/com.palm.app.calendar/app/edit/ContactView.js:43",
  "adb: grep -i attendee /usr/palm/services/org.webosports.service.cdav/javascript/assistants/syncassistant.js"
 ]
}
---

If an event has attendees, you can view them.

1. Tap the event name. The event details show the organizer and the number of attendees.
2. Tap that line to see the attendees' names.
3. (Optional) Tap a name to see the contact details.
4. (Optional) Tap **Contact Attendees** to send an email to all attendees.
