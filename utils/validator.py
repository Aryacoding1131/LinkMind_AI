from urllib.parse import urlparse

def validate_url(url):
    try:
        res= urlparse(url)
        if res.scheme in ["http", "https"] and res.netloc:
            return True
        return False

    except:
        return False