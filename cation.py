#!/usr/bin/env python3
import sys, time

# ANSI escape codes
PURPLE = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"

def typewriter(text, delay=0.05):
    """Typing animation"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Print project logo
    print(f"{PURPLE}{BOLD}")
    print("  ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗")
    print(" ██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║")
    print(" ██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║")
    print(" ██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║")
    print(" ╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║")
    print("  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝")
    print(f"{RESET}")

    # Typing animation tagline
    typewriter(f"{CYAN}An unrestricted open-source search engine{RESET}", 0.05)
    typewriter(f"{CYAN}Developed by: {BOLD}Sajad Troy{RESET}", 0.05)
    typewriter(f"{CYAN}GitHub: https://github.com/SajadTroy{RESET}", 0.05)

    print("\n")  # spacing

    # Input box for search query
    query = input("🔎 Enter your search query: ")

    # Just echo back (for now)
    print(f"\nYou searched for: {PURPLE}{query}{RESET}")

if __name__ == "__main__":
    main()
