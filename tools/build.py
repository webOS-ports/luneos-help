#!/usr/bin/env python3
"""Build the help site from content/en. usage: build.py <repo-dir> [out-dir] [--app]"""
import html
import json
import pathlib
import re
import shutil
import sys

import markdown
from bs4 import BeautifulSoup

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import art  # noqa: E402

DEVICES = [("slab", "Slab phone"), ("qwerty", "QWERTY phone"), ("tablet", "Tablet")]
# Features mirror the machine's deviceinfo adaptation. "tablet" is set by the presets.
FEATURES = [
    ("keyboard", "Physical keyboard", "a physical keyboard"),
    ("modem", "Calls and mobile data", "calls and mobile data"),
    ("camera", "Camera", "a camera"),
    ("homebutton", "Home button", "a home button"),
    ("volumebutton", "Volume buttons", "volume buttons"),
    ("powerbutton", "Power button", "a power button"),
    ("brightness", "Adjustable brightness", "adjustable brightness"),
]
PHRASE = {k: v for k, _, v in FEATURES} | {"tablet": "a tablet layout"}
COND = re.compile(r"^\s*\{if:([a-z!,]+)\}\s*")
NOTICE = ("Adapted from the Palm and HP webOS Help, preserved by "
          '<a href="https://www.webosarchive.org/">webOS Archive</a>. '
          "Original text &copy; 2009&ndash;2011 Hewlett-Packard Development Company, L.P.")
UNTRIED = "These steps haven&rsquo;t been confirmed on LuneOS yet, so some may differ."
CHECKED = "Checked against the LuneOS code and installed apps. Nobody has tried these steps by hand yet, so tell us if something differs."
# Whole-page audience, until an article's own "requires" says otherwise.
AUDIENCE = {"basics/keyboard": ["keyboard"], "basics/use-the-keyboard": ["keyboard"], "basics/use-the-onscreen-keyboard": ["!keyboard"]}
PAGE = """<!doctype html>
<html lang="en" data-root="{root}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
{device_js}<script>{boot}</script>
<link rel="stylesheet" href="{root}help.css"><link rel="icon" href="{root}luneos-mark.png"></head>
<body class="{cls}">
<header class="bar">
 <details class="appmenu"><summary>Help</summary>
  <nav class="appmenu-list" aria-label="Help menu"><a href="{root}index.html">Help home</a><a href="{root}index.html#topics">All topics</a><a href="{root}get-help.html">Get help</a><a href="{root}about.html">About Help</a></nav>
 </details>
 <a class="bar-mark" href="{root}index.html" aria-label="Help home"><img src="{root}luneos-mark.png" alt=""></a>
</header>
<div class="devicebar"><div class="devices" role="radiogroup" aria-label="Show help for">{device_buttons}</div>
<details class="features"><summary>Device features</summary><div class="feature-list">{feature_boxes}</div></details></div>
{main}
<footer class="foot"><p>{notice}</p><p><a href="{root}about.html">About Help</a></p></footer>
<script src="{root}search-index.js"></script><script src="{root}help.js"></script>
</body></html>
"""
BOOT = (pathlib.Path(__file__).parent.parent / "static" / "boot.js").read_text().strip()


def parse(path):
    raw = path.read_text()
    head, body = raw.split("\n---\n", 1)
    return json.loads(head.lstrip("-\n")), body.strip()


def device_buttons():
    return "".join(f'<button type="button" role="radio" data-set="{k}">{v}</button>' for k, v in DEVICES)


def feature_boxes():
    return "".join(f'<label><input type="checkbox" data-feature="{k}">{v}</label>' for k, v, _ in FEATURES)


def needs(conds):
    """Plain words for a page's requirements."""
    have = [PHRASE[c] for c in conds if not c.startswith("!")]
    lack = [PHRASE[c[1:]] for c in conds if c.startswith("!")]
    parts = (["with " + " and ".join(have)] if have else []) + (["without " + " or ".join(lack)] if lack else [])
    return "This page is for devices " + " and ".join(parts) + "."


