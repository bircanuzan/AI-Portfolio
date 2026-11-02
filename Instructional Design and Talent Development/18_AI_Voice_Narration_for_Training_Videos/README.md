# Project 18 — ElevenLabs Text-to-Speech for Multilingual Technical Learning

**Independent learning-product prototype** inspired by ElevenCreative, ElevenAPI and technical-trainer course-production requirements. Not a published course, certified voice talent, live ElevenLabs deployment or audio-generation result.

## Problem
Engineers learning machine learning or AI/DevOps benefit from concise, paced narration, transcript-first accessibility and consistent audio review. This demo prepares a short technical lesson for ElevenLabs text-to-speech output while keeping an offline dry-run as default.

## Working demonstration
- src/tts_preview.py: a dependency-free Python CLI that validates approved lesson text, safely prepares an ElevenLabs text-to-speech request and can optionally make a real call when explicitly enabled and an API key is set locally.
- tests/test_tts_preview.py: tests input constraints and that preview is offline.
- lessons/lesson_01_en.txt: original compact English technical lesson sample.
- docs/production_workflow.md: ~6-minute story-led instructional design, localization QA, consent, captions, editor feedback and cost-control checklist.

## Safe offline use
Python >=3.10:
1. python src/tts_preview.py --text-file lessons/lesson_01_en.txt --voice-id YOUR_APPROVED_VOICE_ID
2. python -m unittest discover -s tests -v

Offline is the **default**; this prints a safe request preview and NEVER synthesizes audio.

## Explicit paid API opt-in (not executed for this portfolio)
1. Use only a voice licensed and approved by the account owner. Set ELEVENLABS_API_KEY in the local environment, not Git.
2. Run python src/tts_preview.py --text-file lessons/lesson_01_en.txt --voice-id APPROVED_VOICE_ID --send --output lesson.mp3
3. Recheck the current ElevenLabs model, limits, prices and commercial rights before use. Each real request can incur charges.

## Technical alignment
The official REST route is POST https://api.elevenlabs.io/v1/text-to-speech/:voice_id with the xi-api-key header and model_id; implementation uses eleven_multilingual_v2 as a documented example. Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/convert

## Portfolio integrity
No actual audio file, voice clone or course has been generated or published. Any Arabic narration must undergo professional native-speaker review; translation fluency is not claimed. Never synthesize someone else's voice without their consent and the necessary rights.
