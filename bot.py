from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("TOKEN")
APP_URL = os.getenv("APP_URL")

async def app_command(update, context):
    print("COMMAND RECEIVED")  # лог в Render

    if update.message:
        keyboard = [[InlineKeyboardButton(
            "🚀 Открыть матрицу",
            web_app=WebAppInfo(url=APP_URL)
        )]]

        await update.message.reply_text(
            "Рабочая матрица:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("app", app_command))

app.run_polling()
