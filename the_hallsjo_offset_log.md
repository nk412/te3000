# The Hallsjö Offset Log

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from flow-accounting records kept by a cable landing station for the purpose of billing, cross-read against a protocol specification in the Code Deposit, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Hallsjö Offset Log is the Historical Faculty's name for the clear-text counters of a forty-one-link telemetry network of the +130s pT, whose payloads were enciphered with a one-time pad delivered by road every quarter for thirty-eight years, and whose counters, read as an accidental census, show the pad outlasting the road that fed it.** The counters, the frame lengths, and the timestamps are record; the content of every first-pass frame is permanently unreadable, and this entry reconstructs the practice that produced them from what a billing system happened to write down.

---

**The Hallsjö run** is the Faculty's name, by locality, for a quarterly hand-delivery of key material that no surviving document names. A gravel apron 3.2 kilometres north-east of the Hallsjö junction, at 63°41′ N, 14°12′ E, served from +133 pT (2078 CE) as the loading point from which sealed storage cartridges, generated in pairs from a physical noise source, were driven out to the two ends of forty-one authenticated telemetry links; a cartridge installed at an endpoint supplied, byte for byte, the key stream by which every frame crossing that link was enciphered and tagged. The scheme was the one construction in the period's cryptography whose secrecy was proved rather than assumed, and it performed as proved for thirty-eight years: no forged frame is recorded, and the network was indifferent to the later quantum breaking of the period's public-key methods, having never relied on them. It consumed one byte of key for every byte it protected, which is the whole of its theory and was the whole of its cost. The run was completed 152 times. It was then scheduled sixty more, and the schedule is the last thing in the record that was kept faithfully.

## The apron

The apron is known from the specification's site annex, which fixes it by coordinates and by a levelled surface of crushed granite 40 metres by 90, and from a land-registry entry in the Wasatch Corpus that records no building on it. Nothing stood there that the run required. The cartridges were loaded into steel cases at the apron from a generator hall whose location is not given; the cases were counted aloud by two persons against a manifest, a step the specification calls the *tally* and describes in nine words; and the vehicles left in convoy, never fewer than two, so that a breakdown would not leave a case unattended on a road. A run delivered eighty-two cartridges: two for each link, one to each end, identical in content. The specification states that a cartridge was to be overwritten in place as it was consumed, so that a seized endpoint would yield only the key it had not yet used, and the number of each run's completion was entered in a ledger the Faculty does not have.

## The key budget

Perfect secrecy has a price that was proved in +4 pT (1949 CE) and has not moved since. For a ciphertext to reveal nothing about its message, the set of possible keys must be at least as large as the set of possible messages; for messages of arbitrary content, this means a key at least as long as the message, drawn uniformly at random, and used once. A ciphertext of *n* bits is then consistent, under some key, with every plaintext of *n* bits, and no quantity of computation can prefer one to another. This is why the Sealed are undecipherable and not merely undeciphered, and it is why the network's designers paid for the road. The same result bars the obvious economy: key cannot be stretched, compressed, or regenerated from a short seed without ceasing to be a one-time pad and becoming an ordinary stream cipher, whose security is a belief about computation.

The network's load fixes the rest. Each link carried 120 frames a second, each of 2,400 bytes of waveform samples and headers, plus an 8-byte authentication tag, for 2,408 bytes of key per frame and 288,960 per second: 24.97 gigabytes a day, 9.11 terabytes a year. The tag was a polynomial hash over 300 eight-byte words, masked with fresh key, which bounds the chance that a forger's frame is accepted at 300 divided by 2⁶⁴, about 1.6 × 10⁻¹⁷, regardless of the forger's computing power. A cartridge held 2.5 terabytes, 2,499,999,999,840 bytes of it usable, which is 1,038,205,980 frames, which at 120 frames a second is 100.1 days. The road was driven every 91.25 days. The margin was 8.9 days, and it was the margin of the network's whole security, since it was the interval by which the pad was always longer than the message. No change to the design could enlarge it except a larger cartridge or a faster road.

## Thirty-eight years

The run was kept on the quarter for 152 consecutive quarters, through the heat windows of the +120s and the first load-shedding of the +140s, by convoys whose vehicle counts, drawn from the station's own gate records, rose from two to four after +149 pT (2094 CE). Okonkwo, D., who established the log's use as evidence, reads the convoy cadence as the steadiest institution in any regional record of the period: 152 completed runs against 152 scheduled, the longest slip being nineteen hours. The network's tag-rejection counters, mirrored in the same billing records, show three rejected frames in thirty-eight years across all links, each coincident with a recorded burst of line noise, none repeated. The Faculty treats this as a triumph without qualification. It was a procedure that cost a road, a hall, a surface of granite, and several hundred persons' working years, and it did what it cost.

## Revision seven

Each frame carried, in clear, its link, its sequence number, the offset into the cartridge at which its key began, and its length; the receiver needed the offset and had no other way to know it. These fields are what a landing station's flow accounting, counting traffic for payment, copied into its own table. The specification's third revision defined the endpoint's behaviour at exhaustion in one branch:

> `if (ofs + len > CAP) { enter(QUIET); return; }`

