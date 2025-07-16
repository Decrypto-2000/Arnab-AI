# Features 

ArnabAI is a futuristic AI assistant built using **Angular** (frontend) and **FastAPI** (backend), powered by **LLaMA3 via Ollama**. It supports:
- 🔊 Voice synthesis and speech recognition
- 🤖 Profile-based personalities (e.g., MentorBot, CAT Guru)
- 💬 Conversational interface with real-time responses
- 🧠 Local LLM integration using Ollama

# Contents

👤 Avatar	Responsive & animated on speech
📤 Input box	Type or dictate your question
🧠 Responses	Generated via LLaMA3 API
🎭 Profile switch	Change AI tone/personality

### 🧱 System Requirements

- Node.js (v14+)
- Angular CLI (`npm install -g @angular/cli`)
- Python 3.8+
- pip
- Ollama (`https://ollama.com`)
- Git

### Installation steps 

git clone https://github.com/your-username/arnabai-assistant.git
cd arnabai-assistant

1. Backend
    cd fastapi-backend
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install fastapi uvicorn requests pydantic
    Start the FastAPI server: uvicorn main:app --reload --port 8000

2. Frontend
    cd angular-frontend
    npm install
    ng serve

3. Setting up Ollama (LLaMA3)
    Install Ollama: https://ollama.com/download
    Start a model (e.g. LLaMA3): ollama run llama3
    You can change the model in main.py if needed: "model": "llama3",



