---
{
 "id": "print-manager/cancel-printing",
 "title": "Cancel printing",
 "section": [],
 "order": 467,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/36749",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/PrintManagerPage.qml:168-235 (Print Queue, Cancel, Cancel All)",
  "adb: luna-send org.webosports.service.print/listJobs"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Print Manager**.
2. Do one of the following:
   - To cancel a single print job: Under **Print Queue**, tap **Cancel** beside the print job.
   - To cancel all your print jobs: Tap **Cancel All**.
