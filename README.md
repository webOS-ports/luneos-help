# LuneOS Help

The help site for LuneOS, published at help.luneos.org. The same output is meant for the on-device Help app.

Build:

    python -m venv venv && venv/bin/pip install -r requirements.txt
    venv/bin/python tools/build.py .

The result is in `dist/`, which works from any static host or directly from disk.

- `content/en/` holds the articles, one Markdown file each, with JSON front matter.
- `tools/import_archive.py` made the first draft from webOS Archive's copy of help.palm.com. It's a one-off and refuses to run over existing content, because `content/en` now holds the audited text.
- `tools/art.py` draws the icons and device drawings as SVG.
- `static/` holds the styles, script, Prelude fonts and LuneOS app icons.

Each article records `status`, `evidence` and `origin`. `verified-device` means its labels and steps were checked against files and queries on a device, `verified-source` against source, and `needs-device-test` that they couldn't be confirmed. Set `tested` once a person has done the steps: only that removes the note at the bottom of the page. The audit reports are in `docs/audit/`.

Text follows the device. `{if:modem}` at the start of a paragraph, list item or heading shows it only with that feature, `{if:!keyboard}` is the opposite, and commas mean AND. `"requires"` does the same for a whole article. The features are `tablet`, `keyboard`, `modem`, `camera`, `homebutton`, `volumebutton`, `powerbutton` and `brightness`, matching the machine's `deviceinfo` adaptation. On the web, readers pick a preset and can adjust it. With `build.py --app`, pages load `device.js`, which sets `window.HELP_DEVICE` to that machine's values and hides the picker. Imported text remains © 2009-2011 Hewlett-Packard Development Company, L.P.; keep the notice on it.
