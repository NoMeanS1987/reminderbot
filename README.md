# reminderbot

Телеграм-бот, который раз в 30 минут присылает напоминание. Работает бесплатно на GitHub Actions.

## Настройка

1. Создай бота через [@BotFather](https://t.me/BotFather) и получи `TELEGRAM_BOT_TOKEN`.
2. Напиши боту любое сообщение, затем открой
   `https://api.telegram.org/bot<TOKEN>/getUpdates` и найди `"chat": {"id": ...}` — это твой `TELEGRAM_CHAT_ID`.
3. В репозитории: **Settings -> Secrets and variables -> Actions -> New repository secret** добавь два секрета:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
4. Проверь вручную: вкладка **Actions -> Reminder Bot -> Run workflow**.

## Заметки

- Cron GitHub Actions срабатывает с задержкой 1-5 минут — для напоминаний это нормально.
- Для публичного репозитория минуты Actions не расходуются (бесплатно).
