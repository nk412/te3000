# /// script
# requires-python = ">=3.9"
# dependencies = ["markdown>=3.5"]
# ///
"""Build a Wikipedia-style static site from the Combustion-Age markdown articles.

Auto-discovers every article `*.md` in this directory (anything not in EXCLUDE),
so adding a new article is: drop the .md file in, run `uv run build.py`.

Each article file is expected to open with:
    # <Title>
    *Terran Encyclopaedia, 3000 CE edition. Rendered into ...*
    > **<one-sentence hatnote used as the card blurb>** ...
    ---
    <lead paragraphs>
    ---
    ## 1. <section> ...

Run with:  uv run build.py
Outputs:   index.html, one .html per article, and assets/{style.css,search.js}
"""

import json
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

# Markdown files that are NOT articles.
EXCLUDE = {"prompt.md", "readme.md", "claude.md"}
# The overview article: sorted first, and used as the portal's featured article.
HOME = "combustion_age"

# Curated "Did you know…" lines. Each is shown only if its target article exists,
# so the box degrades gracefully as articles are added or removed.
DYK_FACTS = [
    {"slug": "combustion_age",
     "html": '&hellip; that the <a href="combustion_age.html#4-material-culture">type fossil</a> '
             'of the age is a broiler chicken, bred to grow too fast to stand, and the most '
             'numerous bird in Terran history?'},
    {"slug": "bharat_combustion_age",
     "html": '&hellip; that a lunar rover&rsquo;s <a href="bharat_combustion_age.html#10-legacy">'
             '101 metres of wheel tracks</a> will outlast every stone structure its makers ever '
             'built by a factor of about ten thousand?'},
    {"slug": "bharat_combustion_age",
     "html": '&hellip; that the <a href="bharat_combustion_age.html#7-society">largest human '
             'gathering in history</a> leaves no archaeological trace at all, because the river '
             'takes the sand?'},
    {"slug": "longyear_deposit",
     "html": '&hellip; that one firm <a href="longyear_deposit.html#9-assessment">solved the hard '
             'problem</a> of preserving its civilisation&rsquo;s memory for a thousand years '
             '&mdash; and lost to the floor of a coal mine?'},
]

# Populated in main() once the articles are discovered.
ARTICLES = []      # list of {src, slug, title, desc}
CROSSLINKS = {}    # {title: "<slug>.html"}


# --------------------------------------------------------------------------- #
#  Discovery                                                                    #
# --------------------------------------------------------------------------- #

def _strip_blurb(text):
    text = re.sub(r"^This article (is about|covers)\s+", "", text).strip()
    return text[:1].upper() + text[1:] if text else text


def discover_articles():
    """Find every article markdown file and read its title + card blurb."""
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
        desc = _strip_blurb(hat.group(1).strip()) if hat else ""
        found.append({"src": path.name, "slug": path.stem, "title": title, "desc": desc})
    found.sort(key=lambda a: (0 if a["slug"] == HOME else 1, a["title"]))
    return found


def lead_excerpt_html(slug):
    """First (and, if short, second) lead paragraph, as HTML, for the featured box."""
    text = (ROOT / f"{slug}.md").read_text(encoding="utf-8")
    parts = re.split(r"(?m)^---\s*$", text)
    lead = parts[1] if len(parts) > 1 else text
    paras = [p.strip() for p in re.split(r"\n\s*\n", lead) if p.strip()]
    if not paras:
        return ""
    chosen = paras[:1]
    if len(chosen[0]) < 340 and len(paras) > 1:
        chosen.append(paras[1])
    return markdown.markdown("\n\n".join(chosen))


# --------------------------------------------------------------------------- #
#  Templates                                                                    #
# --------------------------------------------------------------------------- #

DOC = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ — Terran Encyclopaedia</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
__HEADER__
<div class="mw-main">
__SIDEBAR__
<main class="mw-content"><div class="mw-content-inner">
__CONTENT__
</div></main>
</div>
__FOOTER__
<script src="assets/search.js"></script>
</body>
</html>
"""

HEADER = """<header class="mw-header">
  <a class="mw-wordmark" href="index.html">
    <span class="mw-globe">TE</span>
    <span><span class="mw-name">Terran Encyclopaedia</span>
    <span class="mw-tag">The free 3000 CE reference</span></span>
  </a>
  <form id="search-form" class="mw-search" role="search">
    <input id="search-input" list="search-suggestions" autocomplete="off"
           placeholder="Search Terran Encyclopaedia" aria-label="Search">
    <datalist id="search-suggestions"></datalist>
    <button type="submit">Search</button>
  </form>
