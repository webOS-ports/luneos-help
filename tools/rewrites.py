"""Mechanical wording changes applied on import. Anything riskier is flagged, not changed."""
import re

# Ordered: longer phrases first.
REPLACE = [
    (r"\bHP webOS\b", "LuneOS"),
    (r"\bwebOS\b", "LuneOS"),
    (r"\byour HP (Pre3|Pre 3|Pre2|Pre 2|Veer|TouchPad)\b", "your device"),
    (r"\bYour HP (Pre3|Pre 3|Pre2|Pre 2|Veer|TouchPad)\b", "Your device"),
    (r"\byour (TouchPad|smartphone)\b", "your device"),
    (r"\bYour (TouchPad|smartphone)\b", "Your device"),
    (r"\bthe (TouchPad|smartphone)\b", "the device"),
    (r"\bThe (TouchPad|smartphone)\b", "The device"),
    (r"\bsmartphones\b", "devices"),
    (r"\bsmartphone\b", "device"),
]

# Terms that mean an article must be read by a person before it can be verified.
REVIEW = [
    "HP", "Palm", "hpwebos", "palm.com", "App Catalog", "Synergy", "Touchstone",
    "Quick Launch", "gesture area", "Center button", "Profile", "Software Manager",
    "Quickoffice", "Facebook", "Skype", "Amazon", "Adobe", "Touch to Share",
    "Exhibition", "Sprint", "Verizon", "AT&T",
]


def _articles(text):
    return re.sub(r"\b([Aa])n LuneOS\b", r"\1 LuneOS", text)


def rewrite(text):
    for pattern, new in REPLACE:
        text = re.sub(pattern, new, text)
    return _articles(text)


def review_terms(text):
    return [t for t in REVIEW if re.search(r"(?<![A-Za-z])" + re.escape(t) + r"(?![A-Za-z])", text)]
