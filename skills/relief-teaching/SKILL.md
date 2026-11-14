---
name: relief-teaching
description: "Relief lessons in NSW secondary schools, from either side. Cover: a casual or relief teacher taking someone else's class (reading the plan left, a class with no plan, the note left afterwards). Handover: a teacher leaving their own class for a reliever (sub plans, cover notes, a relief day pack). Use for \"I'm on a casual day at X\", \"no work was left\", \"I'm away tomorrow\" or \"write cover notes\"."
metadata:
  version: "0.1.1"
---

# Relief Teaching

A relief lesson succeeds when the class is safe, the students do work that moves their learning on, and the class teacher can pick up the next lesson from what the reliever leaves. Both branches work towards that same handover.

Decide the branch first: **Cover** when the user is the one walking into someone else's room; **Handover** when the user is leaving their own class. A casual teacher can need both in one week.

## Rules for both branches

- **Duty of care first.** Medical alerts, students who leave the room, evacuation point and a named colleague nearby come before any lesson content. For a medical alert, record where the student's action plan is kept, where the medication is, and who in the building is trained; the action plan governs what to do, so point to it rather than restating its steps.
- **Anonymise.** Use initials or "Student A" in anything an AI tool processes; the teacher adds names in the school's own system. NSW public schools endorse NSWEduChat and no other free AI tool for this work.
- **The reliever may not teach this subject.** A Mathematics or Computing class is often covered by a teacher from another faculty, so the task must run from the page: no new explanation needed, no dependence on a login, a specialist room or a machine. If the lesson uses computers, give a paper fallback.
- **Plain language.** No outcome codes, syllabus terms or school acronyms in what the reliever reads.
- **The pack supplements the school's induction.** It does not replace child-protection training or the school's casual induction; say so in the pack.

## Cover: taking someone else's class

1. **Before the day (or at the front office):** collect the timetable, room numbers, roll procedure, the duty roster and the name of the head teacher or a neighbouring teacher to call. Use `assets/day-sheet.md` as the checklist; fill what the school gives you and list the gaps to ask about at sign-in.
2. **Read what was left** against the Handover pack in `assets/relief-pack.md`. Mark what is missing (medical alerts, where to leave work, what to do with early finishers) and ask the office or faculty before period 1.
3. **No work left:** ask the faculty first; they usually hold emergency lessons. Otherwise build a single-period task from the class's year, subject and current topic (ask students what they did last lesson and check their books): retrieval questions on the last two weeks' work, then practice of the same kind as in their books, then a short written reflection. Each part on the board, timed. For TAS practical classes, no workshop, kitchen or machine work without the specialist teacher; give a design, theory or reading task instead.
4. **During the lesson:** roll in the first five minutes in the school's system; seating plan if one exists; collect work as the pack says.
5. **Leave a note** for the class teacher on `assets/handover-note.md`: what was done and how far each part got, absences and late arrivals, incidents with times and what you did, work collected and where, anything the next lesson must deal with. Keep it to facts; put it where the pack said, or on the teacher's desk and with the faculty head.
6. **Keep the day for accreditation:** add a line to the teacher's day log, `_accreditation/day-log.md` in the teacher's own folder (date, school, classes, days count). A provisionally or conditionally accredited casual teacher needs the teaching days and the evidence; `accreditation-evidence` turns the log into items.

Done when the class is accounted for on the roll, the note is left, and the day is logged.

## Handover: leaving your class for a reliever

1. **Gather** in one pass: the date and periods, rooms, duties, the named colleague, medical alerts and students who leave the room, support staff in the room, and for each class what the students are working on now. Reuse existing lesson files and `_course_context.md` where they hold the answer.
2. **Choose the task per class.** Continue the current work when it runs from the page; otherwise use consolidation of what was already taught (practice, retrieval, a reading with questions). Introduce nothing new, and run no assessment task, practical test or workshop activity without a qualified teacher. When a lesson is built from an existing one, derive it as `plan-secondary-teaching` does for derived material and keep its terms.
3. **Write the pack** on `assets/relief-pack.md`: duty of care first, then the day at a glance, then one block per lesson with the task written as it is said to students, early-finisher work that continues the learning, and where to leave the work.
4. **Check** that a teacher from another faculty could run every lesson from the page, that every medical alert has a location and a trained person, and that the pack names a person to call, not just "the office".
5. **Ask for the note back:** the pack ends with a request for the reliever's handover note, so the next lesson starts from what happened.

Done when every period of the day has a block, the welfare section is complete or explicitly empty, and the three checks in step 4 hold.

## Sources

See `SOURCES.md`.
