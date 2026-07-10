# Code Deposit

*Terran Encyclopaedia, 3000 CE edition. Rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Code Deposit is the single surviving snapshot of the Combustion Age's public software: every openly shared program on one large repository, copied in a day and shelved for a thousand years — the most complete text the period bequeathed, and among the least representative.** For the mountain that kept it, and the accident of shelf height that let it, see **Longyear Deposit**. For the intercepted-traffic corpus it is habitually set against, see **Wasatch Corpus**. For what became of everything the snapshot did not catch, see **Attrition, the**.

---

On a Sunday in early +75 pT, a large public software repository copied every project it hosted openly — on the order of 21 × 10¹² bytes, several tens of millions of separate works — onto photographic film, and sent the film to a coal working at 78° N. The copy ran to 186 reels. It is bit-exact and self-verifying; a thousand years have altered nothing in it that can be detected, because the encoding was built so that any alteration could be. It is the fullest, cleanest, most literally trustworthy text the Combustion Age has left. It is also made, in its entirety, of instructions for machines.

That is the difficulty the article exists to state. Every other body of the period's writing reaches us in fragments — biased, corrupted, undateable, contested line by line. This one corpus arrives whole, and the temptation, indulged for the better part of two centuries, has been to read the whole of it as the age's testament: the thing it chose, deliberately, to send forward to us. It chose nothing of the kind. The snapshot was copied not because anyone had weighed it against a thousand years and found it worthy, but because it was the one large body of text a private firm already held in a form that could be shipped north in an afternoon. What survived is not what the period valued. It is what the period had already made machine-readable and public, which is a different quantity, and the distance between the two is the subject of this entry.

The programs themselves, read as programs, tell us remarkably little about the people who wrote them. What tells us a great deal is the bookkeeping wrapped around the programs — who changed what, on which day, by a clock set how many hours off a global reference — a record that nobody curated, that nobody addressed to us, and that nobody at the time considered a record at all. The code is the monument. The metadata is the witness. Most of this article is about the difference.

---

## The copy that checks itself

The repository did not store files. It stored histories: for each project, the full succession of its states, and for each state a name computed from that state's own contents — a fixed-length fingerprint such that identical content always yields an identical name, and any change of content, however small, yields a different one. The names were chained. Each state's fingerprint was folded into the next, so that the fingerprint of a project's latest state depended, by construction, on every byte of every state that preceded it. The arrangement was designed to let a machine detect corruption in transit. It also lets us detect it across a millennium: a recovered file is exactly the file that was written if, and only if, it reproduces the fingerprint it was stored under — and the recovered files reproduce their fingerprints.

This is a claim available for no manuscript in Terran history. Every other textual tradition the discipline works with is a chain of hand copies, each free to introduce error, and the entire apparatus of textual criticism exists to reason backward through the accumulated errors toward an original that nobody holds. The Code Deposit has no errors to reason through. The recovered files are not excellent copies of the originals. They are the originals, bit for bit, as committed on a February morning in +75 pT — the one promise the period made to its future and kept exactly. The medium that carried them, the shelf height that sorted the reels, and the acid that took the rest are treated under **Longyear Deposit** and are not rehearsed here; what matters for the corpus is only the consequence, which is that where the film survived at all, it survived perfect.

What the snapshot froze was a single instant. It is a cross-section of one civilisation's public software as it stood on one day, sealed weeks before a respiratory pandemic that the corpus does not contain and could not have foreseen — the same pandemic that delayed the reels' shipment by some five months, and so, incidentally, stamped the corpus with the sharpest external date it carries. Nothing comparable exists for any other domain of the period's life. It is a Pompeii, and it is made of nothing but instructions.

The contrast the discipline draws is with the **Wasatch Corpus**, the period's other great surviving body of text, and the two are photographic negatives of one another. The Wasatch is a record of ordinary traffic — intercepted, unposed, overwhelmingly commercial, kept by a bureau that wanted to read it. The Code Deposit is deliberate, curated by its own authors, and public by design. One is what the period said of itself to machines without meaning to be overheard; the other is what it built for machines on purpose and left in the open. Neither, it should be said at the outset, was addressed to us.

## A library of parts

