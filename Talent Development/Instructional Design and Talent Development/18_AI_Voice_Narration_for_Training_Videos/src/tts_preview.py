"""Opt-in ElevenLabs REST TTS example; dry run by default, no external deps."""
import argparse
import json
import os
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

BASE_URL = "https://api.elevenlabs.io/v1/text-to-speech/"
DEFAULT_MODEL = "eleven_multilingual_v2"

def prepare_request(text, voice_id, model_id=DEFAULT_MODEL):
    if not text or not text.strip():
        raise ValueError("Narration text cannot be empty")
    if len(text) > 3000:
        raise ValueError("Demo limit: text must be at most 3000 characters; split into lessons")
    if not voice_id or voice_id == "YOUR_APPROVED_VOICE_ID" or any(c in voice_id for c in "/?&# "):
        raise ValueError("Use a real, approved voice ID")
    if not model_id or not model_id.strip():
        raise ValueError("Model ID required")
    return {
        "url": BASE_URL + quote(voice_id, safe=""),
        "body": {"text": text, "model_id": model_id},
        "characters": len(text),
    }

def preview(text, voice_id, model_id=DEFAULT_MODEL):
    """No network calls; intentionally excludes API key and full text from output."""
    result = prepare_request(text, voice_id, model_id)
    return {"mode": "offline-preview", "endpoint": result["url"],
            "model_id": model_id, "characters": result["characters"],
            "billable_request_sent": False}

def send_audio(text, voice_id, output_path, model_id=DEFAULT_MODEL):
    """Only caller's explicit --send triggers external billable request."""
    request_spec = prepare_request(text, voice_id, model_id)
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        raise RuntimeError("ELEVENLABS_API_KEY must be set locally; never commit it")
    output = Path(output_path)
    if output.suffix.lower() != ".mp3":
        raise ValueError("Use an .mp3 output path")
    payload = json.dumps(request_spec["body"]).encode("utf-8")
    request = Request(
        request_spec["url"], data=payload, method="POST",
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"}
    )
    with urlopen(request, timeout=30) as response:
        data = response.read()
        if not response.headers.get("Content-Type", "").startswith("audio/"):
            raise RuntimeError("Expected audio response")
    output.write_bytes(data)
    return output

def main():
    p = argparse.ArgumentParser(description="ElevenLabs TTS teaching demo: offline by default")
    p.add_argument("--text-file", required=True)
    p.add_argument("--voice-id", required=True)
    p.add_argument("--model-id", default=DEFAULT_MODEL)
    p.add_argument("--send", action="store_true", help="Explicitly send a potentially billable API request")
    p.add_argument("--output", default="lesson.mp3")
    args = p.parse_args()
    text = Path(args.text_file).read_text(encoding="utf-8")
    if args.send:
        saved = send_audio(text, args.voice_id, args.output, args.model_id)
        print("Saved audio:", saved)
    else:
        # Preview accepts placeholder voice to avoid requiring account sign-up.
        voice = args.voice_id
        if voice == "YOUR_APPROVED_VOICE_ID":
            voice = "REPLACE_WITH_APPROVED_VOICE_ID"
        print(json.dumps(preview(text, voice, args.model_id), indent=2))

if __name__ == "__main__":
    main()
