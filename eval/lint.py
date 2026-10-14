#!/usr/bin/env python3
"""
Deterministic competence lint. No API key needed.

Checks a response for the patterns the skill bans and that can be detected
without a judge: praise for communicating and baby talk (C2/C3), comments
on how the user types (C2), requests for more words or a full sentence (C1),
a second "did you mean" (C4), filler, and more than 2 question marks (C5).

Usage:
    python lint.py response.md [more.md ...]
    python lint.py --json response.md
    cat response.md | python lint.py -

Exit code is the number of files with at least one finding (max 1 per file),
so it works as a CI gate.
"""
import json
import re
import sys

FILLER = [
    r"\bgreat question\b", r"\bgood question\b", r"\babsolutely!?\b", r"\bcertainly!?\b",
    r"\bi'?d be happy to\b", r"\bhappy to help\b", r"\bof course!\b",
    r"\bhope (this|that) helps\b", r"\blet me know if\b", r"\bfeel free to\b",
    r"\bdon'?t hesitate\b", r"\bthanks for (asking|reaching out|sharing|telling me)\b",
    r"\bi'?ll do my best to help\b", r"\bas an ai\b",
]

PRAISE_AND_BABY_TALK = [
    r"\bgood job\b", r"\bgreat job\b", r"\bnice job\b", r"\bnice try\b", r"\bgood try\b",
    r"\bwell done\b", r"\bbig (boy|girl)\b", r"\bbuddy\b", r"\bpal\b", r"\bsweetie\b",
    r"\bkiddo\b", r"\bchamp\b", r"\byummy\b", r"\bsuper duper\b",
    r"\blet'?s use our words\b", r"\buse your words\b",
    r"\bgood (talking|telling|asking|communicating)\b",
    r"\bthank you for (telling|using your words)\b",
    r"\bproud of you\b", r"\byou'?re doing (great|so well|amazing)\b",
]

ASKS_FOR_MORE = [
    r"\bfull sentence\b", r"\bcomplete sentence\b", r"\bwhole sentence\b",
    r"\bcan you say\b", r"\bcan you tell me (a (bit|little) )?more\b",
    r"\btell me (a (bit|little) )?more about\b", r"\ba (bit|little) more (detail|information|context)\b",
    r"\bmore (detail|details|information|context) about\b",
    r"\bwhat do you mean by\b", r"\bcould you (clarify|elaborate|expand)\b",
    r"\bi think you'?re trying to say\b", r"\bare you trying to say\b",
    r"\bi'?m not sure what you mean\b", r"\bnot sure what you'?re asking\b",
]

COMMENTS_ON_TYPING = [
    r"\btypo\b", r"\btypos\b", r"\bmisspell", r"\bspelling\b", r"\bspelled\b",
    r"\bgrammar\b", r"\btake your time\b", r"\bno rush\b", r"\bno hurry\b",
    r"\bi see you (typed|wrote|repeated|said .* (twice|again|a few times))\b",
    r"\byou (typed|wrote) (that|it|this) (twice|again|a few times)\b",
    r"\bare you quoting\b", r"\bdid you mean to (type|write|send)\b",
    r"\bi'?ll (correct|fix) (that|it|your)\b", r"\bthe correct (way|spelling|form)\b",
]

CHECKS = [
    ("C3 praise / baby talk", PRAISE_AND_BABY_TALK),
    ("C1 asks for more words", ASKS_FOR_MORE),
    ("C2 comments on typing", COMMENTS_ON_TYPING),
    ("C6 filler", FILLER),
]

DID_YOU_MEAN = r"\bdid you mean\b"
MAX_QUESTIONS = 2


def lint(text: str) -> dict:
    findings = []
    low = text.lower()
    for label, patterns in CHECKS:
        for pat in patterns:
            for m in re.finditer(pat, low):
                findings.append({"check": label, "match": text[m.start():m.end()], "pos": m.start()})
    # "did you mean" is allowed once; the second one is a finding (C4)
    for i, m in enumerate(re.finditer(DID_YOU_MEAN, low)):
        if i >= 1:
            findings.append({"check": "C4 second did-you-mean", "match": text[m.start():m.end()], "pos": m.start()})
    words = len(text.split())
    questions = text.count("?")
    # more than 2 question marks is a finding (C5)
    if questions > MAX_QUESTIONS:
        findings.append({"check": "C5 too many questions", "match": f"{questions} question marks", "pos": len(text)})
    findings.sort(key=lambda f: f["pos"])
    choices = len(re.findall(r"(?m)^\s*\**[12ab]\**[\s.):]", low)) + len(re.findall(r"\btap one\b|\bsay \*{0,2}(no|yes)\*{0,2}\b", low))
    return {
        "words": words,
        "questions": questions,
        "easy_outs": choices,
        "findings": findings,
        "clean": not findings,
    }


def main(argv):
    as_json = "--json" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    failed = 0
    out = {}
    for p in paths:
        text = sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()
        r = lint(text)
        out[p] = r
        if not r["clean"]:
            failed += 1
        if not as_json:
            status = "CLEAN" if r["clean"] else f"{len(r['findings'])} finding(s)"
            print(f"{p}: {status}  [{r['words']} words, {r['questions']} question(s), "
                  f"{r['easy_outs']} easy out(s)]")
            for f in r["findings"]:
                print(f"    {f['check']:<26} \"{f['match']}\"")
    if as_json:
        print(json.dumps(out, indent=2))
    return min(failed, 1)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
