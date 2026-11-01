---
{
 "id": "security/use-hardware-privacy-switches",
 "title": "Use hardware privacy switches",
 "section": [
  "Protect your data"
 ],
 "order": 100305,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "luna-next-cardshell/qml/Connectors/KillSwitchService.qml",
  "luna-next-cardshell/qml/StatusBar/Indicators/KillSwitchIndicator.qml",
  "luna-next-cardshell/qml/StatusBar/SystemIndicators.qml:112",
  "luna-next-cardshell/qml/Notifications/KillSwitchAlert.qml",
  "meta-smartphone/meta-furilabs/conf/machine/radon.conf killswitch",
  "adb MindPhone: org.webosports.service.killswitch not on this device"
 ]
}
---

Only some devices have hardware privacy switches. They physically turn off parts of the device, such as the camera, microphone, or mobile network. Which switches there are depends on your device.

When you move a switch, a picture of the hardware appears briefly in the middle of the screen. While a switch has something turned off, its icon stays in the status bar.

Some switches can't be read by LuneOS. If so, you see no picture and no icon, but the switch still works.
