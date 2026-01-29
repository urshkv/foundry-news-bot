import sqlite3


conn = sqlite3.connect("news.db", check_same_thread=False)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    link TEXT PRIMARY KEY,
    title TEXT,
    description TEXT,
    published TEXT
)
""")
conn.commit()


def is_duplicate(link):
    cursor.execute("SELECT 1 FROM news WHERE link=?", (link,))
    return cursor.fetchone() is not None


def save_news(item):
    cursor.execute(
        "INSERT OR IGNORE INTO news VALUES (?, ?, ?, ?)",
        (item['link'], item['title'], item['description'], item['date'])
    )
    conn.commit()