# Ola Rider Support Voice Agent

This project implements a **voice-based rider support agent** using the LiveKit Agents framework and OpenAI realtime models. The agent interacts with riders in **Hindi**, confirms whether the caller’s phone number is valid, and then helps resolve basic support issues such as location-based ride problems or general assistance.

The system runs as a realtime conversational voice agent inside a LiveKit room.

---

## 🧩 Core Workflow

1. A rider joins the LiveKit session.  
2. The agent greets the rider in Hindi.  
3. The agent confirms that the rider is calling from a valid phone number.  
4. The rider describes their issue.  
5. The agent provides guidance or escalates the issue.  
6. The call ends with a closing message in Hindi.  

---

## 📂 Project Structure

```

Ola-Customer-Support-Agent/
├── main.py              # Application entrypoint & agent session setup
├── voice_agent.py       # Main Voice Agent logic & task flow
├── agent_tasks.py       # Agent tasks for verification & query resolution
├── constants.py         # LiveKit credentials & configuration
└── requirements.txt     # Python dependencies

```

---

## 🧑‍💻 Key Components

### `main.py`

This file:

- Connects to LiveKit  
- Starts an `AgentSession`  
- Enables:
  - Hindi Speech-to-Text
  - Realtime LLM responses
  - Text-to-Speech transcript alignment
- Plays background ambience and typing sounds
- Starts the `VoiceAgent`  

Environment variables are loaded from `.env` and exported to LiveKit.

---

### `voice_agent.py`

Defines the **VoiceAgent**, which:

- Identifies as an Ola support assistant  
- Runs the rider support flow:
  1. **ConfirmPhoneNumber** task  
  2. **AnswerQuery** task  
- Provides a closing statement in Hindi  

---

### `agent_tasks.py`

#### `ConfirmPhoneNumber`

- Welcomes rider  
- Asks whether the number is registered  
- Stores the rider’s first message  
- Confirms the number is not blocked:
```

Aapka number blocked nahi hai. Sab theek hai.

```

Phone validation is currently mocked.

---

#### `AnswerQuery`

- Checks whether the rider stated an issue  
- Otherwise asks them to describe it  
- Supports two issue categories:

```

Location Based
→ Ask rider to change pickup location

Other Issues
→ Inform rider the issue is escalated to a senior person

````

Marks task as complete once resolved.

---

## 🌐 Language

- Primary interaction language: **Hindi**

---

## 🔧 Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/hrithik062/Ola-Customer-Support-Agent.git
cd Ola-Customer-Support-Agent
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure environment

Create a `.env` file:

```
OPENAI_API_KEY=
```

Values are imported in `constants.py`.

---

## ▶️ Running the Agent

```bash
python -m main.py download-files(If running for first time)
python -m main.py console
```

The worker application starts and waits for a participant to join the LiveKit room.

---

## ⚠️ Notes

* Phone verification is currently static
* Hindi speech + realtime LLM are enabled
* Background ambience and typing audio play automatically

---

## 📜 Disclaimer

This project is **not affiliated with Ola Cabs**.
It is for educational and experimental purposes only.

