---
{
 "id": "music/remove-a-streaming-service",
 "title": "Remove a streaming service",
 "section": [],
 "order": 310.6,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.music/qml/StreamingStore.qml:31",
  "/usr/palm/applications/org.webosports.app.music/qml/js/Streaming.js:122",
  "luneos-synergy-connectors/music/_core/service/secrets.go:118",
  "luneos-synergy-connectors/music/_core/service: removeSecret is called only for a failed sign-in (providerauth.go:100,132,170)"
 ],
 "review": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** and tap the service.
2. Tap **Remove Account**, then confirm. See [Edit or delete an online account](/accounts/use-the-accounts-application-to-edit-or-delete-an-online-account).

The service leaves Music's **Streaming** category and search. You can't remove YouTube Music.

Removing the account doesn't end your subscription. Do that with the service.

The streaming service keeps your sign-in on the device after the account is removed. If you add the account again, you may not be asked to sign in.
