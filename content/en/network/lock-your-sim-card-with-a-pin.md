---
{
 "id": "network/lock-your-sim-card-with-a-pin",
 "title": "Lock your SIM card with a PIN",
 "section": [
  "Mobile network"
 ],
 "order": 100004,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:267",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:322",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:337",
  "adb MindPhone: settings-common/qml/Connectivity/NetworkSettingsPage.qml:739"
 ],
 "requires": [
  "modem"
 ]
}
---

**Turn the SIM PIN on or off**

1. **[Open](/basics/open-an-application-in-the-launcher) Network Settings**.
2. Under **SIM PIN**, if your device has two SIMs, tap **SIM** and choose one.
3. Turn **Lock SIM with PIN** on or off.
4. Enter the **PIN** and tap **OK**.

**Change the PIN**

1. Under **SIM PIN**, tap **Change PIN...**. The PIN lock must be on.
2. Enter the **Current PIN** and the **New PIN**, and tap **OK**.

**Unblock a locked SIM**

If the PIN is entered wrongly too many times, the SIM is PUK-locked.

1. Under **SIM PIN**, tap **Unblock with PUK...**.
2. Enter the **PUK code** from your operator and a **New PIN**, and tap **OK**.
