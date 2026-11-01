#!/usr/bin/env python3
"""One-off import of webOSArchive/help.palm.com into content/en as draft articles.

usage: import_archive.py <archive-dir> <repo-dir>
"""
import html
import json
import pathlib
import re
import shutil
import sys

from bs4 import BeautifulSoup, Comment
from markdownify import markdownify

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from link_names import NAMES
from rewrites import review_terms, rewrite  # noqa: E402

MISSING_TOC = []
BASE = "en-us/c000-01/d400-01"
TABLET = "en-us/c000-01/d500-01"

DROP = {"Facebook", "Facebook Tablet", "Quickoffice", "App Catalog", "HP App Catalog",
        "Amazon MP3", "Voice Dial", "Phone & Video Calls"}
RENAME = {"HP mobile hotspot": "Tethering", "PDF View": "PDF", "Adobe Reader": "PDF",
          "Photos & Videos": "Photos"}
LEGACY = {  # app help targets -> topic
    "accountsmgr": "accounts", "palm_acct": "accounts", "basics": "basics",
    "bluetooth": "bluetooth", "web": "web", "calculator": "calculator",
    "calendar": "calendar", "device_info": "device-info", "clock": "clock",
    "contacts": "contacts", "data_transfer": "basics", "date_time": "date-and-time",
    "email": "email", "exhibition": "exhibition", "language": "regional-settings",
    "location": "location-services", "messaging": "messaging", "music": "music",
    "memos": "memos", "notes": "memos", "pdf_view": "pdf", "phone": "phone",
    "photos": "photos", "video": "videos", "print_manager": "print-manager",
    "screen": "screen-and-lock", "searchpreferences": "just-type",
    "universalsearch": "just-type", "launcher": "launcher",
    "sounds_ringtones": "sounds-and-ringtones", "softwaremgr": "software-manager",
    "tasks": "tasks", "textassist": "text-assist", "updates": "system-updates",
    "backup": "backup", "vpn": "vpn", "wifi": "wi-fi", "youtube": "videos",
}


def slug(text):
    text = text.lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")[:70]


def clean(text):
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def article_body(path):
    raw = path.read_text(errors="replace")
    m = re.search(r'class="inner">(.*?)(?:<span class="link-to-chat"|<!-- Span inner)', raw, re.S)
    return m.group(1) if m else ""


def walk(root, tree, url, section=()):
    """Yield (section path, title, article id) under a toc url."""
    m = re.search(r"/toc/(\d+)/", url)
    path = root / tree / "toc" / m[1] / "index.json"
    if not path.exists():
        MISSING_TOC.append(f"{tree}/toc/{m[1]}")
        return
    data = json.loads(path.read_text())
    for item in data.get("items", []):
        title = clean(item["text"])
        art = re.search(r"/article/(\d+)\.html", item["url"])
        if art:
            yield section, title, art[1]
        elif "/toc/" in item["url"]:
            yield from walk(root, tree, item["url"], section + (title,))


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", rewrite(t).lower()).strip()


def collect(root):
    articles, topics = [], {}
    seen = {}
    for tree, device in ((BASE, "phone"), (TABLET, "tablet")):
        index = json.loads((root / tree / "index.json").read_text())
        for it in index["items"]:
            name = clean(it["text"])
            if name in DROP:
                continue
            name = RENAME.get(name, name)
            tid = slug(name)
            topics.setdefault(tid, {"title": name, "group": clean(it["category"]), "id": tid,
                                    "app": it.get("app_name", "")})
            for section, title, aid in walk(root, tree, it["url"]):
                key = (tid, norm_title(title))
                if key in seen:
                    seen[key]["devices"].append(device)
                    seen[key]["other"] = (tree, aid)
                    continue
                entry = {"topic": tid, "section": [rewrite(x).replace(" :", ":") for x in section], "title": title,
                         "source": f"{tree.split('/')[-1]}/{aid}", "tree": tree, "aid": aid,
                         "devices": [device]}
                seen[key] = entry
                articles.append(entry)
    return articles, topics


def resolve_names(articles):
    """Palm named links went through a server lookup that is lost. Match names to titles."""
    by_title = {norm_title(a["title"]): a for a in articles}
    manual = {k.lower(): norm_title(v) for k, v in NAMES.items()}
    wrong = sorted(v for v in manual.values() if v not in by_title)
    if wrong:
        raise SystemExit(f"link_names.py titles not found: {wrong}")
    words = {t: set(t.split()) for t in by_title}
    stop = {"a", "an", "the", "to", "in", "on", "of", "your", "and", "or", "from", "basics"}

    def find(name):
        name = name.lower()
        if name in manual:
            return by_title[manual[name]]
        want = set(name.replace("app", "application").replace("apps", "applications").split("_")) - stop
        best, score = None, 0.0
        for t, w in words.items():
            w2 = w - stop
            union = want | w2
            s = len(want & w2) / len(union) if union else 0
            if s > score:
                best, score = t, s
        return by_title[best] if score >= 0.6 else None
    return find


def fix_image(src):
    m = re.search(r"images/(device_images|app_icons_small|css_images|device_drawings)/([^/]+)$", src)
    return (m[1], m[2]) if m else None


