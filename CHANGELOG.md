# Changelog

## 1.0.0 — 2026-10-13

- Initial release: 12 rules, pre-send self-check, 16 hosts.
- Rule 12 is "I don't understand yet" plus two choices; a second "did you mean" is banned under rule 5.
- CompetenceBench: 48 prompts, 8 categories (single word, echoed phrase, letter string, pasted AAC output, yes/no only, repeated word, mixed with typos, silence then word), LLM judge + deterministic lint with a question-mark cap.
- `install.sh` with `--project` and `--dry-run`.
