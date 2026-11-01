---
{
 "id": "network/use-nfc-tags",
 "title": "Use NFC tags",
 "section": [
  "NFC"
 ],
 "order": 100010,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:259",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:322",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/NfcPage.qml:358",
  "luna-next-cardshell/qml/NFC/NfcAutoDispatch.qml",
  "luna-next-cardshell/qml/NFC/NfcGlow.qml",
  "adb: org.webosports.app.settings.nfc absent on both devices"
 ]
}
---

NFC isn't installed on every device. If there's no **NFC** app, your device doesn't offer it.

1. **[Open](/basics/open-an-application-in-the-launcher) NFC**.
2. Tap the switch at the top of the screen to turn NFC on.
3. Hold a tag against the back of your device.

From any screen, your device acts on a tag as soon as it reads it:

- A web link opens in the web browser.
- A phone number opens the Phone app.
- An email address opens a new email.
- A location opens the web browser.

To see what's on a tag, hold it against your device with the **NFC** app open. The **Tag** group shows its **Technology**, **Protocol**, **UID**, and what it contains.
