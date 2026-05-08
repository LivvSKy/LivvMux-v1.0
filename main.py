import google.generativeai as genai
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from banner import show_banner
from config import API_KEY_FILE, PROMPT_FILE
import os

console = Console()

# === API KEY ===
def load_api_key():
    if not os.path.exists(API_KEY_FILE):
        console.print("[bold green]Masukkan Gemini API Key kamu:[/bold green]")
        key = Prompt.ask("API Key", password=True)
        with open(API_KEY_FILE, "w") as f:
            f.write(key)
        return key
    return open(API_KEY_FILE).read().strip()

# === PROMPT AI ===
def load_prompt():
    if not os.path.exists(PROMPT_FILE):
        console.print("[green]Masukkan PROMPT AI kamu:[/green]")
        prompt = Prompt.ask("Prompt")
        with open(PROMPT_FILE, "w", encoding="utf-8") as f:
            f.write(prompt)
        return prompt
    return open(PROMPT_FILE, encoding="utf-8").read().strip()

api_key = load_api_key()
system_prompt = load_prompt()

genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    "gemini-pro",
    system_instruction=system_prompt
)

show_banner()
console.print(Panel(
    "/setkey     → ganti API key\n"
    "/setprompt  → ganti prompt AI\n"
    "/clear      → clear layar\n"
    "/exit       → keluar",
    border_style="green"
))

while True:
    user = Prompt.ask("[bold green]Kamu[/bold green]")

    if user == "/exit":
        break

    if user == "/clear":
        console.clear()
        show_banner()
        continue

    if user == "/setkey":
        new_key = Prompt.ask("API Key baru", password=True)
        open(API_KEY_FILE, "w").write(new_key)
        genai.configure(api_key=new_key)
        console.print("[bold green]API Key diganti[/bold green]\n")
        continue

    if user == "/setprompt":
        new_prompt = Prompt.ask("Prompt baru")
        open(PROMPT_FILE, "w", encoding="utf-8").write(new_prompt)
        model = genai.GenerativeModel(
            "gemini-pro",
            system_instruction=new_prompt
        )
        console.print("[bold green]Prompt diganti[/bold green]\n")
        continue

    try:
        res = model.generate_content(user)
        console.print(f"[bold green]LivvMux[/bold green]: {res.text}\n")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
