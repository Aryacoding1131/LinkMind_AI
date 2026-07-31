from datetime import datetime
from urllib.parse import urlparse

def format_date(date):
    if isinstance(date, datetime):
        return date.strftime("%d %B %Y")
    return date

def get_domain(url):

    domain = urlparse(url).netloc

    return domain.replace(
        "www.",
        ""
    )
