---
{
 "id": "web/search-for-a-website",
 "title": "Search for a website",
 "section": [],
 "order": 364,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/7239",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.atlas/source/URLSearch.js:82",
  "/usr/palm/applications/org.webosports.app.atlas/source/URLSearch.js:86",
  "adb: luna-send -n 1 luna://com.palm.universalsearch/getAllSearchPreference {} (defaultSearchEngine google)"
 ]
}
---

Do one of the following:

- **[Open](/basics/open-an-application-in-the-launcher) Atlas Web** > tap the address bar > enter the search term > press Enter or tap a search option.
- Tap **Just type...**, type the search term > tap a search engine.

Atlas Web searches with Google unless you changed **Default Web Search Engine** in Preferences ([learn how](/web/customize-web-browser-settings)).
