---
{
 "id": "vpn/add-a-vpnc-vpn-profile",
 "title": "Add a Cisco IPsec VPN profile",
 "section": [],
 "order": 405,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/9179",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/VPNPage.qml:235",
  "adb MindPhone: /usr/share/luneos-vpn-adapter/formfields/vpnc.json",
  "adb: getAgents lists Cisco IPsec on MindPhone only; /usr/lib/connman/plugins-vpn has no vpnc.so on TouchPad"
 ]
}
---

**Cisco IPsec** is not available on every device. If it isn't listed in step 2, your device doesn't offer it.

Get this info from your system administrator:

- VPN server
- User name and password
- Group name and group password
- Domain
- Encryption method: **Secure**, **Single DES**, or **No encryption**
- NAT traversal method: **NAT-T (auto-detect)**, **Cisco-UDP**, **NAT-T (always)**, or **Disabled**

1. **[Open](/basics/open-an-application-in-the-launcher) VPN** > **Add profile manually...**.
2. Tap **Connection type** > **Cisco IPsec**.
3. Enter a **Profile name** and the **VPN server**.
4. Enter the other information you got from your system administrator. Fields marked with **\*** are required.
5. Tap **Save**.
