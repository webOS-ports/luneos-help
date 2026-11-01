---
{
 "id": "clock/change-the-alarm-volume",
 "title": "Change the alarm volume",
 "section": [],
 "order": 295,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/25579",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "~/Documents/GitHub/org.webosports.app.settings/src/qml/General/SoundsAndAlertsPage.qml:51 (ringtone volume only remembered)",
  "~/Documents/GitHub/audiod-pro-ports/src/modules/palmLegacyManager/palmLegacyManager.cpp:48 (no /alarm category)",
  "adb: /usr/palm/applications/com.palm.app.clock/utility/audiomanager.js:46",
  "adb: luna-send -n 1 luna://com.webos.service.audio/master/getVolume '{}'"
 ]
}
---

Alarms have no volume setting of their own. They play at the device volume.

1. Open **Sounds & Ringtones** (**[learn how](/basics/open-an-application-in-the-launcher)**).
2. Drag the **Volume** slider.

{if:volumebutton}You can also press the volume buttons.
