---
{
 "id": "device-info/view-system-information",
 "title": "View system information",
 "section": [],
 "order": 426,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/23239",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/DeviceInfoPage.qml:91-191 (rows; Android rows only on Halium)",
  "adb: luna-send org.webosports.service.update/retrieveVersion",
  "adb: appinfo.json of org.webosports.app.settings.deviceinfo"
 ]
}
---

**[Open](/basics/open-an-application-in-the-launcher) Device Info**.

Under **Device**, you see the device name, serial number, and Wi-Fi MAC address. Under **Software**, you see the LuneOS version, codename, build tree, build number, and kernel version. On devices that run LuneOS on top of Android drivers, you also see the Android version and Android vendor version.
