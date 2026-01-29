FoundryNewsBot

Telegram-бот для агрегации новостей о стартапах, технологиях и венчурных инвестициях из региональных и локальных tech-медиа.
Бот автоматически собирает новости, устраняет дублирование, формирует ежедневный дайджест и отправляет топ наиболее релевантных публикаций.

Функциональность

- Парсинг новостей с профильных tech- и business-ресурсов
- Извлечение:
  - заголовка
  - ссылки на источник
  - краткого описания
  - даты публикации
- Исключение дубликатов
- Формирование топ-5 новостей по релевантности
- Telegram-интерфейс:
  - `/now` — получить актуальный топ новостей
  - автоматическая ежедневная рассылка (готово к расширению)


Источники данных

- digitalbusiness.kz  
- er10.kz  
- the-tech.kz  
- spot.uz  
- limon.kg  
- bluescreen.kz  
- astanahub.com  
- it-park.uz  
- it-park.kg  
- most.com.kz  
- forbes.kz  
- kursiv.media  
- weproject.media  
- asiaplustj.info  
- profit.kz  


Технологический стек

- Python 3.10+
- requests
- BeautifulSoup4
- python-telegram-bot
- SQLite


Структура проекта

foundry-news-bot/
│
├── bot.py # Telegram-бот
├── parser.py # Парсинг новостей
├── filters.py # Фильтрация и приоритизация
├── database.py # SQLite (антидубли)
├── requirements.txt
├── README.md
└── .gitignore

