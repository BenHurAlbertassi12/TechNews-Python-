# Requisito 7
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    return [(i["title"], i["url"]) for i in search_news(
        {"title": {"$regex": title, "$options": "i"}})]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
