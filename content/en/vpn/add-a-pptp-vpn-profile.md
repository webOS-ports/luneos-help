---
{
 "id": "vpn/add-a-pptp-vpn-profile",
 "title": "Add a PPTP VPN profile",
 "section": [],
 "order": 405.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: /usr/share/luneos-vpn-adapter/formfields/pptp.json",
  "adb: getAgents lists PPTP on MindPhone only; absent on TouchPad"
 ]
}
---

**PPTP** is not available on every device. If it isn't listed in step 2, your device doesn't offer it.

PPTP encryption is broken and can be decrypted by an attacker. Use WireGuard or OpenVPN if your network offers them.

1. **[Open](/basics/open-an-application-in-the-launcher) VPN** > **Add profile manually...**.
2. Tap **Connection type** > **PPTP**.
3. Enter a **Profile name** and the **VPN server**.
4. Enter the **User name** and **Password**.
5. Change these settings only if you were told to: **Require MPPE 128-bit**, **Refuse EAP**, and **LCP echo interval (s)**.
6. Tap **Save**.
