# The Serai Hold

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from a single intercepted telemetry stream in the Wasatch Corpus and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Serai Hold is the Historical Faculty's name for a Contraction-era quarantine allocator at one gate on the road north out of the plain, whose eleven years of intercepted hold decisions are the only surviving record of how the machine held people, and for how long.** The stream is record; the gate's location, its keepers, and the people it held are reconstruction, and its name survives nowhere in the stream at all.

---

**The Serai Hold was an automated cohort-hold allocator — an ordinary instance of the period's real-time reproduction-number estimators — that governed, from +147 to +158 pT (2092–2103 CE), the quarantine of arrivals at a gate on one of the roads by which the plain emptied northward and upward.** It counted rash-onset cases from its hold-halls, estimated how many further cases each was producing, and set every cohort's hold at the measles quarantine maximum of twenty-one days, extending it whenever the estimate ran above one. It ran that rule on more than a million people. Its decisions survive complete; its name survives only on stamped aluminium tokens.

## The estimator

The stream is the machine's own decision log, one line per cohort per day, in the standard method of its age: cases in a seven-day window over the infectiousness inherited from earlier cases, weighted by a measles serial interval of mean 11.7 days, under a gamma prior of mean 5 and standard deviation 5. The notation is the log's own:

```
node=0x2A7 cohort=03318 n=388 win=7d si_mean=11.7 prior=gamma(1,5)
I[t-6..t]=3,5,4,9,11,8,14
R=1.63 [1.12,2.27] -> hold=21d extend cohort=03318
```

Measles is the correct pathogen for a road. Its basic reproduction number in a susceptible population is put at twelve to eighteen, so a population is shielded only above roughly 92 to 94 percent immunity, and a hold-hall receiving unimmunised arrivals daily is never above it. A case is infectious from four days before the rash to four after; incubation runs seven to twenty-one days, median twelve and a half, and the twenty-one-day hold is the period's own quarantine rule. An estimate of this kind cannot be current: it sees a transmission only after the cases it produced are reported, one serial interval late. The machine ran, for its whole service life, about twelve days behind the disease it was holding people for, and no design could shorten that, because the delay belonged to the pathogen and not to the machine.

## The cohorts

Cohorts were assembled by day of arrival; the log carries no field for village or descent. Okonkwo, D., reading the manifests as an unintended census, matched that sorting against the identity-by-descent structure of the upland populations north of the gate: endogamy that had held for a hundred generations relaxes there in the generation that dates, by segment length, to the +150s pT, and the pairings follow cohort numbers rather than any community or doctrine. People were held by arrival day, and were married, the genomes show, the same way.

## The tokens

Each hold was receipted with a stamped aluminium token: SERAI HOLD, a cohort number, a day count. Two hundred and fourteen have been recovered, most from upland graves. The name is on no line of the stream, which calls itself only by node.

## The last extensions

Arrivals fall through +157 pT (2102 CE) and stop in +158 pT. With no cases in the window the posterior reverts to the prior, and the log's final months carry, for every open cohort, the identical line R=5.00 [0.13,18.44] — the interval of a gamma with shape one and scale five, an estimate of nothing printed as an epidemic. The machine issued twenty-one-day extensions to cohorts of zero persons for one hundred and six days, and the stream ends mid-line. The manifests, summed over the eleven years, record 1,206,411 holds.

---

## Provenance and ground

The decision log was skimmed at a cable landing station under the harvest-now policy and read out after the era's public-key cryptography fell; it is the single witness, and the tokens add only the name and cohort numbers that anchor it. The serial interval, incubation, reproduction-number range, and prior are the period's own published values.

## See also

- **The Fourteen Is Done** — another exposure dispatcher's clearance, surviving as an idiom.
- **The Seven-Centimorgan Line** — a machine adjudicating kinship among people on the same road.
- **The Manzil Line** — a road corridor named from stamped plates alone.

## Notes

Whether *serai* names the gate, the hold-halls, or the machine is not recoverable; the tokens do not say.
