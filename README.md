# teaching-skills

Agent skills for secondary teaching in New South Wales. They work from the school's adopted syllabus and program, so outcome codes and content come from the locked source and never from model memory.

## Skills

| Skill | Use it for |
|---|---|
| `plan-secondary-teaching` | Lessons and slides, units and pacing, assessment and marking, syllabus lookup, and materials derived from an existing lesson (practice sheets, versions, quizzes, marking guides). Deep support for Mathematics 7-12 and TAS courses. |

## Install

Claude Code, Cowork and cloud sessions:

```bash
claude plugin marketplace add Lutra-Fs/teaching-skills
```

```bash
claude plugin install staffroom@lutra-teaching
```

Other agents: copy or link a folder under `skills/` into the agent's skills directory.

## Your own files

The skills read two files you keep with your teaching material, outside this repository:

- `_course_context.md` in each course folder: period length, timetable, mentor direction and the curriculum lock.
- `_teacher_profile.md` in the folder above your course folders: your standing preferences. Start from `skills/plan-secondary-teaching/assets/teacher-profile-template.md`.

## Status

Written by a teacher for their own classes. Rules are recorded with their source and date in each skill's `SOURCES.md`.

## Licence

The skills' text, references, templates and evals are licensed under [CC BY-NC-SA 4.0](LICENSE): you may use and adapt them for teaching, including in a paid teaching job, with attribution, and share adaptations under the same licence. Selling them, or building them into a paid product, is not permitted.

Scripts (`skills/*/scripts/`) are licensed under [MIT](LICENSE-MIT).
