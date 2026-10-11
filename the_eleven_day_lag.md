# The Eleven-Day Lag

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from the uplink and maintenance telemetry of three roadside effluent samplers, skimmed in transit for a billing purpose they were never part of, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Eleven-Day Lag is the delay between two peaks of one bacterial gene in the sewage of two transit camps sixty-six kilometres apart, and the only measurement of the pace of a migrating population that the Contraction record contains.** The telemetry is record; the sampler's purpose, the camps' size, and the people the numbers stand for are reconstruction.

---

**The Eleven-Day Lag** is a free-text note, a flow series, and two columns of gene counts, repeated in the same layout for three automated samplers on one road from +158 to +171 pT (2103–2116 CE). The device is unnamed in every frame; the schools call it the *composite unit*. It drew a measured aliquot of sewage from a camp outfall at intervals set by flow, held the pooled sample at 4 °C, and reported on a cellular link the concentration of two targets: a gene of the diarrhoeal bacterium *Vibrio cholerae*, and the genome of a plant virus that is present in human stool wherever peppers are eaten. The first measures an outbreak. The second measures how many people produced the sewage. Both come out of the same stool, and so the record is at once a disease surveillance and a census, which its keepers did not intend. The upstream camp's bacterial peak preceded the downstream camp's by eleven days. The pace implied is that of people on foot.

## The unit

Wastewater surveillance was established practice before the Contraction. Stool carries the pathogens of the gut and, in some infections, of the airway, and a single outfall integrates a catchment that no clinic reaches. The composite unit was a flow-proportional version: a pump sampled a fixed volume per fixed volume of flow, so that a day's pooled sample weighted busy hours as the camp's output weighted them. The plant-virus count served as the normaliser. It is shed by nearly everyone, at a roughly steady rate per person (of the order of 10⁶ to 10⁹ genome copies per gram of stool across the published range), so the ratio of target to normaliser removes the effect of rain, dilution, and a camp that doubles in size overnight. Divided out, what remains is prevalence. Left in, the normaliser alone is a head count, with an error band the schools put at a factor of about two.

## The three camps

The samplers stood at the outfalls of three camps designated by the road's own mile marks, 66 kilometres apart, a three-day walk at the 22 kilometres per day that a loaded adult sustains on a road. Normaliser counts place the population of the upstream camp between 3,100 and 9,400 persons over the record, and the middle camp between 2,000 and 6,000. The camps are not otherwise attested. Residence was short: the normaliser's flow-adjusted rise and fall give a mean stay near six days.

The target gene appears first in the upstream camp at +160 pT (2105 CE), at a concentration just above the assay floor. It grows with a doubling time of about two days (r ≈ 0.35 per day) for nineteen days, and then falls. The middle camp's series is the same curve displaced.

## The convergence

The two measurements, an outbreak and a headcount, would be unrelated were it not for the stool. The headcount gives the camp its size and its turnover; the outbreak gives the camp its reproduction number; and the two cannot be separated by the camp itself, because the people leaving are the people carrying. A closed population with a basic reproduction number of 2 ends with about 80 per cent infected (the root of z = 1 − e^(−2z) is 0.797). An open one is different. If infectious spells last five days and the mean stay is six, a case spends on average 2.7 of its five infectious days inside the camp, since the expected local time is the product of the two durations over their sum. About 55 per cent of transmission potential is used locally; the other 45 per cent leaves down the road. With a basic reproduction number of 2.5, the local figure is 1.36 and the exported share is the camp's contribution to the next camp's curve. The peak the downstream sampler records is therefore partly the upstream camp's, carried.

The eleven days decompose without remainder. The walk accounts for three. An imported infection must then grow from a handful of cases to the assay floor; at a doubling time of two days, sixteen-fold growth takes eight, and the arithmetic closes: 3 + 8 = 11. The lag is the pace of the road plus the time the disease takes to become measurable, and it is the first of these that is the finding. It is the only direct reading in the record of how fast a displaced population moved.

## The note

Each frame carries a free-text field, filled at the unit and relayed without alteration. The frame of +164 pT (2109 CE) reads in full:

> "Flow low, intake line cleared of silt. Cooler at 11 C, compressor cycling long. Hold sample 0412 for lab. Camp larger than the sheet says."

The first sentences conform to the vendor's template for service-assistant output; the last does not, or does. Three schools read the field. One holds the author a person, a technician who visited the outfall. One holds it an automated drafting service that composed notes from the unit's own sensor flags, the final clause a spurious generalisation. The third, which since Marchetti has been the largest, holds that the question is meaningless: by +164 pT the service's output was tuned to be indistinguishable from the technician's, and the technician's notes had been revised by the service. The sentence is accurate. The normaliser count for that week was 7,800 against a registered 4,500.

The cooler's drift matters to the numbers. Samples held at 11 °C rather than 4 °C under-read, and the plant virus, an RNA genome, loses signal faster than the bacterial DNA gene. The ratio is therefore biased upward in the last six weeks, and the schools disagree on the correction.

## How it survived

The record should not exist. The units were commissioned by a public health office whose registers are lost. The telemetry was not archived by it. It survives because the cellular modems were provisioned, in error, on a plan sold for tracking shipping containers, and the plan's traffic left through a landing station whose cable was tapped for bulk collection. The Wasatch Corpus carries the frames as a minor flow, indexed under cargo. The error was a clerk's, or a script's; the plan was one tier from the correct one. The three samplers are the only public-health instruments in the corpus.

## Reading

Okonkwo reads the record as an unintended census, the pattern of his study of commit timestamps and routing logs. Ranganathan's caution applies in full: three outfalls on one road are not the road. The lag shows that people moved, with a bacterium in some of them, at a pace; it does not show how many, from where, or how many arrived. The sizes derived from the normaliser are of the people who stayed long enough to be in the pipe.

---

## Provenance and ground

Three series, 4,108 frames, +158 to +171 pT (2103–2116 CE), in the Wasatch Corpus. Flow, temperature, and conductivity are instrument readings; gene counts are as relayed; population figures are derived, with the normaliser's per-person range taken from published values. Walking pace is a standard figure for loaded adults.

## See also

- **The Crossing Ledger** — another record of movement kept for a different purpose.
- **The Morbidity Return** — a count of illness read from a form.
- **The Giant Component** — a network read for what connects.

## Notes

The upstream unit's last frame, dated +171 pT (2116 CE), is a firmware deprecation notice addressed to the unit: support for its reporting format would end at the close of the month, and the frame asks for no reply. No later frame from any of the three exists.
