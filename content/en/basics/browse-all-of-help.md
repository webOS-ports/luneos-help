---
{
 "id": "basics/browse-all-of-help",
 "title": "Get help",
 "section": [
  "Get help"
 ],
 "order": 68,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27787",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "tools/build.py:279 search field, :48 device bar",
  "adb: /usr/palm/applications has no com.palm.app.help; org.webosports.app.settings.help is the example page qml/General/HelpPage.qml:27-32",
  "adb: com.palm.app.accounts, com.palm.app.clock have HelpMenu; enyo HelpMenu targets com.palm.app.help, not installed (docs/audit/shell.md)"
 ]
}
---

LuneOS has no Help application. Help is a website, **help.luneos.org**, so you need an internet connection to read it. Open it in Atlas Web, or in a browser on your computer.

- Type in the **Just type...** field to search all of Help.
- Tap a topic to see its articles.
- Pick your kind of device at the top of the page, so that you only see steps that apply to it.

If an application's menu has a **Help** item, it doesn't open anything. Use the website instead.

For more ways to get help, see [Support site](/basics/support-site).
