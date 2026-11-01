---
{
 "id": "clock/see-your-next-alarm-in-the-notification-area",
 "title": "See your next alarm in the notification area",
 "section": [],
 "order": 293.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/com.palm.app.clock/utility/dashboardmanager.js (MindPhone: one item; shown only while Clock is not in front)",
  "/usr/palm/applications/com.palm.app.clock/utility/alarmdashstate.js (MindPhone: texts; badge count)",
  "/usr/palm/applications/com.palm.app.clock/alarmDashboard/alarmDashboard.js (MindPhone: icon and text taps)",
  "TouchPad build: utility/dashboardmanager.js pushes one layer per enabled alarm; no Snoozed text in build.js; messageTap handler not defined"
 ],
 "review": []
}
---

The way alarms appear in the notification area isn't the same on every device.

While an alarm is on and Clock isn't the app in front, a notification shows your alarms.

On some devices, you see one notification with the next alarm to ring and the day it rings. If more than one alarm is on, a number on the icon shows how many. If an alarm is snoozed, the notification counts down, for example "Snoozed for 9 more minutes".

- To open that alarm: Tap the notification text.
- To see all your alarms: Tap the notification icon.
- To clear the notification: Throw it off the side of the screen. It comes back after you've been in Clock, or when an alarm rings or changes.

On other devices, each alarm that's on has its own notification.

See Also [**Set an alarm**](/clock/set-an-alarm)
