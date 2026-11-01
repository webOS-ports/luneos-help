---
{
 "id": "wi-fi/view-wi-fi-network-details",
 "title": "View details about a Wi-Fi network",
 "section": [],
 "order": 396.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/WiFiNetworkInfoPopup.qml:346",
  "adb: settings-common/qml/Connectivity/WiFiNetworkInfoPopup.qml:397",
  "adb: settings-common/qml/Connectivity/WiFiNetworkInfoPopup.qml:427"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Wi-Fi** > touch and hold the network name.
2. Scroll to see the details. A detail appears only if your device knows it. A network you are not connected to shows fewer.

   - **Access Point Info:** **Signal**, **Security**, **Encryption**, **BSSID**, **Channel**, **Frequency**, **Channel width**, **Max speed**, and **Hidden network**
   - **IP Address:** **Configuration**, **IP address**, **Subnet mask**, **Gateway**, **IPv6 address**, **IPv6 gateway**, **DNS**, **Search domains**, and **Proxy**
   - **Interface:** **Interface**, **MAC address**, and **MTU**
3. Tap **Done**.

The line under the network name shows the connection state, such as **Connected** or **Connected – internet available**.

Related: [Customize Wi-Fi connection settings](/wi-fi/customize-wi-fi-connection-settings)
