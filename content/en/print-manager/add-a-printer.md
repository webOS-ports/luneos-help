---
{
 "id": "print-manager/add-a-printer",
 "title": "Add a printer",
 "section": [],
 "order": 466,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/36311",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/PrintManagerPage.qml:287-319 (Add a Printer)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/PrintManagerPage.qml:335 (default printer)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/PrintManagerPage.qml:247 (Auto Discovered)",
  "adb: luna-send org.webosports.service.print/listPrinters (both devices; found a network printer)"
 ]
}
---

Your device finds printers on your network by itself and lists them under **Auto Discovered**. If yours is not listed, add it yourself:

1. **[Open](/basics/open-an-application-in-the-launcher) Print Manager**.
2. Under **Add a Printer**, tap **Name printer** and enter a name for the printer.
3. Tap **IP address or ipp:// address** and enter the printer's address.
4. Tap **Add Printer**.

To make a printer the default, tap it in the list.
