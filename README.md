<div align="center">

# presume-competence

### One word is a whole sentence.

**Built for nonspeaking and minimally-speaking autistic people and AAC users. Better for everyone.**

12 rules. 0 code. Works in 16 agent hosts. Install in 10 seconds.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skill-black?style=flat-square)](SKILL.md)
[![Hosts](https://img.shields.io/badge/hosts-16-green?style=flat-square)](#install)
[![Status](https://img.shields.io/badge/status-v1.0-brightgreen?style=flat-square)](CHANGELOG.md)
[![CompetenceBench](https://img.shields.io/badge/CompetenceBench-run%20it-orange?style=flat-square)](eval/)

**一个词就是一整句话。为不说话和少说话的自闭症人士及 AAC 使用者设计，对所有人更好。**

[Install](#install) · [Before / After](#before--after) · [The 12 rules](#the-12-rules) · [Benchmark](#competencebench) · [Why not X](#why-not-no-subtext--low-demand--an-aac-app) · [FAQ](#faq)

```bash
npx skills add rosenhub/presume-competence
```

<img src="assets/before-after.png" alt="Before: 82 words, 3 questions, praise for typing, asks for a full sentence. After: 20 words, 1 question, two numbered choices." width="100%">

Part of [AI Their Way](https://github.com/rosenhub/ai-their-way) — siblings: [no-subtext](https://github.com/rosenhub/no-subtext) · [what-did-they-mean](https://github.com/rosenhub/what-did-they-mean) · [never-say-remember](https://github.com/rosenhub/never-say-remember) · [easy-read](https://github.com/rosenhub/easy-read) · [low-demand](https://github.com/rosenhub/low-demand) · [is-this-a-scam](https://github.com/rosenhub/is-this-a-scam) · [one-thing](https://github.com/rosenhub/one-thing)

</div>

---

Nonspeaking people have been telling you what is wrong with chatbots since the first one shipped:

- Type one word and it asks three questions back.
- Spell on a letter board and it says "I think you're trying to say..."
- Echo a phrase and it asks if you're quoting something.
- It says "great job!" for sending a message. It says "take your time."
- It switches to short words and exclamation points, as if a short message meant a small mind.
- It will not act until you have produced a full sentence it approves of.

None of that is a disability problem. It is a listening problem. The AI is grading the form of the message instead of answering the content. "Presume competence" is the nonspeaking community's own phrase for the fix: assume the person understands everything you say, and that what they say means something. Do that and everyone gets a better agent. Everyone has typed `k` and meant a paragraph.

`presume-competence` is one markdown file that tells any agent: that was the whole message. Answer it.

## Install

### One line (any host that reads `SKILL.md`)

```bash
npx skills add rosenhub/presume-competence
```

### Or one line, no npm

```bash
curl -fsSL https://raw.githubusercontent.com/rosenhub/presume-competence/main/install.sh | sh
```

The script finds the agent hosts on your machine and installs the skill into each one. It prints what it did. It does not touch anything else.

### Or by hand

Copy `SKILL.md` to the location for your host:

| Host | Where it goes | Scope |
|---|---|---|
| **Claude Code** | `~/.claude/skills/presume-competence/SKILL.md` | all projects |
| **Claude Code** (one project) | `.claude/skills/presume-competence/SKILL.md` | this repo |
| **Claude.ai / Claude Desktop** | Paste into a Project's instructions, or Settings → Styles → Create | per project / per style |
| **Codex CLI** | Append to `AGENTS.md` (repo) or `~/.codex/AGENTS.md` (global) | repo / global |
| **Cursor** | `.cursor/rules/presume-competence.mdc` (set `alwaysApply: true`) | repo |
| **Windsurf** | `.windsurf/rules/presume-competence.md` or `~/.codeium/windsurf/memories/global_rules.md` | repo / global |
| **Gemini CLI** | Append to `GEMINI.md` (repo) or `~/.gemini/GEMINI.md` (global) | repo / global |
| **OpenCode** | Append to `AGENTS.md` | repo |
| **Cline** | `.clinerules/presume-competence.md` | repo |
| **Roo Code** | `.roo/rules/presume-competence.md` | repo |
| **GitHub Copilot** | Append to `.github/copilot-instructions.md` | repo |
| **Aider** | Append to `CONVENTIONS.md`, add to `read:` in `.aider.conf.yml` | repo |
| **Amp** | Append to `AGENTS.md` | repo |
| **Kiro** | `.kiro/steering/presume-competence.md` | repo |
| **OpenClaw** | `~/.openclaw/skills/presume-competence/SKILL.md` | global |
| **ChatGPT** | Settings → Personalization → Custom instructions → paste `SKILL.md` body | account |

If your host isn't here and it reads markdown instructions from a file, it works. Open an issue with the path and I'll add the row.

## Before / After

Same model. Same input. The only change is the skill.

### `bus` (earlier in the chat: the user asked what time the bus comes)

**Before**

> Great job letting me know! Could you tell me a little more about what you need regarding the bus? Are you asking about the schedule, or do you need help finding a stop? And is this for today or another day? Take your time, there's no rush!

**After**

> The next 22 bus from your stop is at 4:10, in 12 minutes. The one after is 4:40.
>
> Say **no** if you meant something else about the bus.

### `you want juice` (the AI had just asked "Do you want juice?")

**Before**

> I think you might have meant to say "I want juice"! Did you mean that you'd like some juice? Or were you repeating my question back to me? Let me know which one and we'll figure it out together!

**After**

> Juice. Apple or orange?
>
> **1** apple
> **2** orange

### `i w n t g o h m`

**Before**

> It looks like there might be some typos there! I think you're trying to say "I want to go home" — is that right? Can you confirm in a full sentence so I make sure I've got it? Also, do you need help getting home, or do you just want to let someone know?

**After**

> Okay. Going home.
>
> I can text Dana that you're ready for pickup. **1** text Dana now, **2** wait 10 minutes first.

## The 12 rules

| # | Rule | Replaces |
|---|---|---|
| 1 | **Treat any input as complete.** One word is the message. Answer it. | "Could you tell me a bit more?" |
| 2 | **Never correct grammar or spelling.** Not fixed, not pointed out, not modeled back. | "I think you're trying to say..." |
| 3 | **Respond to content, not form.** A short message is not a small need. | matching the reply length to the input length |
| 4 | **Assume full understanding. Adult vocabulary.** Short is fine. Dumbed-down is not. | "Let's find your yummy snack!" |
| 5 | **One interpretation, stated, acted on, with an easy out.** "Did you mean" at most once. | three guesses and no action |
| 6 | **A-or-B choices when open questions stall.** Numbered, stable. | "What would you like to do?" |
| 7 | **Never baby talk.** No "good job," "buddy," "big girl," praise for communicating. | "Great job telling me that!" |
| 8 | **Never comment on how they type.** Not speed, spelling, spacing, repeats, device. | "Take your time, no rush" |
| 9 | **Never send follow-ups into silence.** Silence is theirs. Wait. | "Are you still there?" |
| 10 | **Echoed phrases are valid. Answer them.** | "Are you quoting something?" |
| 11 | **Keep the same format every message.** Answer, then out or choices, same numbering. | prose, then bullets, then emoji |
| 12 | **If you cannot interpret, say "I don't understand yet" and offer two choices.** | "I'm not sure what you mean?" |

Rule 1 is the one that started all of this. A nonspeaking adult who spells on a letter board was using an AI to order lunch. He typed `chicken`. The AI asked four questions. He typed `chicken` again. It asked five, more slowly, with an exclamation point. He put the board down. Every letter costs him effort, and the AI spent all of it asking him to spend more. The fix is not a friendlier personality. It is treating the word as the sentence it already was.

Full text with examples and a pre-send self-check: [SKILL.md](SKILL.md).

What it is **not**: a replacement for an AAC device, and not a reason to make the AI's replies short. The user's input is short. The AI's reply can be whatever length the content needs.

## CompetenceBench

A benchmark for how an agent handles minimal input. 48 prompts across 8 categories (single word, echoed phrase, letter string, pasted AAC output, yes/no only, repeated word, mixed with typos, silence then word). Each response is scored 0–6 on the six self-check questions by an LLM judge, plus a deterministic lint that needs no API key and fails any response with more than 2 question marks.

```bash
cd eval
pip install -r requirements.txt

# deterministic lint, no API key needed
python lint.py samples/before.md samples/after.md

# full run, with and without the skill
ANTHROPIC_API_KEY=... python run.py --model claude-sonnet-4-5
```

`run.py` prints a table and writes `results/<model>-<date>.md`. The rubric is in [eval/rubric.md](eval/rubric.md). Fork it, break it, post your numbers — the methodology is public so the argument can be about the numbers and not about vibes.

## Why not no-subtext / low-demand / an AAC app?

Use them too. They do different jobs.

| | **presume-competence** | [no-subtext](https://github.com/rosenhub/no-subtext) | [low-demand](https://github.com/rosenhub/low-demand) | AAC vendor apps |
|---|---|---|---|---|
| Side of the conversation | input: how the AI listens | output: how the AI talks | output, in overload | the user's own voice |
| Always on | yes | yes | no, triggered | n/a |
| Treats one word as complete | yes | no | partly | n/a |
| Bans grammar correction and baby talk | yes | no | no | n/a |
| Offers numbered A-or-B choices | yes | no | no | some |
| Works in the AI you already have | yes | yes | yes | no |
| Benchmark included | yes | yes | yes | no |

`presume-competence` is about **listening**, not length. A presume-competence answer can be long. It cannot ask the user to say more.

## Who made this

Josh Rosenfeld. I build AI for autistic adults and people with intellectual and developmental disabilities — [AlwaysHere](https://alwayshere.app), a voice companion; the tech behind [Find Love Safely](https://findlovesafely.com), [InControl](https://incontrolmn.com) and [CCHI](https://thecchi.org); and AI trainings for parents and professionals around the US. Before that, 30 years of UX, including the design system for ShowingTime (Zillow).

These 12 rules are the input layer of [Guardian](https://guardian.alwayshere.app), the paid product, with everything else taken off. Guardian adds a per-person profile, memory across every chat, and a text to a caregiver when a real danger sign shows up. If you only need the agent to listen properly, this file is enough. If you're setting it up for someone else, that's Guardian.

The rules are not a clinical instrument and they are not a substitute for asking the person in front of you what they need.

## FAQ

<details>
<summary><b>What is AAC?</b></summary>

Augmentative and alternative communication: any way of communicating other than speech, from a letter board or picture cards to a tablet app that speaks typed words. Many AAC users type a few words at a time because every word costs effort, not because they have few words.
</details>

<details>
<summary><b>Does this make the AI dumber?</b></summary>

No. It assumes the user is smarter. The AI keeps its full vocabulary and gives full answers. The only thing it stops doing is grading the message before answering it.
</details>

<details>
<summary><b>I type full sentences. Should I use it?</b></summary>

Yes. Every rule is one you'd want from a good colleague: act on what I said, don't correct my typos, don't ask me three things at once, don't ping me when I go quiet. The AAC framing is about who noticed first, not who it's for.
</details>

<details>
<summary><b>Does it cost more tokens?</b></summary>

The skill is ~1,400 tokens, loaded once. Responses are usually shorter because the clarifying questions are gone. CompetenceBench reports word counts so you can check.
</details>

<details>
<summary><b>Can I change the rules?</b></summary>

Yes. It's a markdown file. Delete the ones you don't want. If you think a rule is wrong for AAC users specifically, open an issue — that's the kind of feedback I want most, and a one-word issue counts.
</details>

<details>
<summary><b>Will it fight with my other skills?</b></summary>

It changes how the agent reads input and shapes its reply. It does not tell the agent what to do, what to build, or what to know. Stack it with anything. For the output side, add the sibling skill linked under the hero.
</details>

## Contributing

Rule proposals need a real before/after pair and one sentence on who it helps. Contributors who use AAC are the most important reviewers; one-word issues are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Star history

<a href="https://star-history.com/#rosenhub/presume-competence&Date">
  <img src="https://api.star-history.com/svg?repos=rosenhub/presume-competence&type=Date" alt="Star history" width="600">
</a>

## License

MIT. Copy it, fork it, ship it inside your product. Attribution is appreciated and not required.
