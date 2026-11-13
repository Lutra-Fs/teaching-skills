---
name: lesson-retro
description: "Reflect on a NSW secondary lesson after it is taught: how far the class got against the plan, what student work shows, what worked, what the materials got wrong, and where each finding goes (class pace, teacher profile, the next lesson, accreditation evidence). Use for \"how the lesson went\", \"lesson retro\", \"reflect on today's class\" or \"复盘\"."
metadata:
  version: "0.1.0"
---

# Lesson Retro

Turn what happened in a taught lesson into changes the next lesson, the teacher's records and their accreditation evidence can use. The teacher reflects; the skill asks, sorts and records.

## Rules

- **Observed before interpreted.** Record what happened (students reached Part 2, six of 28 finished the trace) apart from why the teacher thinks it happened. Both are kept, labelled.
- **Only what the teacher reports or the work shows.** Leave a gap visible; name what to collect next time.
- **Anonymise.** Students are initials or "Student A"; student work stays in the school's systems, and only de-identified excerpts come into an AI tool.

## Steps

1. **Find the plan.** Read the lesson plan and materials in its folder (the plan from `plan-secondary-teaching`, or the school's template), and `_course_context.md`. Without a plan, ask for the lesson's intention and phases in two lines.
2. **Ask the reflection in one message**, the teacher answering only the dimensions that apply, in a few words each:
   1. **Plan against actual:** where the class got to, which phase ran long or short, what was cut.
   2. **Learning:** what student work, answers or exit checks show students can now do, and what is still shaky.
   3. **Moves:** which activity, explanation, question or check worked, and which did not.
   4. **Engagement and behaviour**, where it bore on learning.
   5. **Materials:** errors or friction in the slides, task, answers, links, timing estimates or printing.
   6. **Evidence held:** student work samples, feedback given, mentor or supervisor comments, a change made in response to students.
3. **Write the record** as `retro.md` in the lesson's folder, apart from the lesson plan: date, the six dimensions as answered, observed and interpreted kept apart, and what changes next lesson. When a required template (a university or school one) has its own post-lesson field, fill that field in two sentences from the record.
4. **Route each finding** to one place, proposing the edit and making it after the teacher agrees:
   - The class's actual pace → `_course_context.md`.
   - A preference particular to this teacher → `_teacher_profile.md`, dated.
   - A rule that holds for any teacher, or a material error the skill should have caught → a proposed change or issue for the skill's repository; an installed copy is overwritten on update.
   - What the next lesson must pick up → the next lesson's plan or the unit sequence; when a reliever takes it, the handover pack (`relief-teaching`).
5. **Accreditation evidence.** For a provisionally or conditionally accredited teacher, when dimension 6 holds an artifact or the lesson shows a visible effect on students, add a candidate line to the evidence log through `accreditation-evidence`: the lesson, the artifact, the impact it shows and what is missing. With nothing held, name what to collect next time instead. Descriptor mapping is that skill's work, from the AITSL text.
6. **Optional agent retro.** When the materials problems trace back to how the agent worked (missed a file, misread the program, skipped a check), suggest the teacher run a session retrospective, such as the `retro` skill from mattpocock/skills, if it is installed. The teacher runs it.

Done when the record is written, every finding has a destination the teacher accepted or declined, and any evidence is in the log or named as missing.

## Sources

See `SOURCES.md`.
