---
{
 "id": "appearance/set-the-e-ink-refresh-speed",
 "title": "Set the E Ink refresh speed",
 "section": [],
 "order": 100205,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "org.webosports.app.settings@b5d8ff4:src/qml/General/DisplayPage.qml:237",
  "org.webosports.app.settings@b5d8ff4:src/qml/General/DisplayPage.qml:247",
  "org.webosports.app.settings@b5d8ff4:src/qml/General/DisplayPage.qml:265",
  "org.webosports.service.eink/src/main.c:128",
  "meta-smartphone/meta-minimal/conf/machine/mp01.conf"
 ]
}
---

These settings appear only on a device with an E Ink screen.

1. **[Open](/basics/open-an-application-in-the-launcher) Display**.
2. Under **E Ink**, tap **Refresh Speed** > tap one of the following:

   - **Slow:** Full greyscale, best for images. This is the slowest.
   - **Balanced:** Greyscale, with clearer text and less ghosting than **Slow**.
   - **Auto:** **Slow** while the screen is still, **Ultra** while it is moving.
   - **Text:** Nearly black and white. Text is crisp, and images lose their greys.
   - **Ultra:** The fastest refresh, with the most ghosting. This is best for scrolling and video.

To clear the ghosting left behind by earlier screens, tap **Refresh Screen Now**.
