---
{
 "id": "security/set-up-face-unlock",
 "title": "Set up face unlock",
 "section": [
  "Unlock your device"
 ],
 "order": 100302,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "org.webosports.app.settings@b5d8ff4:src/qml/General/FaceUnlockPage.qml:294",
  "org.webosports.app.settings@b5d8ff4:src/qml/General/FaceUnlockPage.qml:311",
  "org.webosports.app.settings@b5d8ff4:src/qml/General/FaceUnlockPage.qml:416",
  "org.webosports.app.settings@b5d8ff4:src/qml/General/ScreenLockPage.qml:349",
  "luna-next-cardshell/qml/LockScreen/LockScreen.qml:173",
  "meta-luneos/.../org.webosports.app.settings-qml.bb REMOVE_FACEUNLOCK_APP_CMD",
  "meta-smartphone/meta-android/conf/machine/halium-arm64.conf faceunlock",
  "adb: org.webosports.app.settings.faceunlock absent on both devices"
 ],
 "requires": [
  "camera"
 ]
}
---

Face Unlock isn't installed on every device. If there's no **Face Unlock** app, your device doesn't offer it.

Face unlock is less secure than your PIN or password. Someone who looks a lot like you may be able to unlock your phone, and a detailed photo or replica can sometimes fool it. It also needs reasonable light. Use it for convenience, not to protect anything sensitive.

**Set up your face**

1. Set a pattern, PIN, or password first ([learn how](/screen-and-lock/set-options-for-unlocking-the-screen)).
2. **[Open](/basics/open-an-application-in-the-launcher) Face Unlock** > **Set up**.
3. Enter your pattern, PIN, or password.
4. Hold the phone at arm's length, look at the screen, and keep still until you see **Face saved.**

Your device stores one face. To replace it, tap **Set up again**. To delete it, tap **Remove**.

**Turn it on or off**

**[Open](/basics/open-an-application-in-the-launcher) Screen & Lock** > under **Face Unlock**, turn **Unlock with Face** on or off.

Face unlock works only while the screen is on. After five failed tries, you must use your pattern, PIN, or password to unlock.
