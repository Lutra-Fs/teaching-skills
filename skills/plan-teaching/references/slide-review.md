# Slide review checklist

Read before delivering or reviewing any slide deck, after `scripts/lint_slides.py` has run. Apply every heading to every slide and its speaker notes. The items come from the teacher's own corrections on real decks (Lessons 4 to 6, October and November 2026). Items marked (lint) are also checked by the script.

## 1. Every word helps students now

- Labels name the content for students ("We do"); design notes for the teacher go in the plan.
- The heading or question carries the instruction; a second line restating it goes.
- The slide holds only what the whole class needs to see now; what the student document or Classroom post already says stays there. (One deck shrank from 8 slides to 3.)
- Reminders cover only what students must do themselves; the platform's automatic behaviour (Google Docs saving) needs none.
- Headlines name the content ("Spotify: location and deleted accounts").
- No kickers or secondary labels ("From Lesson 5:", a card label repeating the card). Two labels stay: the "Extension" tag (section 2) and the formal-term label (section 5). A term the cohort has not met is still defined on the slide.
- Sentences read as a person wrote them: keep "that" in object clauses; no stacked noun compounds, nouns used as verbs, inanimate subjects doing actions, long subject-verb gaps or paired slogans. Prefer a human subject. The mentor's own sentences and genre forms ("The app must …") stay.
- Earlier lessons come back through the design: the same boxes lit up again on the familiar diagram.
- The opening and closure formats differ from the previous two or three lessons, unless the notes give a learning reason.

## 2. Questions leave the thinking to students

- Questions are neutral. Words that presuppose an answer (still, fully, only, really, even, just, already) come out. (lint flags them in questions)
- Each question is open and led by a directive verb at the cohort's level: "Assess how ACL responded after the breach." For Stage 6 use HSC glossary verbs and ask for more than recall; for Stage 4 use everyday verbs in plain questions, with no bold key words and no abstract verbs (Assess, Justify). Task lines start with the verb too.
- Each question is concrete and answerable from what is on the slide, in words students have; the teacher names the formal term after they answer.
- Success-criteria slides show the blueprint's "I can …" statements word for word; success-criteria and closure slides check the core; Extension content is labelled "Extension" on its slide.
- At the moment a question is asked, the screen shows only the question and what students need to answer it. Check every click-reveal for this.
- Progressive disclosure: each slide shows only the step the lesson has reached. The lesson's agenda and later steps live in the plan, the title slide included.

## 3. Students can do it

- Reading is at the cohort's level: regulator pages, company statements and plain summaries.
- Every concept a task or check uses was taught first, on its own slide if needed (de-identification methods needed a slide before Check 1).
- Modelling uses a different case from the one students analyse themselves.
- Examples use apps the school allows; an app the school blocks (Discord) needs a VPN students cannot use.

## 4. Standard practice, fewest steps

- Use established conventions: the citation style in `_teacher_profile.md`; evidence status written into the sentence ("The OAIC alleges…").
- Use the terms students already learned ("MFA").
- Discuss orally what can be discussed; online posts follow `_teacher_profile.md`.
- Grouping follows `_teacher_profile.md` and the class's `_course_context.md`; teaching chunks are named by content ("Part 1: …").

## 5. The teacher can run it

- Every teaching slide has notes the teacher can speak from; timings stay in the blueprint and add up to the period. (lint adds up blueprint timings)
- Formal or legal terms sit in a small, muted label (for example "Law calls this:"); the notes explain them in plain words.

## 6. Format and accessibility

- Phrases on separate lines, with few colons; the body font everywhere except code. (lint)
- WCAG 2.2 AA: text contrast at least 4.5:1, graphics and UI 3:1; meaning carried by text or shape as well as colour; decorative glyphs `aria-hidden`.
- Tool limits: in the Slides artifact type, click-to-reveal (`data-build-in`) works only on `position:absolute` elements, so check that every reveal is pinned and test one in Present mode.

## 7. Change once, change everywhere

- After any change, update every file that repeats it in the same round: notes, lesson plan, teacher guide, student task, Classroom template, quiz, marking guidelines, the previous lesson's "next" slide, and every "Slide N" reference in the plan and Classroom post. Copies drift silently, and the teacher finds out in class.
- Every file of one lesson keeps the slide order, examples and terms; each worksheet question maps to a teaching slide, and a slide with no question is marked teach-only.
- **Done when** a search finds the old wording in no file.

When reporting a review, give each finding as slide, problem, fix, grouped by these headings, most consequential first.
