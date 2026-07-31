import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        # ------------------------
        # Website Title
        # ------------------------

        title = ""

        if soup.title:
            title = soup.title.get_text(strip=True)

        # ------------------------
        # Meta Description
        # ------------------------

        meta_description = ""

        meta = soup.find("meta", attrs={"name": "description"})

        if meta:
            meta_description = meta.get("content", "")

        # ------------------------
        # Headings
        # ------------------------

        headings = []

        for tag in ["h1", "h2", "h3"]:

            for heading in soup.find_all(tag):

                text = heading.get_text(" ", strip=True)

                if text:
                    headings.append(text)

        # ------------------------
        # Paragraphs
        # ------------------------

        paragraphs = []

        for p in soup.find_all("p"):

            text = p.get_text(" ", strip=True)

            if len(text) > 30:
                paragraphs.append(text)

        clean_text = "\n".join(paragraphs)

        word_count = len(clean_text.split())

        return {

            "success": True,

            "title": title,

            "description": meta_description,

            "headings": headings,

            "paragraphs": paragraphs,

            "clean_text": clean_text,

            "word_count": word_count

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }
