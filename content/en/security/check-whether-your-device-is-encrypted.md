---
{
 "id": "security/check-whether-your-device-is-encrypted",
 "title": "Check whether your device is encrypted",
 "section": [
  "Protect your data"
 ],
 "order": 100303,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/EncryptionPage.qml:135",
  "adb: settings-common/qml/General/EncryptionPage.qml:182",
  "adb: settings-common/qml/General/EncryptionPage.qml:199",
  "adb: luna-send com.palm.storage/volumes/getEncryptionStatus (both devices: encrypted false on every volume)"
 ]
}
---

**[Open](/basics/open-an-application-in-the-launcher) Encryption**. Under **Volumes**, each storage area shows **Not encrypted** or **Encrypted**.

If your device is not encrypted, anyone who can take the storage out can read what is on it, whatever screen lock you set.

You can't turn encryption on from this app. It has to be set up when the device is flashed.

A screen lock is a different thing: it keeps someone out of a device that is switched on. See [Set options for unlocking the screen](/screen-and-lock/set-options-for-unlocking-the-screen).
