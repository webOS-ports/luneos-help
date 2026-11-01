---
{
 "id": "just-type/search-the-web",
 "title": "Search the web",
 "section": [],
 "order": 142,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42450",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: com.palm.launcher pulled from both devices, identical",
  "app/LaunchAndSearch.js:45-65,185-191",
  "app/LaunchItems.js:Go to website",
  "adb: getUniversalSearchList has no Maps entry on either device, so the Maps step was removed",
  "data/AppLauncher.js launchBrowser org.webosports.app.atlas"
 ]
}
---

1. [Display Card view](/basics/display-card-view-minimize-an-application) and tap the **Just type...** field.
2. Type your search term or a website address.
3. To see only actions and searches, tap the **Actions** tab.
4. Do one of the following:
   - To search with your default search engine: Tap **Search Google**, or the name of the engine you picked.
   - To go to a website: Tap **Go to website**. This appears when you type a complete address.
   - To see suggested search terms: Tap **Suggest** next to the search engine, and then tap a suggestion. Not all search engines have this.
   - To use another search engine: Tap it under **Search Using...**. Tap **More...** if you don't see it. If it searches one website, such as Wikipedia, you search that site only.

Results open in Atlas Web. To change your search engines, see [Customize Just Type](/just-type/customize-just-type).
