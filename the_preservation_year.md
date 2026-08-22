# The Preservation Year

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from a content-addressed monitoring repository and its source, the latter surviving bit-exact in consignment L-III of the Longyear Deposit, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The preservation year was a Late Combustion unit of remaining time: the number of years a store of cellulose-acetate film could be expected to hold below the threshold of its own self-destruction, if the room around it stayed exactly as it stood at the moment of reading.** The unit's defining source code and one vault's nightly readings are bit-exact record; what the unit was called aloud, and every room it was read in but one, are reconstruction.

---

**The preservation year was a unit of measure that stated the future of a room as a single falling number.** It descends from a permanence index published by a photographic-materials laboratory in +48 pT (1993 CE) and was reworked, by +71 pT (2016 CE), into a live figure computed continuously by shelf-mounted monitoring appliances: temperature and humidity in, years remaining out. Archives of the period disputed budgets, staffing, and duplication schedules in this denomination the way earlier centuries had argued in grain. One deployment's log, recovered whole, shows the number being kept faithfully for fourteen years after the last human hand in the record, and then stopping without remark.

## The rate and the threshold

The chemistry under the unit is ester hydrolysis. Acetate film is cellulose esterified with acetic acid; ambient water cleaves the ester bond and returns the acid, and the acid so released catalyses further cleavage. Below a measured free acidity of about 0.5 — the titration point the period's own studies fixed as onset — decay creeps; above it, the reaction supplies its own catalyst and accelerates, and no storage condition in the surviving literature returns a reel below the line. Fresh film held at 18 °C and half-saturated air reached onset in roughly fifty years; each sustained cooling of five to six degrees roughly doubled that, on the ordinary exponential dependence of reaction rate on temperature. That exponential was the unit's floor and its ceiling at once: cold and dryness bought time at a fixed, calculable price, and nothing else bought any. The tool's core survives as four lines:

```
# years to onset at held conditions; onset = free acidity 0.5
# T kelvin, rh fraction; EA/R fitted 9.8e3 K
pyr = (1.0 / A0) * exp(EA_R / T) / rh
```

The docstring's expansion of `pyr` was a link to custodially hosted documentation, withdrawn on the date a payment lapsed. What the unit was called aloud is unrecoverable; the Faculty's "preservation year" is a convention.

## The vault that kept counting

The recovered log belongs to a subarctic film store whose monitoring appliance sat inside the cold room it was metering, committing one nightly reading to a repository that named every file by a fingerprint of its own contents. The last human-signed commit is a sensor recalibration in +117 pT (2062 CE). The nightly readings continue, correctly computed, through +131 pT (2076 CE) — the number rising a little each winter, sagging when the compressors ran short — and end mid-week. Whether custodians remained in the town above it by then is exactly the kind of count the age stopped keeping; the log records the room's future to the day, and nothing about its people. The reels the code was written to save were on polyester base, for which the projection ran effectively off-scale — the film that carried the unit's own source into the Longyear Deposit describes, imperishably, the chemistry of a different film's death.

The final committed reading gives the hall forty-one preservation years; the film it was metering has not been found.

---

## Provenance and ground

The tool's source survives bit-exact in consignment L-III of the Longyear Deposit, in the Sunday snapshot of +75 pT (2020 CE); the vault log, content-addressed under the same fingerprint scheme and therefore provably unaltered, was read from an appliance recovered in a Consolidation-era building survey of +641 pT (2586 CE). Terauds, M. treats the pairing as the discipline's cleanest case of a record preserved by the conditions it existed to measure (*The Metered Shelf*, Journal of Anthropogenic Stratigraphy); Okonkwo's school reads the nightly commits as an unintended census of one building's electricity, and declines to read them as a census of anything else.

## See also

- The Halving Interval
- The Yilgarn Vault

## Notes

The hydrolysis of cellulose acetate, its autocatalysis past a free acidity of about 0.5, the roughly fifty-year onset horizon at 18 °C and 50 per cent relative humidity, and the doubling of that horizon per five to six degrees of cooling are as the period measured them; the fitted constant in the quoted code corresponds to an activation energy near the middle of the published range. The linear humidity term is the tool's own simplification of a measured, stronger dependence. The unit, the appliance network, the vault, and its log are reconstructions built on that real mechanism.
