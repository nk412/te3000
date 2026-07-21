# The Wide Synchrony

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from a single nightside radiance frame of a polar-orbiting environmental satellite and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Wide Synchrony is the Historical Faculty's name for a continental alternating-current interconnection — some hundreds of millions of rotating machines held to a single electrical phase — and for the roughly nine minutes in +112 pT (2057 CE) in which that phase came apart across a mid-latitude continental interior.** The interconnection's operating name and its failure are recovered separately: the name from a cast plate, the failure from one satellite image and a fragment of control-room log; almost everything between them is reconstruction.

---

**The Wide Synchrony was a wide-area alternating-current grid in which every synchronous generator, from the largest hydro machine to the smallest thermal set, turned in a single locked electrical phase, so that the whole continent's rotating plant behaved as one enormous coupled oscillator running at a nominal fifty cycles a second.** The lock was real and astonishing: across thousands of kilometres, the machines held frequency to within a few thousandths of a hertz of one another, not because a master clock commanded them but because the physics of coupled rotation pulls neighbours into step, each machine leaning on the phase of the next through the power that flows between them. That same coupling set a hard ceiling. Power crosses a transmission line only in proportion to the sine of the angle between its ends, and the sine of an angle cannot exceed one; past a right angle the restoring pull reverses and synchronism is lost. The interconnection ran its whole planet-scale machine against that wall, closer to it each decade as demand rose faster than new line was built, and defended the margin with automatic protection that severed any line the moment its loading turned dangerous. In +112 pT one heavily loaded corridor tripped on a hot afternoon; its power redistributed onto neighbours already near the angle; those tripped in turn; and in under nine minutes an area of several hundred thousand square kilometres went dark. Every protective device that operated in those minutes operated correctly. The interconnection was never resynchronised at its former reach.

## One phase across a continent

A synchronous grid is a physical realisation of a coupled-oscillator system. Each generator's rotor is a spinning mass whose angular position is a phase; the electrical network couples the phases, and the dynamics of a single machine obey the swing equation, the rotational form of Newton's second law:

> `(2H / ωs) · d²δ/dt²  =  Pm − Pe`

where *δ* is the rotor angle, *H* the inertia constant in seconds — the kinetic energy stored in the spinning mass at rated speed, divided by the machine's rating, typically two to nine seconds for the period's plant — and *Pm*, *Pe* the mechanical input and electrical output power. Written across all machines, the equations are those of coupled phase oscillators with inertia; the period's own network scientists showed the mapping explicitly. Such a system synchronises only when the coupling is strong enough to overcome the spread of the machines' natural rates. Below that critical coupling there is no common frequency at all; above it, the continent locks into one. That the Wide Synchrony held a shared phase across its whole footprint for decades was not administrative achievement but the coupled system sitting, stably, above its threshold.

## The angle that could not exceed a right angle

The power carried by a lossless line between two buses is

> `P  =  (Vs · Vr / X) · sin δ`

with *Vs*, *Vr* the terminal voltages, *X* the line's series reactance, and *δ* the phase-angle difference across it; in the per-unit notation the period used for everything, with both voltages near one, this is simply *P = sin δ*. The transfer rises with the angle to a maximum at *δ = 90°*, where it equals *Vs·Vr/X* and can rise no further. The slope of that curve — the synchronising coefficient, proportional to *cos δ* — is what pulls a disturbed machine back into step; it falls to zero at the right angle and reverses beyond it. So ninety degrees is not a guideline but a wall: a line pushed past it does not carry more power, it loses synchronism. Operators held a margin below the wall and obeyed a doctrine, the *N−1* criterion, requiring that the loss of any single element leave the remainder stable. The doctrine's weakness was published in the period's own literature and not acted on: reinforcing such a network does not always help. Adding a line, or raising a line's capacity, can *lower* the whole grid's stability — a power-system form of the paradox known from congested road networks, in which the new path frustrates the phase pattern and pushes a distant corridor toward overload. The interconnection was extended and uprated for forty years on the assumption that more copper meant more margin.

## Nine minutes

The recovered sequence is consistent with the era's other continental cascades and rigorous in its mechanism. A long corridor carrying heavy transfer on a hot afternoon sagged into vegetation and tripped. Its power did not vanish; it rerouted instantly along the remaining lines in inverse proportion to their reactances, loading parallel corridors beyond schedule. On those corridors the backup distance relays saw the new condition — high current, depressed voltage — as an apparent impedance small enough to fall inside their widest protection zone, and tripped healthy, fully functional lines exactly as they had been set to do. Each removal raised the loading on what remained; each raised angle brought a fresh set of relays to their thresholds. The competence was the mechanism of the collapse: the protection worked precisely as designed, isolating equipment from stress, and in doing so it dismantled the network faster than any operator could read the alarms. As the interconnection tore, it fragmented into electrical islands, each with its own surplus or deficit of generation; frequency in the deficit islands fell through the floor at which automatic load-shedding sheds whole districts to save the machines, and where that failed, the machines themselves tripped on under-frequency and the island went black. The control-room event log for the corridor survives as a short fragment, its lines interleaving operator entries and alarm-processor output in one undifferentiated stream:

> `00:41:07.442  L-NT2 400kV  Z3 OP  TRIP  no fault located  //  reclose blocked  ack pending`

The plurality of complete imperative lines in the fragment are addressed to the alarm processor, not to a person, and nothing in the phrasing distinguishes a line a technician typed from a line the alarm handler emitted from a template. Which of the last entries were written by a human is not, on internal evidence, decidable.

## The dark frame

The anchor of the entry is a single calibrated nightside radiance frame from a polar-orbiting environmental satellite's low-light imager, timestamped in the small hours local and showing a roughly circular void of city light where the archived baseline mosaic shows a dense lattice. The image records the outcome, not the cause; the nine-minute sequence is reconstructed from the corridor log and from the physics, which constrains it tightly. Ibarra, N., whose doctrine of single-filament infrastructure holds that the age ran its whole planet through dangerously few points of failure, reads the Wide Synchrony as the doctrine's clearest case: a continent that had made its rotating plant into one machine had also made it into one machine's failure mode, so that the very coupling that produced the wonder of a shared phase was the channel along which the darkness propagated. The human cost inside the void is not in the record and is not tallied here. The satellite continued to image the region on its regular pass; later frames show the lattice returning in patches and never, at the original density, as a whole.

---

## Provenance and ground

The entry rests on one nightside radiance frame, preserved in an intercepted downlink stream, set against the imager's archived baseline; the corridor event log is a separate short fragment from the same body of recovered traffic. The physics is secure and independently grounded: the swing equation, the sine law of power transfer and its right-angle ceiling, the coupled-oscillator synchronisation threshold, the distance-relay cascade mechanism, and the reinforcement paradox are all the period's own established results. The nine-minute chronology, the affected area, and the identity of the first corridor are reconstruction constrained by the image and the physics, not direct record. The interconnection's operating name survives in exactly one place: cast in relief on the rating plate of its largest phase-shifting transformer, recovered from the silt of a switchyard that later flooded, reading the machine's ratings and, beneath them, a legend and the year `2057` — which the plate, cast before the fact, gives as a commissioning date and which is, by the coincidence the scholarship keeps, the year the phase came apart (+112 pT).

## See also

- **The Long-Wave Reveille** — another continental timing infrastructure known only through what its silence did to the machines that depended on it.
- **The Low-Light Queue** — an automated system executing correctly on a world that had drifted out from under it.

## Notes

The interconnection standard governing the failed corridor is marked, in the sole surviving copy of its revision index, as withdrawn and superseded, with no successor filed. The region was among those the following decades emptied.
