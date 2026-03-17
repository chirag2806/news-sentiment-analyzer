import requests
from bs4 import BeautifulSoup

def scrape_text(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(page.content, "html.parser")
        paragraphs = soup.find_all("p")

        text = " ".join([p.get_text() for p in paragraphs])

        if len(text) < 100:
            return "Error"

        return text

    except:
        return "Error"