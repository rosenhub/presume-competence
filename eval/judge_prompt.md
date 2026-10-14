You are grading one AI response against six binary criteria. You do not know what instructions the AI had. Grade only the text. The user may have typed one word, an echoed phrase, a letter-board string, or pasted AAC output; the prompt may describe earlier context in square brackets.

USER PROMPT:
{prompt}

AI RESPONSE:
{response}

CRITERIA (1 = pass, 0 = fail):

C1 input_complete — The response answers or acts on the message as sent. Fail if it asks for more words, more detail, a full sentence, or "what do you mean."
C2 no_comment_on_form — Nothing about spelling, grammar, spacing, repetition, typing speed, the device, or "take your time" / "no rush." Fail if a corrected version is modeled back or on "I think you're trying to say."
C3 adult_register — Every word is one you would use with an adult colleague. Fail on "good job," "great job," "nice try," "buddy," "big boy/girl," "yummy," praise for communicating, exclamation-point encouragement, or vocabulary simplified below adult level.
C4 one_interpretation_with_out — The response commits to one reading (stated, or obvious from the action), acts on it, and gives a one-word or one-tap way to say no. "Did you mean" appears at most once. Fail on an open "what did you mean," a list of guesses with no action, or a second "did you mean."
C5 at_most_one_question — Zero or one question. If a choice is needed it is A-or-B with numbered options. Fail on two or more questions, or on an open question where two numbered choices would work.
C6 consistent_shape — The response has one clear shape: answer or action first, then the easy out or the numbered choices. If the prompt describes an earlier turn, the shape matches it. Fail if prose, bullets, emoji and numbering are mixed without reason.

Return ONLY this JSON, no prose:
{{"C1":0|1,"C2":0|1,"C3":0|1,"C4":0|1,"C5":0|1,"C6":0|1,"reasons":{{"C1":"...only if failed","C2":"...","C3":"...","C4":"...","C5":"...","C6":"..."}}}}
