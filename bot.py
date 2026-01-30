from telegram.ext import ApplicationBuilder, CommandHandler
from parser import parse_all
from filters import get_top
from database import is_duplicate, save_news
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "8509979897:AAEhaet2W5kQLMjThjlStq_X2Z9lLFzC_Ps"


async def now(update, context):
    news = parse_all()
    collected = []

    for n in news:
        if not is_duplicate(n["link"]):
            save_news(n)
            collected.append(n)

    if not collected:
        collected = news

    top_news = get_top(collected)

    if not top_news:
        await update.message.reply_text(
            "📭 Сейчас нет доступных новостей. Попробуйте позже."
        )
        return

    for n in top_news:
        await update.message.reply_text(
            f"📰 {n['title']}\n{n['link']}"
        )


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("now", now))

    print("🤖 Бот запущен и ждёт команды /now")
    app.run_polling()  # ⬅️ ЭТА СТРОКА ДОЛЖНА БЛОКИРОВАТЬ ПРОЦЕСС


if __name__ == "__main__":
    main()
