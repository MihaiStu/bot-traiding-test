import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("🟢 Comando /start recibido")
    await update.message.reply_text("✅ Bot en modo test activado. Esperando operaciones...")

async def simulate_operations():
    while True:
        print("🔄 Simulando operación...")
        await asyncio.sleep(10)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    asyncio.create_task(simulate_operations())
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())

