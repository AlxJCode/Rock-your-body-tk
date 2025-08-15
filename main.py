import os
import time
from rich.console import Console
from rich.text import Text

console = Console()

lyrics_with_timing = [
    ("I wanna da-, I wanna dance in the lights", 2.9),
    ("I wanna ro-, I wanna rock your body", 2.85),
    ("I wanna go, I wanna go for a ride", 2.6),
    ("", 0.4),
    ("Hop in the music and rock your body right", 2.8),
    ("Rock that body, come on, come on, rock that body", 2.1),
    ("Rock that body", 0.40),
    ("Rock that body, come on, come on", 1.0),
    ("ROCK", 0.1),
    ("THAT", 0.1),
    ("BODY", 0.1),
]

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def type_line_karaoke(line: str, duration: float, is_big: bool = False):
    clear_terminal()

    if is_big:
        
        text = Text("", style="bold yellow")
        console.print("\n" * 2)  
    else:
        text = Text("", style="yellow")

    delay = duration / max(len(line), 1)

    for char in line:
        text.append(char)
        console.print(text, end="\r")
        time.sleep(delay)

    console.print(text)
    time.sleep(0.5)

def run_karaoke():
    total_lines = len(lyrics_with_timing)
    for idx, (line, duration) in enumerate(lyrics_with_timing):
        is_big = idx >= total_lines - 7
        type_line_karaoke(line, duration, is_big)

    clear_terminal()

if __name__ == "__main__":
    run_karaoke()
