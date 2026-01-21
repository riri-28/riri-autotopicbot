import asyncio
import os
import sys
from datetime import datetime
import pytz # This library handles the timezone math
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

async def create_topic():
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Missing Environment Variables.")
        sys.exit(1)

    bot = Bot(token=BOT_TOKEN)

    # --- TIMEZONE FIX ---
    # We define the Philippine timezone
    ph_tz = pytz.timezone('Asia/Manila')
    
    # We get the current time specifically in PH
    # If it is 12:01 AM in Manila, this will now show the correct new date
    now_in_ph = datetime.now(ph_tz)
    
    topic_name = now_in_ph.strftime("%b. %d, %Y")

    print(f"Current PH Time: {now_in_ph}")
    print(f"Creating topic name: {topic_name}")

    try:
        await bot.create_forum_topic(chat_id=CHAT_ID, name=topic_name)
        print("Success! Topic created.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(create_topic())
