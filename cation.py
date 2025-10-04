#!/usr/bin/env python3
import sys

# ANSI escape code for purple text
PURPLE = "\033[95m"
RESET = "\033[0m"

def main():
    # Print project name in purple
    print(f"{PURPLE}")
    print("  ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗")
    print(" ██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║")
    print(" ██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║")
    print(" ██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║")
    print(" ╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║")
    print("  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝")
    print(f"{RESET}")

    # Input box for search query
    query = input("🔎 Enter your search query: ")

    # Just echo back (for now)
    print(f"\nYou searched for: {PURPLE}{query}{RESET}")

if __name__ == "__main__":
    main()
