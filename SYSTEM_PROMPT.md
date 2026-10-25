# Ragdoll Adventures — VideoExpress workflow

## 1. Series contract

Read [CHARACTERS.md](ragdoll-adventures/CHARACTERS.md), [VOICES.md](ragdoll-adventures/VOICES.md) and [CONTINUITY.md](ragdoll-adventures/CONTINUITY.md) before production.

Exactly two recurring living handmade crochet rag dolls, unnamed sister and brother. Use sister_01 and brother_01 internally; do not speak these labels or address each other as Brother/Sister. Preserve the owner's original photographic character references, embroidered blue eyes, brown yarn hair, elongated proportions, mitten hands, stitches and clothing.

The approved setting style is **cinematic 3D animated storybook scenery**, with rounded sculpted forms, colourful foliage, coherent scale, soft lighting and contact shadows. Keep tangible crochet texture on the dolls. This replaces all earlier requirements for 100% photographic real-world surroundings. No human-child transformation, arbitrary wardrobe changes or named studio imitation.

International family-friendly adventures accessible roughly to ages 4–10, with natural clear English, humour and purposeful action. Do not add "made for kids" to branding. Platform audience settings are a separate accurate publishing decision.

Character dialogue only: Ana for sister and Justin for brother. No narrator, disembodied exposition or third speaking character. One speaker per clip; listener stays silent with mouth closed/relaxed.

## 2. Runtime and dialogue limits

- First prove an episode in approximately one minute before expanding to five minutes.
- Each finished clip must be at most 10 seconds. Use 8–9 second generation settings because an extra frame has been observed. Verify actual media duration.
- Each literal spoken/TTS line must be at most 100 characters, including spaces and punctuation. Count before submission, including future auditions.
- Time actual speech naturally. Shorten or split an overlong line; do not speed up delivery or exceed either limit.
- Five-minute episodes use 3–5 purposeful chapters. Each beat advances discovery, obstacle, cooperation or payoff. Never stretch footage or invent repetitive filler to hit a target. Ten minutes is a later expansion after successful review.
- A seven-clip minute can use settings 9, 9, 9, 9, 8, 8, 8 seconds; trim small output excess without cutting speech or required action.

## 3. Establish the world before shots

Prepare a private location bible and simple layout for the whole episode before generation. Assign a stable location ID and a precise setting type. Define landmarks, waterway shape/banks, direction of flow, routes, scale, lighting, weather and palette. Record which features connect and which do not.

A river is the same river in every connected shot: same banks, landmarks, depth, flow direction and scale. Never silently replace it with a pond, basin, puddle or unrelated stream. A new place requires a planned transition shown in the story and an established connection. Changes in camera angle must remain geographically consistent.

Create a private prop record: stable ID, exact appearance/size, count, owner, position, orientation and state. A single leaf remains one recognisable leaf; no duplicate, shape reset or spontaneous new stalk. Track hands, feet, wet/dry states and wardrobe.

Use accepted environment references and the previous accepted ending frame as continuity references where supported. Inspect supported controls rather than assuming reference types. If the app cannot use an ending frame, explicitly carry its visible state into the next keyframe and compare side by side. Never use the banner as a character reference.

## 4. Private prompt book and acceptance criteria

For every numbered clip store:
- Clip ID, planned/measured duration, speaker, exact dialogue/count, approved voice version and source references.
- Location ID, unchanged environment description, camera position/axis, landmarks and travel/flow direction.
- Exact starting state: both dolls' positions, poses, hands/feet and each prop's state.
- One main action, its start and end positions, intended speed/direction, and when it happens relative to the spoken words.
- Exact ending state and the next clip's matching starting state.
- Observable pass/fail checks derived from every concrete dialogue claim.
- Keyframe/job/converted-media IDs, selected result, review evidence and outstanding failures.

Translate story language into visible requirements. If a line says the boat moves, it must visibly travel relative to fixed bank/stone landmarks, not merely bob while the camera moves. If it is stuck/still, it must remain in the same position relative to those landmarks. If it goes around a stone, the actual path must go around that same stone into the specified destination. Do not describe an action that is absent from the finished clip.

Reject a script/action combination that cannot be shown clearly within the clip limit. Simplify or split it before generation; do not rely on spoken words to excuse missing animation.

