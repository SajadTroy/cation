import requests, json, time, os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# CONFIG
SEEDS = [
    "https://github.com/SajadTroy/cation",
]
OUTPUT = "data/webdata.json"
CRAWL_DELAY = 1.0
HEADERS = {"User-Agent": "CationCrawler/0.4 (+https://github.com/SajadTroy)"}


# -------------------------------
# Helpers
# -------------------------------
def normalize_url(url):
    """Normalize URL to avoid duplicates"""
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    netloc = parsed.netloc.lower()
    path = parsed.path.rstrip("/")  # remove trailing slash
    norm = f"{scheme}://{netloc}{path}"
    return norm


def clean_text(text, limit=200):
    return " ".join(text.split())[:limit]


def fetch_page(url):
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
        print(f"Error fetching {url}: {e}")
        return None


# -------------------------------
# Main crawler
# -------------------------------
def crawl():
    # Load existing dataset if available
    if os.path.exists(OUTPUT):
        with open(OUTPUT, "r") as f:
            try:
                existing = {normalize_url(d["url"]): d for d in json.load(f)}
            except:
                existing = {}
    else:
        existing = {}

    visited = set(existing.keys())
    to_visit = [normalize_url(u) for u in SEEDS]
    results = dict(existing)  # keep old data

    count = 0
    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)

        page = fetch_page(url)
        if not page:
            continue

        norm_url = normalize_url(url)
        results[norm_url] = {
            "title": page["title"],
            "url": norm_url,
            "snippet": page["snippet"]
        }
        count += 1
        print(f"[{count}] {page['title']} ({norm_url})")

        # ✅ Save progress immediately after each crawl
        os.makedirs("data", exist_ok=True)
        with open(OUTPUT, "w") as f:
            json.dump(list(results.values()), f, indent=2)

        # Extract new links (stay in same domain only)
        try:
            r = requests.get(norm_url, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")
            base = "{uri.scheme}://{uri.netloc}".format(uri=urlparse(norm_url))
            for a in soup.find_all("a", href=True):
                new_url = urljoin(base, a["href"])
                new_url = normalize_url(new_url)
                if new_url.startswith(base) and new_url not in visited:
                    to_visit.append(new_url)
        except:
            pass

        time.sleep(CRAWL_DELAY)

    print(f"\n✅ Crawl finished. {len(results)} unique pages saved to {OUTPUT}")


if __name__ == "__main__":
    crawl()
