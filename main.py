
import json
from datetime import datetime, timedelta
from rich.console import Console
from rich.text import Text

console = Console()
DATA_FILE = "habits.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def log_habit(habit_name):
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    if habit_name not in data:
        data[habit_name] = []

    if today not in data[habit_name]:
        data[habit_name].append(today)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

    console.print(f"[green]Logged '{habit_name}' for today![/green]")

def show_heatmap(habit_name):
    data = load_data()

    if habit_name not in data:
        console.print(f"[red]No data for {habit_name}.[/red]")
        return

    dates = data[habit_name]
    today = datetime.now()

    console.print(f"\n[bold blue]Heatmap for: {habit_name}[/bold blue]")

    heatmap = Text()

    for i in range(30, -1, -1):
        day = (today - timedelta(days=i)).strftime("%Y-%m-%d")

        if day in dates:
            heatmap.append(" 🟩 ", style="green")
        else:
            heatmap.append(" ⬜ ", style="dim")

        if i % 7 == 0:
            heatmap.append("\n")

    console.print(heatmap)

if __name__ == "__main__":
    habit = input("Enter habit name: ")
    log_habit(habit)
    show_heatmap(habit)
