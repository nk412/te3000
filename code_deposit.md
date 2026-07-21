# Code Deposit

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from the uncurated commit metadata of consignment L-III of the Longyear Deposit and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Code Deposit is the one bit-exact, self-verifying snapshot the Combustion Age left of its public software — a single Sunday's copy of every openly hosted project, on 186 reels of film — and the fullest surviving text of the age, legible as a record of its makers only in its timestamps.** For the archive it was shelved in, see **Longyear Deposit**; for the sampling trap it is the type case of, see the complete fragment. The bytes, offsets, handles, and messages are transcribed from the deposit; the single working day reconstructed from them is inference.

---

The Code Deposit is consignment L-III of the Longyear Deposit: one Sunday's snapshot of a large public repository of shared software, on the order of 21 × 10¹² bytes and several tens of millions of separate works, copied whole and written to 186 reels of silver-halide film. It reached the archive months late, was shelved high, and by that accident stayed above the acid and the flood that took most of what lay below it (the Svalbard bias). It is the completest text the age left behind, and more than nine parts in ten of all bit-exact surviving Combustion-Age text is on these reels.

The Deposit is bit-exact and self-verifying, and for the better part of two centuries it was read as the age's literature, because it was the literature that had survived. That reading did not hold. What the reels overwhelmingly contain is instructions, in one dominant interpreted language, for machines — and read as what they are, they testify to almost nothing about the hands that wrote them. The one layer that does testify was never regarded as content: the bookkeeping the storage tool attached to every change, in which the hour and the longitude of each edit survive by accident. Aggregated across tens of millions of changes, that bookkeeping resolves into a census — of who was awake, and where, and at work (Okonkwo & Halvorsen 2981).

The census leans hard. It records not who could write software but who had a machine, a fast line, and a wage or a spare night to give the work away in the open; whole spans of longitude, where most of the living were, stand nearly empty. It cannot be closed: a share of the changes cannot be assigned to a human or a machine author at all (Sarmiento 2986). And it keeps almost nothing of any single person — a handle, an hour, a place, and now and then one line of plain language — while the names are gone, the repository's own name among them.

## The copy that checks itself

The repository stored not files but histories. Each state of a project was named by a fingerprint computed from its own contents, and the names were chained, so that every recorded change either reproduced the fingerprint it was filed under or it did not. On the reels, every one of them does. Nothing in a thousand years has altered a byte the encoding could not have caught, and a recovered file is provably the original rather than a copyist's version of it — textual criticism, the discipline's ordinary instrument, has no purchase here and no work to do. More than nine parts in ten of all bit-exact surviving text of the period is L-III; against every other class of survival in the corpus, which the reader reconstructs through damage, the Deposit is read directly.

Its survival is a matter of shelf height. The consignment arrived at the archive months after it was written and was placed on the upper racks; when the chamber flooded and the coal seam's pyrite turned the standing water acid, the reels that stayed dry stayed legible, and these were among them. Had it come on time it would have gone lower, with the rest. The Deposit is the one promise the age is recorded as having made to whoever came after — a copy that could prove itself intact across any interval — and, on the evidence of the reels, it is the promise the age kept exactly. What it did not undertake to preserve was any account of the people who made it.

## A library of parts

The reels reproduce the repository with all its redundancy intact, and the redundancy is itself a finding. The bulk is written in one dominant interpreted language and composed of very many small packages — a great many of them a few lines long, a great deal of the whole auto-generated rather than authored, and a great deal never run at any point in its recorded life. Some routines recur in their thousands: roughly fourteen thousand near-identical copies of a routine for capitalising the first letter of a word are present, not as a text repeatedly chosen but as a machine faithfully preserving its own duplication. The corpus is a library assembled less from works than from parts, most of them small, many of them the same part.

