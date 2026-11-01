---
{
 "id": "just-type/customize-just-type",
 "title": "Customize Just Type",
 "section": [],
 "order": 147,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/21695",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: com.palm.launcher pulled from both devices, identical",
  "adb: org.webosports.app.settings-common qml/General/SearchPreferencesPage.qml",
  "adb: luna-send getAllSearchPreference, getUniversalSearchList on both devices",
  "app/JustType.js:60-63 Preferences"
 ]
}
---

1. [Open](/basics/open-an-application-in-the-launcher) **Just Type** on the **Prefs** tab. If Just Type is already open, you can also tap **Just Type** in the upper-left corner of the screen, and then **Preferences**.
2. Change any of the following:

   **Search Results:** Turn **Applications** and **Contacts** on or off. If you have an account with a global address list, **Automatic Global Address Lookup** appears here too.

   **Default Search Engine:** **Search the Web** turns the web search row on or off. Tap **Engine** to pick a different search engine.

   **Content:** What Just Type looks for in your applications: **Calendar Events**, **Email**, **Bookmarks & History** and **Songs**.

   **Search Using:** Other search engines. **Wikipedia** and **DuckDuckGo** are on to start with, and **CNN**, **Amazon** and **IMDb** are off.

   **Actions:** The Quick Actions, such as **New Memo**.

   In these last three, **All** turns the whole group on or off. The checkboxes change one item at a time.
