from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
import requests

app = FastAPI()

# CORS settings for Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    user_input: str
    profile: str  # 'arnab', 'mentor', 'catguru', etc.

# Voice selection based on tone
def get_voice_from_tone(tone: str):
    tone = tone.lower()
    if "witty" in tone or "fun" in tone:
        return "Google UK English Male"
    elif "confident" in tone or "assertive" in tone:
        return "Microsoft Mark - English (United States)"
    elif "supportive" in tone or "calm" in tone:
        return "Google US English"
    elif "serious" in tone or "mentor" in tone:
        return "Microsoft David - English (United States)"
    return "Google US English"  # fallback


@app.post("/ask")
def ask(message: Message):
    profile_path = f"profiles/{message.profile}.json"
    if not os.path.exists(profile_path):
        return {"reply": f"Profile '{message.profile}' not found.", "voice": "en-IN-NeerjaNeural"}

    with open(profile_path) as f:
        profile = json.load(f)

    # Prepare prompt
    prompt = f"You are {profile['name']}, {profile['tone']}. {profile['style']}\n"
    prompt += f"User: {message.user_input}\n{profile['name']}:"

    # Call Ollama (LLaMA3)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    reply = result.get("response", "").strip()
    voice = get_voice_from_tone(profile['tone'])

    # Save chat history
    with open("history.json", "a") as f:
        f.write(json.dumps({
            "profile": message.profile,
            "name": profile['name'],
            "q": message.user_input,
            "a": reply
        }) + "\n")

    return {"reply": reply, "voice": voice}
