# /// script
# requires-python = ">=3.9"
# dependencies = ["markdown>=3.5"]
# ///
"""Build the Terran Encyclopaedia static site from the Combustion-Age markdown.

Auto-discovers every article `*.md` in this directory (anything not in EXCLUDE),
so adding an entry is: drop the .md file in, run `uv run build.py`.

Each article file is expected to open with:
    # <Title>
    *Terran Encyclopaedia, 3000 CE edition — ...*
    > **<one clean sentence used as the front-page blurb>** ...
    ---
    <body>

Design: a quiet, typographic reading site — a simple front-page listing and
plainly-styled article pages. Headings in Space Grotesk, body in Newsreader
(both Google Fonts). No sidebar, no search chrome; the type does the work.

Run with:  uv run build.py
Outputs:   index.html, one .html per article, and assets/style.css
"""

import pathlib
import re
import subprocess

import markdown

ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

# Markdown files that are NOT articles.
EXCLUDE = {"prompt.md", "readme.md", "claude.md", "variety_ledger.md"}
# The overview article: sorted to the top of the listing.
HOME = "combustion_age"

# Populated in main() once the articles are discovered.
ARTICLES = []      # list of {src, slug, title, desc}
CROSSLINKS = {}    # {title: "<slug>.html"}


# --------------------------------------------------------------------------- #
#  Discovery                                                                    #
# --------------------------------------------------------------------------- #

def _created_ts(slug):
    """First-added git commit timestamp for <slug>.md (creation order).

    Returns a large sentinel for files git doesn't know yet (a new entry built
    before it is committed), so brand-new articles sort to the bottom as newest.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "log", "--diff-filter=A", "--follow",
             "--format=%at", "--", f"{slug}.md"],
            capture_output=True, text=True, timeout=15,
        ).stdout.split()
        return int(out[-1]) if out else 2**63
    except Exception:
        return 2**63


def discover_articles():
    """Find every article markdown file and read its title + front-page blurb."""
    found = []
    for path in sorted(ROOT.glob("*.md")):
        if path.name.lower() in EXCLUDE:
            continue
        text = path.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+?)\s*$", text, re.M)
        if not m:
            continue
        title = m.group(1).strip()
        hat = re.search(r"^>\s*\*\*(.+?)\*\*", text, re.M)
        desc = hat.group(1).strip() if hat else ""
        found.append({"src": path.name, "slug": path.stem, "title": title, "desc": desc})
    # Order of creation, oldest first; the overview leads its (oldest) day.
    found.sort(key=lambda a: (_created_ts(a["slug"]), 0 if a["slug"] == HOME else 1, a["title"]))
    return found


# --------------------------------------------------------------------------- #
#  Templates                                                                    #
# --------------------------------------------------------------------------- #

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;'
    '1,6..72,400;1,6..72,500&family=Space+Grotesk:wght@400;500;600;700&display=swap">'
)

DOC = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
__FONTS__
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="wrap">
__CONTENT__
</div>
<footer class="site-footer"><div class="site-footer-inner">
<p>Terran Encyclopaedia · 3000 CE edition. A work of speculative fiction: every
article, source, scholar, and citation is invented. Rendered into Reconstructed
Late Combustion English by convention of the Historical Faculty.</p>
</div></footer>
</body>
</html>
"""


# --------------------------------------------------------------------------- #
#  Markdown -> article HTML                                                     #
# --------------------------------------------------------------------------- #

def crosslink(html, slug):
    self_url = f"{slug}.html"
    for phrase, url in CROSSLINKS.items():
        if url == self_url:
            continue
        html = html.replace(f"<li>{phrase}</li>",
                            f'<li><a href="{url}">{phrase}</a></li>')
        html = html.replace(f"<strong>{phrase}</strong>",
                            f'<strong><a href="{url}">{phrase}</a></strong>')
    return html