def to_markdown(tree, aid, root, find, used, unresolved):
    # Palm's HTML leaves <LI> and <P> open, which only an HTML5 parser closes correctly.
    soup = BeautifulSoup(article_body(root / tree / "article" / f"{aid}.html"), "html5lib").body
    for c in soup.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    for t in soup(["script", "style", "input", "form"]):
        t.decompose()
    for img in soup.find_all("img"):
        ref = fix_image(img.get("src", ""))
        if not ref:
            img.decompose()
            continue
        used.add(ref)
        img["src"] = f"/legacy/{ref[0]}/{ref[1].rstrip(chr(34))}"
        img["alt"] = "image"
    for a in soup.find_all("a"):
        href = a.get("href", "")
        m = re.search(r"buildHelpURL\('[^']*','([^']+)'", href)
        art = re.search(r"/article/(\d+)", href)
        if m:
            hit = find(m[1])
            if hit:
                a["href"] = f"/{hit['topic']}/{hit['slug']}"
            else:
                unresolved[m[1]] = unresolved.get(m[1], 0) + 1
                a.unwrap()
        elif art or not href.startswith("http"):
            a.unwrap()
        else:
            a.unwrap()  # dead hp/palm sites
    for s in soup.find_all(class_=["launcher_icon", "textProcedure", "textHelpLink", "menu_link"]):
        s.name = "strong"
        s.attrs = {}
    for t in soup.find_all(["span", "div"]):
        t.unwrap()
    for t in soup.find_all(["p", "li"]):
        if not t.get_text(strip=True) and not t.find("img"):
            t.decompose()
    md = markdownify(soup.decode_contents(), heading_style="ATX", bullets="-", strip=["font"])
    md = md.replace("\xa0", " ")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    md = re.sub(r"\*\*>", "** >", md)
    return rewrite(md)


def main():
    root, repo = map(pathlib.Path, sys.argv[1:3])
    out = repo / "content" / "en"
    if out.exists() and "--overwrite" not in sys.argv:
        raise SystemExit("content/en holds audited text. Pass --overwrite to replace it with the raw import.")
    shutil.rmtree(out, ignore_errors=True)
    articles, topics = collect(root)
    used_slugs = set()
    for n, a in enumerate(articles):
        a["order"] = n
        a["title"] = rewrite(a["title"])
        s = slug(a["title"]) or a["aid"]
        while (a["topic"], s) in used_slugs:
            s += "-" + a["aid"]
        used_slugs.add((a["topic"], s))
        a["slug"] = s
    find = resolve_names(articles)
    used, unresolved, flagged = set(), {}, {}
    variants = 0
    for a in articles:
        md = to_markdown(a["tree"], a["aid"], root, find, used, unresolved)
        if "other" in a:
            other = to_markdown(*a["other"], root, find, used, unresolved)
            if re.sub(r"\s+", "", other) != re.sub(r"\s+", "", md):
                variants += 1
                md = "<!-- ui:phone -->\n\n" + md + "\n\n<!-- ui:tablet -->\n\n" + other
        review = review_terms(a["title"] + "\n" + md)
        for t in review:
            flagged[t] = flagged.get(t, 0) + 1
        path = out / a["topic"] / f"{a['slug']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        head = {"id": f"{a['topic']}/{a['slug']}", "title": a["title"], "section": a["section"],
                "order": a["order"], "devices": a["devices"], "origin": f"palm/{a['source']}", "status": "draft",
                "review": review}
        path.write_text("---\n" + json.dumps(head, indent=1, ensure_ascii=False) + "\n---\n\n" + md + "\n")
    by_source = {a["aid"]: a for a in articles}
    featured = []
    for f in (BASE, TABLET):
        for i in json.loads((root / f / "index_features.json").read_text())["items"]:
            m = re.search(r"/article/(\d+)", i["url"])
            hit = by_source.get(m[1]) if m else None
            if hit and hit not in featured:
                featured.append(hit)
    groups, order = {}, []
    for t in topics.values():
        if t["group"] not in groups:
            order.append(t["group"])
        groups.setdefault(t["group"], []).append(t["id"])
    toc = {"groups": [{"title": g, "topics": groups[g]} for g in order],
           "topics": topics,
           "featured": [f"{a['topic']}/{a['slug']}" for a in featured],
           "legacy": {k: v for k, v in LEGACY.items() if v in topics}}
    (out / "toc.json").write_text(json.dumps(toc, indent=1, ensure_ascii=False) + "\n")
    print("articles", len(articles), "topics", len(topics), "images", len(used))
    print("tablet only", sum(1 for a in articles if a["devices"] == ["tablet"]),
          "shared", sum(1 for a in articles if len(a["devices"]) > 1))
    print("articles with phone and tablet text", variants, "missing toc", len(MISSING_TOC))
    print("flagged", sorted(flagged.items(), key=lambda x: -x[1]))
    print("unresolved link names", len(unresolved), sum(unresolved.values()),
          sorted(unresolved.items(), key=lambda x: -x[1]))
    print("legacy targets without topic", sorted(k for k, v in LEGACY.items() if v not in topics))


main()
