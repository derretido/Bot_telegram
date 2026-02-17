## 🌐 Languages
- [English](READMEpt.md)
- [Português](README.md)


# Telegram Promo Bot

A Telegram bot that automatically sends promotional links at scheduled times (9 AM to 6 PM) and also responds manually to the `/promo` command.  
The project integrates MongoDB Atlas, scheduling tasks, and interactive messages with inline buttons.

---

## 🚀 Features
- Automatic sending of promotions at predefined times using the job queue.
- `/promo` command to list all available promotions.
- Messages with interactive buttons that redirect users to the promotion link.
- Integration with MongoDB Atlas to store and update links.
- Timezone configuration to ensure messages are sent according to Brasília time.

---

## 🛠️ Libraries Used
- **[python-telegram-bot](https://python-telegram-bot.org/)**  
  Core library for building the bot, sending messages, and creating inline buttons.

- **pymongo**  
  Connects to MongoDB Atlas, enabling reading and updating of promotion links.

- **pytz**  
  Handles timezone management, ensuring scheduling follows Brasília time.

- **datetime**  
  Defines job execution times (`datetime.time`).

- **os / python-dotenv**  
  Loads environment variables (bot TOKEN and group CHAT_ID), keeping sensitive data outside the code.

---

## 📂 Project Structure
- `bot.py` → main bot code (functions, handlers, and scheduling).
- `load_promotions()` → reads links directly from MongoDB Atlas.
- `promo()` → manual command that lists all promotions.
- `send_scheduled_message()` → automatically sends the promotion corresponding to the scheduled time.
- `.env` → environment file containing variables (TOKEN and CHAT_ID).

---

## ⚙️ How It Works
1. The bot connects to MongoDB Atlas and loads promotion links.
2. The `job_queue` schedules automatic messages based on defined times.
3. The `/promo` command can be used anytime to list all promotions.
4. Messages include inline buttons that redirect users to the promotion link.

---

## ▶️ Running the Bot
1. Configure the `.env` file:
   ```env
   TOKEN=your_bot_token
   CHAT_ID=-123456789
