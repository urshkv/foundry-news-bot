from datetime import datetime

KEYWORDS = [
    "инвести",
    "стартап",
    "венчур",
    "раунд",
    "финанс",
    "акселератор",
    "фонд",
    "ai",
    "it",
    "технолог"
]


def calculate_relevance(news_item: dict) -> int:
    """
    Подсчитывает релевантность новости на основе ключевых слов.
    """
    text = f"{news_item.get('title', '')} {news_item.get('description', '')}".lower()
    score = 0

    for keyword in KEYWORDS:
        if keyword in text:
            score += 1

    return score


def parse_date(date_value) -> datetime:
    """
    Унифицирует дату публикации.
    """
    if isinstance(date_value, datetime):
        return date_value

    try:
        return datetime.fromisoformat(date_value)
    except Exception:
        return datetime.now()


def get_top(news_list: list, limit: int = 5) -> list:
    """
    Формирует топ новостей:
    1. По релевантности
    2. По дате публикации
    """
    for item in news_list:
        item["relevance"] = calculate_relevance(item)
        item["parsed_date"] = parse_date(item.get("date"))

    sorted_news = sorted(
        news_list,
        key=lambda x: (x["relevance"], x["parsed_date"]),
        reverse=True
    )

    return sorted_news[:limit]
