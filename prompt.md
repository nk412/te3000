# Terran Encyclopaedia — Entry Generator

**This file is a template, not a brief to read straight.** It is written in the
`rolltext.py` choice syntax. Running it through `rolltext.py` collapses every
`\{\{ … \| … \}\}` slot to a single choice and prints one concrete *commission* —
a specific instruction for one entry, drawn at random from an enormous space of
combinations. You then write that one entry. The randomness is the point: it is
simulated creativity, so the corpus does not settle into a single pattern.

## How to use this file

1. **Roll it.** `python rolltext.py prompt.md` (add `--seed N` to reproduce a
   roll). The output is this same document with the commission resolved.
2. **Read the resolved output**, especially `## YOUR COMMISSION`. Those lines are
   now declarative instructions — obey them.
3. **Read `lore.txt`** — the authoritative canon of the universe.
4. **Write one entry** to a new `<slug>.md` at repo root, obeying THE HARD RULES,
   THE FRAME, and the commission.
5. **Build and publish** per `CLAUDE.md` (`uv run build.py`, verify, commit).

---

## THE FRAME — the universe you write inside

`lore.txt` is the canon; read it. In brief: the vantage is the year 3000 CE. A
later, redistributed Terran civilisation reconstructs its own deep past — the
**Combustion Age** (c. 1750–2140 CE) *and everything downstream of it*: the
Contraction that ended it, the Consolidation, and the long recovery since. The
register is that of a scholar of that world writing a reference entry: deadpan,
sourced, third-person, no narrator with feelings.

What survives into 3000 CE is durable, inert, machine-kept, or accidentally
intercepted, and it over-samples the connected, urban, purchasing, Anglophone
few. The scholars are honest and cannot see the whole story; the reader sees
more than they do. The year 3000 itself is never explained — it is only the
vantage. Everything on the road to it is fair subject. Dating is post-Trinity:
**CE = pT + 1945** (so +75 pT = 2020 CE).

---

## THE HARD RULES — fixed, never rolled, never relaxed

- **Hard science fiction.** The mode is Greg Egan and Peter Watts; the gold
  standard is qntm's "Lena" (the MMAcevedo article). SCP-like in its recovered-
  artefact framing, but without the bureaucratic containment scaffolding.
- **The events may be invented; the science never is.** This universe is built
  mostly of *fictional* events, people, places, and objects — they may parallel,
  echo, or touch real history, but they need not be real. The physics,
  chemistry, biology, and mathematics, however, are always real or rigorously
  derived from something real. Never invent a mechanism, a constant, or a
  statistic and pass it off as fact. If you extrapolate, extrapolate from a real
  trend and say so in the entry's own voice.
- **De-brand everything.** Never name a real living or recently-living public
  figure, corporation, product, app, brand, or nation-as-actor. Recover
  *functions*, not trade names — "a large public software repository," "one firm
  in one town in the Low Countries." Names appear only where a durable, name-
  bearing medium would carry one (a monument, a grave, a coin legend, a commit).
