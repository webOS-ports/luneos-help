---
{
 "id": "authenticator/lock-authenticator",
 "title": "Lock Authenticator",
 "section": [],
 "order": 100007,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.authenticator/qml/main.qml:152-187,292-304 (menu items, toggles, face warning)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/main.qml:74 (relock after 60 s in the background)",
  "/usr/palm/applications/org.webosports.app.authenticator/qml/LockScreen.qml:84,99,123,210,311 (labels)",
  "~/Documents/GitHub/org.webosports.app.authenticator/README.md (lock rules)",
  "No fingerprint or face enrolment could be tried from here"
 ],
 "review": []
}
---

Anyone holding your unlocked device could otherwise see and copy your codes. With the lock on, Authenticator asks for your fingerprint or screen lock passcode when you open it, and again after it's been in the background for a minute.

**Before You Begin**

Set a screen lock passcode ([**learn how**](/screen-and-lock/set-options-for-unlocking-the-screen)). Authenticator uses the same PIN, password, or pattern.

1. **[Open](/basics/open-an-application-in-the-launcher) Authenticator** > **[Menu](/basics/open-the-application-menu)** > **Lock with fingerprint or passcode**.
2. To open the app from then on, touch the fingerprint sensor if your device has one and a fingerprint is enrolled, or enter your passcode and tap **Unlock**.

To turn the lock off: **[Menu](/basics/open-the-application-menu)** > **Stop locking the app**.

If you have a face enrolled on your device, you can also tap **[Menu](/basics/open-the-application-menu)** > **Also open with a face**. A face is weaker than the passcode: someone who looks like you, or a good photo of you, can sometimes pass.

After too many wrong tries, you must wait before you try again. These tries count together with those on your lock screen.
