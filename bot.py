from telegram.ext import ApplicationBuilder, CommandHandler
from parser import parse_all
from filters import get_top
from database import is_duplicate, save_news
import asyncio


TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


async def now(update, context):
    news = parse_all()
    fresh = []

    for n in news:
        if not is_duplicate(n['link']):
            save_news(n)
            fresh.append(n)

    for n in get_top(fresh):
        await update.message.reply_text(f"📰 {n['title']}\n{n['link']}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("now", now))
app.run_polling()