# Homework 2
# Web Scraping Assignment
# Website: https://books.toscrape.com
# Goal: Scrape book data (title, price, availability) across multiple pages.

#Imports
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List, Optional, Dict
import csv
import time
from urllib.parse import urljoin


#1. Fetcher Function
def fetch_html(url: str, headers: Optional[Dict[str, str]] = None, timeout_s: float = 15.0) -> str:
    """
    Fetch HTML content from the given URL with optional headers and timeout.
    """
    response = requests.get(url, headers=headers, timeout=timeout_s)
    response.raise_for_status()
    return response.text


#2. Dataclass Definition
@dataclass
class Book:
    title: str
    price: str
    availability: str


#3. Parser Function
def parse_books(html: str) -> List[Book]:
    """
    Parse book details from a Books to Scrape HTML page.
    Extracts title, price, and availability for each book.
    """
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"].strip()
        price = article.select_one("p.price_color").text.strip()
        availability = article.select_one("p.instock.availability").get_text(strip=True)
        books.append(Book(title, price, availability))
    return books


#4. Pagination Logic
base_url = "https://books.toscrape.com/catalogue/"
url = "https://books.toscrape.com/catalogue/page-1.html"

all_books = []
max_pages = 10  # safety limit
page_count = 0

while url and page_count < max_pages and len(all_books) < 50:
    print(f"Fetching: {url}")
    html = fetch_html(url)
    books = parse_books(html)
    all_books.extend(books)
    print(f"  Collected {len(books)} books from this page (total so far: {len(all_books)})")

    # Politeness delay
    time.sleep(1)

    # Find next page
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next > a")
    if next_link:
        next_href = next_link["href"]
        url = urljoin(url, next_href)
        page_count += 1
    else:
        url = None

print(f"\n Total books collected: {len(all_books)}")


#5. CSV Export
csv_path = "books.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Title", "Price", "Availability"])
    for book in all_books:
        writer.writerow([book.title, book.price, book.availability])

print(f"CSV file saved as: {csv_path}")
