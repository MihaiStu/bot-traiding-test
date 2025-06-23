import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Añade esta variable en Railway

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot en modo test activado. Esperando operaciones...")

async def simulate_operations():
    while True:
        print("Simulando operación...")
        await asyncio.sleep(10)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    asyncio.create_task(simulate_operations())
    await app.start()
    await app.bot.set_webhook(url=WEBHOOK_URL)
    await app.updater.start_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        url_path="",
        webhook_url=WEBHOOK_URL,
    )
    await app.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())
