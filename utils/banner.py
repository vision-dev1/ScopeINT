# codes by vision
import os
import platform
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

BANNER_ART = r"""
   _____                          ____  _   __  ______
  / ___/_________  ____  ___     /  _/ / | / / /_  __/
  \__ \/ ___/ __ \/ __ \/ _ \    / /  /  |/ /   / /   
 ___/ / /__/ /_/ / /_/ /  __/  _/ /  / /|  /   / /    
/____/\___/\____/ .___/\___/  /___/ /_/ |_/   /_/     
               /_/                                    
"""

TAGLINE = "Domain Intelligence & OSINT Framework"
GITHUB = "GitHub: vision-dev1"

def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    os.system(command)

def print_banner():
    brand_panel = Panel(
        Text.from_markup(f"[bold cyan]{BANNER_ART}[/bold cyan]\n[bold white]{TAGLINE}[/bold white]\n[bold green]{GITHUB}[/bold green]"),
        border_style="bright_blue",
        expand=False
    )
    console.print(brand_panel)
    console.print("\n")

def get_text_banner():
    return f"{BANNER_ART}\n{TAGLINE}\n{GITHUB}"

if __name__ == "__main__":
    clear_screen()
    print_banner()

