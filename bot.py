from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")
APP_URL = os.getenv("APP_URL")

async def app_command(update, context):
    keyboard = [
        [InlineKeyboardButton(
            "🚀 Открыть матрицу",
            web_app=WebAppInfo(url=APP_URL)
        )]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Рабочая матрица:",
        reply_markup=reply_markup
    )

async def start(update, context):
    await update.message.reply_text("Бот работает. Напиши /app")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("app", app_command))

app.run_polling()
