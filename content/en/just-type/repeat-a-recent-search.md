---
{
 "id": "just-type/repeat-a-recent-search",
 "title": "Repeat a recent search",
 "section": [],
 "order": 146,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/40186",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: com.palm.launcher pulled from both devices, identical",
  "app/HomeView.js:32,62-68 five, kept in memory",
  "app/JustType.js justTypeDeactivated"
 ]
}
---

1. [Display Card view](/basics/display-card-view-minimize-an-application) and tap the **Just type...** field.
2. Your last five searches appear under **Recent Searches**. Tap one to search for it again.

To remove a search from the list, tap the **X** next to it. The list is empty again after the shell restarts.
