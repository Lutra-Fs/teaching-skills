#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Mechanical checks for lesson slides, blueprints and student files.

Usage: lint_slides.py PATH [PATH ...] [--period 60] [--talk-words 40] [--work-words 80] [--min-px 28]

PATH may be a Slides-artifact project folder (deck.json + slides/*.html),
a single .html slide, a Markdown deck/plan, or a folder of these.
Checks:
  - words on screen per slide against a budget for its purpose (speaker notes
    and code excluded): about 40 while the teacher talks, about 80 on slides
    students read while working (case, task, worked example, model). Over
    budget is a warning to rethink the slide, not a target to trim to.
  - code blocks longer than about 15 lines
  - monospace fonts used outside code (labels, tags, captions)
  - questions with words that presuppose an answer (still, fully, only, really, even, just, already)
  - separator glyphs between phrases (·, •, |) in on-screen text
  - small fonts in HTML slides (positioned footers and logos excluded)
  - timeline minutes in a blueprint table add up to the period
  - answer-like text in student-facing files (name contains "student",
    "task", "template" or "worksheet")
Exit status 1 when any problem is found. It cannot judge teaching quality:
slop, previews of later steps and question quality still need a read.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

SEPARATOR = re.compile(r"\S\s*[·•]\s*\S|\S\s+\|\s+\S")
ANSWERISH = re.compile(
    r"\b(answer key|answers?:|expected (response|answer)s?|model answer|"
    r"possible answer|sample answer|suggested answer|solution:|marking (guide|notes))",
    re.I,
)
MONO = re.compile(r"monospace|courier|consolas|menlo|monaco|source code|jetbrains mono|fira code|ibm plex mono|roboto mono|sf mono|ui-monospace", re.I)
CODEISH = re.compile(r"[(){}\[\]=<>;:/\\_.$#@*+-]|^\w+\(|\d")
LEADING = re.compile(r"\b(still|fully|only|really|even|just|already)\b", re.I)
STUDENT_NAME = re.compile(r"student|task|template|worksheet|handout", re.I)
RANGE = re.compile(r"(\d{1,2}:\d{2}|\d{1,3})\s*(?:min)?\s*[–\-—]\s*(\d{1,2}:\d{2}|\d{1,3})")


def minutes(token):
    """'0:35' (h:mm) or '35' -> minutes."""
    if ":" in token:
        h, m = token.split(":")
        return int(h) * 60 + int(m)
    return int(token)


def words(text):
    return len(re.findall(r"[A-Za-z0-9][\w'’\-]*", text))


def html_slide(raw):
    """Return (on-screen text, notes text, small font sizes) for one slide."""
    notes = " ".join(re.findall(r"<aside[^>]*>(.*?)</aside>", raw, re.S | re.I))
    screen = re.sub(r"<aside[^>]*>.*?</aside>", " ", raw, flags=re.S | re.I)
    small = []
    for m in re.finditer(r"<(\w+)[^>]*style=\"([^\"]*)\"[^>]*>([^<]*)", screen):
        style, text = m.group(2), m.group(3).strip()
        size = re.search(r"font-size:\s*(\d+(?:\.\d+)?)px", style)
        if size and text and "position:absolute" not in style.replace(" ", ""):
            small.append((float(size.group(1)), text[:40]))
    code = [html.unescape(re.sub(r"<[^>]+>", "", c))
            for c in re.findall(r"<pre[^>]*>(.*?)</pre>", screen, re.S | re.I)]
    screen = re.sub(r"<pre[^>]*>.*?</pre>", " ", screen, flags=re.S | re.I)
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", screen))).strip()
    text += "".join(f"\n```\n{c}\n```" for c in code)
    return text, html.unescape(notes), small


def md_slides(raw):
    """Split a Markdown deck into (title, on-screen text) pairs."""
    heading = re.compile(r"(?mi)^#{1,3}\s*slide\b")
    if heading.search(raw):
        parts = [p for p in re.split(r"(?mi)^(?=#{1,3}\s*slide\b)", raw) if heading.match(p)]
    else:
        parts = re.split(r"(?m)^---\s*$", raw)
    slides = []
    for part in parts:
        part = re.sub(r"(?m)^---\s*$", "", part)
        if not part.strip():
            continue
        screen, in_notes = [], False
        for line in part.splitlines():
            if re.match(r"^\s*[#>*_]*\s*(speaker|teacher|presenter)?\s*(notes?|script)\b|^\s*[#>*_]*\s*讲稿|^\s*<aside|^\s*<!--", line, re.I):
                in_notes = True
            if not in_notes and not re.match(r"^\s*\|?\s*:?-{3,}", line):
                screen.append(line)
        title = next((l.strip("# ").strip() for l in part.splitlines() if l.strip()), "")
        slides.append((title[:50], "\n".join(screen[1:])))
    return slides


def check_timeline(raw, period, label, problems):
    """Find a blueprint table with a Time column and check the minutes."""
    for table in re.findall(r"((?:^\|.*\|\s*$\n?)+)", raw, re.M):
        rows = [r for r in table.strip().splitlines() if not re.match(r"^\|\s*:?-", r)]
        if not rows or "time" not in rows[0].split("|")[1].lower():
            continue
        spans = []
        for r in rows[1:]:
            cell = r.split("|")[1]
            m = RANGE.search(cell)
            if m:
                spans.append((minutes(m.group(1)), minutes(m.group(2))))
        if not spans:
            continue
        if spans[0][0] != 0:
            problems.append(f"{label}: timeline starts at minute {spans[0][0]}, not 0")
        for (a1, b1), (a2, b2) in zip(spans, spans[1:]):
            if a2 != b1:
                problems.append(f"{label}: gap or overlap between {a1}–{b1} and {a2}–{b2}")
        end = max(b for _, b in spans)
        if end != period:
            problems.append(f"{label}: timeline ends at minute {end}, period is {period}")


WORK_SLIDE = re.compile(
    r"\b(task|you do|we do|i do|case|scenario|worked|example|model|activity|"
    r"practice|write|self-?check|exit|part [a-z]|your (diagram|turn|response))\b|"
    r"purpose:\s*(task|case|worked|model)|任务|案例|示范|练习", re.I)
CODE_BLOCK = re.compile(r"```.*?```|<pre[^>]*>.*?</pre>", re.S | re.I)


def lint_text_slide(label, screen, args, problems, title=""):
    for block in CODE_BLOCK.findall(screen):
        lines = [l for l in block.splitlines() if l.strip() and not l.strip().startswith("```")]
        if len(lines) > args.code_lines:
            problems.append(f"{label}: code block of {len(lines)} lines (about {args.code_lines} readable)")
    prose = CODE_BLOCK.sub(" ", screen)
    n = words(prose)
    first_lines = "\n".join(prose.strip().splitlines()[:2])
    working = bool(WORK_SLIDE.search(title) or WORK_SLIDE.search(first_lines)
                   or re.search(r"(?mi)^\W*(task|you do|case \d)", prose))
    budget = args.work_words if working else args.talk_words
    if n > budget:
        kind = "students work from it" if working else "teacher talks over it"
        problems.append(f"{label}: {n} words on screen, budget {budget} ({kind}); "
                        "move detail to the student doc or notes, or split; do not compress into fragments")
    for span in re.findall(r"(?<!`)`([^`\n]+)`(?!`)", prose):
        if not CODEISH.search(span):
            problems.append(f"{label}: inline code formatting on plain words “{span[:40]}” (monospace is for code only)")
    for q in re.findall(r"[^.?!\n]*\?", prose):
        m = LEADING.search(q)
        if m:
            problems.append(f"{label}: question presupposes an answer (“{m.group(1)}”): “{q.strip()[:60]}”")
    for line in prose.splitlines() or [prose]:
        if line.lstrip().startswith("|"):
            continue  # Markdown table row, not slide prose
        m = SEPARATOR.search(line)
        if m:
            problems.append(f"{label}: separator glyph in “{line.strip()[:60]}”")
            break


def lint_file(path, args, problems):
    raw = path.read_text(encoding="utf-8", errors="replace")
    label = str(path)
    if path.suffix.lower() in (".html", ".htm") and "<section" in raw:
        screen, notes, small = html_slide(raw)
        head = re.search(r"<h[12][^>]*>(.*?)</h[12]>", raw, re.S | re.I)
        title = path.stem + " " + (re.sub(r"<[^>]+>", " ", head.group(1)) if head else "")
        lint_text_slide(label, screen, args, problems, title)
        bare = re.sub(r"<(pre|code)[^>]*>.*?</\1>", " ", re.sub(r"<aside[^>]*>.*?</aside>", " ", raw, flags=re.S | re.I), flags=re.S | re.I)
        for m in re.finditer(r"<(\w+)[^>]*style=\"([^\"]*font-family:[^\";]*)[^\"]*\"[^>]*>([^<]*)", bare):
            if MONO.search(m.group(2)) and m.group(3).strip():
                problems.append(f"{label}: monospace font outside code: “{m.group(3).strip()[:40]}”")
        for size, text in small:
            if size < args.min_px:
                problems.append(f"{label}: {size:g}px text “{text}” (min {args.min_px}px)")
        if notes:
            for m in RANGE.finditer(notes):
                if args.period < minutes(m.group(2)) <= 180:
                    problems.append(f"{label}: notes mention minute {m.group(2)} beyond the period")
        return
    if path.suffix.lower() in (".md", ".markdown", ".txt"):
        if re.search(r"(?mi)^#{1,3}\s*slide\b", raw):
            for i, (title, screen) in enumerate(md_slides(raw), 1):
                lint_text_slide(f"{label} slide {i} ({title})", screen, args, problems, title)
        check_timeline(raw, args.period, label, problems)
    if STUDENT_NAME.search(path.name) and not re.search(r"teacher|answer|key", path.name, re.I):
        for no, line in enumerate(raw.splitlines(), 1):
            if ANSWERISH.search(line):
                problems.append(f"{label}:{no}: answer-like text in a student file: “{line.strip()[:70]}”")


def collect(paths):
    for p in map(Path, paths):
        if p.is_dir():
            deck = p / "deck.json"
            if deck.exists():
                order = json.loads(deck.read_text()).get("order", [])
                for sid in order:
                    f = p / "slides" / f"{sid}.html"
                    if f.exists():
                        yield f
                continue
            for f in sorted(p.rglob("*")):
                if f.suffix.lower() in (".html", ".htm", ".md", ".markdown", ".txt"):
                    yield f
        elif p.exists():
            yield p


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--period", type=int, default=60, help="period length in minutes")
    ap.add_argument("--talk-words", type=int, default=40, help="budget for slides the teacher talks over")
    ap.add_argument("--work-words", type=int, default=80, help="budget for case, task and worked-example slides")
    ap.add_argument("--code-lines", type=int, default=15, help="readable code lines on one slide")
    ap.add_argument("--min-px", type=float, default=28, help="smallest font on a 1920px slide")
    args = ap.parse_args()
    problems, files = [], list(collect(args.paths))
    for f in files:
        lint_file(f, args, problems)
    for p in problems:
        print(p)
    print(f"{len(files)} file(s) checked, {len(problems)} problem(s).")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
