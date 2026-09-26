# The Thursday Sitting

*Terran Encyclopaedia, 3000 CE edition — Recovered Narratives. Reconstructed from a single micro-etched nickel plate recovered face-down from the grout of a concrete regulator plinth, and rendered into Reconstructed Late Combustion English by convention of the Historical Faculty.*

> **The Thursday Sitting is the Historical Faculty's designation for a weekly open-air water court of an unnamed Late Combustion gravity-irrigation district, which went on sitting for thirty-one years after an automatic channel controller had taken over every decision it had been created to make, and which is known from one nickel plate on which the district etched its rules, its roll, its controller's settings, and the court's own minutes.** The plate and the physics of the channel it describes are record; who sat, and for how long after the plate was set, is reconstruction.

---

**On Thursday 2 November +128 pT (2073 CE), at noon, the eight elected members of a lowland irrigation district's water court sat at the head regulator of the district's main channel and ratified a schedule of water deliveries that had been computed, timed, and already partly released by a machine.** They had done so every Thursday since +97 pT (2042 CE), and the court had sat in one form or another since the district's first season in +28 pT (1973 CE). Its original work — hearing who had taken water out of turn, and fining them in hours of flow — had ended with the turn itself, when motorised gates and metered outlets made taking water out of turn physically impossible. What remained was a signature: the controller's scheduler required a weekly ratification flag before it would run the coming week, and the sitting supplied it. The plate that records all this was etched for the district's hundredth season and set into the plinth of the regulator the court sat beside. It carries 9,412 pages; the minutes of thirty-one years occupy 1,690 of them, most one line long.

## The turn

The district was a Middle Combustion gravity scheme of the kind the age built on every regulated river it had: a head regulator on a river weir, a main channel of 38 km, and a branching tree of secondary channels serving 2,214 holdings through concrete outlets. Water moved by gravity and by a rota. An irrigator ordered water four days ahead; a channel-keeper — the age's word was *bailiff* — planned the releases, set the head gate, and walked the reaches lifting and dropping the timber bars of the check structures by hand. Four days was the transport time of a flow change down the channel, the keeper's rounds, and the bundling of orders so that a reach ran near capacity or not at all.

The court existed because the rota could be broken. An outlet opened out of turn drew down the pool for every holding below it, and the sitting heard such cases in the open, orally, at the regulator, without record, fining in hours of entitlement forfeited to the aggrieved. The discipline's comparison is to a medieval water court of the Iberian east that sat every Thursday at noon at a cathedral door on the same terms; the district's by-laws, etched on the plate, give the sitting's quorum as five and its judgments as final and unwritten.

## Integrator and delay

In +82 pT (2027 CE) the district automated. Every check structure became a motorised overshot gate with a level sensor on either side; every outlet was metered; a controller in the district office regulated the whole tree. The plate carries the commissioning handover, and the handover carries the model.

A channel pool between two gates behaves, for control purposes, as an *integrator with delay*. Its level rises at a rate set by the difference between inflow and outflow divided by the pool's backwater surface area *A_s*; but a change at the upstream gate reaches the downstream level only after a delay τ, the time a shallow-water wave takes to run the pool's uniform-flow reach. For the main channel's seventh pool the handover gives *A_s* as 2.2 × 10⁴ m² and τ as 1,300 s — 5.6 km of channel at a wave speed a little over four metres a second.

The delay is the whole difficulty. A controller that raises the upstream gate when the downstream level falls is acting on a level that will not answer for twenty-two minutes, and if it acts too hard each correction arrives after the last has already done its work. For a pure integrator under proportional control the loop is stable only while the gain is less than π/2 times *A_s*/τ; for the seventh pool that limit is about 27 m²/s, and the handover sets the gain at a sixth of it, with an integral time of 5,200 s and a first-order filter of 900 s on the measured level. The plate quotes the block as installed:

```
pool_07:
  model:      integrator_delay
  A_s_m2:     2.2e4
  tau_s:      1300
  ctrl:       PI_filtered
  kp:         4.5        # m2/s
  Ti_s:       5200
  lpf_s:      900
  q_cap_m3s:  2.6
  order_min_notice_s: 21600
  ratify:     required
  ratify_timeout_s:   604800
  on_timeout: carry_previous
```

## The string

The gates were run in the *distant-downstream* configuration: each gate held the level at the far end of the pool below it, where the outlets were, so that a holding drawing water drew on its own pool and the gate above answered the draw. The arrangement has a known vice. A flow change at the tail propagates upstream from pool to pool as each controller answers the one below, and unless each loop is shaped so that its flow demand never exceeds the disturbance that caused it, the string amplifies: the head regulator sees a swing larger than the outlet that started it. The handover's filter and its modest gain are the price of the property the age's engineers had borrowed from the theory of vehicle convoys and called *string stability*; they bought it with slower level recovery, and the plate records the trade without comment.

