# Continuity, progression and handoffs

Read when a handoff between lessons, units, terms or teachers matters, when an activity or resource is replaced, when a project runs across lessons, or for recovery after lost time. Continuity means keeping a functional learning dependency intact: the next lesson can safely assume what this one hands on. Where modules are genuinely independent, record `no downstream dependency confirmed`.

## Pacing and recovery

Start from the approved course sequence. For the affected horizon, list the remaining usable lessons, required untaught content, assessment and project deadlines, protected practice and revision, and any real buffer. Keep **untaught** separate from **taught but not yet independently evidenced**.

Estimate time from recent comparable class performance first, then mentor or faculty experience and established sequences; mark model-only estimates provisional. Respect supplied evidence that a topic takes two or three weeks. Unpack a broad activity into prerequisites, new learning and student actions, including reading instructions, modelling, writing, correction, feedback, transitions, logins and closure. When the work exceeds the time, change scope or sequence and keep the estimates honest.

When learning needs and the schedule conflict:

1. Decide whether the gap blocks the next dependency, and for whom (whole class or a subset).
2. Compare whole-class reteaching, targeted support, later retrieval or practice, a different explanation or resource, and removing non-essential overhead. Required content keeps real teaching and practice time.
3. Recalculate against remaining time and fixed milestones. For each adjustment, show the time recovered or needed, what moves, what it displaces and which deadline or shared dependency it affects. Stage 6 deadlines are fixed; Stage 4 and 5 deadlines have limited room too.
4. Apply authorised changes and update the affected materials; changes outside the teacher's authority go to the mentor or faculty owner as proposals. When the plan cannot fit, give that owner the shortfall and concrete options, with honest estimates, every content point accounted for, and requirements, revision time and deadlines intact.
5. Update estimates from actual progress, faster or slower. Move the class on once the dependency is met; targeted support carries individual gaps.

Stage shapes the trade-off: Stage 4 often warrants more foundation-building, Stage 5 balances consolidation, coverage and pathway preparation, and Stage 6, especially near an HSC deadline, protects complete required teaching and assessment preparation while scheduling targeted recovery. Every Stage still needs learning evidence and has course obligations.

### Worked decisions

- **Routine inheritance:** the mentor's worksheet fits the next lesson and the class has shown its prerequisites. Reuse it, check its answers, and adapt the identified barrier.
- **Overloaded novice task:** a 50-minute request combines learning loops, designing a program and evaluating it, with no prerequisite evidence. Draft an entry check and a feasible first step, map the rest into the sequence and flag any milestone conflict.
- **Fixed-deadline recovery:** two extra lessons are needed before an HSC milestone and one buffer lesson exists. Test targeted recovery or replacing non-essential activities, and show any remaining shortfall to the owner.
- **Resource failure:** computers are unavailable. An unplugged tracing task keeps algorithm reasoning, and running and debugging the program still needs a lesson; record that missing evidence and reschedule it.

## What to keep continuous

Check the dimensions that matter for this boundary:

1. **Concepts:** prerequisite ideas and skills, agreed terminology, notation, representations and misconceptions.
2. **Evidence:** what has been collected, common criteria, moderation, assessment milestones and the next decision the evidence supports.
3. **Artifact state:** folio, dataset, codebase, design, prototype, draft or product that later work uses.
4. **Enactment:** routines, tools and environment, practical safety competence, group roles, help and submission routes.
5. **Coordination:** approved sequence, shared classes, versions, teacher handoff, deadlines and change authority.
6. **Re-entry:** a catch-up route for absence, transfer or incomplete prerequisites.

Subject notes: in Mathematics keep notation and representations and bridge a changed method explicitly; in Technology 7–8 keep the course-level plan for all four focus areas; in Computing courses keep repository, file, schema and tool versions, test evidence, authorship and the exact downstream interface, each course on its own structure; in Design and Technology keep the brief, criteria, folio state, prototype, testing evidence and material competence; Food Technology handoffs stay `unverified` until the specialist review is complete.

## Boundary record

One compact record at each consequential boundary:

```yaml
continuity_contract:
  boundary: lesson-to-lesson | module-to-module | term-to-term | teacher-to-teacher
  owner_or_approver:
  upstream: {required_learning, evidence_available, evidence_state, artifact_state}
  stable_conventions:
  downstream: {next_module_or_assessment, may_safely_assume, handoff_output_and_format, due}
  non_negotiables:
  teacher_may_adapt:
  reentry:
  status: ready | partial | blocked | unverified
```

Use `unverified` when the unit, worksheet, file schema or downstream expectation is unavailable; a creative draft can still help, labelled as a draft. Evidence states follow `scaffolding-differentiation.md` (`modelled | guided | prompted | independent | transfer`).

## Replacing an activity or resource

Before replacing, resequencing or omitting one, check that the new version gives the same learning advance and prerequisite rehearsal; evidence for the same next decision; the shared terminology, notation and routines (or a deliberate bridge); the required artifact in the required format; the mandatory order, milestones and practice; competence checks, adjustments and re-entry; and that the change is within the teacher's authority. Classify the result as a **teacher-level adaptation** (all interfaces intact and authorised), a **proposed change** (needs approval or coordination) or **blocked** (a dependency cannot yet be checked). A more engaging activity counts as equivalent once these checks pass.

## Handoff report

At the end of a lesson or module, report: what is independently evidenced and what was only taught or attempted; what needed support and whether it should stay, reduce or return; the exact artifact, version and location handed on; open misconceptions, missing work and blockers; who needs a recovery route; what the next lesson may safely assume; and the next owner and date.