def build_article(a):
    src = (ROOT / a["src"]).read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=["extra", "sane_lists", "smarty"])
    html = md.convert(src)

    # Pull the <h1> title and the italic byline out of the body flow.
    m = re.match(r"\s*<h1[^>]*>(.*?)</h1>\s*", html, re.S)
    title_html = m.group(1).strip() if m else a["title"]
    if m:
        html = html[m.end():]
    m2 = re.match(r"\s*<p>\s*<em>(.*?)</em>\s*</p>\s*", html, re.S)
    byline = m2.group(1).strip() if m2 else ""
    if m2:
        html = html[m2.end():]
    # Pull the leading hatnote blockquote out as a standfirst.
    m3 = re.match(r"\s*<blockquote>(.*?)</blockquote>\s*", html, re.S)
    hatnote = m3.group(1).strip() if m3 else ""
    if m3:
        html = html[m3.end():]
    # Drop the horizontal rule that separated the hatnote from the body.
    html = re.sub(r"^\s*<hr\s*/?>\s*", "", html)

    # Clean table styling + horizontal scroll on small screens.
    html = html.replace("<table>", '<div class="table-wrap"><table>')
    html = html.replace("</table>", "</table></div>")

    html = crosslink(html, a["slug"])

    byline_html = f'<p class="byline">{byline}</p>' if byline else ""
    hatnote_html = f'<div class="hatnote">{hatnote}</div>' if hatnote else ""
    content = (
        '<nav class="topnav"><a href="index.html">Terran Encyclopaedia</a></nav>\n'
        "<article>\n"
        f'<h1>{title_html}</h1>\n{byline_html}\n{hatnote_html}\n'
        f'<div class="prose">{html}</div>\n'
        "</article>"
    )

    page = (DOC.replace("__TITLE__", f'{a["title"]} — Terran Encyclopaedia')
               .replace("__FONTS__", FONTS)
               .replace("__CONTENT__", content))
    (ROOT / f'{a["slug"]}.html').write_text(page, encoding="utf-8")


# --------------------------------------------------------------------------- #
#  Front page (index.html)                                                      #
# --------------------------------------------------------------------------- #

def build_index():
    items = "".join(
        f'<li><a class="entry" href="{a["slug"]}.html">'
        f'<span class="entry-title">{a["title"]}</span>'
        f'<span class="entry-blurb">{a["desc"]}</span></a></li>'
        for a in ARTICLES
    )
    n = len(ARTICLES)
    content = (
        '<header class="masthead">\n'
        '<h1 class="site-title">Terran Encyclopaedia</h1>\n'
        '<p class="site-sub">A reference to the Combustion Age, c. 1750–2140 CE, '
        'read from the vantage of the year 3000.</p>\n'
        '</header>\n'
        f'<p class="site-note">{n} entries · a work of speculative fiction</p>\n'
        f'<ul class="index-list">{items}</ul>'
    )
    page = (DOC.replace("__TITLE__", "Terran Encyclopaedia — 3000 CE edition")
               .replace("__FONTS__", FONTS)
               .replace("__CONTENT__", content))
    (ROOT / "index.html").write_text(page, encoding="utf-8")


# --------------------------------------------------------------------------- #
#  Assets                                                                        #
# --------------------------------------------------------------------------- #

