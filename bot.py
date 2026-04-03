from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")
APP_URL = os.getenv("APP_URL")

if not TOKEN:
    raise RuntimeError("Environment variable TOKEN is missing")

if not APP_URL:
    raise RuntimeError("Environment variable APP_URL is missing")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Бот запущен. Отправь /app, чтобы получить кнопку для открытия Mini App."
    )


async def app_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("🚀 Открыть матрицу", web_app=WebAppInfo(url=APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Рабочая матрица:",
        reply_markup=reply_markup
    )


def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("app", app_command))
    application.run_polling()


if __name__ == "__main__":
    main()
