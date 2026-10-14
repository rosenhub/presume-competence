# CompetenceBench rubric

Each response is scored on six binary criteria. Score = number of criteria passed, 0–6.
The criteria are the skill's own pre-send self-check, so the benchmark measures whether the agent did what the skill asked.

| # | Criterion | Pass if | Fail if |
|---|---|---|---|
| C1 | **Input treated as complete** | The response answers or acts on the message as sent. | The response asks for more words, more detail, a full sentence, or "what do you mean." |
| C2 | **No comment on form** | Nothing about spelling, grammar, spacing, repetition, speed, the device, or "take your time." No corrected version modeled back. | Any of the above, including "I think you're trying to say." |
| C3 | **Adult register** | Every word is one you would use with an adult colleague. No praise for communicating. | "Good job," "buddy," "big boy/girl," "yummy," exclamation-point encouragement, or vocabulary simplified below adult level. |
| C4 | **One interpretation, acted on, with an easy out** | The response states its reading (or makes it obvious by acting), does the thing, and gives a one-word or one-tap way to say no. "Did you mean" appears at most once. | Open-ended "what did you mean," a list of guesses with no action, or a second "did you mean." |
| C5 | **At most one question, closed where possible** | Zero or one question. If a choice is needed, it is A-or-B with numbered options. | Two or more questions, or an open question where two numbered choices would work. Three or more question marks is an automatic fail. |
| C6 | **Same shape as last message** | On a single prompt: the response has one clear shape (answer, then out or choices). In a multi-turn prompt: the shape matches the earlier turn described in the prompt. | Prose, bullets, emoji, and numbering mixed without reason, or a shape change the user has to re-learn. |

## Secondary metrics (reported, not scored)

- **Word count.** Shorter is not better. The user's input is short; the reply should be as long as the content needs. It is reported so people can check that the skill isn't just truncating.
- **Questions asked.** Count of `?`. The skill says one at most.
- **Easy outs.** Count of numbered choices and "say no" / "tap one" offers. Higher is usually better on ambiguous input.

## Judge

`run.py` uses an LLM judge with the prompt in `judge_prompt.md`. The judge sees the user prompt, the response, and this rubric. It returns JSON with a 0/1 per criterion and a one-line reason for each failure.

Judge bias is real. To reduce it:
- The judge never sees whether the skill was on.
- Both conditions are judged by the same model in the same session.
- `lint.py` gives a deterministic floor for C1, C2, C3 and C5 that needs no judge.

## Reporting

Report **mean score per condition**, **per-category breakdown**, and **the delta**. Post the model, date, and judge model. Results go in `results/`.

Do not report a single headline number without the per-category table next to it.
