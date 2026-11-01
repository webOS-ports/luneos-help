---
{
 "id": "wi-fi/connect-to-a-captive-portal",
 "title": "Connect to a captive portal",
 "section": [],
 "order": 392,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/4179",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "webos-connman-adapter/src/wifi_service.c:4112",
  "webos-connman-adapter/src/connectionmanager_service.c:251",
  "no captivePortal consumer in luna-next-cardshell, luneos-components or org.webosports.app.*",
  "adb: settings-common/qml/Connectivity/WiFiNetworkInfoPopup.qml:127"
 ]
}
---

Some Wi-Fi networks, such as those in a coffee shop, hotel, or airport, make you sign in on a web page, known as a captive portal, before you can reach the Internet.

1. Connect to the network ([learn how](/wi-fi/connect-to-a-new-open-network "Connect to a new open network")).
2. Open **Atlas Web** and go to any web page.
3. Follow the onscreen instructions on the sign-in page.

To check whether the device has Internet access: **[Open](/basics/open-an-application-in-the-launcher) Wi-Fi** > touch and hold the network name. The line under the name reads **Connected – internet available** when it does.
