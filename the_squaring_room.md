# The Squaring Room

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from a single reel of eight-level punched paper tape holding the nightly settlement record of one provisioning depot, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Squaring was a nightly inter-depot settlement run by an automated clearing machine, and its reel of paper tape records, in a repeat-count code, how steadily the volume of distinct transactions fell until the machine was balancing one depot against itself.** The tape and its parity are record; the machine, its staffing, and the name of the practice are reconstruction.

---

The Squaring was not an audit, and it was not a count of stock. It was a nightly close in which a clearing machine matched every depot's issues against every depot's receipts and punched the differences to tape. It began in +92 pT (2037 CE), ran for forty-three years, and by its last three produced a record shorter than a hand. The name appears on one object only, a cast-bronze plate above the door of the machine room, reading SQUARING ROOM; no tape, form, or manifest uses the word.

## The code

Each line was 64 characters: depot pair, item, quantity, and a field for the count of immediate repeats. Run-length coding of this kind costs 8 characters per run and saves 64 for every line the run absorbs, so it pays only when lines repeat. On a stream with no repeats it expands, as it must: no lossless code shortens every input. Every frame carried seven data bits and an eighth even-parity hole, which detects any single-bit punching error in a frame and corrects none. Of the frames read, none fails parity.

## The shrinking

| Year | Lines/night | Mean run | Raw (characters) | Coded (characters) | Ratio |
|---|---|---|---|---|---|
| +92 (2037 CE) | 1,000 | 1 | 64,000 | 72,000 | 0.89 |
| +104 (2049 CE) | 1,000 | 3 | 64,000 | 24,000 | 2.7 |
| +116 (2061 CE) | 800 | 14 | 51,200 | 4,100 | 12.4 |
| +127 (2072 CE) | 120 | 40 | 7,680 | 216 | 35.6 |
| +132–135 (2077–2080 CE) | 1 | 1,100 | 70,400 | 72 | 978 |

The coded length of a stream approximates its information, and the information fell because the world it described stopped varying. The first row is a machine facing near-incompressible demand; the last is one line, one item, one run. For 1,100 nights the Squaring balanced a depot against itself on flat washers, 6 mm, and balanced. The run occupies 72 frames, about 18 centimetres of tape. Okonkwo, D., reads the column as an unintended census, and Ibarra, N., reads the same depot as single-filament infrastructure at the scale of a stockroom; the tape supports both and the ratio decides neither.

## Survival

The machine's printer was meant to carry the record, but the last ribbon consignment was of the wrong width, and the machine fell back to its tape punch, a fallback not exercised since commissioning. Paper tape holds information as geometry, so yellowing and acidity leave it readable. The reel was filed by the clerk under its item field, and survives because it was shelved in the bin of flat washers, 6 mm, in a stockroom nobody ever counted.

---

## Provenance and ground

One reel, recovered from a collapsed stockroom; read optically by Halvorsen, E.'s laboratory. The machine's printed record, kept on thermal paper, is blank.

## See also

- **The Night-Charge Ledger**
- **The Reckoner's Ledger**

## Notes

1. Coded size is 72 characters per run (64 plus an 8-character count field); the ratio is raw divided by coded.
2. The earlier designation "the Washer Run" is deprecated. The tape ends with a closed count field of 1,100 and no following run; whether a 1,101st night was balanced is not recorded.
