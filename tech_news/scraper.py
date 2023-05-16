import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)

    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        return response.text if response.status_code == 200 else None
    except (requests.ReadTimeout, requests.RequestException):
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    sess = Selector(text=html_content)
    return sess.css(".entry-title > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
