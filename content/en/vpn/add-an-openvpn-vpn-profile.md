---
{
 "id": "vpn/add-an-openvpn-vpn-profile",
 "title": "Add an OpenVPN VPN profile",
 "section": [],
 "order": 404.7,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/VpnProfilePopup.qml:214",
  "adb: /usr/share/luneos-vpn-adapter/formfields/openvpn.json",
  "adb: settings-common/qml/Common/VpnFormFieldsColumn.qml:72",
  "adb: settings-common/qml/Common/VpnFormFieldsColumn.qml:159"
 ]
}
---

If you have an OpenVPN file (.ovpn), [import it](/vpn/import-a-vpn-profile) instead. The **Config file** setting can only be filled in that way.

Get this info from your VPN provider or system administrator:

- VPN server
- CA certificate, client certificate and client key, as files
- Whether the server asks for a user name and password
- Protocol, port and any other settings that differ from the standard ones

1. Copy the certificate and key files to the **downloads** folder on your device ([learn how](/basics/copy-files-between-your-device-and-your-computer)).
2. **[Open](/basics/open-an-application-in-the-launcher) VPN** > **Add profile manually...**.
3. Tap **Connection type** > **OpenVPN**.
4. Enter a **Profile name** and the **VPN server**. Enter the name first, because the **Import...** buttons need it.
5. For **CA certificate**, **Client certificate**, and **Client key**, tap **Import...** > tap the file.
6. If the server asks for a user name and password, turn on **Username / password auth**. You are asked for them when you connect.
7. Change these settings only if you were told to: **Protocol**, **Port**, **Device type**, **Cipher**, **HMAC digest**, **Verify peer cert type**, **LZO compression**, **MTU**, and **Never cache credentials**.
8. Tap **Save**.