</header>"""

FOOTER = """<footer class="mw-footer">
  <p><strong>Terran Encyclopaedia</strong> — the free 3000 CE reference.
  This is a work of speculative fiction: every article, source, scholar and
  citation is invented. Text rendered into Reconstructed Late Combustion English
  by convention of the Historical Faculty.</p>
</footer>"""


def sidebar(active):
    rows = []
    for a in ARTICLES:
        cls = ' class="active"' if a["slug"] == active else ""
        rows.append(f'<li{cls}><a href="{a["slug"]}.html">{a["title"]}</a></li>')
    main_active = ' class="active"' if active == "index" else ""
    articles = "".join(rows)
    return f"""<nav class="mw-sidebar" aria-label="Site navigation">
  <div class="sb-block">
    <h3>Navigation</h3>
    <ul>
      <li{main_active}><a href="index.html">Main page</a></li>
      <li><a id="rand-link" href="#">Random article</a></li>
    </ul>
  </div>
  <div class="sb-block">
    <h3>Articles</h3>
    <ul>{articles}</ul>
  </div>
  <div class="sb-block">
    <h3>This edition</h3>
    <ul>
      <li><a href="index.html#about">About this edition</a></li>
      <li>3000 CE edition</li>
      <li>Reconstructed Late<br>Combustion English</li>
    </ul>
  </div>
</nav>"""


# --------------------------------------------------------------------------- #
#  Markdown -> article HTML                                                     #
# --------------------------------------------------------------------------- #

def render_toc(tokens):
    if not tokens:
        return ""
    out = ["<ul>"]
    for t in tokens:
        out.append(f'<li><a href="#{t["id"]}">{t["name"]}</a>')
        if t.get("children"):
            out.append(render_toc(t["children"]))
        out.append("</li>")
    out.append("</ul>")
    return "".join(out)


def build_toc_box(tokens):
    src = tokens
    if len(tokens) == 1 and tokens[0]["level"] == 1:
        src = tokens[0]["children"]
    body = render_toc(src)
    if not body:
        return ""
    return ('<div class="toc" role="navigation" aria-label="Contents">'
            '<div class="toctitle"><h2>Contents</h2></div>' + body + "</div>")


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
    md = markdown.Markdown(extensions=["extra", "toc", "sane_lists", "smarty"])
    html = md.convert(src)
    toc_tokens = md.toc_tokens

    # Pull the <h1> title and the italic byline out of the body flow.
    m = re.match(r"\s*<h1[^>]*>(.*?)</h1>\s*", html, re.S)
    title_html = m.group(1).strip() if m else a["title"]
    if m:
        html = html[m.end():]
    m2 = re.match(r"\s*<p>\s*<em>(.*?)</em>\s*</p>\s*", html, re.S)
    subtitle = m2.group(1).strip() if m2 else ""
    if m2:
        html = html[m2.end():]

    # Wikipedia table styling + horizontal scroll on small screens.
    html = html.replace("<table>", '<div class="table-wrap"><table class="wikitable">')
    html = html.replace("</table>", "</table></div>")

    html = crosslink(html, a["slug"])

    # Drop in a table-of-contents box just before the first section heading.
    toc_html = build_toc_box(toc_tokens)
    idx = html.find("<h2")
    if idx != -1 and toc_html:
        html = html[:idx] + toc_html + html[idx:]

    sub = f'<div class="mw-subtitle">{subtitle}</div>' if subtitle else ""
    content = (f'<h1 class="firstHeading">{title_html}</h1>{sub}'
               f'<div class="mw-body-content">{html}</div>')

    page = (DOC.replace("__TITLE__", a["title"])
               .replace("__HEADER__", HEADER)
               .replace("__SIDEBAR__", sidebar(a["slug"]))
               .replace("__CONTENT__", content)
               .replace("__FOOTER__", FOOTER))
    (ROOT / f'{a["slug"]}.html').write_text(page, encoding="utf-8")

    # Search-index entries: the article itself + every section heading.
    entries = [{"label": a["title"], "url": f'{a["slug"]}.html'}]
    def walk(tokens):
        for t in tokens:
            if t["level"] in (2, 3):
                entries.append({"label": f'{a["title"]} § {t["name"]}',
                                "url": f'{a["slug"]}.html#{t["id"]}'})
            walk(t.get("children", []))
    walk(toc_tokens)
    return entries


# --------------------------------------------------------------------------- #
#  Portal (index.html)                                                          #
# --------------------------------------------------------------------------- #

def build_index():
    cards = "".join(
        f'<div class="portal-card"><h3><a href="{a["slug"]}.html">{a["title"]}</a></h3>'
        f'<p>{a["desc"]}</p></div>'
        for a in ARTICLES
    )

    feat = next((a for a in ARTICLES if a["slug"] == HOME), ARTICLES[0])
    featured = (
        f'<div class="box featured"><h2>Featured article</h2>'
        f'{lead_excerpt_html(feat["slug"])}'
        f'<p style="margin-top:.6rem"><a href="{feat["slug"]}.html">Read more →</a></p></div>'
    )

    present = {a["slug"] for a in ARTICLES}
    dyk_items = "".join(f'<li>{d["html"]}</li>' for d in DYK_FACTS if d["slug"] in present)
    dyk = (f'<div class="box dyk"><h2>Did you know&hellip;</h2><ul>{dyk_items}</ul></div>'
           if dyk_items else "")

    n = len(ARTICLES)
    portal = f"""<div class="portal-hero">
  <h1>Welcome to the Terran Encyclopaedia</h1>
  <p>The free 3000 CE reference that anyone can read. Rendered into Reconstructed
  Late Combustion English by convention of the Historical Faculty.</p>
  <p><strong>{n}</strong> article{"s" if n != 1 else ""} on the Combustion Age (c. 1750–2140 CE).</p>
