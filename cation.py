import sys, time, json, os

# Colors
PURPLE = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"

RESULTS_PER_PAGE = 3

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def load_data():
    path = os.path.join("data", "webdata.json")
    with open(path, "r") as f:
        return json.load(f)

def search_data(data, query):
    results = []
    query = query.lower()
    for item in data:
        if query in item["title"].lower() or query in item["snippet"].lower():
            results.append(item)
    return results

def show_results(results, page=0):
    start = page * RESULTS_PER_PAGE
    end = start + RESULTS_PER_PAGE
    page_results = results[start:end]

    if not page_results:
        print(f"{PURPLE}No more results.{RESET}")
        return False

    print(f"\n{BOLD}Showing results {start+1} - {min(end,len(results))} of {len(results)}{RESET}\n")
    for i, r in enumerate(page_results, start=1+start):
        print(f"{GREEN}{i}. {r['title']}{RESET}")
        print(f"   {r['url']}")
        print(f"   {r['snippet']}\n")
    return True

def main():
    # Logo
    print(f"{PURPLE}{BOLD}")
    print("   ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗")
    print("  ██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║")
    print("  ██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║")
    print("  ██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║")
    print("  ╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║")
    print("   ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝")
    print(f"{RESET}")

    typewriter(f"{CYAN}An unrestricted open-source search engine{RESET}", 0.04)
    typewriter(f"{CYAN}Developed by: {BOLD}Sajad Troy{RESET}", 0.04)
    typewriter(f"{CYAN}GitHub: https://github.com/SajadTroy{RESET}\n", 0.04)

    data = load_data()

    while True:
        query = input("🔎 Enter your search query (or 'q' to quit): ")
        if query.lower() in ["q", "quit", "exit"]:
            print(f"{PURPLE}Goodbye!{RESET}")
            break

        results = search_data(data, query)
        if not results:
            print(f"{PURPLE}No results found for '{query}'.{RESET}\n")
            continue

        page = 0
        while True:
            if not show_results(results, page):
                break

            # Navigation menu (conditional)
            menu = []
            if page > 0:
                menu.append("[p] Previous")
            if (page + 1) * RESULTS_PER_PAGE < len(results):
                menu.append("[n] Next")
            menu.append("[s] New search")
            menu.append("[q] Quit")

            cmd = input("\n" + " | ".join(menu) + " : ").lower()

            if cmd == "n" and (page + 1) * RESULTS_PER_PAGE < len(results):
                page += 1
            elif cmd == "p" and page > 0:
                page -= 1
            elif cmd == "s":
                break
            elif cmd == "q":
                print(f"{PURPLE}Goodbye!{RESET}")
                return
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
