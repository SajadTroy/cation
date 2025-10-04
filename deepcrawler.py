#!/usr/bin/env python3
import requests, json, time, os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

OUTPUT = "data/webdata.json"
CRAWL_DELAY = 1.0
HEADERS = {"User-Agent": "CationDeepCrawler/0.1 (+https://github.com/SajadTroy)"}

# -------------------------------
# Helpers
# -------------------------------
def normalize_url(url):
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    netloc = parsed.netloc.lower()
    path = parsed.path.rstrip("/")
    return f"{scheme}://{netloc}{path}"


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
        print(f"⚠️ Error fetching {url}: {e}")
        return None


# -------------------------------
# Deep crawler
# -------------------------------
def deep_crawl():
    if not os.path.exists(OUTPUT):
        print("❌ No existing webdata.json found. Run crawler.py first.")
        return

    # Load current dataset
    with open(OUTPUT, "r") as f:
        try:
            results = {normalize_url(d["url"]): d for d in json.load(f)}
        except:
            print("❌ Failed to read JSON file.")
            return

    visited = set(results.keys())
    to_visit = list(results.keys())  # start from already crawled pages
    count = len(visited)

    while to_visit:
        url = to_visit.pop(0)

        # Extract links
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")
            base = "{uri.scheme}://{uri.netloc}".format(uri=urlparse(url))

            for a in soup.find_all("a", href=True):
                new_url = urljoin(base, a["href"])
                new_url = normalize_url(new_url)

                # Only crawl same domain + skip if already visited
                if new_url.startswith(base) and new_url not in visited:
                    page = fetch_page(new_url)
                    if page:
                        results[new_url] = {
                            "title": page["title"],
                            "url": new_url,
                            "snippet": page["snippet"]
                        }
                        visited.add(new_url)
                        to_visit.append(new_url)
                        count += 1
                        print(f"[{count}] {page['title']} ({new_url})")

                        # Save after each crawl
                        os.makedirs("data", exist_ok=True)
                        with open(OUTPUT, "w") as f:
                            json.dump(list(results.values()), f, indent=2)

                        time.sleep(CRAWL_DELAY)
        except Exception as e:
            print(f"⚠️ Error crawling links from {url}: {e}")

    print(f"\n✅ Deep crawl finished. {len(results)} total pages saved to {OUTPUT}")


if __name__ == "__main__":
    deep_crawl()