CSS = """/* Terran Encyclopaedia — typographic reading edition */
:root{
  --paper:#fbfaf6; --ink:#221f1a; --muted:#6d675d; --rule:#e0dacd;
  --accent:#9c3b28; --accent-2:#b24d38;
  --measure:40rem;
  --serif:"Newsreader",Georgia,"Times New Roman",serif;
  --sans:"Space Grotesk",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%; color-scheme:light}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:var(--serif); font-optical-sizing:auto;
  font-size:1.16rem; line-height:1.72;
  -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility;
}
::selection{background:var(--accent); color:var(--paper)}
.wrap{max-width:var(--measure); margin:0 auto; padding:3.4rem 1.5rem 1rem}

a{color:var(--accent); text-decoration:none; text-decoration-skip-ink:auto}
a:hover{text-decoration:underline; text-underline-offset:.14em;
  text-decoration-thickness:.06em; color:var(--accent-2)}

/* ---- article top nav ---- */
.topnav{margin:0 0 2.8rem}
.topnav a{font-family:var(--sans); font-size:.74rem; font-weight:500;
  letter-spacing:.13em; text-transform:uppercase; color:var(--muted)}
.topnav a::before{content:"\\2190\\00a0"}
.topnav a:hover{color:var(--accent); text-decoration:none}

/* ---- front page ---- */
.masthead{margin:0 0 1.5rem}
.site-title{font-family:var(--sans); font-weight:700; font-size:2.7rem;
  line-height:1.02; letter-spacing:-.02em; margin:0}
.site-sub{font-family:var(--serif); font-style:italic; font-size:1.2rem;
  color:var(--muted); margin:.6rem 0 0; max-width:32rem}
.site-note{font-family:var(--sans); font-size:.72rem; font-weight:500;
  letter-spacing:.14em; text-transform:uppercase; color:var(--muted);
  border-top:1px solid var(--rule); border-bottom:1px solid var(--rule);
  padding:.75rem 0; margin:1.8rem 0 0}

.index-list{list-style:none; margin:0; padding:0}
.index-list li+li{border-top:1px solid var(--rule)}
.entry{display:block; padding:1.15rem 0; color:inherit}
.entry:hover{text-decoration:none}
.entry-title{display:block; font-family:var(--sans); font-weight:600;
  font-size:1.12rem; line-height:1.25; letter-spacing:-.005em; color:var(--ink)}
.entry:hover .entry-title{color:var(--accent)}
.entry-blurb{display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical;
  overflow:hidden; color:var(--muted); font-size:1rem; line-height:1.5; margin-top:.32rem}

/* ---- article ---- */
h1{font-family:var(--sans); font-weight:700; font-size:2.25rem; line-height:1.1;
  letter-spacing:-.02em; margin:0 0 .4rem}
.byline{font-style:italic; color:var(--muted); font-size:1rem; line-height:1.5;
  margin:0 0 1.9rem}
.hatnote{font-size:1.22rem; line-height:1.56; color:var(--muted);
  border-left:2px solid var(--accent); padding:.1rem 0 .1rem 1.15rem; margin:0 0 2.4rem}
.hatnote p{margin:0}
.hatnote strong{color:var(--ink); font-weight:600}

.prose h2{font-family:var(--sans); font-weight:600; font-size:1.36rem; line-height:1.2;
  letter-spacing:-.01em; margin:2.8rem 0 .85rem}
.prose h3{font-family:var(--sans); font-weight:500; font-size:1.08rem; line-height:1.25;
  margin:2rem 0 .5rem}
.prose p{margin:0 0 1.1rem}
.prose ul,.prose ol{margin:0 0 1.1rem; padding-left:1.35rem}
.prose li{margin:.35rem 0; padding-left:.2rem}
.prose li::marker{color:var(--muted)}
.prose strong{font-weight:600}
.prose hr{border:0; border-top:1px solid var(--rule); margin:2.6rem 0}

/* record / ledger lines quoted inside a tale */
.prose blockquote{margin:1.5rem 0; padding:.15rem 0 .15rem 1.15rem;
  border-left:2px solid var(--rule); color:var(--muted); font-style:italic}
.prose blockquote p{margin:.35rem 0}
.prose blockquote code{font-style:normal}

code{font-family:var(--mono); font-size:.86em}
.prose p>code,.prose li>code{background:var(--rule); padding:.05em .35em; border-radius:3px}

/* tables (used by the overview entries) */
.table-wrap{overflow-x:auto; margin:1.8rem 0}
table{border-collapse:collapse; width:100%; font-family:var(--sans); font-size:.88rem;
  line-height:1.45}
th,td{text-align:left; vertical-align:top; padding:.5rem .8rem;
  border-bottom:1px solid var(--rule)}
th{font-weight:600; border-bottom:2px solid var(--rule)}

sup{line-height:0}

/* ---- footer ---- */
.site-footer{border-top:1px solid var(--rule); margin-top:3rem}
.site-footer-inner{max-width:var(--measure); margin:0 auto; padding:1.6rem 1.5rem 3.5rem}
.site-footer p{font-family:var(--sans); font-size:.74rem; letter-spacing:.02em;
  line-height:1.65; color:var(--muted); margin:0}

/* ---- small screens ---- */
@media (max-width:640px){
  body{font-size:1.08rem}
  .wrap{padding:2.2rem 1.25rem 1rem}
  .site-title{font-size:2.1rem}
  h1{font-size:1.85rem}
  .hatnote{font-size:1.12rem}
  .prose h2{font-size:1.24rem}
}
"""


def build_assets():
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "style.css").write_text(CSS, encoding="utf-8")


# --------------------------------------------------------------------------- #

def main():
    global ARTICLES, CROSSLINKS
    ARTICLES = discover_articles()
    if not ARTICLES:
        print("No article markdown files found (everything matched EXCLUDE).")
        return
    CROSSLINKS = {a["title"]: f'{a["slug"]}.html' for a in ARTICLES}

    for a in ARTICLES:
        build_article(a)
    build_index()
    build_assets()

    print(f"Built Terran Encyclopaedia — {len(ARTICLES)} entries discovered:")
    for a in ARTICLES:
        print(f"  {a['slug']}.html   ← {a['src']}   ({a['title']})")
    print("  index.html, assets/style.css")
    print("\nOpen index.html in a browser.")


if __name__ == "__main__":
    main()
