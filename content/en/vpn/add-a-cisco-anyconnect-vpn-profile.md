---
{
 "id": "vpn/add-a-cisco-anyconnect-vpn-profile",
 "title": "Add an OpenConnect (AnyConnect) VPN profile",
 "section": [],
 "order": 406,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/9017",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/VPNPage.qml:235",
  "adb: settings-common/qml/Connectivity/VpnProfilePopup.qml:214",
  "adb: settings-common/qml/Common/VpnFormFieldsColumn.qml:159",
  "adb: /usr/share/luneos-vpn-adapter/formfields/openconnect.json",
  "adb: getAgents vpnAgentLabel OpenConnect (AnyConnect)"
 ]
}
---

Get this info from your system administrator:

- VPN server name
- How you log in, such as a username and password or a certificate

1. **[Open](/basics/open-an-application-in-the-launcher) VPN** > **Add profile manually...**.
2. Tap **Connection type** > **OpenConnect (AnyConnect)**.
3. Enter a **Profile name** and the **VPN server**.
4. Enter the other information you got from your system administrator. Fields marked with **\*** are required.

   If you need a certificate or key file, copy it to the downloads folder on your device first, then tap **Import...** beside the field.
5. Tap **Save**.
