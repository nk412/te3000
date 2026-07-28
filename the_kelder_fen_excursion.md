# The Kelder Fen Excursion

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from a corrupted telemetry tail recovered from the Wasatch Corpus and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Kelder Fen Excursion is the Historical Faculty's name for an unresolved gamma-spectrometry anomaly logged by a single automated radiological monitoring post in the years after its district's depopulation, and read out three centuries later from an intercepted telemetry hoard.** The spectrum, its timestamp, and the post's decades of subsequent, uninterrupted transmissions are physical record; what produced the anomaly, and the post's own operating name, are not, and the Faculty's schools do not expect that to change.

---

**KELDER FEN** survives as four words stamped into an anodised aluminium tag, riveted to a solar array recovered separately from the telemetry it once powered — the only proper name to reach the record intact. It designates one post in a coastal gamma-spectrometry network commissioned in +65 pT (2010 CE) to keep continuous, unattended watch over background radioactivity: routine peacetime infrastructure, built to notice a reactor release, a lost industrial source, or worse, well before any human observer would. The post outlived the district it watched. Evacuated ahead of a rising, storm-driven coastline through the +120s–140s pT (2065–2085 CE), the fen emptied of the technicians who read the post's output and left the post itself running on solar charge and cellular uplink, unattended and uncancelled. In +146 pT (2091 CE) its detector logged an elevated, multi-line gamma spectrum consistent with either a fresh release of fission products, a malfunctioning piece of the post's own calibration hardware, or nothing more than a rain shower washing natural radon daughters out of the air — and then, for forty-five more years, kept transmitting, hourly, faultlessly, to no one. The three readings remain open. The record needed to close any of them is precisely the part the archive does not have.

## A post that watches itself

The network to which Kelder Fen belonged monitored ambient gamma radiation along a low, flood-prone coast as part of a wider Late Combustion practice: unattended stations, each built around a sodium-iodide (NaI(Tl)) scintillation detector coupled to a multichannel analyser, that accumulated a full energy spectrum on a fixed cycle — at Kelder Fen, hourly — and reported it by cellular telemetry to a central authority no fragment of which survives by name. NaI(Tl) was the coastal network's economy choice: cheap, rugged, and unattended for years at a stretch, at the cost of coarse energy resolution, roughly 7–9% of the peak energy as full width at half maximum. A smaller number of inland reference posts used cooled germanium detectors with resolution better by more than an order of magnitude; none of that finer instrumentation covered the fen. Each post carried a small sealed check source, caesium-137, mounted on a motorised arm that swung it briefly in front of the crystal on a fixed schedule to confirm the detector's energy calibration had not drifted, then withdrew it — a design answer to the ordinary problem of an unattended instrument silently going wrong. The post's firmware compared every accumulated spectrum against an alarm threshold and, on an exceedance, retransmitted the triggering frame at higher priority with forward error correction, on the reasoning that an alarm frame was exactly the one message the network could not afford to lose to a bad link. That reasoning is why one frame from Kelder Fen survives complete while nearly everything transmitted around it does not.

## The excursion

The surviving alarm frame is timestamped +146.31 pT (2091 CE, day 113) and carries a spectrum with excess counts, above local background, in four energy windows: near 352 keV, near 365 keV, near 662 keV, and near 1,596 keV. Read against the standard nuclear data for the candidate isotopes, the four windows admit more than one identification:

| Window (keV) | Candidate isotope | Reference line (keV) | Half-life | Reading it feeds |
|---|---|---|---|---|
| ~352 | lead-214 (Rn-222 daughter) | 351.9 | 26.8 min | natural, radon washout |
| ~365 | iodine-131 | 364.5 | 8.02 d | fresh fission |
| ~662 | caesium-137 | 661.7 | 30.17 yr | fission **or** stuck check source |
| ~1,596 | lanthanum-140 (Ba-140 daughter) | 1,596.2 | 40.3 h (parent Ba-140: 12.75 d) | fresh fission |

The 352 and 365 keV windows sit only 12.6 keV apart — well inside a NaI(Tl) crystal's resolution at that energy, itself on the order of 30–35 keV full width at half maximum — so a single broad excess there cannot be cleanly assigned to lead-214 or iodine-131 by shape alone. The 662 keV line is native to two entirely different processes: it is produced by fission of both uranium-235 and plutonium-239, and it is the exact line of the post's own onboard check source. The 1,596 keV window is the strongest evidence for the fission reading, since neither radon's decay chain nor a caesium check source has a line anywhere near it, but the counts there are the weakest in the frame, close to the post's stated detection threshold for that energy.