Those parts sat in towers. A package could rest on a second, which rested on a third, down through depths no single author held in view. The clearest measurement of that structure is an incident its contemporaries filed as minor: in +71 pT the author of an eleven-line routine for padding a string withdrew it from the shared index during a dispute, and construction halted across much of the network for the better part of a day, because so much else was found to be standing, at some remove, on those eleven lines. The Deposit preserves the shape that made this possible — a single-filament dependency at the foot of a great deal of the whole — and preserves nothing of the dispute, or of the author, beyond a handle.

## Read as literature

For the better part of two centuries the Deposit was read as the age's literature — not by preference but by default, since it was the literature that had survived the Attrition, and a corpus that proves its own fidelity is a standing temptation to a reader with little else. The most-copied fragment in it, the few lines for padding a string, was discussed as though it were a canonical text; the fourteen thousand capitalise-a-word routines were read as a tradition. Marchetti (2955) took the reading apart: a text's frequency in L-III measures the machinery of its duplication and not the age's regard for it, and a routine copied by a build tool ten thousand times over is emblematic of nothing but its own shelf. Rautio (2968) named the trap for good — the complete fragment, a body of evidence exhaustive within its own narrow domain and a vanishing sliver of everything past it. "The Deposit is not a small sample of everything," Rautio wrote; "it is everything of a small thing."

The code testifies to one thing about itself readily, and to almost nothing about its makers. Even the single text in the consignment composed for a distant reader — the patient orientation guide its makers called a tech tree, the Instruction, the only Combustion-Age document known to have been written expressly for whoever would find it — spends its pages on how a machine was etched and how a system was raised, and not a line on who did the etching, or why. The programs were written to be read by machines, and at one remove by other builders; none of them was addressed to a historian, and the reconstruction proceeds against that grain.

## The census in the timestamps

What is legible about the people is the bookkeeping no one thought of as content. Every change in every history carries, as a matter of the tool's mechanism and not of anyone's intent, a handle chosen by whoever made it, an address, a short message, and two moments: when the change was written, and when it was recorded. Each moment is stored not as a bare instant but beside a number — the offset of the writer's own clock from a single global reference clock, the hours and half-hours by which local time ran ahead of it or behind.

That number is the whole of the census. A clock's offset is a tag of local time, and local time is a tag of place: to set a clock five hours behind the reference is to say, without meaning to say anything at all, where on the turning planet the writer was standing. No one composing a change regarded the offset as more than plumbing; no one shaped it, curated it, or addressed it to a reader. It is the one layer of the entire Deposit that is an unposed sample of what people did, and it is trustworthy for precisely the reason that makes it so — the code was written to be seen, and the timestamp was not (Okonkwo & Halvorsen 2981).

Sorted and stacked, tens of millions of offsets resolve into a distribution of the contributing population across the longitudes, and the distribution leans. It leans into a narrow band of the world's meridians, a few clusters where the great mass of the work was done, and thins to almost nothing across whole spans where, on any census of the living, most people were. The Deposit does not record who could write software; it records who held a machine, a fast enough line, and the wage or the spare night to spend giving the work away in the open. The band is the finding. The empty longitudes are also the finding, and the reconstruction lets them stand empty.

Sorted the other way — by the hour of the local day each change was made — the same timestamps give a rhythm rather than a map. The count rises through a local morning, dips at a midday hour, runs on through the afternoon, and falls away into evening; twice in every seven days it collapses to a trough and recovers, the two-day rest of a working week drawn without a word said about it; and along the floor of every night runs a long thin tail of changes made in the small hours, by people awake when the rest slept. It is a working life reconstructed from the exhaust of the work.

## The authorship void

The census is not clean, and cannot be, because not every handle is a person. A large part of the Deposit was produced by other programs rather than written by a hand, and some changes arrive at intervals too exact to be human — on the hour, to the second, a machine committing on a schedule under a name of its own. Those declare themselves by their regularity and can be stripped out. But between the plainly human and the plainly automatic lies a band that cannot be sorted: changes that might have come from a person or from a script wearing a handle, made in an age that had learned to render the one indistinguishable from the other and had not troubled to mark which was which.

