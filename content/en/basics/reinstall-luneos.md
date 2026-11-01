---
{
 "id": "basics/reinstall-luneos",
 "title": "Reinstall LuneOS",
 "section": [
  "Reinstall LuneOS"
 ],
 "order": 66,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "curl 2026-11-01: https://webos-ports.org/ 200; https://wiki.webos-ports.org/wiki/Devices 200; https://github.com/webOS-ports/luneos-testing/releases 200",
  "webOS-ports.github.io/index.html #devices: \"Test images for every device are published together in the luneos-testing releases. Flashing replaces the operating system on the phone, so read the device page on the wiki first.\"",
  "adb: com.palm.app.backup source/BackupInfo.js:10 backups copied off over USB"
 ]
}
---

Reinstalling (flashing) replaces the operating system on your device. You do it from a computer, and the steps are different for each device. Your information may be erased, so try [restarting your device](/basics/2-turn-your-device-completely-off-and-on) first.

To get a newer version of LuneOS without reinstalling, see [Update LuneOS to a newer version](/system-updates/update-luneos-to-a-newer-version).

1. [Make a backup](/backup/manually-back-up-information-to-your-luneos-account), and [copy the **webos-backups** folder to your computer](/basics/copy-files-between-your-device-and-your-computer).
2. On your computer, go to [webos-ports.org](https://webos-ports.org/) and check that your device is listed under **Devices**.
3. Find your device's page on the [LuneOS wiki](https://wiki.webos-ports.org/wiki/Devices), and read it.
4. Download the image for your device. Test images for every device are on the [luneos-testing releases](https://github.com/webOS-ports/luneos-testing/releases) page.
5. Flash the image, following the steps on your device's page.

To get your information back afterwards, see [Move your information to another device](/basics/move-your-information-to-another-device).
