# The Giant Component

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from partial route-collector snapshots set against one of the Sealed, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Giant Component is the Historical Faculty's name for a regional Internet exchange point of the Gangetic plain and for the roughly forty minutes in +121 pT (2066 CE) in which its member networks stopped, almost entirely, being able to reach one another.** The exchange's full internal graph is sealed beyond recovery; what survives is a handful of incomplete outside snapshots of it, taken before the fact, and the physical rack on which its operating name was stamped.

---

Six percent of the exchange's members were enough to end it. At its last complete outside count the exchange carried two hundred and thirty-one autonomous systems — the independently operated networks of local carriers, a university consortium, two irrigation-authority telemetry operators, and a cluster of small hosting firms — each identified only by a registry number and bound to the others by bilateral peering links and a shared route-server pair. Fourteen of those two hundred and thirty-one stopped answering across the same forty minutes. What should, on the network's own recovered shape, have been a shrug became a fracture: the exchange came apart into islands that could not route to one another at all, and the largest surviving connected cluster afterward — the *giant component*, in the discipline the age itself used for the term — held under a third of the members it had held that morning. The event is legible only at one remove: the exchange's own encrypted operations archive is one of the Sealed, and the reconstruction is built entirely from what other systems happened to record about it from outside.

## A co-operative among rivals

The exchange was established in +89 pT (2034 CE) as a neutral meeting point where competing regional carriers exchanged traffic directly rather than paying to route it through a distant transit provider, an arrangement common across the period and never itself remarkable. Each member ran its own router, advertised the address blocks it served, and withdrew that advertisement the moment it could no longer serve them; a shared route-server pair relayed each member's routes to every other member, so the exchange's connectivity graph was redrawn continuously and held by no single custodian at any one time. This is ordinary Late Combustion network engineering, and the mathematics that governs its failure is the same mathematics that governed every such exchange on the planet.

## The shape of the tail

A handful of members carried disproportionate weight. Reconstructed from the surviving fragments, the exchange's degree distribution — the number of peering links a member held — falls off as a power law, roughly *P(k) ∝ k⁻ˠ* with an exponent γ near 2.1, the same range the period's own topology studies reported for autonomous-system graphs generally. A distribution with an exponent between two and three has a defining, counter-intuitive property, proven in the period's own network-percolation literature: its second moment grows far faster than its mean as the sample grows, so κ = ⟨k²⟩/⟨k⟩ — the expected degree of a node reached by following a random edge — has no obvious bound as the network is measured more completely. The critical fraction of nodes that must fail at random before a giant component ceases to exist is *f꜀ = 1 − 1/(κ − 1)*; for the exponent reconstructed here, κ already runs into the tens at the exchange's modest scale, putting the random-failure threshold above nine-tenths of the membership. Against uncorrelated failure such a network is close to unbreakable — the period's own engineers called this "robust yet fragile," because the same mathematics gives the opposite answer against a different failure: remove nodes in descending order of degree instead of at random, and the same graph fragments after the loss of a small fraction of its highest-degree members, since those few carry a share of all edges wildly out of proportion to their number. The fourteen autonomous systems that went dark in +121 pT held, between them, past sixty percent of all peering edges recorded at the exchange. By degree alone, their loss is indistinguishable from a targeted attack on the network's hubs.

Nothing attacked it. A capacity-planning memorandum filed with the exchange's steering committee in +114 pT (2059 CE) — six years earlier — had already run this exact calculation, named the fourteen highest-degree members by registry number, and recommended a mandated minimum peering diversity to blunt the concentration. The memorandum survives complete, was circulated, and was not acted on.

## Fourteen nodes

