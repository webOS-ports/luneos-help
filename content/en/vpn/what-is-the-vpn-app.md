---
{
 "id": "vpn/what-is-the-vpn-app",
 "title": "What is the VPN app?",
 "section": [],
 "order": 404,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/10577",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/VPNPage.qml:244",
  "adb: luna-send luna://com.webos.service.vpn/getAgents (both devices)"
 ]
}
---

If you want to reach files on your company's servers, you may need a VPN (virtual private network). A VPN lets you log in to a private network through its firewall, for example from a public location or from home. Check with your system administrator whether you need one.

The **VPN** app stores your VPN connections as profiles. You can [import a profile](/vpn/import-a-vpn-profile) from a file or add one manually.

The connection types include **WireGuard**, **OpenVPN**, **OpenConnect (AnyConnect)**, and **L2TP/IPsec**. Some devices also offer others, such as **Cisco IPsec** and **PPTP**.
