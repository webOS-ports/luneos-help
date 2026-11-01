---
{
 "id": "vpn/import-a-vpn-profile",
 "title": "Import a VPN profile",
 "section": [],
 "order": 404.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/VPNPage.qml:226",
  "adb: settings-common/qml/Connectivity/VpnImportProfilePopup.qml:45",
  "adb: settings-common/qml/Common/FilePickerPopup.qml:69",
  "adb: luna-send com.webos.service.vpn/getAgents supportsImport"
 ]
}
---

If you received your VPN settings as a file, you can import it instead of entering every setting yourself.

You can import these file types:

- **WireGuard config** (.conf)
- **OpenVPN config** (.ovpn)
- **ConnMan config** (.config)

1. Copy the file to the **downloads** folder on your device ([learn how](/basics/copy-files-between-your-device-and-your-computer)). Don't put it in a folder inside **downloads**.
2. **[Open](/basics/open-an-application-in-the-launcher) VPN** > **Import profile...**.
3. Tap **File type** and tap the type of your file.
4. Enter a **Profile name**.
5. Tap **Choose file...** > tap the file.
6. Tap **Import**.

The profile appears under **Choose a Profile**. To use it, see [Connect to a profile](/vpn/connect-to-a-profile).

A profile imported from a ConnMan config can't be edited. It has no **Edit** button.
