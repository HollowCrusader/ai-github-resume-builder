# 🧠 AI-Powered GitHub Resume CLI

A CLI-first interactive résumé builder that turns your GitHub activity into a professional, customizable resume — with AI-enhanced project summaries, PDF generation, and interactive prompts.

Built for developers who want to go from GitHub to resume in seconds — directly from the terminal.

---

## 🚀 Features

- 🧾 **YAML-based resume structure** (`resume.yaml`)
- 🔗 **GitHub repo integration** — pull metadata automatically
- 🧠 **AI-powered summaries && Render to PDF** using Gemini AI (Google)
- 🧑‍💻 **Interactive CLI** — confirm, customize, or auto-add
- 💬 **Prompt-free mode** with `--yes` for automation

---

## 🧰 Tech Stack
Typer — CLI framework

python-dotenv — env loader

Gemini API (Google AI) — resume generation

Rich — CLI UX (spinners, prompts)

Pydantic — Data Validation

HTTPX — fully featured HTTP client

Hishel — HTTP Caching for HTTPX

---

## 📦 Installation

```bash
git clone https://github.com/HollowCrusader/ai-github-resume-builder

cd ai-github-resume-builder

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## 🔐 Gemini API Key <span style="color:green;">It's free!</span>
### How to Get Your Gemini API Key (Google AI Studio) 
To use Gemini AI for generating your résumé content, you’ll need an API key from Google’s AI Studio.

🪜 Step-by-Step Instructions
Go to Google AI Studio
→ Log in directly to: https://aistudio.google.com/app/apikey

Click “Create API key”
→ Copy the generated key

Set up your ``.env`` file
In the project root, create a file called .env with the following contents:

```bash
GEMINI_API_KEY=sk-your-google-api-key-here
```
✅ Done!
The CLI will now automatically load the key when generating your résumé.

---

## 💻 Resume CLI Instructions
To explore all commands and flags:
```bash
Python3 main.py --help

 Usage: main.py [OPTIONS] COMMAND [ARGS]...                                                                                    
                                                                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                     │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.              │
│ --help                        Show this message and exit.                                                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ init              Initialize an empty resume.yaml file.                                                                     │
│ add-experience    Add key projects to resume.yaml                                                                           │
│ get-profile       Add the user's GitHub profile to resume.yaml...                                                           │
│ generate-resume   Generate a resume from the resume.yaml file and save it as a PDF.                                         │
│ run-all           Run all commands in sequence.                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

```bash
python3 main.py run-all --help

                                                                                                       
 Usage: main.py run-all [OPTIONS] USERNAME                                                             
                                                                                                       
 Run all commands in sequence.                                                                         
                                                                                                       
                                                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────╮
│ *    username      TEXT  [default: None] [required]                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────╮
│ --yes   -y        Skip confirmation prompts                                                         │
│ --help            Show this message and exit.                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
The rest is pretty much self-explanatory from there.