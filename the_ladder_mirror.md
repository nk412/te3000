# The Ladder Mirror

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from the commit history of a replicated road register, preserved as a stack of laser-marked stoneware tiles in an engraver cabinet at 3,610 metres, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Ladder Mirror is the Historical Faculty's name for a hash-verified register of the households climbing an upland valley road in the Contraction, kept in step on eight roadside boards whose nightly self-checks failed six times as often at the top of the road as at the bottom, and for the 960 glazed tiles on which that register's history was written.** The register, its checks, and the failure counts are record; why the counts rise with the road, and who read them, are reconstruction.

---

**The Ladder Mirror is a content-addressed commit history of 11,962 objects, 2.1 megabytes packed, mirrored across eight small boards along a 214-kilometre valley road that rises from 940 metres to 3,610, and its name occurs nowhere in its own contents.** It was commissioned on 1 March +141 pT (2086 CE) to keep one book of who had come up the road and who had gone on, and to keep it identical in every house. Each board checked every object in it against the object's own name each night, and logged each disagreement. The log is the second book, and it was never read as one. Its soft disagreements, the ones that vanished on a second read, number 1,967 over the record, and they climb with the road: about 2.6 a year at the lowest house and about 15 at the highest, against a ratio of 6.1 that the weight of the air above the two houses predicts from physics older than the road. The record ends at the engraver's last tile, on 1 January +177 pT (2122 CE), fourteen years after the last human hand touched it. The scrub was still running. It was still finding what it found.

## The road and the book

The valley road ran north and upward from a lowland basin to a pass, and the households that used it were, in the register's own columns, coming from the south and going on to the north: the people of the plains who had left once the wells and the grid failed together, in the order that the money and the roads allowed. The register called them *households*, counted at the door of each of eight houses by a steward who wrote the count, the date, and the number who went on up the road. The houses are numbered 1 to 8 from the bottom and stand at 940, 1,480, 1,960, 2,330, 2,710, 3,050, 3,320, and 3,610 metres. House 1 recorded 14,380 households entering between +141 and +158 pT. House 8 recorded 9,806. The register keeps a column for households that went on, and it has no column for households that turned off to the spur settlements, stopped at an intermediate house, or did not arrive. The difference of 4,574 is therefore all of those together and cannot be divided among them. The Faculty has not tried to divide it.

Each house had a board, of the cheapest class then made, with 512 mebibytes of unprotected memory and a flash store, and a short-range radio link to its neighbours that exchanged changes in a fixed pre-dawn window. The register was a repository: each month the steward's roll for that house was committed, and each month the board committed a summary of its own scrub. Every commit, every file, and every directory in it is named by a 256-bit digest of its contents, and each commit names its parent's digest, so that the whole history is one chain. A house that received a change from its neighbour could prove it was the change that had been sent. A house that held a stored object could prove, at any hour, that it was still the object it had been.

## The scrub

The scrub was a short program, which survives in full in the history, run at three in the morning: read every object from the flash store into memory, hash it, compare the result with the object's name. If they disagreed, read it again. If the second read agreed, record the event as *soft* and move on. If the second read also disagreed, record it as *hard* and fetch the object by name from the next house up or down, which could be checked on arrival against the same name.

A flipped bit in a hashed object changes about half the bits of its digest, and a 256-bit digest of the wrong bytes agrees with the right name with a probability of one in 2^256, so the scrub could not miss a flip and could not mistake one. What it could do was tell where the flip had been. A soft event is a flip in the memory between the store and the hash: the object on the flash was right, and the copy being read was wrong for the length of one read. A hard event is a flip in the store. The log holds 58 hard events in 36 years, each repaired from a neighbour, and they show no preference for any house. The 1,967 soft ones show a very strong one.

## What the air does to a bit

The physics the soft events obey was fully known to the age and is not in doubt. The top of the atmosphere is struck at some thousand particles per square metre per second by primary cosmic rays, about nine in ten of them protons, with kinetic energies from around a gigaelectronvolt upward, which makes them already relativistic: a one-gigaelectronvolt proton has a Lorentz factor of about 2.1. A primary meets an air nucleus after about 90 grams per square centimetre of air and shatters it, and the fragments shatter others, and a cascade falls through the column. Sea level is some 1,033 grams per square centimetre of air, a dozen interaction lengths, and by the time the cascade reaches the ground the primaries are gone. What arrives is its tail.

