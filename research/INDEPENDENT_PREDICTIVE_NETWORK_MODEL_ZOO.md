# Independent Predictive Networks — adversarial finite model zoo

All rows use finite local record histories and finite challenge–response
interfaces.  Slot addresses are local syntax only; no row identifies an A
send with a B receive.

| ID | declaration | result / firewall |
|---|---|---|
| IPN-M1 | Two length-6 cyclic local predictors; A sends `001011` at phase 0, B records the ordered received word at phase 2; response checks pass. | Trivial cyclic stabilizer fixes `delta_AB=2`; each origin remains locally ambiguous. |
| IPN-M2 | Same local sectors; bridge word `0101` on a length-4 cycle. | shifts 0 and 2 survive: periodic records do not synchronize uniquely. |
| IPN-M3 | M1 with interface storing only the multiset of received labels. | forward and reverse alignments remain: correlation does not fix orientation. |
| IPN-M4 | Local record labels are both `tick`; no send/receive procedure or interface clause. | label equality is syntax; no correspondence is defined. |
| IPN-M5 | Equal alternating profile tables in two systems, but no IPN3 bridge. | apparent correlation is not theory content. |
| IPN-M6 | Raw A duplicates are one A quotient class but produce two proposed code translations; B input is fixed. | value varies on a fibre: `HIDDEN_Q_DEFECT / NOT DEFINED`. |
| IPN-M7 | M1 plus simultaneous phase-coordinate shifts. | same predictions and bridge facts, different absolute origins: origin is surplus. |
| IPN-M8 | A/B/C offsets in `Z_5`: AB=1, BC=1, AC=1. | all pair bridges exist but no one global phase representation. |
| IPN-M9 | A/B/C offsets in `Z_5`: AB=1, BC=2, AC=3. | global representations exist but differ by common shift; edge offsets and cycle law survive. |
| IPN-M10 | Pairwise bridge factors each exist only on separately declared supports whose shared local record overlaps with incompatible code. | pairwise factors do not automatically glue; support union needs its own check. |

The required positive claim uses M1, not the stronger M9 coordinate
representation.  M9 merely exhibits representational surplus after the
shared edge facts have already been admitted.
