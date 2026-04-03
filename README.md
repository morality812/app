# Telegram Mini App Button Bot

Готовый минимальный бот для Telegram, который отправляет в чат кнопку `Открыть матрицу`.
По нажатию кнопка открывает ваш Mini App внутри Telegram.

## Что умеет
- команда `/start` - проверка, что бот запущен
- команда `/app` - отправляет кнопку `web_app` с вашим Mini App URL

## Файлы
- `bot.py` - код бота
- `requirements.txt` - зависимости
- `.env.example` - пример переменных окружения

## Что нужно перед запуском
1. Создать бота через BotFather
2. Получить токен бота
3. Задеплоить ваш Mini App и получить HTTPS-ссылку

## Локальный запуск
```bash
pip install -r requirements.txt
```

Windows PowerShell:
```powershell
$env:TOKEN="ВАШ_ТОКЕН"
$env:APP_URL="https://ваш-miniapp.vercel.app"
python bot.py
```

macOS / Linux:
```bash
export TOKEN="ВАШ_ТОКЕН"
export APP_URL="https://ваш-miniapp.vercel.app"
python bot.py
```

## Запуск на Render
1. Загрузите этот репозиторий на GitHub
2. Зайдите в Render
3. New + -> Web Service
4. Подключите GitHub-репозиторий
5. Runtime: `Python 3`
6. Start Command:
```bash
python bot.py
```
7. Добавьте Environment Variables:
- `TOKEN` = токен вашего бота
- `APP_URL` = ссылка на ваш Mini App

## Как использовать в группе
1. Добавьте бота в группу
2. Выдайте право отправлять сообщения
3. Если нужно, отключите privacy mode в BotFather:
   - `/setprivacy`
   - выберите бота
   - `Disable`
4. Напишите в группе:
```text
/app
```
5. Бот отправит сообщение с кнопкой `Открыть матрицу`
6. Закрепите это сообщение

## Важно
- Mini App должен быть доступен по `https`
- обычная URL-кнопка открывает ссылку как ссылку
- `web_app` кнопка открывает приложение внутри Telegram
