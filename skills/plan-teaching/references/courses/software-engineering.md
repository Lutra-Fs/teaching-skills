# Software Engineering 11–12

Board Developed Stage 6 course. Use [Software Engineering 11–12 (2022)](https://curriculum.nsw.edu.au/learning-areas/tas/software-engineering-11-12-2022/overview/course) with the live Course Specifications and record of changes. Course facts below are an 11 August 2026 routing snapshot: recheck the live course page, implementation advice and record of changes for each new cohort or version (see `../curriculum-lock.md`).

## Structure

- Year 11: Programming Fundamentals; The Object-Oriented Paradigm; Programming Mechatronics.
- Year 12: Secure Software Architecture; Programming for the Web; Software Automation; Software Engineering Project.
- Check each module's indicative time, the required programming language and examination assumptions, and any specification updates on the live page.
- Lock the school-based assessment components and weightings and the HSC examination page; task-count examples are examples.

## What good evidence looks like

Executable code, tests, documentation, secure design decisions, debugging and individual authorship evidence alongside the interface. Algorithm design, debugging, testing and trade-offs are usually the target thinking: starter code or a worked example may remove an access barrier, and the assessed decision stays with the student (`../scaffolding-differentiation.md`).

Software Engineering content, assessment and artefacts come from this course's own syllabus; Enterprise Computing is a separate course.

## Code across languages

When a task uses a programming language students have not been taught, put a syntax mapping table on the task page, with the taught language beside the new one. Run both versions before class, because a literal port can behave differently (in PHP, `(int)"abc"` is silently 0).

## Continuity artefacts

Repository, branch or file state; environment and dependencies; data or API contract; code style and naming; test results; issue log; design documentation; authorship evidence; a runnable handoff state.

## Runtime checks (software, data or network lessons)

Accounts, permissions and devices; file naming, storage and backup; starter code, test data and expected output; privacy, cybersecurity and data ethics; a debugging checkpoint and code readable on screen; authorship and GenAI conditions.

## Review quizzes (Stage 6)

- A paper review quiz is HSC practice: multiple choice, select-all and matching, plus two short-answer items modelled on real HSC items.
- Size it at about 1.8 minutes per mark (the HSC rate, 180 minutes for 100 marks), faster for pure recall, then fit it to the time in `_course_context.md`.
- Layout: HSC-style question pages under a compact header.
- Every quiz comes with NESA-style marking guidelines, in HSC format from the first draft: answer key; per short answer a Criteria/Marks table, a sample answer, "Answers could include" and marker notes. Model each item on a real HSC item with the same verb and marks (3-mark Explain: Explains 3, Outlines 2, Identifies 1; "Provides some relevant information" only for open 2-mark items); cap a generic answer at 1 mark.
- Write the band boundaries into the marker notes before marking, from the NESA glossary: Identify names the measure; Outline adds one concrete detail (what data, when, who decides); Explain adds why it protects the user, as a result (repeating the measure is not a reason). Section II carries a box defining its key words.
- Marker notes for common items: a privacy-by-design answer naming only security technology (encryption, MFA) reaches Identify at most (2025 HSC 16(c) feedback); an exploit-plus-fix answer needs a fix that matches the exploit, removing the feature is not a fix, and a correctly described method earns credit even when misnamed.
- Student feedback: one or two English sentences on the answer, naming the level reached and the missing step in the question's verb; no re-teaching. Class feedback uses NESA's form, "In better responses, students were able to" and "Areas for students to improve include", one to three short bullets each, with "rather than".

## Case material

Use current, source-checked Australian cases (for example OAIC actions, local breaches), dated. Use fictional or de-identified data for any example students handle.

Common design, activity and assessment guidance for TAS courses: `tas-common.md`.
