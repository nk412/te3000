# The Clearance Curve

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from a sixty-one-week posting log of an unnamed settlement clearing node, intercepted at a cable landing station, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Clearance Curve is the Historical Faculty's name for the epidemic curve read out of one settlement node's fee ledger in the upper Indo-Gangetic staging belt, long taken as the standard picture of how a waterborne enteric disease behaved on the great displacement road, and now held to describe only the people who could pay to appear in it.** What is record is the log's postings, codes and arithmetic; the outbreak, the road and the population outside the ledger are reconstruction — and the curve is a curated record that three generations of scholarship mistook for a sample.

---

On 11 September +117 pT (2062 CE), a settlement clearing node in the staging belt of the upper plain posted the first of 1,906 entries carrying the void code H-7, which cancelled a travel-clearance fee and returned it to the payer less a retention of fifteen per cent. The last H-7 posts in the seventeenth week after it. Between them the weekly count rises for nine weeks, peaks, and falls to zero in eight, a single smooth hump, and for most of the discipline's history that hump was read as the epidemic curve of the displacement itself. It is the epidemic curve of a ledger. The node's own name is unrecoverable; so is any local name for the outbreak, and the scholarship's term, the *clearance curve*, is the name of the instrument and not of the event. The curve fixed a low reproduction number for a crowded, waterborne contagion on the road, and the low number fed forward into every early estimate of what the road cost. It was a false idol, and it is still cited, in the older handbooks, as a result.

## The posting log

The class of facility is attested by function. Through the Late Combustion Age the movement of people out of the failing wells of the plain was licensed, at the staging towns, by a clearance: a paid certificate that the holder was fit to board a sealed carriage to the uplands, issued against a settled account and logged by a clearing node that held no opinion about the traveller beyond whether the account would settle. The log that survives is that node's posting record: a flat sequence of timestamped lines, each with an account hash, a fee amount, a carriage-class code, and a short free-text memo field the node's software filled from a fixed vocabulary. It carries 214,380 clearance postings over sixty-one weeks. It was never an epidemiological instrument. It was intercepted, with the rest of the traffic of its landing station, for the same reason as everything else in the Wasatch Corpus, and read out with it.

Its public face was a printed tariff card, reproduced verbatim at the head of each carriage-class file, which the Faculty treats as a caption in the sense that it is the only passage in the log written to be read by a person:

> CLEARANCE IS GRANTED TO THE HOLDER OF A SETTLED ACCOUNT. THE HOLDER MUST PRESENT FIT. A HOLDER PRESENTING WATERY STOOL, VOMITING OR COLLAPSE IS VOIDED, THE FEE RETURNED LESS FIFTEEN PERCENT, AND THE HOLDER REFERRED TO THE NODE CLINIC. UNSETTLED PERSONS ARE REFERRED TO THE HOLDING LINE.

The card names no disease. The Faculty's identification of it rests on the stated symptoms, the incubation implied by the lag between a fee posting and its void, and the clinic's dispensing lines, which follow the void with a single code for a measured oral rehydration salt sachet.

## The curve and the fit

Collected by carriage class, the H-7 voids are not spread across the whole log. They fall almost wholly in three consecutive convoys of the class that boarded after a four-day hold at the node, 4,760 holders in all. Of these, 1,906 were voided: 40.0 per cent.

The reading that followed is arithmetic, and the arithmetic is correct. In a closed, wholly susceptible population mixing at random, the fraction eventually infected, *z*, satisfies *z* = 1 − e^(−R₀*z*), so that R₀ = −ln(1 − *z*) / *z*. For *z* = 0.40 the reproduction number is 1.28. A first generation of Ranganathan's students published that figure with the curve as its plate, and the conclusion drawn from it was the *benign-road reading*: that a faecal–oral enteric disease, loosed in a crowd under road conditions, spread only just above threshold, burned out with two-fifths of the exposed, and could not have been the engine of any large loss. The ledger also supplied, as it seemed, a fatality figure. Nine of the 1,906 voids end in an account-closure code, which is 0.47 per cent, and the Faculty's handbooks long carried that as the lethality of the disease on the road.

Each of the figures is a real property of the ledger. The disease is a real one: infection with the cholera vibrio is asymptomatic or mild in roughly three of every four cases, becomes the severe, rice-water form in about one in twenty, and in that form kills up to half of untreated patients within hours through loss of fluid, and fewer than one in a hundred of those given prompt rehydration. A rehydrating node clinic, a closed carriage-class account and a death rate under one per cent are each exactly what the disease predicts for people given salts. They are not what it predicts for people who were given nothing.

## Who was in the ledger

The correction came from outside the log's disease codes, from its water. The node posted, as a recurring bulk line, the purchase of treated water for the holding line, in weekly volumes near 4.9 million litres. Later humanitarian practice, derived from the metabolic and hygiene minimum, set fifteen litres per person per day as the floor below which enteric disease accelerates, and a node supplying the holding line at that floor serves 4.9 million ÷ (7 × 15) = about 46,700 people. The convoys in the curve held 4,760. The people outside the ledger numbered roughly ten times the people inside it, drinking the same river upstream of the same intake.

