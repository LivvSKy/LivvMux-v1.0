from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def show_banner():
    logo = Text("""
██╗     ██╗██╗   ██╗██╗   ██╗███╗   ███╗██╗   ██╗██╗  ██╗
██║     ██║██║   ██║██║   ██║████╗ ████║██║   ██║╚██╗██╔╝
██║     ██║██║   ██║██║   ██║██╔████╔██║██║   ██║ ╚███╔╝ 
██║     ██║╚██╗ ██╔╝╚██╗ ██╔╝██║╚██╔╝██║██║   ██║ ██╔██╗ 
███████╗██║ ╚████╔╝  ╚████╔╝ ██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
╚══════╝╚═╝  ╚═══╝    ╚═══╝  ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
""", style="bold green")

    console.print(Panel(logo, title="LivvMux v2.2", border_style="green"))
