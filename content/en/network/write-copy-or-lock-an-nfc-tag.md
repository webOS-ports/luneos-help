---
{
 "id": "network/write-copy-or-lock-an-nfc-tag",
 "title": "Write, copy, or lock an NFC tag",
 "section": [
  "NFC"
 ],
 "order": 100011,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:443",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:474",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:491",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:529",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:543"
 ]
}
---

NFC isn't installed on every device. If there's no **NFC** app, your device doesn't offer it.

Only Type 2 tags can be written or copied.

**Write a tag**

1. **[Open](/basics/open-an-application-in-the-launcher) NFC**. Make sure NFC is on.
2. Under **Write a tag**, choose **Link** or **Text** and enter what to write.
3. Hold a writable tag against your device and tap **Write**.

**Copy a tag**

1. Under **Copy a tag**, hold the tag you want to copy against your device.
2. Tap **Copy this tag**.
3. Remove the tag and hold a blank tag against your device.

**Lock a tag**

Locking is permanent. The tag can never be written to again.

1. Hold the tag against your device.
2. Under **Lock a tag**, tap **Lock tag** > **Confirm lock**.