The fourteen were not chosen by an adversary; they were chosen by heat. Every one operated from, or leased colocation floor space in, one of three low-lying district towns on the exchange's service footprint that crossed the wet-bulb 35 °C threshold earlier and more often than the exchange's inland members, and all fourteen belonged to the wealthier tier of the exchange's membership — the tier able to relocate its operations staff, if not always its hardware, ahead of the heat rather than after it. They left in the same six-week window, not because they were the exchange's hubs but because they were the members positioned, by capital and by geography, to leave early; that they were also the hubs was a consequence of which networks a co-operative peering exchange rewards with the most connections in the first place — the well-capitalised, well-connected, and urban. One surviving route-server log fragment, timestamped in the exchange's own operational shorthand, records the withdrawals as they arrived:

> `03:14:52Z  AS132904 WITHDRAWN  peer down  no keepalive  // link is not coming back, isn't it`
> `03:19:08Z  AS132917 WITHDRAWN  peer down  no keepalive`
> `03:41:26Z  AS132861 WITHDRAWN  peer down  no keepalive  // second one today only`

The invariant tag on the first line and the particle "only" on the third — a South Asian English construction already displacing its prescribed alternative throughout the exchange's own operator corps, and the direct ancestor of a feature Standard Terran still carries — mark the log as human-annotated rather than machine-templated at those two lines, one of the few places in the fragment where a person, rather than the route server's own logging daemon, can be shown to have touched the record.

## Two readings of the same graph

The exchange's full route-server database — every peering session, every withdrawal, every member's complete advertised table — was backed up nightly to a symmetric-ciphered archive keyed from a hardware security module that zeroised its key material on the same power loss that took the fourteen members offline; unlike the public-key traffic of the Wasatch Corpus, broken wholesale once quantum factoring caught up with it, a well-implemented symmetric cipher of that era resists even that attack, its effective work factor merely halved, not broken, by the fastest method known against it. The archive is accordingly one of the Sealed: known to exist, known to contain the complete graph, and provably beyond recovery. Everything in this entry is instead built from partial snapshots taken by an unrelated offsite route-collector project, which peered with the exchange's route servers for research purposes and logged whatever portion of the table happened to propagate to it — a visibility that was never complete even when the exchange was healthy.

Adeyemi-Solberg, F., who reconstructed the degree distribution from these snapshots, reads the event as confirmation of Ibarra, N.'s doctrine of single-filament infrastructure: a network built, like so much of the age's infrastructure, on a small number of load-bearing points, whose fall was made to look targeted only because wealth and hub status had already been made the same thing. Zhou-Ferreira, A. holds the opposite: that a degree distribution inferred from an incomplete, unevenly sampled collector feed cannot support an exponent precise enough to justify the distinction between "robust" and "fragile" in the first place, and that a small, ordinarily uneven network might have fragmented at six percent regardless of who left or why. The complete graph that would settle it sits, undamaged and unreadable, on the archive that recorded it.

---

## Provenance and ground

The entry rests on route-collector snapshots covering roughly four months before +121 pT, an operator log fragment recovered from the same collector's cache, and the exchange's Sealed nightly backup archive, confirmed intact by its unbroken checksum header but not decryptable. The percolation mathematics — the degree-dependent giant-component threshold, the divergence of κ for exponents below three, and the targeted-versus-random asymmetry it implies — is the period's own established network theory, independently verifiable and untouched by the reconstruction's uncertainties; only the exponent estimate, the identity of the fourteen members, and the reading of their departure as heat-correlated rather than engineered are reconstruction. The exchange's operating name, "Fatehgarh Exchange, node one," survives in exactly one place: stamped into a steel asset tag riveted to the chassis of a route server recovered from a flooded ground-floor server hall, legible under the corrosion by relief alone.

## See also

- **The Wide Synchrony** — a continental machine whose coupling, not its concentration, carried a different failure.
- **The Silent Quarter** — the same threshold mathematics run on an unweighted network, thinning rather than fracturing.
- **The Nine of Fifteen** — another custody broken by the same class of archive this entry cannot open.

## Notes

The capacity-planning memorandum of +114 pT is complete in the collector's cache; the minutes of the steering-committee meeting that received it record only that the item was "noted," with no vote entered either side.
