
## Assignment - Choose Your Own List Page & Navigate It

**Your task:** Pick a website that lists items across **multiple pages** (e.g., quotes, articles, products, events).  
Avoid login walls and sites that forbid scraping. Educational sandboxes like `books.toscrape.com` are fine, but feel free to choose your own.

### Requirements
1. **Describe the target** (1–2 sentences): what you’re scraping and why it’s suitable.
2. **Inspect with DevTools**: include 1–2 screenshots highlighting the key request and the HTML structure you’ll parse.
3. **Fetcher**: implement a typed function  
   `fetch_html(url: str, headers: Optional[Dict[str, str]] = None, timeout_s: float = 15.0) -> str`  
   (you may reuse ours).
4. **Parser**: implement a typed function that extracts at least **three fields** per item (e.g., title, author, date/tags).
   - Return type: `list[tuple[str, str, list[str]]]` or a `dataclass`. If not applicable, use `list[dict[str, Any]]`.
5. **Pagination**: follow “Next” (or numbered pages) until you collect **≥ 50 items** (or exhaust pages).
6. **CSV export**: save to a CSV with **`;`** as the separator; if you have a list field, join with **`,`**.
7. **Politeness**: add a small `time.sleep` between requests; keep a `max_pages` cap.
8. **Documentation**: brief markdown section summarizing **what worked**, **what broke**, and **how you handled it**.

### Deliverables
- Notebook with completed cells and your screenshots.
- A CSV file in the repo (or alongside the notebook).

### Deadline
- Submit by **Thursday, October 30, 2025 at 09:45** (start of class).