The selection runs one way and is the point. To receive a clearance a holder needed a settled account, which meant a bank that still settled, which meant that the holder had, in effect, already chosen to leave early and safely: the fee class moved by sealed carriage on a four-day hold, drank the node's treated water in the hold, and were counted at the gate. The holding line, whose members the card names in its last sentence and does not number, waited weeks or months for what the account-holders waited days for, on water that had no line item. The ledger is a clean census of the wealthy and an unwitting census of the poor only by subtraction.

The consequence is a second mistake inside the first. Within the fee class, treated water and a clinic hold the effective person-to-person reproduction number below one; call it 0.6. A subcritical chain started by a single introduction produces, in expectation, 1/(1 − 0.6) = 2.5 cases in all. The 1,906 voids therefore correspond to something near 760 independent introductions from outside the ledger, and the hump, which looks like a propagating epidemic with *R*₀ = 1.28, is closer to the shadow cast on a protected group by a larger and higher-reproduction epidemic in the unprotected one. In a waterborne outbreak among people with no treatment of any kind, published estimates of the basic reproduction number run from just above 1 to several. For an *R*₀ of 3, the same final-size relation gives an attack fraction of 94 per cent. The final-size equation was applied to a population that the log's own cohort definition guaranteed was not homogeneous, not closed and not the one at risk. The quantity inferred from it, 1.28, is a property of the sample frame.

## The schools

The *corpus-critical* school, following Ranganathan's aphorism that the discipline does not know what the people said to each other, only what was said about them to machines, holds that the curve should be struck from the handbooks outright: a ledger of the paying cannot give the shape of an epidemic in the unpaying, and the benign-road reading and the 0.47 per cent fatality are artefacts of who could appear. The *maximalist* school replies that the log is the single bit-exact, time-resolved, machine-kept record of a contagion anywhere on the road, that a biased measurement of the fee class is still a measurement, and that the water line, if it supports a holding-line population of 46,700, supports it only because the log's own postings made it legible. A third position, associated with Okonkwo's programme of reading incidental metadata as unintended census, accepts both and treats the log as a bound: the curve is a floor on the epidemic's reach, not an estimate of it, in the way that a Middle Combustion district's persistent childhood fever is a floor on its population. Marchetti's comparison, to the weekly burial bills of an early modern city that omitted the dissenting and the pauper dead, is cited by all three and settles none of them.

None of the schools can adjudicate, and the log gives the reason. The holding line left no postings of its own: it paid nothing, so it generated no line, and the only trace of its size is the volume of water bought to keep it alive. The ratio of illness inside the ledger to illness outside it is a quantity the ledger would have to contain to estimate, and it does not.

## What the curve is still used for

The Faculty's current index carries the log under three entries, none of them "epidemic curve of the road." As a **treated-cohort series** it is admitted, with the rehydration lines, as the best-quantified record of the outcome of oral rehydration on a displacement route. As a **floor on introductions** it is admitted at about 760 chains. As a **water-based headcount** of the holding line it is admitted, with the fifteen-litre assumption stated, at about 46,700 on the weekly volumes. The benign-road reading and the 0.47 per cent figure are withdrawn from the handbooks as of the current edition, though both survive in the older plates, still captioned as results.

The log ends in its sixty-first week at an interrupted line. The ledger posts a refund against each of the 1,906 voids and no entry against anyone who had no account to refund.

---

## Provenance and ground

The sole witness is the posting log, a single sixty-one-week extract of a larger flow intercepted at a cable landing station and read out of the Wasatch Corpus after the break of the period's public-key cryptography. Timestamps are internal; the extract cannot be radiocarbon dated and does not need to be. The node's identity is carried only by a routing code, and the staging town, the river and the intake are inferred from the carriage-class destinations and the water vendor's route, not stated. The carriage-class files are bit-exact where the corpus's checksums survive, and 3.1 per cent of the lines are fragmentary and excluded from every figure above. The corpus over-samples the connected and purchasing; here that bias is also the subject.

## See also

- The Morbidity Return
- The Waiting List
- The Siwalik Intake

## Notes

The fraction of cholera infections that are asymptomatic or mild (about three-quarters), the severe fraction (about one in twenty), the untreated and rehydrated fatality ranges, the final-size relation *z* = 1 − e^(−R₀*z*) and the subcritical branching mean 1/(1 − *R*) are standard results of the epidemiological literature; the basic reproduction numbers for waterborne enteric outbreaks are quoted only as the published range, which spans just above 1 to several. The fifteen-litre-per-person-per-day figure is the later humanitarian minimum, applied here as an assumption and not a measurement; the node's actual draw per head is unrecovered, and the holding-line headcount scales inversely with it. The value 0.6 for the within-class reproduction number is the Faculty's illustrative choice, not a fitted quantity. Identification of the disease rests on the tariff card's symptoms and the clinic's rehydration lines; no pathogen was named in the log.
