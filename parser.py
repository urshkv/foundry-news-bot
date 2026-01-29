import requests
from bs4 import BeautifulSoup
from datetime import datetime


HEADERS = {"User-Agent": "Mozilla/5.0"}


SITES = {
"digitalbusiness": "https://digitalbusiness.kz",
"er10": "https://er10.kz",
"thetech": "https://the-tech.kz",
"spot": "https://www.spot.uz",
"limon": "https://limon.kg",
"bluescreen": "https://bluescreen.kz",
"astanahub": "https://astanahub.com",
"itpark_uz": "https://it-park.uz",
"itpark_kg": "https://it-park.kg",
"most": "https://most.com.kz",
"forbes": "https://forbes.kz",
"kursiv": "https://kursiv.media",
"weproject": "https://weproject.media",
"asiaplus": "https://asiaplustj.info",
"profit": "https://profit.kz"
}

def parse_site(url):
    r = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    news = []
    
    for a in soup.find_all("a", href=True)[:20]:
        title = a.text.strip()
        link = a['href']

        if len(title) < 25:
            continue


        if link.startswith('/'):
            link = url + link

        news.append({
            "title": title,
            "link": link,
            "description": title,
            "date": datetime.now().isoformat()
            })
    return news

def parse_all():
    all_news = []
    for site in SITES.values():
        try:
            all_news.extend(parse_site(site))
        except:
            pass
    return all_news