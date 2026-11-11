# Curriculum lock and official resources

Read only when `_course_context.md` has no valid lock for this course, the cohort, term or syllabus version changed, or the teacher asks about currency or official resources. Once a lock is confirmed, record it in `_course_context.md` so later tasks reuse it instead of repeating this lookup.

## Contents

- Where to read syllabus text (for a wording lookup, this section is enough)
- Who decides what
- Find the live source
- The lock record
- Official resources: roles and compatibility
- When to stop and confirm

## Where to read syllabus text

This table is the one place these pointers live; update it here when an address changes.

| Order | Source | Use |
|---|---|---|
| 1 | [nesa.easedup.com/index.md](https://nesa.easedup.com/index.md): NSW TAS, Mathematics K–10, HSIE (third-party republication; add `.md` to a page URL) | First stop for outcomes and content wording |
| 2 | `~/Documents/Teaching/<Subject>/Curriculum_and_Syllabus/`; `Teaching/Library/Syllabus_and_Curriculum/` (Mathematics in `Mathematics/`) for subjects not currently taught. Read the official copy found there (a per-course PDF `NESA - <Course> (<year>) - Syllabus / Support (downloaded YYYY-MM).pdf` first, else a docx or a dated extract); for a PDF read only the pages needed (`pdftotext -f N -l M`) | Courses the wiki lacks (Software Engineering 11–12), "Example(s):" blocks, and checks |
| 3 | The school or mentor program and scope and sequence in the course folder; the NSW What Works Best guides in the teacher's Google Drive | What this class is taught; teaching practice |
| ref | [acv9.easedup.com/index.md](https://acv9.easedup.com/index.md) (Australian Curriculum v9, F–10); [aitsl.easedup.com/index.md](https://aitsl.easedup.com/index.md) (APST, to look up Standard numbers) | Comparison and resource mapping only, never NSW outcomes |

The wiki is unofficial and shows no version, so the lock records the page URL and the date read. It drops the syllabus "Example(s):" blocks; read those in the official copy. Some courses are reachable only from the wiki's HTML home menu, not `index.md` (Computing Technology 7–10: `/tas/computing-technology-years-7-10/content-stage-5.md`, focus areas as headings). A check on 5 November 2026 found its CT 7–10 outcomes and Analysing data content identical to the official 2022 syllabus. Check outcome codes, and any wording that goes into an assessment task or marking guidelines, against the official page or the dated official PDF.

**Local IDs.** NESA does not number content points. When a lock or coverage table needs to point at one, give it a local ID (`SE-SSA-03`: course, focus area, order) marked local. Local IDs stay out of student material and outcome columns.

**Learning components.** Under each content point the lesson or unit uses, list the smaller steps students learn it through, in teaching order, labelled proposed. When designing a sequence (backward design), break down every content point of the unit first, then sequence; when following an existing program, break down only the points each lesson uses.

## Who decides what

Use the sources together, not as a simple ranking:

1. **NESA** defines the permitted syllabuses, outcomes, content, course structure, assessment, reporting and ACE rules.
2. **Sector or school implementation** decides which permitted version and timeline this cohort follows.
3. **The faculty program** controls the approved units, sequence, common assessment, resources and change process.
4. **The mentor and classroom** control lesson enactment, routines, facilities and learner needs.
5. **University or practicum requirements** control PST documentation only; they do not replace the school program.

The newest publication is not automatically the right one: during reform an outgoing syllabus can still be correct for one Year 12 cohort while Year 11 uses the new one. If the school's version looks inconsistent with NESA advice, record both observations and flag it for the mentor or head teacher; the program stays as it is until they decide.

**Ownership:** note whether the unit is faculty-led, collaborative or teacher-led, who owns lessons, sequence and assessment, what the teacher may adapt and what needs approval. In a faculty-led unit, propose rather than make changes that affect coverage, common assessment, comparability or handoffs. For a PST: follow school and university templates, label unapproved changes `proposed`, and describe possible APST evidence without claiming a Standard is met.

## Find the live source

Start at [NSW Curriculum](https://curriculum.nsw.edu.au/), [NESA curriculum](https://www.nsw.gov.au/education-and-training/nesa/curriculum), [Assessment and reporting](https://curriculum.nsw.edu.au/assessment-and-reporting) and the [Record of changes](https://curriculum.nsw.edu.au/resources/record-of-changes). Resolve the exact course first: "Maths Standard", "D&T", "computing" or "food" is not a course.

For the exact course, check: status label (`Teach in`, `New from`, `Outgoing`, `In development`); implementation advice for the target year and cohort; outcomes with exact code and wording; content with focus area and parent outcome; assessment, course specifications and HSC examination where they apply; glossary and record of changes; ACE and the school assessment policy.

Read the live official page itself; a search snippet or an old page that still opens can be out of date. If a dynamic page shows only "Loading", use its official custom download or direct asset link, or ask the teacher for the official extract. Follow [NESA copyright conditions](https://www.nsw.gov.au/education-and-training/nesa/copyright).

## The lock record

Write this once per course and cohort into `_course_context.md`:

```yaml
curriculum_lock:
  checked_on:
  exact_course:            # e.g. Software Engineering 11-12 (2022)
  cohort_and_year:         # e.g. Year 11, 2026-27
  status_for_cohort:       # Teach in | New from | Outgoing | unknown
  evidence_of_school_adoption:
  source:                  # wiki URL or official extract file, with date read
  outcomes_used:           # code + exact wording, only those this program uses
  content_used:            # local ID + exact wording + focus area; learning components in teaching order
  course_requirements:     # hours, mandatory projects or practicals, specifications
  assessment_requirements:
  ownership:               # faculty-led | collaborative | teacher-led; who approves changes
  unresolved:
```

Refer to it in course, unit, assessment and lesson work. Recheck when the cohort, term, syllabus, school direction, unit version or assessment rules change.

## Official resources: roles and compatibility

Open the exact course and choose the branch that matches the request: `Overview / Outcomes / Content` for authority; `Teaching and learning support` for advice, sample scope and sequence and sample units; `Assessment` for standards, sample schedules and tasks and HSC specifications; the legacy NESA course page when the school uses an outgoing syllabus; [HSC exam papers](https://www.nsw.gov.au/education-and-training/nesa/curriculum/hsc-exam-papers) and [HSC standards materials](https://www.nsw.gov.au/education-and-training/nesa/curriculum/hsc-standards) for Stage 6 exam evidence.

| Role | Includes | Use |
|---|---|---|
| authority | syllabus, outcomes, content, mandatory course and assessment rules | must be followed |
| official guidance | teaching advice, implementation support, glossary | informs judgement |
| official example | sample scope and sequence, unit, schedule, task | adaptable model, never a mandated sequence |
| exam evidence | past or sample papers, marking guidelines, marker feedback, standards samples | evidence of examined demand |

Check each candidate against the exact course and pathway, syllabus version, cohort and implementation window, Year 11 versus Year 12, course type, and its status (current, outgoing, future or sample). Label it `compatible`, `partial mapping required`, `future or sample only`, `outgoing for another cohort`, `incompatible` or `unverified`. A filename date does not prove applicability. Retrieve only what the current decision needs, and record title, URL, checked date, compatibility and any adaptation needed.

For a pure lookup, stop at the shortlist and provenance.

## When to stop and confirm

Keep preparing reversible, independent parts with labelled assumptions, but confirm before finalising a decision that could change: the syllabus or cohort; a mandatory component or assessment condition; the approved sequence or a common task; a required handoff or carried-forward artefact; Life Skills or VET selection; safety, supervision, adjustments or privacy. Mark affected parts unverified or proposed, and carry on with unrelated preparation.