Read as a whole, the corpus is not a literature but an inventory of components. Its composition — reproduced faithfully into our own libraries, along with everything else, because the encoding reproduces everything — is lopsided in ways that are themselves the evidence: overwhelmingly one interpreted language; a very large number of very small packages; a great deal of it generated automatically rather than written by a hand; a great deal never executed by anyone; and, threaded through the whole of it, dependency — packages built upon packages built upon packages, in towers hundreds deep.

The age left its own demonstration of what that structure meant. In +71 pT a single author, in a dispute, withdrew an eleven-line routine that padded a string of text with leading characters — a function trivial enough to rewrite from memory in a minute, and depended upon, directly or through other packages, by a substantial fraction of the entire network. Construction halted across that network for the better part of a day, until the routine was restored. The event was filed, at the time, as a minor operational incident. It is in truth the plainest single illustration the period produced of a single-filament dependency: the same structural fragility the discipline traces in the age's agriculture and its fuel chemistry, here reduced to eleven lines and shrugged off within the day. Ibarra's model of single-filament infrastructure applies to it without a word changed.

The redundancy is the other diagnostic. The corpus holds, by one count, some fourteen thousand substantively identical copies of a routine for capitalising the first letter of a word. It preserves its own duplication perfectly, because it preserves everything perfectly, so that a great part of the largest text of the age is other parts of the same text.

For close to two centuries this material was read as the literature of the Combustion Age — because it was the literature that had survived — and a much-copied routine for padding a string became, and in popular treatment remains, the emblematic "text" of the period. Marchetti's demolition of that reading (2955) is now standard: the routine is emblematic of nothing except its own shelf. The corpus study that replaced the literary reading is Rautio's, which names the trap precisely — **the complete fragment**, a body of evidence at once exhaustive within its own narrow domain and a vanishing sliver of the civilisation that made it, whose very exhaustiveness is what tempts a reader to mistake it for the whole. *The Deposit is not a small sample of everything,* Rautio wrote; *it is everything of a small thing.*

## The census in the timestamps

The historically useful stratum of the Code Deposit is not the code. It is the metadata that the version-control system recorded around every change, as a matter of mechanism, and that no one thought to shape because no one thought of it as content at all.

Each change carried, at minimum, an author's chosen handle — rarely a legal name, in keeping with a corpus that is systematically pseudonymous — an address for reaching them, a short message describing the change, and two timestamps: the moment the change was authored and the moment it was recorded. Each timestamp was stored together with a numeric offset from a single global reference clock. That offset is the load-bearing datum. It is a tag of local time, and local time is a tag of place: the offset says, in effect, where on the turning planet the author's own clock was set when the work was done.

Aggregated across tens of millions of changes, the offsets resolve into a census. They give the distribution of the contributing population across the longitudes — and its severe concentration in a narrow band of them — with a directness no other source for the period approaches. Aggregated instead by hour of the local day, the same timestamps give the working rhythm: the shape of the working day, the twofold weekly trough of a two-day rest, the long thin tail of changes authored deep in the local night. This is the one layer of the entire corpus that is a genuine unposed sample of human behaviour, and it is unposed for an exact reason. Nobody composing a change ever regarded the timestamp on it as anything but plumbing, so nobody arranged it. The code was written to be seen. The timestamp was not, and that is precisely why it can be trusted.

The standard treatment is Okonkwo and Halvorsen's reading of the L-III commit metadata as a labour census (2981), which recovers from the offsets alone both the geography of the contributing population and the temporal shape of its working life, and, from the concentration, the outline of who was doing this work and who was not. The correspondence the discipline reaches for here is not the Bronze Age but the administrative archives that follow it: the palace tablets of a script we can read perfectly and which hold no literature whatever — inventories, ration lists, personnel rosters, the logistics of a society and nothing of its beliefs. The Code Deposit is such an archive, with the single peculiarity that it dates and indexes itself. We can read every line of it, and what it tells us is who was at work, and when, and almost nothing of why.

Ranganathan's formulation for the other corpus fits this one exactly inverted. Of the Wasatch he wrote: *we do not know what they said to each other; we know what was said about them to machines.* Of the Code Deposit the sentence runs the other way. We still do not know what they said to each other. We have, in full, what they said to machines — and it is addressed, every line of it, to the machine and not to us.

## What the corpus will not say

