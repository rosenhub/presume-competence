# Contributing

## Proposing a rule change

Open an issue using the **Rule proposal** template. It asks for three things:

1. A real before/after pair. Real means you saw the "before" from an actual agent.
2. One sentence on who it helps.
3. Which existing rule it changes, or where it goes if it is new.

Contributors who use AAC, a letter board, or type a few words at a time are the most important reviewers of this file. Your experience is the evidence. One-word issues are welcome: an issue that says `buddy` with a screenshot is a complete bug report. I will write the rest.

Rules are capped at 12. A new rule has to replace or merge into an existing one. This keeps the skill short enough that every host loads it in full.

## Adding a host

Open a PR that adds a row to the table in README.md and, if the host has a standard path, a line in `install.sh`. Include a link to the host's docs for the path.

## Benchmark results

Run `eval/run.py`, then open a PR that adds the generated `results/<model>-<date>.md` and a row in `results/README.md`. Say which judge model you used. Results from models other than the one the maintainer tested are the most useful.

## Translations

`README.<lang>.md`, kept to the first screen plus the 12-rule table. Link it from the language bar at the top of README.md. Translating SKILL.md itself is welcome as `SKILL.<lang>.md`; the English file stays canonical.

## What will not be merged

- Rules that shorten the agent's replies because the user's input was short. See "What this is not" in SKILL.md.
- Rules that only apply to one AAC app or one device. The skill is for every host and every input method.
- Anything that adds code to the install path. The skill is a markdown file. The installer is a shell script. That's it.
