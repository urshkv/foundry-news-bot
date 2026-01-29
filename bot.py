from telegram.ext import ApplicationBuilder, CommandHandler
from parser import parse_all
from filters import get_top
from database import is_duplicate, save_news

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


async def now(update, context):
    news = parse_all()
    fresh = []

    for n in news:
        if not is_duplicate(n["link"]):
            save_news(n)
            fresh.append(n)

    top_news = get_top(fresh)

    # Fallback: если новостей нет
    if not top_news:
        await update.message.reply_text(
            "📭 Сейчас нет свежих новостей. Попробуйте позже."
        )
        return

    for n in top_news:
        await update.message.reply_text(
            f"📰 {n['title']}\n{n['link']}"
        )


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("now", now))
    app.run_polling()


if __name__ == "__main__":
    main()
