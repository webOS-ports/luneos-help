---
{
 "id": "wi-fi/customize-wi-fi-connection-settings",
 "title": "Customize Wi-Fi connection settings",
 "section": [],
 "order": 396,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/4335",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/WiFiNetworkInfoPopup.qml:177",
  "adb: settings-common/qml/Connectivity/WiFiNetworkInfoPopup.qml:522",
  "adb: settings-common/qml/Connectivity/WiFiNetworkInfoPopup.qml:573",
  "adb: settings-common/qml/Connectivity/WiFiNetworkInfoPopup.qml:673",
  "adb TouchPad: WiFiNetworkInfoPopup.qml Private Wi-Fi address row"
 ]
}
---

You can customize a network that your device is connected to or has joined before.

1. **[Open](/basics/open-an-application-in-the-launcher) Wi-Fi** > touch and hold the network name.
2. Under **IP Address**, turn **Automatic IP settings** on or off.

   When it is on, the network assigns the address automatically. When it is off, you enter the settings yourself.
3. If you turned it off, enter these settings:

   - **Address:** The IP address for your device
   - **Subnet:** The subnet mask
   - **Gateway:** The gateway address
   - **DNS Server:** Up to two DNS server addresses. The second is optional.
4. Tap **Save**. If you changed nothing, the button reads **Done**.

If **Private Wi-Fi address** appears under **IP Address**, it shows the network an address of its own instead of the device's hardware address. A change applies from the next connection.

Related: [View details about a Wi-Fi network](/wi-fi/view-wi-fi-network-details), [Connect to a new open network](/wi-fi/connect-to-a-new-open-network), [Connect to a new secure Wi-Fi network](/wi-fi/connect-to-a-new-secure-wi-fi-network), [Connect to a previously used Wi-Fi network](/wi-fi/connect-to-a-previously-used-wi-fi-network)
