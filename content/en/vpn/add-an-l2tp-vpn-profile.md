---
{
 "id": "vpn/add-an-l2tp-vpn-profile",
 "title": "Add an L2TP/IPsec VPN profile",
 "section": [],
 "order": 404.8,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/VpnProfilePopup.qml:214",
  "adb: /usr/share/luneos-vpn-adapter/formfields/l2tp.json",
  "adb: no ipsec binary on either device; /usr/sbin/xl2tpd and /usr/sbin/pppd present"
 ]
}
---

The form has no field for an IPsec pre-shared key. If your VPN needs one, this profile may not connect.

Get this info from your system administrator:

- VPN server
- User name and password

1. **[Open](/basics/open-an-application-in-the-launcher) VPN** > **Add profile manually...**.
2. Tap **Connection type** > **L2TP/IPsec**.
3. Enter a **Profile name** and the **VPN server**.
4. Enter the **User name** and **Password**.
5. Change these settings only if you were told to: **Use IPsec SA reference**, **UDP port**, **Use as default route**, **Require MPPE 128-bit**, **Refuse EAP**, **LCP echo interval (s)**, and **LCP echo failures**.
6. Tap **Save**.