Set beside what the Deposit keeps — every instruction, exactly, without decay — the scale of what it omits is easy to overlook. It carries, in enormous and perfect detail, how the period's machines were told to behave. It carries almost nothing of why anyone told them to. There is, in the whole corpus, no sustained account of what the institutions that paid for the work were, what money was and what it was for, or what any of the authors understood themselves to be doing. The only natural-language prose in it is documentation and the short messages attached to changes, and both are written by programmers for other programmers: they explain the how to a colleague and take the why entirely for granted, because at the time the why did not need setting down.

The single exception is the one text in the corpus composed deliberately for a reader a thousand years off: the accompanying guide its authors called a *tech tree*, and which standard usage calls **the Instruction**. It is patient, lucid, and, in its own terms, a success — the finest artefact of its class the age produced. It is also, in one respect, the corpus's whole silence in miniature: it spends eleven pages on how a semiconductor is etched and not one on what a corporation was, or on why the people whose work it introduces were doing that work at all. It assumed its readers would have lost the machines and kept the world. The opposite is nearer the truth.

The de-branding this encyclopaedia practises everywhere is, for the Code Deposit, not a matter of style but a report of the evidence. We do not know, and cannot recover, the name of the repository. Its function is reconstructable in complete detail — a large commercial host of shared software, on which the world's programmers kept, versioned, and exchanged their work — but the name it went by is exactly the sort of thing that lived only on the perishable record, and it is gone. We hold every one of its files and cannot tell you what it was called.

## One change

Because every change is dated and attributed, the corpus can be read down to the single act. Consider one, recovered bit-exact from an upper-rack reel: a change authored at fourteen minutes past two in the morning, local time, by a clock set five and a half hours ahead of the global reference — an offset that places it over one subcontinent and very nearly nowhere else — under a handle that is an ordinary word and not a name, with a one-line message reading, in the period's English, *ok this actually works now*.

Everything in that sentence is certain. Someone was awake in the small hours, on a date we can fix to the day, somewhere beneath a particular meridian, and made one change to something, and believed — with evident relief — that it had at last come right. What the change was, whether it stayed right, what it was for, who they were, and why it had mattered enough to be awake for: none of that is in the corpus, and none of it survives anywhere else. The Code Deposit keeps the act, timestamped and de-named, and lets the reason go. It is the completest record the age left of itself, and this is what a complete record of the age turns out to be.

---

## See also

- Attrition, the
- Combustion Age
- Complete fragment, the
- Instruction, the
- Longyear Deposit
- Sealed corpora
- Svalbard bias, the
- Voyager Records
- Wasatch Corpus

## Notes and references

1. Rautio, J. (2968). *The Complete Fragment: The Code Deposit as a Corpus.* — The standard corpus study, and the source of §2's argument; coins **the complete fragment** for a body of evidence exhaustive within its domain and unrepresentative of everything beyond it. Displaced the older literary reading for good; occasionally faulted for treating the corpus's silences as more uniform than they are.
2. Marchetti, L. (2955). "Canon Formation Under Extreme Sampling Bias." *Historiography* 12: 201–228. — The demolition of the reading of a string-padding routine as a canonical text. Correct in method, and its object has still not caught up with it in popular treatment.
3. Okonkwo, D. & Halvorsen, E. (2981). "Timezone offsets as a labour census: the L-III commit metadata." *Journal of Anthropogenic Stratigraphy* 61: 402–466. — The reconstruction of the contributing population's geography and working day from the commit timestamps alone; the source of §3. The finest use anyone has made of the corpus's uncurated layer.
4. Ranganathan, V. (2963). *Reading the Wasatch Corpus: An Essay on Sampling.* 3rd edn. — Ch. 6 sets the two great corpora against each other, one preserved because somebody meant to be read, the other because somebody meant to read; the aphorism §3 inverts is his.
5. Ibarra, N. (2977). "Single-filament infrastructure and the centennial disposal programmes." *Journal of Anthropogenic Stratigraphy* 63: 201–244. — Cited in §2 for the dependency model the corpus's own withdrawal incident illustrates in eleven lines.
6. Institute for Deep Record Studies (2712–2884). *The Longyear Reels.* 40 vols. and continuing. — The standard edition; the recovered change quoted in the final section is catalogued here among the L-III upper-rack material.
7. Adeyemi, F. (2969). *A Reconstructed Grammar of Late Combustion English.* — Cited for the reading of the corpus's commit messages, the largest single body of dated, localisable, informal period English yet recovered; his caution that a language survived because it was already loud applies to this corpus with unusual force.
