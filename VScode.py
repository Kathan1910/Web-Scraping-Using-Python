from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def scrape(site):
    # storing all visited urls in a set to prevent duplicates
    visited = set()

    # creating a queue to keep track of urls to scrape
    queue = [site]

    while queue:
        current_url = queue.pop(0)
        if current_url in visited:
            continue

        visited.add(current_url)

        try:
            # making a request to the current url
            r = requests.get(current_url, timeout=5)
        except requests.exceptions.RequestException as e:
            # handling exceptions during request
            print(f"Error connecting to {current_url}: {e}")
            continue

        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            full_url = urljoin(site, href)
            # checking if the url belongs to the same domain
            if site in full_url and full_url not in visited:
                queue.append(full_url)
                print(full_url)

if __name__ == "__main__":
    site = "http://example.webscraping.com"
    scrape(site)