The tail has two parts, and they obey different rules. The first is muons, from the decay of charged pions made in the cascade. A muon at rest lives 2.2 microseconds on average. The mean muon that reaches sea level was made about 15 kilometres up and has an energy near 4 gigaelectronvolts, a Lorentz factor of about 39. Travelling at nearly the speed of light for 15 kilometres takes 50 microseconds, twenty-three lifetimes, after which one muon in ten billion should remain; with the clock of a muon running thirty-nine times slow, the journey is 1.3 microseconds of its own time, and a little over half survive. The muon flux at the ground, about one per square centimetre per minute, is the standing evidence of time dilation. It is also nearly harmless to a memory cell. A muon crossing a micrometre of silicon leaves about 0.4 kiloelectronvolts, roughly a hundred electron–hole pairs at 3.6 electronvolts each, or 0.017 femtocoulombs, in a cell that holds tens of femtocoulombs.

The second part is neutrons, made by spallation in the lower cascade, with energies from megaelectronvolts to a gigaelectronvolt. A neutron has no charge and so loses nothing by ionising; it passes a thousand nuclei and then hits one. When it hits a silicon nucleus the nucleus breaks, and the pieces, alpha particles and recoiling heavier ions, run a few micrometres and leave megaelectronvolts, which is 44 femtocoulombs for each megaelectronvolt at the same 3.6 electronvolts per pair. That is enough to flip a cell. At sea level in mid-latitudes the flux of neutrons above ten megaelectronvolts is of the order of ten per square centimetre per hour. It falls with the air above it as an exponential in the overburden, with an attenuation length that the age's own measurements put near 140 to 150 grams per square centimetre, and the age had measured it from the ground up: a city at 1,600 metres, where the overburden is 850, sees about three and a half times the flux of one at the shore. The soft event is the neutron's, not the muon's.

## What the houses counted

On the standard atmosphere, House 1 sits under 923 grams per square centimetre of air and House 8 under 661, and an attenuation length of 145 puts the neutron flux at the top at 6.1 times that at the bottom, and at about thirteen times the sea-level figure. The logged rates, in soft events per board-year, run 2.6, 3.9, 5.5, 9.1, 11.3, 13.3, and 15.1 for the houses that never moved, against predictions of 2.6, 3.9, 5.5, 9.1, 11.3, 13.3, and 15.8; the counts are small, and the Poisson scatter of the lowest house, with 44 events in all, is about a seventh. Pooled across the record, Okonkwo's regression of log count on overburden returns an attenuation length of 139 grams per square centimetre, with an uncertainty of 22, which contains the age's figure.

One board moved. The board of House 4 was lifted off its shelf at 1,960 metres and carried up to House 7 at 3,320 in the spring of +152 pT (2097 CE), and the commit that records it reads *h4 up to 7, same board, new shelf*. The overburden predicts a rise of 2.4 times. The board logged 4.4 soft events a year for its eleven years at the lower house, 48 in all, and 11.2 a year for its eleven at the upper, 123 in all, a rise of 2.5 times. The same commit also changes the board's power file from *mains* to *hydro-buck*, since House 7 had no mains.

Each house kept a barometer, entered by hand twice a day in the pass bulletin, because the pass above House 8 closed on falling pressure, and each board kept a scrub. The instrument that the stewards read to forecast the pass measures, in hectopascals, the weight of air standing on the house, and the same weight sets the scrub's error rate, at about 0.7 per cent of the rate for every hectopascal of fall; the book has the two columns on facing pages. The bulletins record the pass shut on 1,140 days in all.

## Three readings

The **hand-me-down** reading, argued by Halvorsen, holds that the boards were salvage, that the newest salvage went to the lowest houses, which were nearest the depots and the stewards, and the oldest to the highest, and that a worn memory misreads more. Memory wear is real, but it has a signature, a rate that grows with a board's age on any one board, and the log shows none. The reading's strongest ground is the log's own gap: the commit that moved House 4 does not say whether the board's memory was reseated, and a module that has been handled once is a module with a worse contact for the rest of its life.

