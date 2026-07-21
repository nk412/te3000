# Terran Encyclopaedia — operating instructions

This repo is a static, Wikipedia-style site published via GitHub Pages. It is generated
from markdown articles about the **Combustion Age** (a 3000 CE view of our own era).

- `prompt.md` — the authoritative brief for writing an article (role, canon, method, voice,
  structure, FORBIDDEN rules, quality gate, and the shared citation **ledger**). It is the
  source of truth for *how an article is written*. Obey it; do not restate it.
- `build.py` — the generator. Auto-discovers every article `*.md` at repo root and renders
  `index.html`, one `<slug>.html` per article, and `assets/`.
- `*.md` articles (e.g. `combustion_age.md`) — the sources you edit.
- `*.html`, `assets/` — **generated output. Never hand-edit. Commit them (Pages serves them).**

---

## Primary task: "add an entry on <TOPIC>"

When the user asks to add / create / write a new entry or article, run this **whole pipeline
autonomously** — do not stop to ask for confirmation between steps.

1. **Read `prompt.md` in full and follow it exactly.** It governs research, canon consistency,
   voice, structure, the FORBIDDEN list, and the quality gate. Everything about article *craft*
   lives there.
2. **Research the real facts** with WebSearch / WebFetch (prompt PROCESS step 1: ~20–30 real
   numbers and dates). The fiction is only in the interpretation — never invent physics,
   chemistry, biology, or statistics.
3. **Write the tale** to a new file `<slug>.md` at repo root. `<slug>` = the topic, lowercased,
   ASCII, words joined by underscores (e.g. *The Ballpoint Pen* → `ballpoint_pen.md`). It **must**
   begin with the header block `build.py` expects — copy the byline verbatim from an existing
   tale such as `the_kharun_corridor.md`:

   ```
   # <Title>

   *Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from <the surviving fragment> and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

   > **<one clean standalone sentence: what this tale is and what fragment it reconstructs.>** <a line on what is record and what is reconstruction.>

   ---

   <THE TALE — foregrounded narrative prose, in the vantage you chose; this is the body and the bulk.>

   ---

   ## Provenance and ground
   ## See also
   ## Notes
   ```

   The hatnote's first **bold** sentence becomes the tale's card blurb on the home page, so write
   it to read well on its own. Title by locality/type or the fragment itself, never a brand. The
   tale is the body; the apparatus below it stays thin, and `prompt.md` is the source of truth for craft.
4. **Run the QUALITY GATE** at the end of `prompt.md` against your draft and fix every miss.
   In particular: check each pT/CE pair (CE = pT + 1945), and confirm no real public figure,
   corporation, product, or brand is named — describe by function.
5. **Update the ledger.** If you introduced any new scholar, work, or coinage, append it to the
   "Established citations" and/or "Reusable facts and coinages" blocks in `prompt.md`, so later
   articles inherit it. This is the one step the prompt cannot self-enforce — do it every time.
6. **Rebuild:** `uv run build.py`. Confirm it lists your new tale in the discovered set and
   exits cleanly.
7. **Verify** the output: grep `<slug>.html` to confirm the title, the Contents box, and the
   `See also` cross-links rendered.
8. **Commit and publish** (below).

## Cross-linking

`build.py` auto-links any exact article **title** that appears in a `See also` list item or in
**bold** in the body. To wire a new article into the web, reference existing titles verbatim in
your `## See also` (e.g. `- Combustion Age`, `- Longyear Deposit`) and, where natural, in bold in
the prose. Do **not** edit other articles to link *back* unless the user asks.

## Build

- `uv run build.py` — idempotent; regenerates everything from the `.md` files.
- If `uv` is unavailable: `pip install 'markdown>=3.5' && python3 build.py`.
- Edit `.md` or `build.py` and rebuild; never edit generated `*.html`/`assets/*` directly.

## Commit & publish (GitHub Pages)

The site deploys from committed static files on the **`main`** branch, so the generated HTML must
be committed alongside the source.

- Stage: the new `<slug>.md`, all regenerated `*.html`, `assets/`, and the updated `prompt.md`.
- Commit message: `Add entry: <Title>` (or `Update entry: <Title>`), ending with:

  ```
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
  ```
- Push directly to `main`: `git add -A && git commit -m "..." && git push`.
- Do **not** open a pull request; direct push to `main` is the deployment mechanism.
- Do this in one step after a successful, verified build.

## Guardrails

- Never name a real living or recent public figure, corporation, product, app, or brand —
  describe it by function. (prompt §7 + FORBIDDEN)
- Every physical/quantitative claim is real or explicitly derived from a real one.
- No verdicts on contested contemporary politics — state named schools, adjudicate nothing.

## Don't

- Don't modify existing articles, `build.py`, or the CSS unless explicitly asked.
- Don't ask permission before writing / building / committing a requested entry — run the full
  pipeline end to end.
- Don't commit or push unrelated changes.
