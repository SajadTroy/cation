import requests, json, time, os
from bs4 import BeautifulSoup

# CONFIG
OUTPUT = "data/webdata.json"
HEADERS = {"User-Agent": "CationUpdater/0.1 (+https://github.com/SajadTroy)"}
CRAWL_DELAY = 1.0


def clean_text(text, limit=200):
    return " ".join(text.split())[:limit]


def fetch_page(url):
    """Fetch updated title + snippet for an existing page"""
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return None
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string.strip() if soup.title else url
        desc = ""
        if soup.find("meta", attrs={"name": "description"}):
            desc = soup.find("meta", attrs={"name": "description"})["content"]
        snippet = desc if desc else clean_text(soup.get_text(), 200)
        return {"title": title, "url": url, "snippet": snippet}
    except Exception as e:
        print(f"⚠️ Error fetching {url}: {e}")
        return None


def update_existing():
    if not os.path.exists(OUTPUT):
        print(f"❌ No {OUTPUT} found. Run crawler first.")
        return

    with open(OUTPUT, "r") as f:
        try:
            data = json.load(f)
        except:
            print("❌ Failed to read JSON.")
            return

    updated = []
    for i, item in enumerate(data, start=1):
        url = item["url"]
        print(f"[{i}] Updating {url} ...")
        new_page = fetch_page(url)
        if new_page:
            updated.append(new_page)
        else:
            updated.append(item)  # keep old data if failed
        time.sleep(CRAWL_DELAY)

    # Save updated dataset
    with open(OUTPUT, "w") as f:
        json.dump(updated, f, indent=2)

    print(f"\n✅ Update finished. {len(updated)} pages refreshed in {OUTPUT}")


if __name__ == "__main__":
    update_existing()