</div>

<div class="portal-two">
{featured}
{dyk}
</div>

<div class="portal-grid">{cards}</div>

<div class="box" id="about">
  <h2>About this edition</h2>
  <p>This is a static, offline reading edition of interlinked encyclopaedia articles
  written from the vantage of the year 3000 CE, looking back at our own era. The articles
  cross-reference one another and a shared apparatus of (invented) sources and scholarship.
  It is a work of speculative fiction.</p>
</div>"""

    page = (DOC.replace("__TITLE__", "Main page")
               .replace("__HEADER__", HEADER)
               .replace("__SIDEBAR__", sidebar("index"))
               .replace("__CONTENT__", portal)
               .replace("__FOOTER__", FOOTER))
    (ROOT / "index.html").write_text(page, encoding="utf-8")


# --------------------------------------------------------------------------- #
#  Assets                                                                        #
# --------------------------------------------------------------------------- #

CSS = """/* Terran Encyclopaedia -- Wikipedia-style clone */
*{box-sizing:border-box}
body{margin:0;background:#f8f9fa;color:#202122;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:15px;line-height:1.62}
a{color:#3366cc;text-decoration:none}
a:hover{text-decoration:underline}
a:visited{color:#795cb2}

/* ---- header ---- */
.mw-header{display:flex;align-items:center;gap:1rem;background:#fff;
  border-bottom:1px solid #a2a9b1;padding:.5rem 1rem;position:sticky;top:0;z-index:20}
.mw-wordmark{display:flex;align-items:center;gap:.6rem;color:inherit}
.mw-wordmark:hover{text-decoration:none}
.mw-globe{width:42px;height:42px;border-radius:50%;flex:0 0 42px;
  background:radial-gradient(circle at 32% 30%,#ffffff,#e6e8eb);border:1px solid #c8ccd1;
  display:flex;align-items:center;justify-content:center;color:#54595d;
  font-family:Georgia,"Times New Roman",serif;font-weight:700;font-size:1.05rem}
.mw-name{font-family:Georgia,"Linux Libertine","Times New Roman",serif;font-size:1.3rem;line-height:1.1}
.mw-tag{display:block;font-size:.7rem;color:#72777d;letter-spacing:.02em}
.mw-search{margin-left:auto;display:flex}
.mw-search input{border:1px solid #a2a9b1;border-right:0;border-radius:2px 0 0 2px;
  padding:.4rem .6rem;font-size:.9rem;width:min(46vw,320px)}
.mw-search button{border:1px solid #a2a9b1;background:#f8f9fa;border-radius:0 2px 2px 0;
  padding:.4rem .8rem;cursor:pointer;font-size:.9rem}
.mw-search button:hover{background:#eaecf0}

/* ---- layout ---- */
.mw-main{display:flex;align-items:flex-start;max-width:1400px;margin:0 auto}
.mw-sidebar{width:11.8em;flex:0 0 11.8em;padding:1rem .7rem 2rem;font-size:.8rem;color:#202122}
.mw-sidebar h3{font-size:.72rem;color:#54595d;font-weight:400;
  border-bottom:1px solid #eaecf0;margin:1rem 0 .3rem;padding-bottom:.2rem}
.mw-sidebar ul{list-style:none;margin:0;padding:0}
.mw-sidebar li{padding:.16rem 0 .16rem .4rem;line-height:1.3}
.mw-sidebar li.active a{font-weight:700;color:#202122}

.mw-content{flex:1 1 auto;min-width:0;background:#fff;padding:1.1rem 1.7rem 2.4rem}
@media (min-width:1000px){.mw-content{border-left:1px solid #eaecf0;min-height:80vh}}
.mw-content-inner{max-width:60rem}

/* ---- headings & text ---- */
.firstHeading{font-family:Georgia,"Linux Libertine","Times New Roman",serif;font-weight:400;
  font-size:1.95rem;line-height:1.3;border-bottom:1px solid #a2a9b1;padding-bottom:.2rem;margin:0 0 .25rem}
.mw-subtitle{color:#54595d;font-size:.85rem;font-style:italic;margin:0 0 1rem}
.mw-body-content h2{font-family:Georgia,"Linux Libertine","Times New Roman",serif;font-weight:400;
  font-size:1.5rem;border-bottom:1px solid #a2a9b1;padding-bottom:.2rem;margin:1.5rem 0 .6rem}
.mw-body-content h3{font-size:1.15rem;font-weight:700;margin:1.15rem 0 .35rem}
.mw-body-content h4{font-size:1rem;font-weight:700;margin:1rem 0 .3rem}
.mw-body-content p{margin:.62rem 0}
.mw-body-content ul,.mw-body-content ol{margin:.5rem 0 .5rem 1.7rem;padding:0}
.mw-body-content li{margin:.26rem 0}
.mw-body-content hr{border:0;border-top:1px solid #eaecf0;margin:1.3rem 0}

blockquote{margin:.4rem 0 .9rem 1.6rem;color:#54595d;font-style:italic;font-size:.95rem;padding:.1rem 0}
blockquote p{margin:.3rem 0}
blockquote strong{color:#202122}

/* ---- tables ---- */
.table-wrap{overflow-x:auto;max-width:100%;margin:.9rem 0}
table.wikitable{border-collapse:collapse;background:#f8f9fa;font-size:.9rem;border:1px solid #a2a9b1}
table.wikitable th,table.wikitable td{border:1px solid #a2a9b1;padding:.35rem .6rem;
  text-align:left;vertical-align:top}
table.wikitable th{background:#eaecf0;font-weight:700}

/* ---- toc ---- */
.toc{display:table;background:#f8f9fa;border:1px solid #a2a9b1;border-radius:2px;
  padding:.55rem 1.3rem .6rem .6rem;margin:1rem 0;font-size:.9rem}
.toc .toctitle{text-align:center;margin-bottom:.25rem}
.toc .toctitle h2{border:0;font-family:inherit;font-size:1rem;font-weight:700;margin:0;padding:0}
.toc ul{list-style:none;margin:0;padding-left:1.3rem}
.toc>ul{padding-left:.3rem}
.toc li{margin:.16rem 0;line-height:1.35}

/* ---- footer ---- */
.mw-footer{max-width:1400px;margin:.5rem auto 3rem;padding:1rem 1.7rem;
  border-top:1px solid #eaecf0;color:#72777d;font-size:.8rem}

/* ---- portal / index ---- */
.portal-hero{text-align:center;border:1px solid #c8ccd1;background:#f8f9fa;border-radius:3px;
  padding:1.7rem 1.2rem;margin-bottom:1.3rem}
.portal-hero h1{font-family:Georgia,serif;font-weight:400;font-size:2rem;margin:.1rem 0 .4rem}
.portal-hero p{color:#54595d;margin:.3rem auto;max-width:46rem}
.portal-two{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.box{border:1px solid #c8ccd1;border-radius:3px;padding:1rem 1.1rem;background:#fff;margin:1rem 0}
.box h2{border:0;font-family:Georgia,serif;font-weight:400;font-size:1.25rem;margin:0 0 .5rem;color:#000}
.box.featured{border-left:4px solid #3366cc}
.box.dyk ul{margin:0;padding-left:1.2rem}
.box.dyk li{margin:.45rem 0}
.portal-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem;margin:1.2rem 0}
.portal-card{border:1px solid #c8ccd1;border-radius:3px;padding:1rem 1.1rem;background:#fff}
.portal-card h3{margin:.1rem 0 .45rem;font-family:Georgia,serif;font-weight:400;font-size:1.2rem}
.portal-card p{margin:0;color:#333;font-size:.92rem}

/* ---- responsive ---- */
@media (max-width:999px){
  .mw-main{flex-direction:column}
  .mw-sidebar{width:100%;flex:none;display:flex;flex-wrap:wrap;gap:.2rem 1.4rem;
    padding:.6rem 1rem;border-bottom:1px solid #eaecf0}
  .mw-sidebar .sb-block{min-width:8rem}
  .mw-content{width:100%;padding:1rem}
  .portal-two{grid-template-columns:1fr}
  .mw-search input{width:40vw}
}
"""

SEARCH_JS = """(function(){
  var IDX = __INDEX__;
  var ARTICLES = __ARTICLES__;
  var input = document.getElementById('search-input');
  var dl = document.getElementById('search-suggestions');
  var map = {};
  IDX.forEach(function(e){
    map[e.label] = e.url;
    if(dl){ var o = document.createElement('option'); o.value = e.label; dl.appendChild(o); }
  });
  function go(){
    var v = (input.value || '').trim();
    if(!v) return;
    if(map[v]){ location.href = map[v]; return; }
    var lv = v.toLowerCase();
    var hit = IDX.filter(function(e){ return e.label.toLowerCase().indexOf(lv) >= 0; })[0];
    if(hit){ location.href = hit.url; }
  }
  var form = document.getElementById('search-form');
  if(form){ form.addEventListener('submit', function(ev){ ev.preventDefault(); go(); }); }
  if(input){ input.addEventListener('change', go); }
  var rand = document.getElementById('rand-link');
  if(rand){ rand.addEventListener('click', function(ev){
    ev.preventDefault();
    location.href = ARTICLES[Math.floor(Math.random()*ARTICLES.length)];
  }); }
})();
"""


def build_assets(index):
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "style.css").write_text(CSS, encoding="utf-8")
    article_urls = [f'{a["slug"]}.html' for a in ARTICLES]
    js = (SEARCH_JS
          .replace("__INDEX__", json.dumps(index, ensure_ascii=False))
          .replace("__ARTICLES__", json.dumps(article_urls, ensure_ascii=False)))
    (ASSETS / "search.js").write_text(js, encoding="utf-8")


# --------------------------------------------------------------------------- #

def main():
    global ARTICLES, CROSSLINKS
    ARTICLES = discover_articles()
    if not ARTICLES:
        print("No article markdown files found (everything matched EXCLUDE).")
        return
    CROSSLINKS = {a["title"]: f'{a["slug"]}.html' for a in ARTICLES}

    search_index = []
    for a in ARTICLES:
        search_index.extend(build_article(a))
    build_index()
    build_assets(search_index)

    print(f"Built Terran Encyclopaedia — {len(ARTICLES)} articles discovered:")
    for a in ARTICLES:
        print(f"  {a['slug']}.html   ← {a['src']}   ({a['title']})")
    print("  index.html, assets/style.css, assets/search.js")
    print(f"  ({len(search_index)} search entries)\n\nOpen index.html in a browser.")


if __name__ == "__main__":
    main()