This is the authorship void (Sarmiento 2986), the same limit that bounds the reading of the intercepted network traffic of the Wasatch Corpus: a stream can be read in full, every character of it, and still not yield who, or what, was speaking. For the census it is a margin that cannot be closed. The reconstruction flags the band, excludes what it must, and states the size of what it cannot place rather than folding it onto one side or the other. A census with a margin it cannot close is still a census; it is only one that reports the margin.

## One reconstructed day

Because the Deposit dates and attributes every change down to the single act, the census runs in reverse as readily as forward: from the aggregate down to one handle, and from one handle to one day. The standard demonstration case, reproduced across the literature, is a handle that is an ordinary word and not a name — the corpus is systematically pseudonymous, legal names the exception, and this is not one of them. Its every change, drawn into a single line, carries the same offset throughout: five and a half hours ahead of the reference, a value that sits over one subcontinent and very nearly nowhere else on the planet. The meridian is therefore fixed, and from the hours a day can be rebuilt.

The record holds a morning's work and an afternoon's, ordinary and evenly spaced. Then a gap across the evening — the hours in which a person eats, and is with whoever they are with, and is not at the machine. Then, past midnight, the handle returns: a run of changes close together now, the short hurried commits of someone circling one problem and not resolving it, each message flatter than the last. The final change of that night, timed at fourteen minutes past two in the morning local time on a date that can be fixed to the day, carries a message legible exactly as it was written: *ok this actually works now.*

From this the reconstruction recovers the meridian the clock was set to, the hour the thing was finally got right, and the plain relief in the one line. It does not recover the name, which lived only on the perishable record; nor what the thing was, nor whether it stayed right, nor why it had mattered enough to lose the sleep for; nor the name of the repository itself, which the Deposit reconstructs in complete function and cannot name at all. The handle is logged among the reconstructed, and the count goes on. There are tens of millions of them, each legible for one true thing and dark for all the rest, and the offset survives on every one.

---

## Provenance and ground

This is a reconstruction. The commit metadata is real, transcribed evidence: the handles, addresses, messages, timestamps, and clock offsets recorded around every change on consignment L-III. Reading the offsets as a labour census — geography from the longitude a local clock implies, rhythm from the hour of the local day — is the method of Okonkwo and Halvorsen. The aggregate distributions, the demonstrated handle, its +5:30 offset, and the message *ok this actually works now* are transcribed; the single working day assembled around them is inference. The ground is real throughout: content-addressed storage with chained cryptographic fingerprints makes the corpus bit-exact and self-verifying; the version-control system records an author-supplied clock offset with every timestamp as a matter of mechanism; and a clock's offset is local mean time, which is longitude. That a share of the corpus cannot be assigned to a human or a machine author at all is a genuine evidentiary limit, not a flourish (Sarmiento).

## See also

- Attrition, the
- Combustion Age
- Combustion-Age Languages
- Longyear Deposit
- Svalbard Seed Vault
- The Kharun Corridor

## Notes

1. Okonkwo, D. & Halvorsen, E. (2981). "Timezone offsets as a labour census: the L-III commit metadata." *J. Anthropogenic Stratigraphy* 61: 402–466. — The reconstruction of the contributing population's geography and working day from the commit timestamps alone; the method this entry works within.
2. Rautio, J. (2968). *The Complete Fragment: The Code Deposit as a Corpus.* — Coins the complete fragment; *"the Deposit is not a small sample of everything; it is everything of a small thing."*
3. Marchetti, L. (2955). "Canon Formation Under Extreme Sampling Bias." *Historiography* 12: 201–228. — The demolition of the reading of a string-padding routine as a canonical text.
4. Sarmiento, J. (2986). *The Unsigned Corpus: On Text That Cannot Be Assigned an Author.* — *"we can read every word of it and not say who, or what, was speaking."* The band of the census that cannot be sorted into human or machine authorship.
