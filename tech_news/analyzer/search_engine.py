# Requisito 7
from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    return [(i["title"], i["url"]) for i in search_news(
        {"title": {"$regex": title, "$options": "i"}})]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    noticias_arr = []
    try:
        for news in search_news(
                {"timestamp": datetime.fromisoformat(date).strftime(
                    "%d/%m/%Y")}):
            noticias_arr.append((news["title"], news["url"]))
        return noticias_arr
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    list_arr = []
    noticias = search_news({"category": {"$regex": category, "$options": "i"}})
    if noticias:
        list_arr = [(new["title"], new["url"]) for new in noticias]
    return list_arr
