# Video factory operating workbook

## Operating status

This is a repeatable, gated production procedure for the VideoExpress UI, with a local validation tool. It is **not a proven unattended video generator**. The next proof is a written 35-second test; no five-minute production until the short production process passes review. A new run starts from the approved animated test, never from a rejected correction.

## Required private run records

Copy templates/episode.json into private production storage. Never commit a filled episode record, original photos, voice samples, private asset IDs, signed URLs or unpublished episode media to this public repository. Store the location map, prop/state ledger, storyboard, prompt book, selected/rejected asset identities, edit decision list and review evidence alongside it. Retain failures to prevent accidental reuse.

Use one stable run ID and numbered shots. Record the workflow commit and style-lock version. Keep exact approved Ana/Justin sample identities in the private record. Verify current UI controls and selected output identities; never select media just because it is newest.

## Stage gates

| Stage | Work required | Gate to advance |
|---|---|---|
| 1. Plan | Inspect approved style reference; write a visual beginning, complication and payoff. Map location/props and start → action → end for every shot. Specify framing, exact dialogue/count and timing. | Plan validation passes; every shot earns its place; reference inspected before generation. |
| 2. Lock | Freeze story intent, style reference, original character identity, voices, location geography and prop identities. | Required actions cannot be silently removed to salvage a failure. |
| 3. Keyframes | Make varied, geographically consistent compositions. Compare each to the approved test and both dolls. | Style, soft character finish, prop state and feasible action pass before motion generation. |
| 4. Motion and voices | Generate one clear action per shot; verify actual motion, then apply and identify Ana/Justin output. Check full processed clip with sound. | Required action happens visibly; words, speaker, listener silence, lip-sync, character finish and measured duration pass. |
| 5. Edit | Cut to actual speech/action. Recheck each join, remove idle tails/heads and preserve needed anticipation/reaction. | No unexplained geography/prop resets, dead-air padding, repeated static coverage or truncated speech. |
| 6. Verify | Play entire final edit with sound; save/reopen populated numbered timeline. If preview buffers, render inside VideoExpress and inspect that exact export. | All per-shot, per-join and whole-film checks have observations and evidence. Any failed/unknown check blocks readiness. |
| 7. Owner review | Show the saved editable project, numbered time ranges and completed internal export. | Only owner-requested corrections should remain. Do not hand over a half-edited or unverified project as ready. |
| 8. Download | Preserve final approval in private run record. | Explicit final 100% go-ahead required for PC video download. Internal export is separately allowed. |

## Timing and cutting rules

Each final clip is at most 10 seconds; each exact spoken line is at most 100 characters including spaces and punctuation. Count literal submitted text, not a paraphrase. Review measured processed-media duration; a nominal 10-second setting may exceed the limit. Use shorter settings and trim only safe tails without cutting words or necessary action.

Plan natural speech against real action. Movement, a meaningful reaction or a motivated pause must justify the screen time. Remove unexplained silence, frozen waiting and repeated setup. Never slow footage, hold blank expressions, add repeated dialogue or lengthen idle tails to hit runtime. For the current test, budget 35 seconds in distinct shots. If a good edit is slightly short, redesign a useful beat before generation; do not pad the finished film. Longer episodes use 3–5 purposeful chapters, not longer holds.

## Failure recovery

1. Mark the exact failed shot/check and actual observation. Stop dependent generation.
2. Change one relevant variable: reference, staging, action direction, framing or prompt. Preserve story outcome and approved look.
3. Inspect the new result, including the full movement and processed audio. Recheck neighbouring joins after replacement.
4. After two failed attempts for the same required action, stop repeating substantially identical prompts. Diagnose a different supported shot technique; if unresolved, report the blocker with saved incomplete state. Do not spend more generations blindly or silently change the story.
5. Do not mark a run passed because it rendered, has a selected voice sample, has a plausible still, or reached the target duration.

## Run the checks

Use Python 3 (standard library only), with the filled record kept private:

```text
python tools/validate_episode.py path/to/private/episode.json --stage plan
python tools/validate_episode.py path/to/private/episode.json --stage generation
python tools/validate_episode.py path/to/private/episode.json --stage review
python tools/validate_episode.py path/to/private/episode.json --stage download
python -m unittest discover -s tests
```

Plan checks cover duration budget, exact dialogue lengths, approved voices, reference name, shot coverage, causal progression and complete shot/state descriptions. Generation additionally requires inspected-reference evidence. Review additionally requires measured clip lengths, all shot checks, all joins and whole-film checks with evidence. Download additionally requires the owner's explicit final approval statement.

The checker validates records, not pixels or sound. A zero exit code is never independent proof that a video looks or sounds correct. Human/agent review must actually inspect the media; inventing observations/evidence invalidates the run. If listening, reference inspection or full playback is unavailable, keep the respective check pending and report that limitation; do not claim readiness.

## Review checklist

- Approved animation and soft character finish match across every shot.
- Visual story remains understandable without dialogue; beginning, complication and payoff are visible.
- All concrete dialogue claims happen on screen at the right time.
- Varied shots support the action within one mapped world; no arbitrary new waterway or prop reset.
- No unused silence, frozen poses, padding or abrupt cut-off; pauses are motivated.
- Correct saved voices, exact speech, intelligibility, lip-sync, listener silence and balanced sound.
- Every clip ≤10 seconds; every line ≤100 characters; actual film runtime recorded.
- Correct converted assets on a saved, reopened, populated editable timeline.
- Internal export inspected when needed; PC download approval remains false until the owner says otherwise.
