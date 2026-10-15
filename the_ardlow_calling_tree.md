# The Ardlow Calling Tree

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from a children's counting rhyme and an idiom preserved in Standard Terran, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Ardlow Calling Tree is the Faculty's name for a flood-warning practice of one river valley, run by hand from +9 pT (1954 CE) and by machine from +39 pT (1984 CE), which worked for forty-odd years and then went on reporting success for the last thirty-eight months of its existence to an empty valley, reconstructed from a rhyme and a word.** The practice's design and its log are record; its purpose, and the rhyme's connection to it, are reconstruction.

---

**Orla Penhallow** is the only person the durable record attaches to the **Ardlow Calling Tree**: a cast-bronze tablet, recovered from the floor of a drained hall at the valley mouth, reads *"Flood Committee, O. Penhallow, Secretary, 1954. Two to ring and two to ring you."* The practice that the tablet describes had a name in its own day. That name is unrecoverable; no surviving medium gives it, and "calling tree" is the Faculty's term. Each of 212 listed households was assigned two others to telephone on a warning and was itself assigned two callers. It reached all but two of the 199 answering households in the valley in about forty minutes in the flood of +31 pT (1976 CE), and it fell silent between +50 and +59 pT (1995–2004 CE), when the households stopped answering. Its machine went on logging.

## Two to ring

The valley took its flood in the night of +8 pT (1953 CE), from a river that rose faster than any rider could cross it. The committee formed the following spring. A warning could be given in one call and carried in many: the secretary rang two households, each rang two more, and so on through eight levels, at about five minutes a level, which is where the forty minutes comes from (2⁸ = 256 exceeds 212).

A plain tree has a known weakness. A household is reached only if every household above it answered. In a full seven-level tree of 254 households in which nine in ten answer, about three-fifths of the answering households are reached. The committee's addition was the second caller: every household was rung by two others, ten minutes apart, and a household already warned told the second caller so.

The mathematics of this is the branching process on a directed graph. With two callers in and two out, and a fraction *q* of numbers answering, the share of answering households reached is 1 − ((1 − *q*)/*q*)², for *q* above one half and zero below it. At *q* = 0.96, the valley's figure in 1954, that is 99.8 percent. At 0.75 it is 88.9. At 0.6 it is 55.6. At 0.55 it is 33, at 0.52 it is 15, and at one half it is nothing. Redundancy raised the plateau; it did not move the edge. The edge sits where each answering household can on average pass the warning to just one other, and no arrangement of two-and-two can carry a warning below it.

## The plates

Each household carried a vitreous-enamel plate by the telephone, stamped from +10 pT (1955 CE) with three numbers in the form *R 14 / 31 · 52*: the household's own slot, then the two it rang. Enamel is a fused glass on steel, and several hundred plates survive on the valley's stone walls.

Eleven papers between 2661 and 2790 CE read the plates as a grading of households. In that reading the leading number was a rank, and the pair after it were the households of equal or lesser standing with which a house was permitted to deal, and the plates were taken as evidence of a stratified valley. The numbers are the dialling order, and the grading reading was set aside only when the plate numbers were laid against the log below. They match for 212 of 212 slots.

## The log

In +39 pT (1984 CE) the committee bought a dialler. It rang the first two slots on the first Sunday of every month at 18:00; a household's keypress then released its own two successors into the queue, and an unanswered number released nothing. The dialler wrote a line for each drill, and a regional civil-defence server took the text nightly over a modem. The server's mirror link crossed a cable landing station and was skimmed. This is how the log came into the Wasatch Corpus.

A drill closed as complete when the queue was empty. That condition, and not the share of the roll reached, was what the machine was built to test. A queue also empties when a tree stops branching. D. Okonkwo, reading the log as an unintended census, took *q* for every month from the RUNG and ANSWERED fields. It crosses one half in the drill of March 2004 CE (+59 pT):

> `2004-03-07 18:00 DRILL 0243 RUNG 011 ANSWERED 006 PENDING 000 TREE COMPLETE`

The last answering number lapsed in October 2006 CE (+61 pT). The households' destinations are not in the log; the exchange's later records show a fall in lines in the same years, and the valley's descendants appear in the genomes of three coastal towns. The exchange was decommissioned in +64 pT (2009 CE). The thirty-eight drills between those dates rang two numbers each:

> `2008-06-01 18:00 DRILL 0294 RUNG 002 ANSWERED 000 PENDING 000 TREE COMPLETE`

## The rhyme

Standard Terran carries an adjective, *both-gone*, meaning wholly out of reach. Nine upland settlements keep a skipping rhyme, first recorded in 2711 CE:

> *Ring two, ring two,*
> *two to ring and two ring you.*
> *If both are gone, if both are gone,*
> *who rings you?*

The link between rhyme and valley rests on the structure alone, two out and two in. No surviving text states it.

---

## Provenance and ground

The log is a Wasatch Corpus stream, one of the few in it that is not advertising telemetry. The tablet and plates are physical. The rhyme and the word are oral residue. Dating of the plates is by stamping style and the tablet's own year.

## See also

- The Giant Component
- The Cut Vertex

## Notes

1. Orla Penhallow's later life is not recorded.
2. The 1976 CE flood figure is from the committee's own minute, carried on the tablet's reverse: 199 households answered; 197 were reached.
3. *Q* crosses one half where the roll's answering fraction is 106 of 212.
4. Drills recovered: 312. Drills marked TREE COMPLETE: 312.
