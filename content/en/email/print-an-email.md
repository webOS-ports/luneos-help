---
{
 "id": "email/print-an-email",
 "title": "Print an email",
 "section": [
  "Work with email messages"
 ],
 "order": 473,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/39435",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.email/mail/source/MessagePane.js:76",
  "adb: /usr/palm/applications/com.palm.app.email/mail/source/MailApp.js:90",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/printdialog/source/PrintDialogString.js:6",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/printdialog/source/PrintDialogString.js:21",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/printdialog/source/PrintDialogString.js:12",
  "adb: /usr/palm/frameworks/enyo/0.10/framework/lib/printdialog/source/PrintDialogString.js:14",
  "adb: ps -ef | grep cupsd"
 ]
}
---

1. Open the email that you want to print.
2. Tap the print icon at the top of the message, or **[Menu](/basics/open-the-application-menu)** > **Print**.

   Printers that are available on your current wireless network are displayed.
3. Do one of the following:
   - If this is your first time using a printer on this network: If a list of printers is displayed, tap one.
   - If you have already used a printer on this network: The last printer you used is selected. To select another printer, tap **Select Another Printer** > tap a printer.
   - To set up a printer manually: Tap **Add a Printer**. Tap **Enter Printer IP address** > enter the IP address of the printer. (Optional) Tap **Name Printer** > enter a name to identify the printer. Tap **Done**.
4. (Optional) Depending on the printer you are using, you can set options such as **Number of Copies** and **Color Printing**.
5. Tap **Print**.
