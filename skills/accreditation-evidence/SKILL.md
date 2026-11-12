---
name: accreditation-evidence
description: "Evidence for Proficient Teacher accreditation in NSW, read against the AITSL Teacher Standards: a running evidence log from the first teaching day, choosing 5-8 items, annotating them, coverage across the 7 Standards, the supervisor observation, and deadlines. Use for \"accreditation\", \"eTAMS\", \"annotated evidence\", \"which Standard does this show\" or \"am I on track for Proficient\"."
metadata:
  version: "0.1.0"
---

# Accreditation Evidence

Help a provisionally or conditionally accredited NSW teacher reach Proficient on evidence that already exists in their practice. Two authorities apply, and each answers a different question:

- **AITSL** owns the *Australian Professional Standards for Teachers*: what Proficient practice is. Descriptor wording, the four career stages, and Illustrations of Practice for calibration come from aitsl.edu.au.
- **NESA** owns the *process* in NSW: what is submitted, by when, and who decides. The rules come from the NSW Teacher Accreditation Manual, section A3.

Keep the two apart: a descriptor question goes to AITSL text, a "how many, by when, who signs" question goes to the NESA manual.

## Ground rules

- **Fetch, never recall.** Quote descriptors from the AITSL Proficient page and process rules from the current A3, and record each source with the date checked in the log. A paraphrased descriptor is a rejection risk; process rules change (HALT, maintenance and supervisor roles all changed since 2022).
- **Only what happened.** Annotations describe the teacher's actual practice and the evidence they hold. When an item lacks impact evidence, say so and name what to collect next time; leave the gap visible.
- **Anonymise.** Student work is de-identified before it goes into any AI tool or the submission.
- **Human steps stay human.** The observation, the supervisor's declaration and the principal's recommendation are done by people; list them as outstanding until they are.

## NESA process (A3, checked 2026-11-12, page current as of 2026-05-14)

- Complete NESA's online Proficient Teacher Orientation Course.
- Submit **5-8 items** of annotated documentary evidence in eTAMS, **up to 35 pages and 10 MB**.
- Each item addresses **2-4 Proficient descriptors**; together they address **at least one descriptor from each of the 7 Standards**.
- One **observation**: teacher and Accreditation Supervisor agree the lesson and 2-4 descriptors beforehand; the report (with the teacher's reflection) is due within 14 days.
- **Supervisor** (Proficient or above, knows the teacher's daily practice) declares within 28 days; **principal or delegate** recommends within 28 days; **NESA** decides within 28 days.
- **Timeframes** from the accreditation date: Provisional 3 years full-time, 5 years part-time or casual; Conditional 4 and 6. A principal cannot record "not accredited" before 160 days of teaching.
- **Several schools** (typical for casuals): evidence from other schools is authenticated by a colleague accredited at Proficient or above; the supervisor usually comes from the school where the teacher works most.

Re-check A3 before any submission step; update this section and `SOURCES.md` when it changes.

## Steps

1. **Status.** Record accreditation type (provisional or conditional), date, employment (full-time, part-time, casual), deadline, days taught so far, orientation course done, and the supervisor if one exists. Keep it at the top of `_accreditation/evidence-log.md` in the teacher's own folder, outside any repository.
2. **Lock the descriptors.** Fetch the 7 Standards' Proficient descriptors from AITSL into `_accreditation/descriptors.md` with the URL and date. Use AITSL's Illustrations of Practice at Proficient to judge what "Proficient-level" looks like before mapping. A Graduate-stage descriptor from initial teacher education shows the starting point, and the Proficient wording is what the item must meet.
3. **Log as you go.** For each candidate artifact add a line: date, school, class, what it is (program, lesson and slides, assessment and marking, student work with feedback, communication with a parent, PD applied, faculty contribution), the 2-4 descriptors it may show, impact evidence held (yes, or what is missing), and the authenticator if from another school. Casual days come in through `relief-teaching`'s day log; lessons and assessments from `plan-secondary-teaching` are candidates as soon as they are taught.
4. **Choose 5-8 items** that between them cover all 7 Standards. Show a coverage table (Standard, descriptors addressed, items) and name the thin Standards, so the teacher collects for those rather than adding more of what is already covered. Prefer items where student work shows a change; Standards 6 and 7 usually need deliberate collection (PD applied in a lesson, work with colleagues, parents or the community).
5. **Annotate** each item in the teacher's voice: context (class, timing, why), practice (what the teacher did, in the descriptor's own terms), impact (what the evidence shows changed for students), and what they would refine. Keep within the eTAMS field and the 35-page total.
6. **Observation.** Help pick a lesson and 2-4 descriptors not yet well covered, and prepare the plan; afterwards draft the teacher's reflection from what they report.
7. **Check before submission:** every quoted descriptor matches the locked AITSL text; every claim is something the teacher reported or the evidence shows; all 7 Standards covered; 5-8 items within 35 pages and 10 MB; other-school items authenticated; outstanding human steps listed.

Done when the check holds and the remaining human steps are listed by name and date.

## Out of scope

Maintenance of accreditation and PD hours; HALT accreditation; AITSL's skills assessment for migration. Each has its own process and source: say which, and point to NESA or AITSL.

## Sources

See `SOURCES.md`.