The rest was allocation. Orders — a flow, a start, a duration — were placed by terminal with six hours' notice, the sum of the pool delays from the head plus a margin, and the scheduler packed them into the channel's capacity reach by reach. Where orders in a reach exceeded its rated flow the scheduler shifted starts, and where shifting could not fit them it refused, by a rule the sitting had set: the roll's priority column first, then pro rata by entitlement. The order book was also the controller's feedforward: the head gate released each order's flow τ ahead of every pool it would cross, and feedback had only the residual to correct. The district's conveyance efficiency, by its own meter data, rose from 64 to 87 per cent in four seasons.

## Ratification

Nothing in the design required the court. The sitting was retained by a by-law of +82 pT that the plate preserves in full, and that the discipline reads as the district's answer to a question it had evidently asked: whether a machine should refuse a holding its water without a person having agreed to it. The answer was the ratification flag. Each Thursday the coming week's schedule, with its refusals, was read to the sitting; the sitting could hear a refused order, reassign priority between holdings, and ratify; the flag was set; the scheduler ran. If the flag was not set within seven days the configuration carried the previous week's schedule forward unaltered. The minutes record that this never occurred in thirty-one years.

The minutes are the plate's largest document, and its thinnest. From +97 pT they record for each sitting the date, the members present, the seasonal allocation fraction in force, the number of refused orders heard, and the word *ratified*. In the first season the fraction is 100 per cent and refusals heard number three for the year; in the hundredth the fraction is 58 per cent and refusals heard number 214. The hearings had no power over the capacity constraint, which was hydraulic, and none over the allocation fraction, which was set above the district by the river authority; what a hearing could do was move a holding up the priority column, which moved another down. The minutes record the reassignments by holding number only.

## Face to the grout

The plate is electroformed nickel, 100 by 100 mm and 1.2 mm thick, its record etched as analogue micro-images at 150 dots per inch, some two thousand pages to the square centimetre, legible under any optical microscope at a hundred and fifty times. The district's whole record occupies a patch 2.3 cm on a side; the rest is mirror. The etching firm sold a fixed number of pages for a fixed price, and the clerk, the transmittal note shows, sent the entire contents of the district's document store — by-laws, roll, minutes, and the controller vendor's handover with its configuration files — rather than select from it.

The firm's advice, printed on the transmittal, was a free-standing stainless mount to keep both faces in air. The mount was struck from the centenary budget, and the plate went to the concrete contractor with the instruction *set flush*. The etched face, to the eye, is a blank grey mirror with a faint rainbow sheen; the reverse carries the firm's stamp, a serial, and a batch date in ordinary engraving. The contractor set the stamped face outward, as the side that could be read, and the record went into the grout. Cement pore water stands at a pH near 13, and nickel — the metal the age used for its caustic vessels — is passive there; the etched face came out of the plinth in 2957 CE without measurable loss of surface. The stamped face, exposed for eight centuries under the silt that buried the regulator when the channel bank failed, is illegible.

The plate bears what it bears. It gives the district's rules, its roll to the holding, its controller to the parameter, and its court to the week, and it stops on the Thursday it was etched. It does not say whether the eight sat the following week, whether the flag was set or the schedule carried, or how long the channel ran; Halvorsen's taphonomy places the bank failure after maintenance had ceased and cannot date it closer than a century. The last document on the plate is the minute of 2 November +128 pT (2073 CE): eight members present, allocation 58 per cent, 11 refusals heard, *ratified*.

---

## Provenance and ground

The plate is the sole witness: a micro-etched nickel centenary record recovered from the grout of a regulator plinth on a silted lowland channel, read by optical magnification without decoding. The channel model, the stability bound, the string-stability property, and the nickel chemistry are the period's own published engineering and are checkable; the district's efficiency figures are its own meter data as etched. The court's sittings before +97 pT are known only from the by-laws, as the by-laws say they kept no record.

## See also

- **The Three-Tenths Setting** — an earlier canal that apportioned water by masonry alone, with no controller and no court.
- **The Weighed Plain** — an irrigation district recorded on unreadable reels and in the gravity field.
- **The Night-Charge Ledger** — another Late Combustion record struck on nickel to satisfy a rule, and read for what the rule never asked.
- **The Waiting List** — an allocation system that went on computing correctly after its subject had gone.

## Notes

- The proportional-gain limit quoted is that of a pure integrator with a pure delay under proportional feedback; the installed PI-with-filter loop's margin is larger, and the handover does not state it.
- Holding numbers in the minutes are cross-referenced to the roll by Okonkwo, who notes that the priority reassignments of the last ten seasons move 61 holdings up and 61 down, and that no holding appears in both lists.
