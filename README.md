# Bot_telegram


Telegram Promo Bot

A Telegram bot built with Python that automatically sends affiliate promotion links at scheduled times, using MongoDB Atlas as a cloud database and a task scheduling system.

This project was created to solve a real problem: automate the daily manual work of sending affiliate links at strategic times, saving time and making the process fully automatic.

🚀 Features

⏰ Automatic sending of promotions at scheduled times

🗄 Integration with MongoDB Atlas (cloud database)

📍 Timezone control (Brasília) using zoneinfo

🔁 Daily message scheduling between 9 AM and 6 PM

💬 Interactive Telegram commands:

/start

/help

/promo

/contato

/info

/feedback

🔘 Inline buttons that redirect directly to the promotion link

🧠 How it works

Promotion links are stored in MongoDB with their scheduled time.

The bot dynamically queries the database.

The Job Queue runs scheduled tasks at defined times.

The correct link is automatically sent to the chat.

🛠 Technologies Used

Python

python-telegram-bot

MongoDB Atlas

PyMongo

ZoneInfo (timezone handling)

JobQueue (task scheduling)

⚙️ Database Structure (example)
{
  "hour": "10:00",
  "url": "https://promotionlink.com",
  "description": "Daily promotion"
}

🧩 Challenges Faced

Connecting the bot properly to MongoDB Atlas

Understanding the difference between:

Command-triggered functions (CommandHandler)

Scheduled functions (job_queue)

Fixing parameter conflicts in scheduling

Adjusting message delivery according to Brasília timezone

✅ Result

✔ Fully functional bot
✔ 100% automated message sending
✔ Scalable structure ready for:

more schedules

new promotions

additional commands

logging system

📌 Possible Future Improvements

Admin panel

Configurable schedules via Telegram

Delivery reports

Click tracking

💡 Project Goal

Apply in practice concepts such as:

Automation

API integration

Cloud databases

Task scheduling

Scalable bot architecture
