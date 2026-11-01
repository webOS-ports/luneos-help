---
{
 "id": "security/set-up-fingerprint-unlock",
 "title": "Set up fingerprint unlock",
 "section": [
  "Unlock your device"
 ],
 "order": 100301,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "org.webosports.app.settings@b5d8ff4:src/qml/General/FingerprintPage.qml:293",
  "org.webosports.app.settings@b5d8ff4:src/qml/General/FingerprintPage.qml:337",
  "org.webosports.app.settings@b5d8ff4:src/qml/General/ScreenLockPage.qml:290",
  "luna-next-cardshell/qml/LockScreen/LockScreen.qml:61",
  "luna-next-cardshell/qml/LockScreen/PadLock.qml:72",
  "meta-luneos/.../org.webosports.app.settings-qml.bb REMOVE_FINGERPRINT_APP_CMD",
  "adb: org.webosports.app.settings.fingerprint absent on both devices"
 ]
}
---

Fingerprint isn't installed on every device. If there's no **Fingerprint** app, your device doesn't offer it.

**Add a fingerprint**

1. Set a pattern, PIN, or password first ([learn how](/screen-and-lock/set-options-for-unlocking-the-screen)).
2. **[Open](/basics/open-an-application-in-the-launcher) Fingerprint**.
3. Under **Add a fingerprint**, enter a name for the finger, or leave it empty to use the suggested name.
4. Tap **Add** and enter your pattern, PIN, or password.
5. Touch the sensor repeatedly, moving your finger slightly between touches, until you see **Fingerprint added.**

**Turn it on or off**

**[Open](/basics/open-an-application-in-the-launcher) Screen & Lock** > under **Fingerprint Unlock**, turn **Unlock with Fingerprint** on or off. Your fingerprints stay stored when it's off.

**Rename or delete a fingerprint**

In the **Fingerprint** app, under **Fingerprints**:

- To rename a fingerprint: Tap its name and type a new one.
- To delete a fingerprint: Swipe it sideways > **Delete**.

After five failed tries, you must use your pattern, PIN, or password to unlock.
