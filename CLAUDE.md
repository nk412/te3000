# Terran Encyclopaedia — operating instructions

This repo is a static, Wikipedia-style site published via GitHub Pages. It is generated from
markdown entries in the **Terran Encyclopaedia** universe: a civilisation in the year 3000 CE
reconstructing the **Combustion Age** (c. 1750–2140 CE) *and the whole millennium downstream of
it* — the Contraction, the Consolidation, and the long recovery — from a thin, biased archive.
The entries are hard science fiction in the deadpan register of qntm's "Lena": mostly *invented*
events, people, and objects, built on *real* science.

## The files

- `lore.txt` — **the universe.** The authoritative backstory, canon, dating system, deposits,
  scholars, and the true (partly unrecoverable) history. World facts come from here. Read it
  before writing.
- `prompt.md` — **a `rolltext.py` template, not a brief to read straight.** Running it through
  `rolltext.py` collapses its `{{ … | … }}` slots into one random *commission* — the concrete
  spec for a single entry (scale, subject, era, science domain, engine, mood, fragment, and so
  on). It is the source of truth for entry *craft* (hard rules, forbidden list, quality gate).
  Roll it; obey the resolved output.
- `rolltext.py` — the roller. `{{ a | b:weight | c }}` picks one choice at random; choices may
  span whole paragraphs; `\{ \} \| \:` escape the specials. `--seed N` reproduces a roll.
- `build.py` — the generator. Auto-discovers every article `*.md` at repo root (anything not in
  its EXCLUDE set) and renders `index.html`, one `<slug>.html` per article, and `assets/`.
- `*.md` articles (e.g. `the_kharun_corridor.md`) — the entry sources you create.
- `*.html`, `assets/` — **generated output. Never hand-edit. Commit them (Pages serves them).**

---

## Primary task: "add an entry" (optionally on a given topic)

When the user asks to add / create / write a new entry, run this **whole pipeline autonomously** —
do not stop for confirmation between steps.

1. **Roll the commission.** `python rolltext.py prompt.md` (add `--seed N` only if the user wants
   reproducibility). The output is the full brief with one `## YOUR COMMISSION` resolved to
   concrete, declarative instructions. Those instructions are binding.
   - If the user named a **specific subject or topic**, honour it and take the rolled parameters
     (scale, era, science domain, engine, mood, fragment, tell, etc.) as its styling. Where a
     rolled slot genuinely fights the user's topic, the user's topic wins — bend that one slot.
   - If the user gave **no topic**, invent one that fits the rolled subject-type and reality-stance.

2. **Read the resolved `prompt.md` output in full and obey it** — the hard rules, the output
   format, the craft notes, the FORBIDDEN list, and the quality gate. Everything about entry craft
   lives there; do not restate it.

3. **Read `lore.txt`** and lock the specific canon the entry will touch. **Invent freely; reuse
   `lore.txt`'s scholars, deposits, and coinages where natural** for consistency. There is no
   ledger to maintain — the universe is fixed in `lore.txt`, and cross-entry variety is provided
   mechanically by the roll.

4. **Get the science right.** The commission's hard-SF science domain must be **real and
   rigorous** — research the actual quantities, mechanism, and constants with WebSearch / WebFetch
   as needed. The events, history, people, and fate are invented; the physics, chemistry, biology,
   and mathematics never are, and invented statistics are never passed off as real.

5. **Write the entry** to a new file `<slug>.md` at repo root. `<slug>` = the title, lowercased,
   ASCII, words joined by underscores (e.g. *The Kharun Corridor* → `the_kharun_corridor.md`).
   Title by locality, type, or the fragment — never a brand. It **must** begin with the header
   block `build.py` expects (this is `prompt.md`'s OUTPUT FORMAT — the source of truth):

   ```
   # <Title>

   *Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from <the surviving fragment> and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

   > **<one clean standalone sentence: what this entry is and what fragment it reconstructs.>** <a line on what is record and what is reconstruction.>

   ---

   <LEAD: open on a bold definition sentence, then give the whole arc in miniature.>

   ## <topic-specific section>   (sections march through origin → use → fate; deadpan wiki register — feeling reported as fact, no scenes)
   ## <topic-specific section>

   ---

   ## Provenance and ground
   ## See also
   ## Notes
   ```

   The hatnote's first **bold** sentence becomes the entry's card blurb on the home page, so write
   it to read well on its own. The entry is the body; the apparatus below it stays thin.

6. **Run the QUALITY GATE** at the end of `prompt.md` against your draft and fix every miss. In
   particular: every pT/CE pair is correct (CE = pT + 1945); no real public figure, corporation,
   product, or brand is named (describe by function); **every roll in the commission was honoured**;
   the agnostic restraint holds (no scholar solves the Contraction; machines are mechanism, not
   villains; the open questions stay open).

7. **Rebuild:** `uv run build.py`. Confirm it lists your new entry in the discovered set and exits
   cleanly.

8. **Verify** the output: grep `<slug>.html` to confirm the title, the section headings, and the
   `See also` cross-links rendered.

9. **Commit and publish** (below).

## Cross-linking

`build.py` auto-links any exact article **title** that appears in a `See also` list item or in
**bold** in the body. To wire a new entry into the web, reference other entries' exact titles
verbatim in your `## See also` and, where natural, in bold in the prose. On a fresh corpus there
may be nothing to link to yet; that is fine. Do **not** edit other articles to link *back* unless
the user asks.

## Build

- `uv run build.py` — idempotent; regenerates everything from the article `.md` files.
- If `uv` is unavailable: `pip install 'markdown>=3.5' && python3 build.py`.
- With **zero** article `.md` files present, `build.py` prints "No article markdown files found"
  and leaves the pages untouched — expected on an empty corpus; it builds normally once an entry
  exists.
- Edit `.md`, `prompt.md`, or `build.py` and rebuild; never edit generated `*.html` / `assets/*`
  directly.

## Commit & publish (GitHub Pages)

The site deploys from committed static files on the **`main`** branch, so the generated HTML must
be committed alongside the source.

- Stage: the new `<slug>.md`, all regenerated `*.html`, and `assets/`.
- Commit message: `Add entry: <Title>` (or `Update entry: <Title>`), ending with:

  ```
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
  ```
- Push directly to `main`: `git add -A && git commit -m "..." && git push`.
- Do **not** open a pull request; direct push to `main` is the deployment mechanism.
- Do this in one step after a successful, verified build.

## Guardrails

- Never name a real living or recently-living public figure, corporation, product, app, brand, or
  nation-as-actor — describe by function. (`prompt.md` hard rules + FORBIDDEN.)
- Events may be invented, but every physical / quantitative / mechanistic claim is real or
  explicitly derived from a real one. Never invent physics, chemistry, biology, or statistics.
- No verdicts on contested contemporary politics — state named schools, adjudicate nothing.
- Keep the mystery: dramatise one thread of the millennium; never explain why the age ended.

## Don't

- Don't hand-edit `prompt.md`, `rolltext.py`, `lore.txt`, `build.py`, existing articles, or the
  CSS as part of adding an entry — only add the new `<slug>.md` (and rebuild). Change those files
  only when the user explicitly asks.
- Don't ask permission before rolling / writing / building / committing a requested entry — run
  the full pipeline end to end.
- Don't commit or push unrelated changes.
