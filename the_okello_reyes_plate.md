# The Okello-Reyes Plate

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from the daily settlement ledger of a groundwater allocation scheme of the Gangetic plain, preserved as a slice of intercepted mirror traffic in the Wasatch Corpus, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Okello-Reyes Plate is the Historical Faculty's name for a cast-bronze plate on a pump-station wall, naming the one person who tuned a basin's water-allocation controller, and for the 13,902-day ledger of that controller, which records the point at which a foreseen failure became arithmetic and then went on running for twenty-nine years.** The plate, the ledger, and the controller's published gains are record; who Dagny Okello-Reyes was, and what she was asked to do, are reconstruction.

---

**Dagny Okello-Reyes, cast in raised letters on a bronze plate riveted beside a pump-station door, with the words *tuned by* and the numeral 0 where a date would stand, is the whole of what the works preserves of its maker.** The plate was found in a closed alluvial basin of the Indo-Gangetic plain whose name did not survive; the ledger that matches it by the cabinet's serial number is a slice of intercepted replication traffic in the **Wasatch Corpus**, whose capture index was lost with its container and whose own headers count days from the scheme's start. The scheme's name, in the language of its cabinet labels, is rendered by the Faculty as *What the Well Is Owed*. It issued each day to some 1,900 holders of shares an allowance of water to pump, set by a controller that compared the measured depth of the water table with a setpoint 22 metres below the ground and cut or raised every allowance in proportion to the error and to its running sum. The sum had no bound. Its commissioning note stated on day 0 when the allowance would reach its statutory floor, and when the shallow wells would fail as a result, and it was right on both counts to within a few weeks. The ledger runs 13,902 days, some 38 years, inside a commissioning window of +88 to +102 pT (2033–2047 CE) that no other record narrows. It ends with allowances still being credited, every day, to accounts that had stopped drawing.

## The controller

A water table in a closed basin is a store, and a store behaves as an integrator: its level rises by what is recharged less what is pumped, and nothing else. The basin's area, taken from the plate's cadastre, is some 240 square kilometres and the specific yield of its sands about 0.12, so one metre of table is some 28.8 million cubic metres of water. A controller that adds an integral term to a proportional one, acting on a plant that is already an integrator, gives a loop whose characteristic equation is that of a second-order oscillator, with a damping ratio set by the gains alone. The ledger's header carries the gains. They give a natural period near thirteen years and a damping ratio of 0.7, which is the figure the age's control texts recommended for a loop that must not ring, and which the Faculty reads as the one design decision in the system that is unmistakably the work of a person who knew what she was doing. The proportional gain was about 20 million cubic metres a year per metre of shortfall. The allowance could fall no lower than a floor of 31 million a year, fixed by statute for drinking water and legacy rights, against a nominal 52. The proportional term alone therefore reached the floor at 1.05 metres of shortfall, and the integral term then went on summing a shortfall the actuator could not act on.

That is integrator windup, and the age had known the remedy for a century: feed the difference between the commanded and the delivered output back into the sum, over a tracking time, so the sum cannot run away from what the actuator can do. The cabinet's firmware had no such term. Day 0 of the ledger carries a note, repeated in the same field every 365 days thereafter, that the floor would bind in the ninth year, that at the floor the basin would lose about 0.97 metres a year against a margin of sixteen to the intake of the shallow wells, that the sum was unbounded, and that a clamp was *deferred to the second phase*. The floor first binds on day 3,087, in the ninth year. The first entry marked *well dry* stands on day 8,566, in the twenty-fourth, fifteen years later to the week, and nobody acted on the note in the meantime. No second phase is in the record.

## What the sum did

By day 8,566 the shortfall stood near sixteen metres and the integral had accumulated more than a hundred metre-years, which at the integral gain is a commanded cut some seventeen times the nominal allowance. After the wells failed, draws fell: of some 1,900 accounts, the last nonzero draw stands on day 11,061, and the table, no longer pumped, began to rise. It could not release the allowance. The sum falls only as fast as the table stands above setpoint, and to bring it back to where the allowance would lift off the floor the basin would have had to stand above setpoint for more than a hundred metre-years, and the setpoint was 22 metres below grade. A basin brimming to the surface would have taken six years. The ledger, correct to its own arithmetic, credited the floor to every account on every day for 2,841 days after the last draw.

## Three readings

The **omission** reading, argued by Tesfaye-Lindqvist, holds that the clamp was a cost the scheme's financier deferred and that the engineer's plate records a tuner, not a decider; the note is a complaint addressed upward and never answered. The **memory** reading, of Ibarra's school, holds that the unbounded sum was the design: a clamp forgives a shortfall once the actuator saturates, and a basin that forgave would have drawn down for ever, so the debt was left to stand as the only perfect record of what the wells had taken. The **continuity** reading, of Zhou-Ferreira, holds that the dry-well entries and the zero draws are not the same fact. A holder who left the wells for a canal or a road leaves the same line in a ledger as a holder whose well has failed, and the floor cost nothing to those who were no longer there.

None of the three can be run against the record. The ledger does not say who left. The cabinet's notes cannot be assigned: the annual advisory is edited six times, each edit grammatical, none changing its figures, and the 38th copy is as fluent as the first. A scheme of this kind generated its own reports, and the Faculty's classifiers return the note, and the six edits, as equally probable from a person and from the controller's report module. If the warning was written by the machine, it was written for a processor, and the reading of it as a plea loses its object.

## End of record

On day 13,902 of the ledger the floor was credited to every account, and no entry follows it.

---

## Provenance and ground

The plate was surveyed in the pump station by the Institute for Deep Record Studies in +1009 pT (2954 CE); its text is physical record, and bronze, in a dry hall, loses nothing legible in a thousand years. The ledger is a mirror batch of the scheme's daily settlement, read out of the Wasatch Corpus in +1013 pT (2958 CE). Tesfaye-Lindqvist, M. recovered the gains and the basin's storage from it (*The Clamp and the Debt*, Historiography, +1017 pT [2962 CE]); the storage figure is to a tenth of a metre of table and the specific yield is the range for alluvial sands. The loop equation, damping ratio, windup, and back-calculation remedy are as the age's own control texts set them out.

## See also

- The Safe Halt
- The Governor Log
- The Ghaggar Sweat Line

## Notes

1. All dates are post-Trinity; CE = pT + 1945. Ledger days are counted from the scheme's start, since its clock reset to zero at every loss of power.
2. The gains are the Faculty's reading of the header's raw values; the damping ratio and the 28.8-million-cubic-metre figure follow from them and from the plate's cadastre by arithmetic given in the text.
