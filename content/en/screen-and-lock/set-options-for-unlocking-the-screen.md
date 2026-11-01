---
{
 "id": "screen-and-lock/set-options-for-unlocking-the-screen",
 "title": "Set options for unlocking the screen",
 "section": [],
 "order": 353,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/17879",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/ScreenLockPage.qml:109",
  "adb: settings-common/qml/General/ScreenLockPage.qml:211",
  "adb: settings-common/qml/General/ScreenLockPage.qml:253",
  "adb: settings-common/qml/General/ScreenLockPage.qml:104",
  "adb: settings-common/qml/General/PasscodePopup.qml:72",
  "adb: /usr/lib/qml/WebOSCompositor/qml/LockScreen/Lockout.js",
  "lockTimeout read only by libLunaSysMgrCommon, not by LunaDisplayManager or the shell"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Screen & Lock**.
2. Under **Secure Unlock**, tap **Unlock with** > tap one of the following:

   **Pattern:** Draw a pattern, then draw it again to confirm.

   **Simple PIN:** Enter a four-digit PIN > enter it again > **Save**. Easily guessed PINs, such as 1234, may be refused.

   **Password:** Enter a password > enter it again > **Save**.
3. Tap **Lock After** to choose when the screen locks: **Screen turns off**, or a time from **30 seconds** to **30 minutes**.

If your device has a fingerprint sensor or Face Unlock, you can also [unlock with your fingerprint](/security/set-up-fingerprint-unlock) or [your face](/security/set-up-face-unlock).

To turn Secure Unlock off: Tap **Unlock with** > **Off** > enter your current pattern, PIN, or password.

Keep your PIN or password somewhere safe. After five wrong tries in a row, you have to wait before you can try again, and the wait gets longer with each further wrong try.
