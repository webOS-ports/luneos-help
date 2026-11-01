---
{
 "id": "vpn/add-a-wireguard-vpn-profile",
 "title": "Add a WireGuard VPN profile",
 "section": [],
 "order": 404.6,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/VpnProfilePopup.qml:214",
  "adb: /usr/share/luneos-vpn-adapter/formfields/wireguard.json",
  "adb TouchPad: zcat /proc/config.gz has no CONFIG_WIREGUARD, no /sys/module/wireguard",
  "adb MindPhone: /sys/module/wireguard present"
 ]
}
---

If you have a WireGuard file (.conf), it's easier to [import it](/vpn/import-a-vpn-profile).

Some devices can list WireGuard but can't connect with it. If a profile won't connect, your device may not support it.

Get this info from your VPN provider or system administrator:

- VPN server
- Private key
- Peer public key
- Address, for example 10.2.0.2/24

1. **[Open](/basics/open-an-application-in-the-launcher) VPN** > **Add profile manually...**.
2. Tap **Connection type** > **WireGuard**.
3. Enter a **Profile name** and the **VPN server**.
4. Enter the **Private key**, **Peer public key**, and **Address**.
5. If you were given them, enter any of the other settings:

   - **Preshared key**
   - **DNS servers**, separated by commas
   - **Allowed IPs**
   - **Endpoint port**
   - **Local listen port**
   - **Persistent keepalive (s)**
6. Tap **Save**.
