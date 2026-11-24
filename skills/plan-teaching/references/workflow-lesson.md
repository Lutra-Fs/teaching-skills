# Workflow: lesson, slides and student material

Use for preparing, adapting, repairing or reviewing one lesson or its materials. This file holds everything a normal lesson needs; deep references load only on the triggers in SKILL.md.

## 1. Blueprint before slides

Make the teaching decision before the visual production. Slides made first come out polished but generic: a list of true statements with no task, no check and no reason for this lesson to exist.

1. **Place the lesson.** From the program and the previous two or three lessons, state what this lesson inherits, what it must leave ready for the next one, and what students already know (taught, evidenced or uncertain). For a first-time lesson, scout supporting material before the blueprint (section 2, Supporting material).
2. **Write a one-page blueprint** (`assets/lesson-portfolio-pack.md`, or the school's template when one is required). One row per phase: time, teacher move, student action, evidence that shows understanding, likely misconception and the response. Explicit teaching usually runs explain, model (I do), guided practice (we do), check, independent practice (you do); use the phases this lesson's role needs, so a practice lesson stays a practice lesson. The blueprint is the lesson plan; the speaker notes carry the script.
3. **Fit the real period.** Take the period length from `_course_context.md`. The phases plus both bookends add up to it exactly. When the essential learning needs more, split it into consecutive single lessons, each with its own opening and closure (for example an evidence lesson then a writing lesson), and say what moves. Splitting protects the closure, which is what an overfull lesson loses. Time the student work from the material itself, not only the phases: reading at the cohort's literacy, each question, a video's full length, handing out and collecting. A real room also runs longer than the plan: checking for understanding, students repeating an idea, recall prompts for earlier concepts and redirecting off-task students all take time, and redirecting one student does not stop the next. Leave about 10 to 15 minutes of a 60-minute period unplanned for this, and start the main independent task by about halfway. When a student models at the board, that is the guided practice: plan one worked example before independent work, not a second guided example. Check the total against this class's recorded pace (`_course_context.md`, else the starting estimate in `_teacher_profile.md`); `lesson-retro` updates that record from what the class actually completes, as every class differs. Plan one main activity per lesson plus at most one short optional extra; a mainstream class with lower literacy runs slower than a selective one. When the teacher's requested pieces exceed this, keep the main activity, mark one extra optional with its trigger, move the rest to a named later lesson or homework, and say what moved.
4. **Separate core from Extension.**
   - Core is the task wording in this lesson's program row plus that row's syllabus content, quoted from the lock's `content_used` (`curriculum-lock.md`) with its learning components. Preparation notes and earlier reviews are background for the teacher.
   - Success criteria come from the core only. Write them as "I can …" statements (NSW "Sharing success criteria"): short, at the level of the skill, each concrete and observable, each checking something different. Task details such as the number of tries go on the activity slide and in Classroom. The closure checks the core.
   - An activity added beyond the program row (a quiz, a game) shows in the blueprint how many minutes it takes from the core task, and goes in only after the teacher decides (12 Kahoot questions took about 9 minutes from a report).
   - The teacher may add reasonable Extensions. Mark each `Extension` in the blueprint: it is taught, not assessed, and has no planned time. A harder version of the core task for some students is a stretch tier (`scaffolding-differentiation.md`), with its own time inside the task. An Extension slide carries one idea, and its notes name the trigger (for example "if 8 minutes remain after Part 2"). When the opening runs long, the core activities keep their time and the Extensions go.
5. **Show the blueprint first** when the unit is new, the lesson is taught for the first time or the teacher asked to see the plan. Otherwise continue to the slides in the same run. In a run with nobody to answer (a batch or scheduled run), make the choice yourself at each stop point, list it as an assumption and continue.

### Fixed purposes, varied formats

A lesson that repeats last lesson's shape bores students. Keep fixed only the logistics (arrival and set-up time from `_course_context.md`, the teacher-talk cap, pack-up) and the purposes of the two ends:

- **Opening (3 to 5 minutes):** connects to prior learning or unfinished work, then moves straight into this lesson's content. A program question students can already answer from earlier lessons or everyday life is asked here as recall instead of being taught.
- **Closure (about 3 minutes):** gives the teacher evidence for the next lesson. When time runs short, activity time shrinks and the closure stays. When the main task already gives that evidence (submitted work, checks while circulating), the task is the closure: add no separate exit question, and the notes say where the evidence comes from. When the next lesson opens with a quiz or test, say so at pack-up.

The teacher-talk cap is half the period. The opening theory block stays under 30 minutes of 60, and what does not fit opens the next lesson, where students need it.

Choose each format for this lesson's content: for the opening, a recall question, a puzzle, a client message or a prediction; for the closure, an exit ticket, a hinge question, a show-and-tell, a peer check or a quiz. Read the previous two or three lesson plans or decks first, so an opening, closure, case, task mechanism or question form repeats only for a learning reason. Keep the help routine and slide style stable. For more formats that use the class's devices, browse the NSW Department of Education [Digital Learning Selector](https://app.education.nsw.gov.au/digital-learning-selector) (50+ activities, filtered by Bloom's level, with Google and Microsoft templates).

### Classroom routines

Plans and speaker notes build in the routines that keep one teacher in control of the room:

- One attention signal, the same every time. A gesture stops talk without inviting students to choose.
- Before each activity the notes say how students work: voice level, alone or in pairs, and which worksheet section.
- Readiness checks are visual. Ask how long students need, then thumbs up or down.
- Each activity slide names its worksheet section, so every student can find where the class is.
- The board stays clear, and the end time sits where students can see it with the projector on.
- The teacher greets students at the door and answers their bids for connection.

## 2. Student tasks and questions

Make every task concrete, judgeable and tied to the evidence row of the blueprint: the exact prompt and the expected output.

| Generic | Teachable |
|---|---|
| "Cybersecurity matters: protect data, identify risks, follow best practices" | "A desktop app stores its login token in a plain-text settings file. Identify one risk, explain how it could be exploited, recommend one mitigation." |

- **Check questions** are answerable from the scenario in front of students, in words they already have. The scenario matches how the real system works: to probe a requirement, ask why it must hold ("Why must the token travel over HTTPS?"), not what happens without it in a system that always enforces it. Students answer in plain words; the teacher then names the formal term. Each question asks about the concept itself, not about the worksheet's headings.
- **A case or discussion slide** runs as two or three short questions that build on each other, each led by a directive verb at the cohort's level (Stage 6: a NESA glossary verb, for example Identify, then Propose; Stage 4: a plain question with an everyday verb), each answer revealed on a click, about 2 minutes in all, so the teacher sees where students are stuck at each step. A full discussion (Stage 6) asks a NESA Discuss question with both cases on screen from the start; students name the factors (written on the board) and propose the rule, and the teacher names the concept last. A vote followed by a twist reveal is not a discussion.
- **Objective items** (multiple choice, matching, quiz platforms) have exactly one defensible answer (for a select-all item, one defensible set), with distractors drawn from common mix-ups; use the HSC stem "matches" rather than "mainly".
- **Task lines** start with the verb.
- **Research prompts** give checked direct links and search phrases that together answer every question; size the reading list to the time available.
- **Grouping** follows `_teacher_profile.md` and the program wording; flag anything added beyond the program. For group work, say where each student's evidence goes (group Doc, individual comment), the same in plan, slides and Classroom post.
- **Task follows modelling:** an example type taught only briefly gets a task variant, so students apply it in depth.
- **Hinge question (optional):** where a concept has a known misconception, place one multiple-choice question mid-lesson, before practice. Each wrong option matches one misconception from the blueprint, and the notes say what the teacher does for each (move on, or re-explain a named way). The whole class answers at once, in about a minute. It differs from the closure: a hinge decides the next five minutes, the closure the next lesson.
- **Prep note:** work the key student task once as a student would (for cards or variants, every card, each supporting the required number of answers from its own text; cut "Optional" scaffolds students will not use), then write a three-line teacher-only note in that slide's notes: where students will likely stick, and the response.
- **Verify:** solve every question and keep the answers teacher-only. Run every code sample, the supervising teacher's included, before planning around it; list a non-standard dependency (for example `pip install cryptography`) as a before-class check, and for a break-and-fix step put the exact error text and its cause in the notes. Check each real case against a source and date it, and against how the mechanism really works today, including recent changes (for example refresh tokens keep a session alive after the access token expires). A slide states verified fact; a hypothetical is labelled "Suppose"; a detail the primary source does not give is written as "most likely", naming who claims it. Mark any check you could not perform.
- **Supporting material:** for a first-time lesson, scout videos, readings and cases by Stage (`resources-external.md`, Scouting) before the blueprint, and build on the ones the teacher picks.
- **Case sources:** prefer this class's earlier work, the school context, the teacher's own examples and current, source-checked Australian cases. To show a mechanism, pick the example with the simplest mechanics (one condition, no arithmetic), drawn from the class's own text where possible. A case uses the technology the program names, not only the topic (an elliptic-curve key case does not illustrate RSA).

## 3. Slides

The deck is how the teacher runs the lesson. Speaker notes hold what the teacher says and asks, expected answers, misconceptions and feedback prompts. Timings live in the blueprint. **Done when** the deck runs from opening to closure, every teaching slide has notes, and the blueprint timings add up to the period.

**Each slide has one purpose.** Choose its layout from this set (styled per `_brand/theme.md` when present): title or opening, explain, worked example, annotated diagram, comparison, student task, check for understanding, recap, closure. Cut a slide whose purpose you cannot name. Similar purposes look alike; different purposes look different.

**Cognitive load (CESE guidance):**
- **Text budget by purpose.** While the teacher talks (title, explain, recap), keep to key words, about 40 words: students who read and hear the same block at once are overloaded. Slides students read on their own while they work (a case, a task, a worked example) carry what the task needs, up to about 80 words. Code is judged by lines, about 15 at most, readable from the back.
- The budget prompts a rethink: move detail to the student document or notes, or split the slide. Keep full sentences, the directive verb (identify, explain, justify) and the information the question depends on.
- The headline states the point. Labels sit on or next to the part of the diagram they name. Every image carries information.
- **Progressive disclosure:** one step per slide, check, then move on. Each slide shows only what has been reached.
- **Function before name:** when two terms are easy to confuse (for example OAuth and OIDC), show what each does on the diagram students already know, one new part per click, and name them last.
- **Recall by design:** link to earlier lessons by lighting up the same boxes again on the familiar diagram.
- **Relationships by layout:** show a relationship with position (a staggered row, a shared box) instead of a paragraph about it; render the diagram and read it as a student would before delivery.
- Task instructions stay on screen while students work.
- Text, code and diagrams are readable from the back of the room (body text at least 24 pt or equivalent).

**Stage language** (a design synthesis from the sources in SOURCES.md, not a NESA rule):
- *Stage 4:* name the routine and the next action; numbered steps, one action per line; define each term on first use with an example, then reuse the same word; literal questions before inference; plain, literal language. Questions use everyday verbs (Explain, Identify) in plain sentences ("Does this fix the problem? Explain why or why not."); no bold key words and no abstract verbs (Assess, Justify, Propose). Assume no programming construct (IF/ELSE, loops) and no subject term, including the one the learning intention names, until the lesson teaches it.
- *Stage 5:* assume earlier terms only where the school sequence taught them; move from describe to explain, compare and justify, showing what each verb asks; fade sentence starters as evidence supports it; give reasons with instructions.
- *Stage 6:* address near-adults directly and precisely, with reasons; use HSC glossary verbs exactly as NESA defines them in tasks and exit questions, with the definition shown the first time in Year 11; keep the course's syllabus terminology.
- For flagged EAL/D or literacy needs, simplify the sentence, add a visual or word bank, and keep the concept and the assessed thinking.

**Style:** use `_brand/theme.json` role names for colour, so a new palette swaps cleanly. The body font sets all text, including labels, tags, file names and captions; the `code` font is for code. Phrases sit on separate lines; use a colon only where a label introduces its content. Where the tool has a master, set the logo once; where each slide is self-contained, repeat the same small logo in the same place on every slide. Without `_brand/`, use a neutral style with a logo placeholder.

**Revisions:** change a published deck or file with targeted edits to the parts that change, instead of rewriting or republishing the whole thing. Re-read the live file just before each publish, because the teacher may be editing it in the page. When fixing wording, keep the teacher's idea and move a line to the notes rather than delete it. When the teacher names a slide by position ("the research task at the start"), confirm which slide first.

## 4. Student material

Lean: the task, the steps, what to submit, and where to get help. For Stage 6 that is often a few lines. Answers, model responses, source scaffolding and rationale go in teacher-only notes. When a school or Classroom template exists, fill it. Worksheets carry a key-terms box for the lesson's terms. Text for a Google Classroom post goes over as plain text with a note of what to bold: the Classroom editor deletes `<strong>` text with its words and strips numbered lists, so type item numbers by hand. For a standalone resource, `assets/activity-student-resource-pack.md` lists optional modules; use those the task needs.

Set the register by the reader: a task plan for a colleague is concise and professional; a student instruction or lesson script uses the student-facing register.

## 5. Check before delivery

1. Run `scripts/lint_slides.py <deck folder or file> --period <minutes>` on slides and student files when the tool is available; its usage is in its first lines, so there is no need to read the rest of its source. It counts words per slide against the purpose budget, finds separator glyphs, monospace outside code, small fonts and leading words in questions, adds up the timings and flags answer-like text in student files. Treat a word-count warning as a question (does this slide's purpose need the words?) and fix the rest.
2. Check the three kinds of slop the script cannot see:
   - **Visual slop:** decoration, identical card layouts on every slide, unreadable code or contrast.
   - **Pedagogical slop:** a vague learning intention, activities that produce no evidence for the blueprint, explanation with no practice or check, more phases than the period holds.
   - **Content slop:** invented cases, outcome codes, statistics or technical details; examples the answer key gets wrong; terms used before they are taught. List every term the learning intention, tasks and checks depend on, and point to where each is taught (this lesson or a named earlier one); this applies to plans and worksheets without slides too.
3. Apply every heading of `slide-review.md` to every slide and its notes.
4. Walk the lesson once as the teacher: distribution, help requests, transitions and one teacher's capacity. Define a useful stop point before the closure and one early-finisher task. A fallback goes in the speaker notes, and only for a named, specific risk (a new platform, a lesson outside the room).

**Done when** lint exits clean or each remaining warning has a stated reason, every slide-review heading has been applied, and the walk-through found nothing the teacher would have to fix.

## 6. Review-only requests

Run the lint script and `slide-review.md` on any slides, then report findings, each tied to the exact slide, question or row, with the problem, why it matters and the proposed fix, ranked by impact on the lesson. Offer to apply the fixes. When auditing criteria or scope, report three things: an Extension that became a success criterion or closure target, an Extension that takes core time, and core content from the program row that the plan leaves out. A teacher-approved Extension in its place is fine. Theory taught in a familiar general context before the unit scenario is legitimate transfer: audit the bridge (does the next task apply the concept to the unit scenario?), not the context.

## 7. Deliver

Lead with the blueprint or deck and student material. Then list only: consequential assumptions, checks you could not run, and local actions the teacher still owns (printing, bookings, accounts). If the next lesson depends on how far this one gets, state the handoff. Close by naming the derived materials this lesson can feed (practice sheet, versions, quiz, revision paper), so the teacher can ask for one by name (`derived-resources.md`).

When the teacher later reports what happened, the record and its routing belong to `lesson-retro`.
