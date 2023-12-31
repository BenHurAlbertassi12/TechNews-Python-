import re
import requests
import time
from parsel import Selector
# from bs4 import BeautifulSoup
from tech_news.database import create_news

# entry-title = h1


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
    return Selector(text=html_content).css(
        ".entry-title > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    return Selector(text=html_content).css(
        "a.next.page-numbers ::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    sess = Selector(text=html_content)
    title = sess.css('h1.entry-title::text').get()
    reading_time = sess.css('.meta-reading-time::text').get().split(' ')[0]
    summary = sess.css('.entry-content p').get()
    return {
        'url': sess.css('link[rel="canonical"]::attr(href)').get(),
        'title': title.replace('\n', '').strip(),
        'timestamp': sess.css('.meta-date::text').get(),
        'writer': sess.css('span.author a::text').get(),
        'reading_time': int(reading_time),
        'summary': re.sub('<.*?>', '', summary).strip(),
        'category': sess.css('.meta-category .label::text').get()
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    page_url = fetch("https://blog.betrybe.com")
    list_arr = []

    while True:
        for link in scrape_updates(page_url):
            list_arr.append(scrape_news(fetch(link)))

            if len(list_arr) >= amount:
                break

        if len(list_arr) >= amount:
            break
        else:
            page_url = fetch(scrape_next_page_link(page_url))

    create_news(list_arr)
    return list_arr
