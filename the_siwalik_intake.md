# The Siwalik Intake

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from a deployment log and control-software mirror in the Code Deposit, cross-read against one of the Sealed, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Siwalik Intake is the Historical Faculty's name for a river-filtration checkpoint at the Gangetic plain's rise into the Siwalik hills, whose admission queue is known, down to its governing equation, to have had no stable solution for as long as the surge that broke it lasted.** Its control software and source comments are physical record; the queue's own database — who waited, how long, and what became of them — is sealed under a cipher the age classed, correctly, as unbreakable.

---

**At 26°47′N, 83°21′E, where the plain's last irrigation canal meets the first rising ground of the Siwalik hills, an automated river-filtration checkpoint held the last filtered water and the last checked crossing on a retreat road the whole exodus out of the wet-bulb plain had narrowed onto.** Built in +122 pT (2067 CE) to meter a modest cross-border trade, it had become, by the time the inland wells failed in +176 pT (2121 CE), a single filament carrying a whole hillside's water and a whole plain's people — Ibarra, N.'s single-filament infrastructure in its plainest form. Its admission queue is recovered whole, as an equation. What the equation was counting — how many people, for how long, and to what end — is not.

## The wall behind the gate

Its control software survives whole, mirrored into the Code Deposit's Sunday snapshot years before anyone thought it would matter. It ran the queueing mathematics of the age's own telephone exchanges, unmodified, on people: arrivals at a rate λ, served singly at a rate μ fixed by the plant's pump pressure and membrane area — a ceiling no patch could raise, because it belonged to the hydraulics, not the code. Below λ = μ the expected wait is, by the age's own formula, 1 / (μ − λ); at λ = μ it is not long but provably unbounded. Cartridge replacement, specified at six months, had been stretched to eighteen three years earlier against a budget line; μ, unaudited, was already under its rated figure when the wells failed. Two checkpoints upstream tried metering arrivals to relieve it, but a chain of queues in series cannot pass, in total, more than its slowest stage allows — the wait only moved backward along the road.

## The fair line

The checkpoint's own internal designation does not survive; a recovered maintenance manual glosses it only in translation, as "the fair line" — the one property its first-come admission rule did in fact guarantee, whatever else it could no longer promise. Its public status feed, intercepted off the same cellular backhaul as the plant's own telemetry, went on issuing increasingly precise estimated-wait figures long after the underlying number had stopped meaning "wait" in any ordinary sense; one surviving source line reads only:

`est_wait = 1 / (mu - lambda)  # clamp to "computing" past capacity — UI only, do not touch`

Nothing in the repository's history distinguishes which of its later commits were entered by a person and which by the deployment system's own automated formatting pass.

---

## Provenance and ground

The checkpoint's operational database — the actual tickets, actual timestamps, actual queue — was written nightly to an encrypted off-site backup under a scheme the era's own cryptography classed as unbreakable rather than merely unbroken; the deployment log names the backup's target archive, now catalogued among the Sealed, and nothing more. The reconstruction here is built entirely from the control software's source and its own comments, cross-read against that naming. No count of who stood in the line, or for how long, is recoverable, or ever will be.

## See also

- **The Serai Hold** — a quarantine allocator on the same emptying road, governed by a different equation and no less exact.
- **The Giant Component** — another network reconstructed from what a Sealed archive is known, and not known, to hold.

## Notes

The repository's final commit, dated +176 pT (2121 CE), reads only: `freeze prod, do not touch`. Nothing about the checkpoint was committed after it.
