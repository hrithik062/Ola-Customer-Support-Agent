# Ola Customer Support Agent

An AI-powered conversational assistant designed to simulate **Ola cab customer support**.
This project demonstrates how to build a voice-driven support bot capable of handling real-world user interactions such as booking issues, complaints, ride queries, pricing, and more.

---

## 🚀 Features

* 🎙 **Voice Input Support**
  Speak naturally — the agent listens and responds.

* 🧠 **LLM-Powered Conversations**
  Built on modern AI models for contextual, human-like replies.

* 🎯 **Customer-Support Focused Logic**
  Designed to handle queries like:

  * Ride booking
  * Fare disputes
  * Driver issues
  * Refunds
  * Trip status
  * Account issues

* 🛠 **Modular & Extensible Codebase**
  Easy to modify for different domains or workflows.

* 🌍 **Real-World UX Simulation**
  Mimics tone and behavior of an actual customer-support desk.

---

## 📂 Project Structure

```bash
Ola-Customer-Support-Agent/
├── main.py              # Application entrypoint
├── voice_agent.py       # Voice interaction handler
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── ...
```

---

## 🧑‍💻 Tech Stack

| Layer     | Tool                      |
| --------- | ------------------------- |
| Language  | Python                    |
| AI        | LLM-based text generation |
| Interface | Voice + Text              |
| Runtime   | Local                     |

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/hrithik062/Ola-Customer-Support-Agent.git
cd Ola-Customer-Support-Agent
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

> Make sure **not** to commit your key.

---

## ▶️ Running the Project

Start the agent:

```bash
python -m main download-files (If running for first time)
python -m main console
```

Follow the on-screen instructions to begin interacting with the support bot.

---

## 🎤 Voice Agent

To use the voice assistant, ensure your system has:

✔ Microphone enabled
✔ Python audio libraries installed

The bot will:

1. Listen to your question
2. Process it via the AI model
3. Speak back the response

---

## 💡 Example Queries

Try asking:

```
I want to complain about my last ride
Why was I charged extra?
Can I schedule a cab?
How do refunds work?
My driver cancelled — what now?
```

---

## 🧩 Customization

You can modify:

🔹 System prompt
🔹 Response style
🔹 Supported intents
🔹 APIs
🔹 Logging / storage

This makes the agent reusable across industries (banking, e-commerce, healthcare, etc.)

---

## 🛡 Disclaimer

This project is **not affiliated with Ola Cabs**.
It is a **proof-of-concept** for learning & experimentation.

---

## 🤝 Contributing

Pull requests are welcome!

If you’d like to:

* improve UX
* add more intents
* enhance voice handling
* integrate a database
* Dockerize the app

feel free to open an issue first.

---

## ⭐ Support

If you find this project useful:

✔ Star the repo
✔ Share it
✔ Suggest improvements

---

## 👤 Author

**Hrithik D**

GitHub: [https://github.com/hrithik062](https://github.com/hrithik062)


Just tell me 👍