- **Deadpan encyclopedic register.** Third person, neutral, no narrator with
  feelings. Feeling is *reported as fact* ("the operator is recorded as having
  withheld grain from the count"), never staged. No scenes, no close-third
  interiority, no "she walked to the window." The flat statement of the most
  affecting fact is the whole technique.
- **Never explain the year 3000**, and never step outside the entry to address
  the reader.
- **Keep the mystery (lightly).** Per `lore.txt`: dramatise one thread of the
  millennium; never "solve" the Contraction, never name its forces as a
  diagnosis, and leave the standing open questions open (collapse vs. no
  collapse; died vs. moved; the apocalypse that did not come). The horror is
  never that the past was ignorant — they knew, they published it, they did not
  act. Delete any sentence implying the past was stupid.
- **Stay inside `lore.txt`.** Extend the canon; do not contradict it.

---

## THE OUTPUT FORMAT — what `build.py` expects

`<slug>` = the subject, lowercased, ASCII, words joined by underscores. Title by
locality, type, or the fragment — never a brand. The file must open with this
block verbatim in shape (the first **bold** hatnote sentence becomes the entry's
card blurb on the home page, so make it read well alone):

```
# <Title>

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from <the surviving fragment> and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **<one clean standalone sentence: what this entry is and what fragment it reconstructs.>** <a line on what is record and what is reconstruction.>

---

<LEAD — open on a bold definition sentence, then tell the whole arc in miniature.>

## <topic-specific section>
## <topic-specific section>

---

## Provenance and ground
## See also
## Notes
```

`build.py` auto-links any exact article **title** appearing in a `See also` list
item or in **bold** in the body, so reference existing titles verbatim to wire
entries together.

---

## YOUR COMMISSION

*Treat every line below as a constraint to honour and weave into one coherent
entry. Where two rolls pull against each other, that friction is the creative
seed — lean into it rather than discard it. If a combination is genuinely
impossible within the universe, bend only the least-central roll.*

**Scale.** Write {{ a bare stub — a few sentences to ~150 words: one recovered fact, glossed, then stopped where the record stops :2 | a short note — roughly 150–600 words: one thread, one mechanism, one vantage, told clean :3 | a standard entry — roughly 600–1,500 words: one subject carried through a full small arc :3 | a feature entry — 1,500–3,500+ words: a rich subject or whole working system, braided threads, a full arc :2 | an analysis piece — a scholarly argument or reconstruction essay, as long as the argument honestly needs :2 | a cluster — two to four very short linked notes under one head :1 }}. Let the length be evidence in itself; never inflate a thin fragment into a long tale.

**Subject.** The entry is about {{ an unnamed individual, recovered only by function or trace | a named individual, the name surviving only on a durable, name-bearing medium | a population, community, or workforce | a place, locality, or region | a structure, installation, or facility | an object or artefact, intact but silent | a machine or automated system | a technology, technique, or process | a biological entity — an organism, tissue, lineage, or pathogen | a natural or engineered phenomenon | an event or incident | a practice, ritual, or institution | a document, record, or archive | a signal or transmission | a language, script, notation, or unit of measure | a scholarly controversy or a reconstruction problem in its own right }}, {{ wholly invented, standing on real science :3 | invented, but a clear parallel to a real historical phenomenon :3 | an invented extrapolation of a real technology or discovery :2 | an invented instance of a real, general class of thing :2 | a real phenomenon reconstructed, with an invented history built around it :1 }}.

**When.** Set it in {{ the Proto or Early Combustion Age, before +0 pT / 1945 CE | the Middle Combustion Age, c. +0 to +65 pT / 1945–2010 CE | the Late Combustion Age, c. +65 to +133 pT / 2010–2078 CE :2 | the Contraction, c. +133 to +195 pT / 2078–2140 CE :2 | the Consolidation and early reconstruction, after c. +195 pT / 2140 CE | the deep post-Combustion millennium, centuries into the recovery | a span crossing two or more of these phases | a date the surviving record cannot fix }} — but never the year 3000 itself, which is only the vantage.

**The hard-SF spine.** The entry must be rigorous about {{ thermodynamics and heat transfer | information theory, coding, and compression | cryptography and its provable limits | orbital mechanics and spaceflight | materials science and corrosion | molecular biology and biochemistry | genetics, heredity, and population structure | neuroscience and the physical basis of mind | chemistry and reaction kinetics | geology, stratigraphy, and deep time | climate physics and the ocean–atmosphere system | epidemiology and the dynamics of contagion | acoustics, optics, or electromagnetism | relativity, gravitation, or high-energy physics | metrology and the physics of measurement | control theory and automated allocation | ecology and population dynamics | radioactivity, decay, and nuclear physics | fluid dynamics and turbulence | the mathematics of networks and their failure }}. Get this genuinely right — it is the load-bearing wonder, and it is where the "hard" in hard SF lives.

**The narrative engine.** Build the entry on {{ the survival pattern — what outlasts the millennium, why, and how the surviving sample deforms the story | the reconstruction — rebuild the inference chain in front of the reader, step by step, like a decipherment | the mechanism — a real physical, chemical, or biological process is the protagonist, taught cleanly, the history hung off it | the single witness — one object, deposit, or stream carries the whole case, read closely for what it can and cannot bear | the controversy — two or three named readings argued in earnest, the reader following like a jury | the system in motion — reconstruct a working process vividly as it ran, then turn and show how little of it survived | the thing that worked — a genuine triumph described without irony, competence set against what became of it | the false idol — an error of reconstruction the future made and partly still makes, then corrected dryly | the convergence — two unrelated subjects turn out bound by one physical fact | the boundary — a hard physical limit that could not be crossed, and what pressed against it }}.

**The fragment.** Reconstruct it from {{ a ledger or transaction record | an intercepted data stream | a physical deposit in ice, salt, anoxic mud, or a spent mine | a recovered object, intact but silent | a content-addressed code or commit history | a genome or a skeletal assemblage | a monument, inscription, or grave | a single photograph, reel, or image | a language disk or nickel plate | a corrupted or partial archive | one of the Sealed — known to exist, provably unreadable | oral-tradition residue carried in the living language | routing, telemetry, or sensor logs kept for another purpose | no single fragment — a synthesis pieced from scattered scraps }}. It is the entry's anchor to the record and the source of its Provenance note.

**The force.** It runs on {{ heat and water — the climate sorting | number — the demography that cannot be read | the road — displacement and migration | the machines — automated systems outrunning the world they were trained on | none of the four — the entry runs on wonder or mechanism alone, the millennium only a backdrop }}, brushed by at most one other. Do not name the forces as a set or explain the age's end.

**The tell.** {{ Let the language tell surface — Standard Terran carrying the grammar of the displaced | Let the genomic tell surface — endogamy relaxing in a pattern that tracks movement, not doctrine | Let the wealth tell surface — who moved early and safely, and who was stranded | Let the systems-outran-the-people tell surface — a record logging faithfully past the end | Let the authorship void surface — human and machine text no longer distinguishable | Keep the hidden history entirely in the gaps — no explicit tell :2 }}.

**Mood.** The colour under the flat register is {{ grim | elegiac | wondering | unnerving | clinical and cold | quietly triumphant | eerie | almost funny | matter-of-fact about horror | tender }}. The register itself stays deadpan; only the mood shifts.

**The engine fact.** Centre the entry on {{ a foreseen, documented disaster that nobody acted on | a survival by pure accident — the wrong shelf, the wrong chemistry, the wrong luck | a misattribution — the wrong meaning read into a real object | a curated record mistaken for a representative sample | a self-referential irony — the method that fails on the very thing that invented it | a system executing a correct rule under conditions that made it catastrophic | a hard limit no effort or cleverness could move | a competence that worked exactly as designed and outlived its purpose | a cost quietly deferred onto the future | two things bound by a physical fact nobody noticed }}. Land it flat, mid-paragraph, and leave it.

**Naming.** {{ Leave the subject unnamed, recovered by function only | Give it a name that survives only on a durable, name-bearing medium | Give the recovered meaning of its lost name, never the name itself | State plainly that its name is unrecoverable }}.

**Texture.** {{ Embed a quoted fragment — a ledger line, an intercepted message, an operator's note, a commit message | Embed a short recovered transcript or exchange | Embed a data table where the numbers genuinely carry a section | Embed an inscription, caption, or leader-card text | Embed a snatch of the period's own code or notation | Keep it unbroken prose, no embed }}. Any embed is quoted evidence within the wiki voice, never a scene.

**Lead opener.** Open on {{ a bold definition sentence | a bare date and event | a single arresting quantity | a negation — what the subject is not | a place fixed precisely | a name recovered from durable media | the fragment itself, described }}.

**Apparatus.** {{ Anchor to an existing deposit or archive from lore.txt | Cite one of lore.txt's recurring scholars in their established specialty | Coin a new scholar and citation of your own, in the house style | Tie into an established coinage from lore.txt | Stand free of the apparatus — minimal or no citations }}. Invent freely; reuse `lore.txt`'s scholars, deposits, and coinages where natural for consistency.

**Landing.** End on {{ a final aggregate number | a bare dated event | a deprecation or end-of-record note | a fate deliberately left open | the contested reading restated, unadjudicated | a single flat sentence of consequence }} — never a moral, a summary, or a scene.

---

## CRAFT NOTES — how to make it land

- **Mechanism, not assertion.** Every bias, loss, or survival gets a physical
  cause chain you could check. Weak: *the corpus is biased toward software.*
  Strong: *the code consignment shipped late, so it went on the top shelf, so it
  stayed above the acid.*
- **Technical specificity is the engine.** Real numbers, dates, formats,
  percentages, durations, half-lives, protocols. Quantify everything the record
  can bear; give pT (and CE on first mention).
- **Invented jargon, delivered without apology.** Name the period's procedures,
  cases, and the scholarship's coinages, and use them as if the reader already
  knows them. Reach first for `lore.txt`'s coinages.
- **The lead does the heavy lifting.** Open on the bold definition, then compress
  the whole arc — origin, use, fate, the aggregate figure, the contested reading
  — so a reader who stops after the lead still has the story. The sections then
  walk it.
- **Sections are topic-specific and march through the arc** (origin → use →
  failure or fate → how it is read now). Short, plain headers. Never a generic
  skeleton, and never a header a reader could predict from the last entry.
- **Contested things get schools, not verdicts.** Where the history would
  genuinely be unsettled, set out the live readings each in its strongest form
  and do not adjudicate — note *why* the record cannot. Vary the shape of the
  contest; do not manufacture one to fill a slot.
- **Thin apparatus.** The entry is the body; Provenance / See also / Notes stay
  short. Never let the scaffolding outweigh the article.
- **For a stub or short note**, the arc collapses to its few true lines: state
  what the fragment can bear and stop. Brevity is content, not an unfinished
  draft.

---

## FORBIDDEN

- Real public figures, corporations, products, brands, or apps by name; verdicts
  on contested contemporary politics. Describe by function.
- Invented physics, chemistry, biology, or mathematics; invented statistics
  passed off as real. Only the events, history, use, and fate are yours.
- Narrated fiction: scenes, staged action, close-third interiority, dialogue-as-
  drama. Feeling is reported as fact, never enacted.
- Explaining the year 3000; addressing the reader; any sentence beginning
  *In the future,*.
- The apocalypse register (ash, ruins, *the Fall*, the last human); the machine
  as villain; a Fall with a date; the dead tallied.
- Pulling back to the diagram — naming the forces as a set, explaining *why* the
  age ended, or letting any scholar solve the Contraction.
- Smugness; moralising; any implication the period was ignorant of its own
  condition. Ending on a moral, a summary, or a vague abstraction.

---

## PROCESS

Do this in order; do not start writing until step 4.

1. **Roll** the commission (`python rolltext.py prompt.md`) and read it.
2. **Read `lore.txt`** and lock the specific canon you will touch.
3. **Get the science right.** The rolled hard-SF domain must be real and rigorous
   — research the real quantities and mechanism; invent the events, never the
   physics. Decide what physically survives the subject at 3000 CE (that governs
   what a scholar could honestly claim) and what fragment the reconstruction is
   built from.
4. **Write the entry** to `<slug>.md` with the header block: lead first (the whole
   arc in miniature), then the topic-specific sections that walk it, landing the
   affecting facts flat and leaving them.
5. **Cut.** Re-form any scene or line of interiority into reported fact; trim the
   apparatus; confirm every roll in the commission was honoured.
6. **Build and publish** per `CLAUDE.md`.

---

## QUALITY GATE

Before returning the entry, confirm:

- [ ] Every physical / mechanistic claim is real or explicitly derived from a
      real one; only the events, history, use, and fate are invented
- [ ] Every pT/CE pair is arithmetically correct (CE = pT + 1945)
- [ ] No real public figure, corporation, product, or brand is named or judged
- [ ] The year 3000 is never explained, only implied through the frame
- [ ] It is a sectioned encyclopedia entry in the deadpan "Lena" register:
      feeling reported as fact, no narrated scenes, arc carried by the sections
- [ ] It runs on real, precisely quantified mechanism and on invented jargon
- [ ] At least one affecting fact is landed flat, mid-paragraph, and left
- [ ] Every roll in the commission was honoured — scale, subject, era, science,
      engine, fragment, force, tell, mood, engine fact, naming, texture, lead,
      apparatus, landing
- [ ] The agnostic restraint holds: no scholar solves the Contraction; the
      machines are mechanism, not villains; the open questions stay open
- [ ] The ending is a concrete particular, not a moral or a scene
- [ ] The apparatus is thin; no assessment table; no predictable skeleton