The **supply** reading, argued by Marchetti, holds that every quantity that increases with house number will fit eight houses, and that the supply is the one that does: mains at the bottom, small turbines and buck converters in the middle, a spring-fed intake at the top, each rung with more ripple and more brown-out than the last. A memory read at a sagging voltage misreads for the length of one read. It explains the soft kind of event exactly, and it explains the move of House 4 as well, since the board changed its supply in the same commit. Marchetti, who is the scholar who showed that a trivial routine was not a canonical text, has no quarrel with the physics of the third reading, only with its being the only physics the data was entitled to.

The **overburden** reading, argued by Okonkwo, holds that the rise tracks the air, and rests on three things that the other two do not explain together: the slope, which fits; the move, which fits to within its scatter; and the barometer, whose coupling is of the right size and the right sign, though across 36 years and 1,967 events it is detectable only as a pooled slope and in no single storm. Okonkwo set the argument out in +1012 pT (2957 CE), and its summary is that the two columns of the book are one measurement taken twice.

The three cannot be separated by what survives. They agree on the slope, and they differ only on the one board that moved, which changed its shelf, its supply, and possibly its seating in one commit. The experiment that would have decided it, a board carried down the road with its supply carried up, was never made, and after +163 pT no one was left to make it. The supply and the overburden do not exclude one another, and the Faculty's standing position is that both were present.

## After the people

The last human commit in the Ladder Mirror is dated 14 March +163 pT (2108 CE), from the steward of House 8, under the identifier that signs 211 earlier rolls. Its message reads *roll 8: nine households in, none on. spares: 0. leave the scrub on.*

The scrub was left on. House 8's roll script, which appended one line to the roll each month from the steward's own entries, went on appending one line each month, and from April +163 the line is the same: *in 0, on 0*. It appears 166 times. The scrub of each house went on committing its monthly summary, and each summary contains a soft event count and a hard event count and the word *verified*, and the soft counts go on following the road's gradient for as long as a house has a neighbour to be compared with. The houses went dark in order of the grid and the intake: House 1 in +158 pT (2103 CE), House 2 in +159, House 3 in +160, House 4 in +163, House 5 in +166 (2111 CE), House 6 in +171, House 7 in +176 (2121 CE). House 8 outlived each of them, since its small turbine drew on a spring that did not freeze, and from +176 it had no neighbour to repair from and nothing to repair.

The history reached the tiles because the engraver at House 8, a laser marker feeding glazed stoneware from a magazine of 960 tiles that a steward loaded once, in +141 pT, was set to write the repository's new objects as a matrix code at the start of each quarter, 2,331 bytes to a tile at a medium level of error correction, and to stop when the magazine was empty. It did. The tiles run in order, with the first carrying a legend in the glaze, the only place that the register's name occurs:

> LADDER
> ONE BOOK, EIGHT HOUSES
> COUNT BEFORE YOU CLIMB
> RECOPY EACH HOUSE FROM ITS NEIGHBOUR

The word is in no object of the repository, and the Faculty uses it by the convention of the tile. Each tile after it carries, in its code, a bundle of the objects new in the quarter. The early bundles fill six or seven tiles, the late ones one.

## End of record

Tile 960 carries one commit, dated 1 January +177 pT (2122 CE), authored by the scrub of House 8: *h8 scrub: all objects verified. soft 1, reread clean. hard 0.*

---

## Provenance and ground

The magazine was recovered in +1006 pT (2951 CE) from an engraver cabinet in the pass house at 3,610 metres, where the cold and the dry had left the stoneware as it was marked, and decoded by the Institute for Deep Record Studies in +1011 pT (2956 CE). The tiles are physical record and decode without loss; the matrix codes' error correction was needed on 31 tiles and exceeded on none. The standard-atmosphere overburdens are the Faculty's arithmetic from the stage altitudes in the roll files, and they carry the uncertainty of a standard atmosphere applied to a real one.

## See also

- The Ascent Ledger
- The Ghaggar Sweat Line
- The Okello-Reyes Plate

## Notes

1. All dates are post-Trinity; CE = pT + 1945. Overburdens are in grams per square centimetre of air, 1 hectopascal being 1.02 of them.
2. The flux, attenuation, and shielding figures are the age's own and the Faculty's; the counts, the move, and the roll are the record's.
