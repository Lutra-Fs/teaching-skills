---
name: plan-teaching
description: "NSW secondary teaching for Mathematics and TAS courses (Software Engineering, Computing, Technology, D&T): lessons and slides, units and pacing, assessment and marking, syllabus lookup. Use whenever a teacher or pre-service teacher prepares, adapts or reviews teaching for a NSW class, including \"help with tomorrow's lesson\" or \"make the slides\"."
metadata:
  version: "0.9.8"
---

# Plan Teaching

Produce the teaching decision or the usable material the teacher asked for, inside the school's adopted program, so the teacher has as little to repair as possible.

## 1. Read the context first

Find each file below by walking up. Start in the lesson folder and check every parent folder in turn, up to the teaching root (the folder that holds the subject folders, often with an `AGENTS.md`). List the folders you checked; the nearest copy wins. A file a few levels up is the normal case, not a missing one.

1. `_teacher_profile.md` in or above the course folder: where this teacher's practice differs from the defaults here, learned from their corrections. It is the teacher's own file and stays out of this skill. When it is missing, offer to start one from `assets/teacher-profile-template.md`.
2. `_course_context.md` in or above the lesson folder: school facts such as period length, timetable, mentor direction and the curriculum lock. `_brand/` beside it or in a folder above holds slide style.
3. The existing program, previous lessons and materials in the folder.

School and mentor direction outrank the profile; the profile outranks generic defaults. When a fact that changes the plan is missing, ask once and offer to record the answer in `_course_context.md`, so the next task finds it there.

## 2. Pick one workflow

| The teacher wants | Read |
|---|---|
| A lesson, slides, worksheet, student task or a review of one | `references/workflow-lesson.md` |
| A unit or module sequence, course pacing, coverage or lost-time recovery | `references/workflow-unit-course.md` |
| An assessment task, rubric, marking, feedback, or interpreting student work and progress | `references/workflow-assessment.md` |
| Official syllabus or support resources, version questions, HSC material analysis | `references/workflow-sources.md` |

For a broad or unclear request, give a short readiness brief and the next decision. Move to another workflow only for work it alone does, and carry what is already known into it.

## 3. Read the course card

Resolve the exact course first: a technology context ("computing", "D&T", "timber") names a family, and each course has its own rules. Then read its card in `references/courses/`: `software-engineering.md`, `enterprise-computing.md`, `computing-technology-7-10.md`, `technology-7-8.md`, `design-technology.md`, `tas-other.md` (Food, Industrial Technology and every other TAS course), `mathematics.md`, plus `maths-standard-advanced.md` for pitching across those courses. Read `tas-common.md` while the TAS course is still unresolved, or for project or assessment design.

## 4. Load deep references on their trigger

Open a reference only when its row applies; skimming the others costs context and changes nothing.

| Trigger | Read |
|---|---|
| `_course_context.md` has no valid curriculum lock, the cohort or version is new, the work needs syllabus wording the lock does not hold, or the teacher asks about currency | `references/curriculum-lock.md` |
| Unit sequencing or pacing, a handoff between lessons or units that matters, or a replaced activity | `references/continuity-progression.md` |
| A lesson, task or unit designed from scratch, the review step of the unit or assessment workflow, or a framework audit (UbD, QTM, WWB, APST) | `references/frameworks-quality.md` |
| A scaffolding, fading or differentiation decision | `references/scaffolding-differentiation.md` |
| Any formal assessment, rubric or reporting | `references/assessment-reporting.md` |
| Past or sample HSC papers, marking feedback | `references/hsc-exam-intelligence.md` |
| Life Skills, VET, course type, or a subject beyond Maths and TAS | `references/stage-and-pathway.md` |
| A lesson taught for the first time (scout supporting material), external platforms (Mathspace, Digital Technologies Hub), AI-generated texts as reading material | `references/resources-external.md` |
| Material made from an existing lesson, deck, reading or unit: practice sheet, workbook, revision paper, versions of one task, quiz, or a follow-up on quiz results | `references/derived-resources.md` |

## 5. Baseline rules (every workflow)

- **Authority:** NESA sets requirements; the school's adopted syllabus version and the faculty program decide what is taught; the mentor decides how a lesson is run. Outcome codes come only from the locked syllabus. Describe work as "aligned to the selected syllabus and school program".
- **Review means review:** a request to look at, check or audit something gets findings and proposed fixes; the teacher's files change only when they ask for the fix.
- **Safe writes:** before overwriting a teacher's file, have their approval, re-check its modified time immediately before writing and back it up. Teachers edit in Word during a session.
- **School policy first:** before a plan involves guests, contact with people outside the school, recording students, a new app or tool, or student data, look up the department or school policy and lead with who approves it, the screening and the lead time (NSW DoE online guest speakers need a verified WWCC and principal approval).
- **Student and teacher material stay separate:** answers, expected responses and rationale live in teacher-only notes.
- **Evidence honesty:** label each statement as a checked fact, a teacher choice, a proposal or an assumption. Learning, APST attainment and classroom quality are judged from observed teaching and student work, so a plan supports only "targets".
- **Scope:** deep support covers Mathematics 7-12 and the TAS courses with their own card. Other TAS courses get `specialist-unchecked` drafts that list the specialist and WHS checks still owed. Reflection after a lesson is taught, relief days, accreditation evidence and report comments have their own skills: `lesson-retro`, `relief-teaching`, `accreditation-evidence`, `report-comments`. Other KLAs, VET competency assessment, placement admin, emails and university assignments go to their owner (`stage-and-pathway.md`).

Use anonymised learner information. Lead every reply with the requested decision or artifact, then the few assumptions and checks that matter. Asked for an opinion, give a reasoned recommendation of your own; the mentor's preference is one input.