## Reading the spectrum

Three schools hold the field, and none can be eliminated from what survives.

The **fission reading** takes the 1,596 keV window at face value and reconstructs a plume of freshly produced fission products drifting across the post from an unstated source within range of the detector — a release the network was explicitly built to catch. It predicts a signature: iodine-131, half-life 8.02 days, should fall to roughly a fifth of its initial activity within nineteen days, by the ordinary decay law N(t) = N₀e^(−λt), λ = ln2/t½ ≈ 0.0864 d⁻¹, e^(−0.0864 × 19) ≈ 0.19. A second alarm frame, transmitted nineteen days later and partially recovered, would settle the question directly — except that its 350–420 keV band is exactly the region lost to packet corruption, one of the gaps left when the intercepting system's flow sampler, built to manage a much larger volume of ordinary consumer traffic, kept only a fraction of the post's low-priority packets and happened to drop that one.

The **stuck-source reading** holds that the check-source arm jammed in the deployed position, leaving the calibration source parked permanently in front of the crystal, and that the post's alarm logic — designed, correctly, to flag any sustained rise in the 662 keV line — did exactly what it was built to do in response to a fault in an entirely different subsystem. The servo-position telemetry that would confirm or rule this out was carried on the same channel, and in the same corrupted region, as the second alarm frame.

The **radon reading** treats the whole excursion as weather: precipitation scavenges short-lived radon daughters, lead-214 and bismuth-214 among them, out of the lower atmosphere and deposits them at the ground, producing a brief, entirely natural rise in ambient gamma dose that unshielded outdoor monitors are well documented to register. The post's own rain-gauge channel logged an active shower in the hour of the alarm. Nothing about this reading requires an external release, a hardware fault, or any event beyond the ordinary hydrology of the fen.

The Faculty's position is that the archive, as recovered, cannot adjudicate between the three. Each reading is falsifiable in principle, by a specific piece of data; each of those specific pieces is missing.

## The unread years

The post did not stop. Kelder Fen went on accumulating and transmitting an hourly spectrum for the whole of the district's abandonment, drawing power from a solar array that needed no one to maintain it and reporting over a cellular network that continued billing an account no one closed. Its firmware performed its scheduled calibration checks, logged them as passed or failed according to what the detector actually returned, and appended each result to a running self-diagnostic report addressed, by template, to "the duty technician" — a field that was completed, without exception, by nobody, for forty-five years. The network's alarm logic, having done precisely what it was designed to do at day 113 of +146 pT, went on being ready to do it again for every one of the roughly 394,000 hourly frames that followed, and on the evidence of the surviving fragment never had cause to. This is the whole of the post's later history: a system that worked exactly as specified, addressed to a reader who was no longer there to receive it, for longer than the district it watched had been occupied in the first place. The post's final transmission is dated +191 pT (2136 CE): one frame, format-valid, background counts only, the duty-technician field blank.

---

## Provenance and ground

The Kelder Fen material survives as a partial telemetry tail inside the Wasatch Corpus, the bulk-intercepted network traffic recovered once quantum computation broke the era's public-key ciphers. The post's cellular uplink shared infrastructure with ordinary consumer data and was swept into the same collection; because the session carried low data volume and no flagged content, the intercepting system's flow sampler retained only a fraction of its packets, producing the long, regular gaps that define the fragment. The alarm frame of day 113, +146 pT, survives complete because the post's own protocol resent triggering frames with forward error correction — a design margin built for exactly this kind of loss, and the reason any single spectrum from Kelder Fen can be read at all. The aluminium tag naming the post was recovered separately, from a different stratum, and cross-matched to the telemetry by its embedded serial number. No fragment of the network's own operating name survives; the header field that would have carried it is truncated to an unexpandable four-character stub in every recovered frame.

## See also

- The Standing Almanac
- The Threshold Registry
- The Danger Stage

## Notes

- All isotope half-lives and gamma-line energies are standard nuclear data, cited to the entry's own precision only. Dates follow the convention CE = pT + 1945.
- The Faculty's agnosticism is procedural, not stylistic: no reading has been retired, and no further data collection is possible.
