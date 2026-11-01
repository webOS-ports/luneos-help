---
{
 "id": "print-manager/what-printers-can-i-add",
 "title": "What printers can I add?",
 "section": [],
 "order": 469,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/41827",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: luna-send org.webosports.service.print/listPrinters (both devices; found a network printer)",
  "meta-luneos/recipes-luneos/luneos-print-adapter/luneos-print-adapter.bb:1-38 (CUPS, IPP Everywhere, cups-filters)",
  "adb: ls /usr/libexec/cups/filter and backend (driverless, ipp, ipps, dnssd present)",
  "/usr/palm/applications/org.webosports.app.photos/qml/Printer.qml:53, PictureView.qml:290 (Print button); adb: luna-send com.palm.printmgr/printers/listActive"
 ]
}
---

Your device prints over the network to printers that support IPP, including IPP Everywhere and AirPrint printers. No printer driver is needed.

Make sure your printer is turned on and that it and your device are on the same network.

To print a picture, open it in the Photos & Videos app and tap the print button ([learn how](/photos/print-pictures)). Photos & Videos is the only app that prints.
