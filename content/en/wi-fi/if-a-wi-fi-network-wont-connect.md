---
{
 "id": "wi-fi/if-a-wi-fi-network-wont-connect",
 "title": "If a Wi-Fi network won't connect",
 "section": [],
 "order": 396.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/WiFiConnectProblemPopup.qml:94",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/WiFiConnectProblemPopup.qml:137",
  "org.webosports.app.settings@b5d8ff4:src/qml/Connectivity/WiFiPage.qml connectFailed"
 ]
}
---

If your device can't connect, a message tells you why. Tap **OK** and tap the network to try again.

- **The passphrase was not accepted.** or **The passphrase is not valid for this network.** Check the passphrase and try again.
- **The network is out of range.** Move closer to the network.
- **The network did not give out an address.** The network did not assign your device an IP address. You can enter one yourself ([learn how](/wi-fi/customize-wi-fi-connection-settings)).
- **Connecting took too long and was stopped.** Try again.
- **Wi-Fi is blocked.** Check that airplane mode is off ([learn how](/basics/turn-all-wireless-services-on-off-airplane-mode)).

If you tap a network while your device is still connecting to it, you see **Still trying to connect from an earlier attempt**. Tap **Stop connecting**, and then tap the network to try again. To let the attempt continue, tap **Keep waiting**.
