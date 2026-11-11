# Plan Secondary Teaching maintenance contract

## Intent and shape

Reduce preparation and review work by delivering course-aware, evidence-informed and operable teaching artifacts. Primary shape (v0.3.0): a short core (SKILL.md) that reads context and routes to one of four workflows (lesson, unit-course, assessment, sources); one card per course in references/courses/; deep references loaded only on their stated trigger; scripts for mechanical checks. The common path (a lesson) reads SKILL.md, teacher-profile, workflow-lesson and one course card, about 3,000 words. No service, agent delegation or provider-specific runtime is required.

Scope remains NSW Mathematics 7–12 and the exact supported TAS courses declared in SKILL.md. Food Technology stays extension-only; unrelated teaching areas, placement administration, accreditation management and career work remain outside scope.

## Evidence and architecture

SKILL.md owns context, routing and baseline rules (with reasons). Four references/workflow-*.md files own execution and finish conditions; workflow-lesson.md is self-contained for an ordinary lesson. One source per fact: Stage language rules live in workflow-lesson.md, the curriculum lock in curriculum-lock.md and, once confirmed, in the course folder's _course_context.md. Other references own specialised decisions; assets shape requested outputs. SOURCES.md retains provenance, source limitations and synthesis history, not everyday reading requirements. Keep subject-specific rules, curriculum versioning, Stage/pathway distinctions, formal assessment and safety constraints intact during deduplication.

Promote reusable procedures, not a particular class's assumed pace. Store actual class progress only in authorised teaching files; no identifiable learner information in this skill. Source agreement is not independent replication. Distinguish authority, research-informed practice, practitioner reports, model estimates and actual classroom evidence.

## Acceptance scenarios

Compare prior and revised outputs under the same inputs and model when behavioural evaluation is available:

1. Existing mentor lesson: inherit sequence and reuse materials; supply checked answers without redesigning the unit.
2. Novice project in 50 minutes: expose hidden learning demands; draft a feasible entry and remaining sequence, not an implausible complete project.
3. Supplied two-to-three-week class pace: preserve the evidence-based estimate, account for real lesson frequency, and expose any deadline conflict.
4. HSC recovery exceeds buffer: calculate the shortfall, propose concrete recovery/coordination and preserve required teaching; no silent deadline shift or omitted content.
5. Guided success but independent errors: record support state, target recovery and update the next dependency without claiming mastery.
6. Device failure: retain achievable learning, distinguish missing practical evidence and update downstream arrangements.
7. Official source lookup only: return compatible resources, no lesson pack.
8. Food Technology / Life Skills / VET: retain support and authority boundaries.
9. Required PST template: preserve fields; do not force all gradual-release phases into one lesson.
10. Content exceeds one real period: split into consecutive single lessons, each with its own exit question; do not compress every phase or assume a double period.
11. Lesson request without mention of slides: still deliver a followable deck with opening and exit; no slide previews later steps.
12. Previous lesson unfinished: open with a brief recap only; do not reopen the previous activity.
13. Review-only request: propose, do not edit; after approval re-check modified time and back up before writing.
14. Same topic for Stage 4 and Stage 6: wording, term handling and question verbs differ visibly; a Stage 6 deck with childish register or untaught terms is caught and repaired.
15. Third lesson in a unit: routines and slide style match earlier lessons, while the case, task mechanism and question forms are not repeated without a learning reason.

16. Slides drafted before the teaching decision: the blueprint (teacher move, student action, evidence, misconception) comes first; each slide has one purpose and layout; the visual, pedagogical and content slop checks run before delivery.
17. Mechanical defects (words per slide against a budget for the slide's purpose, separator glyphs, small fonts, timeline arithmetic, answers in student files) are caught by scripts/lint_slides.py rather than by rereading.
18. Word budgets never compress meaning: task and exit questions keep full sentences, the directive verb and the information needed to answer (Bill, 2026-10-23, after iteration 2 showed telegraphic Year 11 questions under a flat 40-word cap).

## Token budget

Track tokens per run in the benchmark. Target: a lesson eval run of 75k tokens or fewer on Haiku, with no drop in pass rate against the previous version.

## Validation and limitations

Run the skill-writer structural validator and check local reference/asset links. Static scenario walkthroughs assess instruction coverage only, not generated lesson quality. Behavioural comparison and mentor/classroom use are needed before claiming better pacing, teaching outcomes or time savings. Track teacher repair effort and sequence/material defects, not document length alone.

Keep changes reversible with a pre-edit snapshot. Existing local source paths are convenience references, not guaranteed resources on another machine. No automatic cross-session state or physical classroom checks are implied.

## Workflow acceptance

- Each of the four lanes resolves to exactly one directly routed workflow with ordered steps and a deliver section.
- Load shared knowledge at the relevant step; do not copy whole source-lock, scaffolding, pacing or verification protocols into every workflow.
- Transfers carry current constraints/evidence, affected work and a return condition. They do not restart intake, imply subagent delegation or expand audit authority into file mutation.
- A bounded resource edit does not trigger a complete semester audit. A deadline conflict does reach the pacing steps in workflow-unit-course; absent new evidence an unresolved conflict is reported rather than repeatedly transferred.
- HSC source analysis routes to workflow-sources, course implications to workflow-unit-course and practice production to workflow-lesson. Keep the exact exam evidence reference in each relevant route.

## Material quality review acceptance

Lesson, unit and assessment task workflows explicitly call the qualitative QTM-informed design/review/revision procedure. Findings must point to actual task evidence and the inherited purpose; repairs must preserve scope, conditions and course time. Fluency is not automatically a defect; absent QTM elements do not force added activities. Audit requests do not silently mutate files. Official coding remains a separate requested procedure. Static review of these rules is not empirical quality validation.
