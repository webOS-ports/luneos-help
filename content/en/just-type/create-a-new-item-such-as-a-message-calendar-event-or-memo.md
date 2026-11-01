---
{
 "id": "just-type/create-a-new-item-such-as-a-message-calendar-event-or-memo",
 "title": "Create a new item such as a message, calendar event, or memo",
 "section": [],
 "order": 463,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/40171",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: com.palm.launcher pulled from both devices, identical",
  "app/Actions.js:30,70-76,88",
  "adb: luna-send com.palm.universalsearch/getUniversalSearchList ActionList"
 ]
}
---

1. [Display Card view](/basics/display-card-view-minimize-an-application) and tap the **Just type...** field.
2. Type the text of the item, such as the text of a message or memo.
3. To see only actions, tap the **Actions** tab.
4. Under **Quick Actions**, tap the item you want. The application opens with your text in a new item.
   - **New Email**
   - **New Memo**
   - **New Message**
   - **New Task**
   - **New Event**

   Tap **More...** if you don't see the item you want.

To choose which items appear, see [Customize Just Type](/just-type/customize-just-type).