class Site:
    def __init__(self, repo, out, app=False):
        self.repo, self.out, self.app = repo, out, app
        self.toc = json.loads((repo / "content/en/toc.json").read_text())
        self.articles = []
        for p in (repo / "content/en").glob("*/*.md"):
            meta, body = parse(p)
            self.articles.append({"meta": meta, "body": body})
        self.articles.sort(key=lambda a: a["meta"]["order"])
        self.byid = {a["meta"]["id"]: a for a in self.articles}
        self.art = {}
        self.broken = []

    def page(self, depth, title, main, cls=""):
        root = "../" * depth
        device_js = f'<script src="{root}device.js"></script>' if self.app else ""
        return PAGE.format(root=root, title=html.escape(title) + " | LuneOS Help", boot=BOOT, device_js=device_js,
                           device_buttons=device_buttons(), feature_boxes=feature_boxes(), main=main, cls=cls, notice=NOTICE)

    def write(self, rel, text):
        p = self.out / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def asset(self, name, root):
        """Replace one legacy image reference with redrawn art."""
        base = name.split("/")[-1]
        if "device_drawings" in name or "conceptual" in base.lower():
            f = re.sub(r"[^a-z0-9]+", "-", base.lower().rsplit(".", 1)[0])
            svg, label = art.drawing(base)
            self.art[f + ".svg"] = svg
            tag = f'<img class="drawing" src="{root}art/{f}.svg" alt="{html.escape(label)}"'
            if "front_view" in base and not re.search("towi|to3g", base):
                svg, label = art.drawing(base, slab=True)
                self.art[f + "-slab.svg"] = svg
                return (tag + ' data-if="keyboard">' +
                        f'<img class="drawing" src="{root}art/{f}-slab.svg" alt="{html.escape(label)}" data-if="!keyboard">')
            return tag + ">"
        hit = art.lookup(base)
        if not hit:
            self.broken.append(("image", name))
            return ""
        glyph, style, label = hit
        f = re.sub(r"[^a-zA-Z0-9]+", "-", f"{glyph}-{style}").lower() + ".svg"
        self.art[f] = art.icon(glyph, style)
        cls = "key" if style == "key" else "glyph"
        wide = " wide" if style == "key" and len(glyph) > 3 and glyph not in ("pill", "opt", "space", "enter", "left") else ""
        return f'<img class="{cls}{wide}" src="{root}art/{f}" alt="{html.escape(label)}">'

    def render(self, md, root):
        md = re.sub(r"!\[[^\]]*\]\((/legacy/[^)\s]+)[^)]*\)", lambda m: self.asset(m[1], root), md)

        def link(m):
            target = m[1].strip("/")
            if target in self.byid:
                return f"]({root}{target}.html)"
            self.broken.append(("link", target))
            return f"]({root}index.html)"
        md = re.sub(r"\]\(/([a-z0-9-]+/[a-z0-9-]+)(?: \"[^\"]*\")?\)", link, md)
        out = markdown.markdown(md, extensions=["tables", "sane_lists"])
        soup = BeautifulSoup(out, "html.parser")
        for stray in soup.find_all(string=lambda x: "**" in x):  # unbalanced bold in Palm's markup
            stray.replace_with(stray.replace("**", ""))
        for t in soup.find_all(["li", "p", "h2", "h3"]):
            first = next(t.strings, None)
            m = COND.match(first) if first else None
            if not m:
                continue
            bad = [c for c in m[1].split(",") if c.lstrip("!") not in PHRASE]
            if bad:
                self.broken.append(("feature", bad))
            t["data-if"] = m[1]
            first.replace_with(first[m.end():])
        return str(soup)

    def article_html(self, a, root):
        parts = re.split(r"<!-- ui:(phone|tablet) -->", a["body"])
        if len(parts) == 1:
            return self.render(a["body"], root)
        out = ""
        for ui, text in zip(parts[1::2], parts[2::2]):
            out += f'<div data-ui="{ui}">{self.render(text.strip(), root)}</div>'
        return out

    def excerpt(self, a):
        """Card preview per UI: the article's own drawing, or its opening words."""
        out = ""
        blocks = re.findall(r'<div data-ui="(phone|tablet)">(.*?)</div>(?=<div data-ui|$)', a["html"], re.S) or [("", a["html"])]
        for ui, block in blocks:
            soup = BeautifulSoup(block, "html.parser")
            pics = soup.find_all("img", class_="drawing")
            attr = f' data-ui="{ui}"' if ui else ""
            if pics:
                for pic in pics:
                    only = f' data-if="{pic["data-if"]}"' if pic.get("data-if") else ""
                    out += f'<span class="card-art"{attr}{only}><img src="{pic["src"][3:]}" alt=""></span>'
                continue
            words = " ".join(t.get_text(" ", strip=True) for t in soup.find_all(["p", "li"]))
            words = re.sub(r"\s+([.,:;)])", r"\1", words)
            out += f'<span class="card-text"{attr}>{html.escape(words[:200])}</span>'
        return out

    def icon(self, tid, root):
        if (self.repo / "static/icons" / f"{tid}.png").exists():
            return f'<img src="{root}icons/{tid}.png" alt="">'
        self.art["topic-sync.svg"] = art.icon("sync", "plain-blue")
        return f'<img src="{root}art/topic-sync.svg" alt="">'

    def topic_articles(self, tid):
        return [a for a in self.articles if a["meta"]["id"].startswith(tid + "/")]

    def requires(self, a):
        m = a["meta"]
        if "requires" in m:
            return m["requires"]
        if m["id"] in AUDIENCE:
            return AUDIENCE[m["id"]]
        return {("tablet",): ["tablet"], ("phone",): ["!tablet"]}.get(tuple(m["devices"]), [])

    def cond(self, a):
        need = self.requires(a)
        return f' data-if="{",".join(need)}"' if need else ""

    def rail(self, tid, current, root):
        """Article links in Palm's order, under their section headings."""
        t = self.toc["topics"][tid]
        groups = []
        for a in self.topic_articles(tid):
            sec = a["meta"]["section"][0] if a["meta"]["section"] else ""
            if not groups or groups[-1][0] != sec:
                groups.append((sec, []))
            groups[-1][1].append(a)
        rows = []
        for sec, items in groups:
            kinds = {self.cond(a) for a in items}
            if sec:
                only = kinds.pop() if len(kinds) == 1 else ""
                rows.append(f"<h3{only}>{html.escape(sec)}</h3>")
            for a in items:
                m = a["meta"]
                cur = ' aria-current="page"' if m["id"] == current else ""
                rows.append(f'<a href="{root}{m["id"]}.html"{cur}{self.cond(a)}>{html.escape(m["title"])}</a>')
        return "".join(rows), t

    def build(self):
        shutil.rmtree(self.out, ignore_errors=True)
        (self.out / "art").mkdir(parents=True)
        shutil.copytree(self.repo / "static/fonts", self.out / "fonts")
        shutil.copytree(self.repo / "static/icons", self.out / "icons")
        for f in ("help.css", "help.js", "luneos-mark.png"):
            shutil.copy(self.repo / "static" / f, self.out / f)
        index = []
        for a in self.articles:
            m = a["meta"]
            tid = m["id"].split("/")[0]
            links, t = self.rail(tid, m["id"], "../")
            body = self.article_html(a, "../")
            need = self.requires(a)
            note = f'<p class="for-note" data-unless="{",".join(need)}">{needs(need)}</p>' if need else ""
            state = m.get("status", "draft")
            check = "" if state == "tested" else f'<p class="unchecked">{UNTRIED if state in ("draft", "needs-device-test") else CHECKED}</p>'
            main = (f'<div class="layout"><aside class="rail"><a class="rail-head" href="index.html">{self.icon(tid, "../")}{html.escape(t["title"])}</a>{links}</aside>'
                    f'<main class="article"><a class="up" href="index.html">{html.escape(t["title"])}</a><h1>{html.escape(m["title"])}</h1>'
                    f'{note}<div class="prose">{body}</div>{check}</main></div>')
            self.write(m["id"] + ".html", self.page(1, m["title"], main))
            text = re.sub(r"\s+", " ", BeautifulSoup(body, "html.parser").get_text(" "))
            index.append({"t": m["title"], "u": m["id"] + ".html", "c": t["title"], "x": text, "r": ",".join(need)})
            a["text"], a["html"] = text, body
        for tid, t in self.toc["topics"].items():
            links, _ = self.rail(tid, None, "../")
            main = (f'<main class="topic"><a class="up" href="../index.html#topics">All topics</a><h1>{self.icon(tid, "../")}{html.escape(t["title"])}</h1>'
                    f'<div class="topic-list">{links}</div><p class="topic-empty" hidden>Nothing in this topic applies to this device.</p></main>')
            self.write(f"{tid}/index.html", self.page(1, t["title"], main))
        self.home()
        self.static_pages()
        self.write("search-index.js", "window.HELP_INDEX=" + json.dumps(index, ensure_ascii=False, separators=(",", ":")) + ";\n")
        self.write("CNAME", "help.luneos.org\n")
        self.write("legacy-map.json", json.dumps(self.toc["legacy"], indent=1) + "\n")
        for f, svg in self.art.items():
            self.write("art/" + f, svg)
        print("pages", len(self.articles), "art", len(self.art), "broken", len(self.broken), self.broken[:10])
        print("conditional blocks", sum(p.read_text().count("data-if=") for p in self.out.glob("*/*.html")))

    def home(self):
        cards = ""
        for aid in self.toc["featured"][:13]:
            a = self.byid.get(aid)
            if not a:
                continue
            m = a["meta"]
            cards += (f'<a class="card" href="{m["id"]}.html" {self.cond(a)}><span class="card-bar">{html.escape(self.toc["topics"][m["id"].split("/")[0]]["title"])}</span>'
                      f'<strong>{html.escape(m["title"])}</strong>{self.excerpt(a)}</a>')
        groups = ""
        for g in self.toc["groups"]:
            rows = ""
            for tid in g["topics"]:
                t = self.toc["topics"][tid]
                rows += f'<a href="{tid}/index.html" data-topic="{tid}">{self.icon(tid, "")}{html.escape(t["title"])}</a>'
            groups += f'<section><h2>{html.escape(g["title"])}</h2><div class="rows">{rows}</div></section>'
        main = f"""<main class="home">
<div class="justtype"><label class="sr" for="q">Search help</label><input id="q" type="search" placeholder="Just type&hellip;" autocomplete="off" spellcheck="false"></div>
<div id="results" class="results" hidden></div>
<div id="browse">
<section class="cardview"><h2>Getting started</h2><div class="cards">{cards}</div></section>
<div class="groups" id="topics">{groups}</div>
</div></main>"""
        self.write("index.html", self.page(0, "Help", main, "at-home"))

    def static_pages(self):
        self.write("get-help.html", self.page(0, "Get help", """<main class="article solo"><h1>Get help</h1><div class="prose">
<p>Help pages cover most things. If you&rsquo;re stuck, these people can help.</p>
<h2>Ask the community</h2><ul><li><a href="https://forums.weboslives.eu/">webOS Lives forums</a></li><li><a href="https://web.libera.chat/#webos-ports">#webos-ports on Libera.Chat</a></li></ul>
<h2>Report a bug</h2><ul><li><a href="https://github.com/webos-ports/luneos-testing/issues">LuneOS issue tracker</a></li><li><a href="https://wiki.webos-ports.org/wiki/Bug_Report_guidelines">How to write a good bug report</a></li></ul>
<h2>Using a Palm or HP device?</h2><p><a href="https://docs.webosarchive.org/">webOS Archive Docs</a> covers classic webOS devices.</p></div></main>"""))
        self.write("about.html", self.page(0, "About Help", f"""<main class="article solo"><h1>About Help</h1><div class="prose">
<p>This is the LuneOS Help. It works without a network connection, and it doesn&rsquo;t collect anything about you or your device.</p>
<p>{NOTICE} Each article was rewritten against the LuneOS code and records its source and evidence. Steps are still being tried by hand on devices.</p>
<p>The artwork was redrawn for LuneOS. Text is set in Prelude, under the <a href="fonts/Prelude_Font_LICENSE.txt">Open webOS font licence</a>.</p></div></main>"""))


def main():
    args = [x for x in sys.argv[1:] if x != "--app"]
    repo = pathlib.Path(args[0])
    out = pathlib.Path(args[1]) if len(args) > 1 else repo / "dist"
    Site(repo, out, app="--app" in sys.argv).build()


main()
