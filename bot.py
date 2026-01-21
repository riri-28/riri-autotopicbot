import asyncio
import os
import sys
from datetime import datetime
import pytz 
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
STICKER_ID = os.environ.get("STICKER_ID") # Get the sticker ID from secrets

async def create_topic():
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Missing Environment Variables.")
        sys.exit(1)

    bot = Bot(token=BOT_TOKEN)

    ph_tz = pytz.timezone('Asia/Manila')
    now_in_ph = datetime.now(ph_tz)
    topic_name = now_in_ph.strftime("%b. %d, %Y")

    print(f"Creating topic: {topic_name}")

    try:
        # 1. Create the Topic and CAPTURE the result in a variable
        # The API returns a 'ForumTopic' object which contains the ID we need
        new_topic = await bot.create_forum_topic(chat_id=CHAT_ID, name=topic_name)
        
        topic_id = new_topic.message_thread_id
        print(f"Topic created successfully. ID: {topic_id}")

        # 2. Send the Sticker to that specific Topic ID
        if STICKER_ID:
            print("Sending sticker...")
            await bot.send_sticker(
                chat_id=CHAT_ID, 
                message_thread_id=topic_id, # This sends it INSIDE the topic
                sticker=STICKER_ID
            )
            print("Sticker sent!")
        else:
            print("No STICKER_ID found in secrets, skipping sticker.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(create_topic())
