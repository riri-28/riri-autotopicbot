import asyncio
import os
import sys
from datetime import datetime, timedelta
import pytz # We will use built-in timezone handling or simple offsets
from telegram import Bot

# We get these from GitHub Secrets (Environment Variables)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

async def create_topic():
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Missing Environment Variables.")
        sys.exit(1)

    bot = Bot(token=BOT_TOKEN)

    # 1. Calculate the Name for the Topic
    # We want the topic to be for "Tomorrow" relative to when the script runs
    # OR if you run this at 12:01 AM, it's for "Today".
    # Let's assume this script runs at 12:00 AM your time.
    
    # Define your timezone offset if needed (e.g., UTC+8 for Philippines)
    # GitHub servers run on UTC time.
    # If you want the topic to say "Jan 25", ensure we format the correct date.
    target_date = datetime.now() 
    
    topic_name = target_date.strftime("%b. %d, %Y")

    print(f"Creating topic: {topic_name}")

    try:
        await bot.create_forum_topic(chat_id=CHAT_ID, name=topic_name)
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(create_topic())