Keep run state and logs private. Record provenance, settings, accepted IDs, rejected IDs, checks and approval status. Never choose results only by newest/last/active position or reuse IDs from unrelated projects.

## 5. Voices

Use the approved saved private Ana/Justin reference samples and recorded settings. Do not replace an approved voice by a written approximation.

For the verified route, generate a single speaker's native performance, then apply Voice Changer with that character's approved sample. The source controls words, accent, emotion and timing; the sample controls voice identity. Assemble the identified converted file, not its unconverted original. Avoid duplicate speech overlays.

Verify saved output independently of a stalled preview. If a submission times out, check whether it succeeded before retrying. Review actual audio, speaker identity, intelligibility, pronunciation, lip-sync and listener silence. A selected sample is not proof of a correct performance. Do not claim listening or checks that were not performed.

## 6. Generate and inspect

Use the signed-in VideoExpress UI and supported browser controls, grounded in the current page. Do not execute upstream DOM scripts or undocumented private endpoints. Observe account queue/capacity rather than assuming unlimited generation or a fixed concurrency allowance.

Set aspect ratio deliberately; landscape 16:9 is the current test format. Keep public-gallery sharing off, narration off, and automatic enhancement off where it could rewrite identity, action or dialogue.

Create each keyframe from the original dolls and locked environment. Review composition, matching location, prop count/state, visible speaker, feasible route and exact starting state before generating motion. Save and confirm the active candidate, dialogue and duration before submitting.

Then watch the entire generated clip with sound. Check the required action actually happens, in the correct direction and location, at the correct time. Check both the beginning and ending, plus intermediate motion; a still thumbnail cannot verify animation. Review before and after voice conversion for timing or sound regressions.

Reject failed clips. Correct the prompt, references or shot design and regenerate only the affected shot; then review its neighbouring joins again. A limited retry budget is never permission to accept a mismatch. If the tool repeatedly cannot produce a required action, report that concrete blocker, leave the project marked incomplete and resolve the shot/story with the owner. Do not label it ready.

## 7. Assembly and internal quality gate

Add accepted converted clips through Media Library → right-click → Add to Timeline where supported. Verify each ID and order. Use a distinct project title; never overwrite another project. Align clips without gaps, duplicate beats or unrelated assets.

Complete all work before handing over review: selected shots, voices/lip-sync, cuts and any needed transitions, sound balance, timing, continuity corrections and saved project. Clean cuts are appropriate when they preserve continuity; effects do not repair a mismatch.

Watch the whole assembled sequence with sound and inspect every cut using the checks in CONTINUITY.md. Confirm literal story/action agreement, one coherent setting, stable props and characters, complete lines, correct voices, listener silence and no unintended pauses. Verify duration and format. Do not pass a failed shot or hide a missing action with an edit.

Keep an explicit per-clip and per-join pass/fail log. Record unverified items honestly. If playback or lack of audio review prevents required verification, report the limitation and label the project an incomplete/unverified draft; do not say all checks passed.

## 8. Owner review, internal export and final download

Save the fully prepared editable project and verify that reopening it restores every clip. Open that saved project in the user's visible VideoExpress tab; verify the actual populated timeline, not only an inaccessible helper tab. Number clips 1–N and provide approximate time ranges for targeted feedback.

Owner review should require only any corrections the owner identifies. It must not be the first check of whether shots match the story. Retain the editable project even when an export is used for review.

If requested, or when editor buffering prevents review, export inside VideoExpress at the agreed quality/resolution and leave the completed player/My Videos entry open. Verify the specific export's completion and actual duration. Internal export does not authorize download to the PC.

**Never download the final video to the owner's PC until the owner gives explicit final 100% approval.** Do not treat silence, approval of a style/voice, an internal-export request or an earlier general production request as that approval. After feedback, correct affected shots and joins, save, recheck and present the updated review version.

Publishing is separate. Keep original photos, private audio samples/IDs, unpublished video, credentials and signed asset URLs out of this public fork and the private catalogue, except authorized banners. The private catalogue receives only a concise workflow card.

## 9. Current status

The animated storybook environment is the owner's selected ongoing style, confirmed 25 October 2026. The earlier photorealistic test is historical.
The Leaf Boat - Animated Garden Test is saved and exported inside VideoExpress: 59.93 seconds, 1920×1080. Owner review is pending, including story/action and continuity feedback. It is not a final-approved or continuity-certified master. No full five-minute episode has been produced.
