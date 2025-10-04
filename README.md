# 🧪 Cation

> **Cation** — An **unrestricted open-source search engine**, developed by [Sajad Troy](https://github.com/SajadTroy).
> Crawl, index, and search the web right from your **terminal (CLI)**.

---

## ✨ Features

* 🔎 Search by **title, snippet, or URL** (like Google, but offline).
* 🌐 **Crawler** (`crawler.py`) → crawl new websites.
* 🔄 **Updater** (`updater.py`) → refresh old data weekly.
* 🌲 **Deep Crawler** (`deepcrawler.py`) → discover sub-pages inside already crawled sites.
* 💾 Data stored in JSON (`data/webdata.json`) — easy to inspect, backup, or sync.
* ⏱ **Incremental saving** — no data lost even if interrupted.
* 🖥 CLI with **pagination & navigation** (`cation.py`).

---

## 📂 Project Structure

```
cation/
├─ data/
│   └─ webdata.json     # crawled dataset (auto-created)
├─ cation.py            # CLI search engine
├─ crawler.py           # crawler for new sites
├─ updater.py           # refresh existing data
├─ deepcrawler.py       # discover uncrawled subpages
└─ README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/SajadTroy/cation.git
cd cation
```

### 2. Install dependencies

```bash
pip install requests beautifulsoup4
```

### 3. Run the CLI search

```bash
python3 cation.py
```

Example:

```
🔎 Enter your search query: python
Showing results 1 - 3 of 10
1. Python — Official Site
   https://www.python.org/
   The official home of the Python Programming Language...
```

---

## 🌐 Crawling the Web

### Run the crawler

```bash
python3 crawler.py
```

* Starts from **seed URLs** (`SEEDS` inside crawler.py).
* Saves crawled results into `data/webdata.json`.
* Updates incrementally after each page.

### Update existing data

```bash
python3 updater.py
```

* Refreshes **titles/snippets** of already saved URLs.
* Designed to be run weekly (via cron job).

### Deep crawl existing dataset

```bash
python3 deepcrawler.py
```

* Expands into **sub-pages** of already crawled websites.
* Saves newly found pages into `webdata.json`.

---

## 🕒 Cron Job Example (Weekly Update)

Run updater every Sunday at 2AM:

```bash
0 2 * * SUN /usr/bin/python3 /path/to/cation/updater.py >> /path/to/cation/update.log 2>&1
```

---

## 🤝 Contributing

We welcome contributions! You can help **Cation** grow in two main ways:

### 1. Contribute Code

* Fork the repository
* Create a new branch (`git checkout -b feature-name`)
* Make your changes
* Commit (`git commit -m "Added new feature"`)
* Push to your branch and open a Pull Request

### 2. Contribute Crawl Data

* Run `crawler.py` or `deepcrawler.py` on your machine to collect new pages.
* Your crawled results will be saved in `data/webdata.json`.
* Review and clean the JSON (remove duplicates, irrelevant or broken entries).
* Submit your updated JSON as a **Pull Request** so it can be merged into the global dataset.

⚠️ **Rules for Crawl Data Contributions**:

* Only include **publicly accessible websites** (no paywalls, logins, or private data).
* Do not include **sensitive or illegal content**.
* Keep JSON format consistent:

  ```json
  {
    "title": "Page Title",
    "url": "https://example.com",
    "snippet": "Short description of the page..."
  }
  ```

---

## ⚖️ License

This project is licensed under **AGPL v3.0** with the following extra condition:

> *Commercial resale, whitelabeling, or removal of contributor/developer credits is prohibited.*

See [LICENSE](./LICENSE).

---

## 👨‍💻 Author

* **Sajad Troy** — [GitHub](https://github.com/SajadTroy)