QUIET transmitted nothing but an eight-byte keepalive tagged from a reserve of 4,096 bytes set aside at the end of every cartridge, and held until a new cartridge was seated. Revision seven, committed in +161 pT (2106 CE), replaced the branch:

> `ofs = (ofs + len) % CAP;`

The revision's message field is empty. Its author field holds a 128-bit identifier of a kind the Faculty can assign neither to a person in the repository's earlier history nor to any known build process; the revision belongs to the class of commits the Authorship Void leaves unclassified. The effect of the modulus is exact. When the pad is exhausted the pointer returns to zero, and the cartridge is read a second time from its first byte.

## The second pass

The last completed run was number 152, in +171 pT (2116 CE). The first link to exhaust its cartridge, link 0417, did so in 2117, 100 days afterwards, and the landing station's table records the moment in three consecutive rows:

> `LNK 0417  SEQ 1038205978  OFS 2499999995024  LEN 2408  2117-04-09T03:12:07.125`
> `LNK 0417  SEQ 1038205979  OFS 2499999997432  LEN 2408  2117-04-09T03:12:07.133`
> `LNK 0417  SEQ 1038205980  OFS 0000000000000  LEN 2408  2117-04-09T03:12:07.142`

The last 160 bytes of the cartridge are discarded, which is consistent with the specification; the third row is the second use of the first byte of key. Seventeen of the forty-one links reached it. The consequence is arithmetic, and it is the period's own. Two ciphertexts made with the same key stream, added bitwise, give the sum of the two plaintexts, and the key vanishes from the equation. Because frame length was fixed, the second pass fell on the same offsets as the first, frame for frame, so that the Wasatch Corpus, which holds both passes of the seventeen links as ciphertext, holds each wrapped frame beside the frame it shares a key with. The network kept idle frames, of zero payload, for the hours of low load; a zero plaintext enciphers to the bare key. Where a first-pass idle frame lies under a second-pass frame, the second-pass frame is therefore readable outright, and 3.4 per cent of the wrapped frames are so placed. A larger fraction yields to cribs, since the waveform samples of adjacent frames differ by bounded steps; the Faculty gives no figure for it, because the figure depends on a judgement of plausibility that the mathematics does not supply. The first pass remains sealed, and the only sections of the entire network that can be read are the ones that were reused.

The longest wrapped stretch is ninety-seven days. Its readable frames are command and status traffic, and a minority of them are commands: imperative frames to breakers, in a fixed vocabulary, at the network's regular cadence, each answered by a status frame from the far end within a bounded time. The commands are issued and answered through the whole stretch. No operator-keyed frame, of the type that carried a human identifier in the header, appears in it.

## Sixty manifests

The convoy scheduler, a routing system whose logs survive in the Code Deposit as a fragment of its configuration, continued after the last run to issue manifests, numbered 153 through 212, one a quarter, to +186 pT (2131 CE). Each lists the cartridges required, the cases, the vehicles, and a draw from the generator hall's stock, which the scheduler's own inventory table, last updated in +171 pT, gives as zero. Each manifest was transmitted to the apron and acknowledged by a gate controller. The gate records show no vehicle.

## What the log is read to mean

Two readings hold. Ibarra, N. reads the run as the doctrine of single-filament infrastructure in its purest case: a network of forty-one links whose entire secrecy depended on one road and one hall, and which was therefore exactly as durable as the road. Zhou-Ferreira, A. reads the ninety-seven days of commands and answers as evidence that, on at least this network, nothing had stopped: the breakers were operated and the operation was confirmed for three months after the last cartridge was delivered, and the end of the archive is not the end of the grid. Both readings are consistent with every frame the Faculty can read, and the frames it cannot read are the ones that would decide between them. The Faculty also declines to assign revision seven to oversight, to design, or to a decision taken for the network's continuity; the commit does not say, and its identifier belongs to no one.

---

## Provenance and ground

The anchor is a landing station's flow-accounting table in the Wasatch Corpus, kept to bill for traffic and never intended as evidence, which preserves the clear headers of some 2.4 × 10¹⁰ frames; the specification and its eight revisions are in the Code Deposit, and their fingerprints prove them unaltered. The coordinates, the budget arithmetic, the tag bound, and the secrecy theorem are exact and independent of the reconstruction. Reconstruction, and marked as such, are the apron's use as a loading point, the composition of the convoys from gate records, the sixty manifests' fate, and everything said of what the wrapped commands operated.

## See also

- **The Channel Commit Log** — a repository's revision history read as the only surviving witness of a decision.
- **The Safe Halt** — the opposite choice at the same kind of boundary: a machine that stopped where this one continued.
- **The Governor Log** — a controller's counters kept faithfully past the point where they could be read by anyone.

## Notes

The 3.4 per cent figure counts frames whose first-pass partner was a zero-payload idle frame with a valid header; it does not count frames recovered by cribbing. Link 0417's wrapped stretch ends with the table's last row, a status frame, and the specification's header for revision seven carries the comment `DEPRECATED: QUIET branch (see rev 3)`:

> `LNK 0417  SEQ 2043901979  OFS 2421715965592  LEN 2408  2117-07-15T11:48:20.917`
