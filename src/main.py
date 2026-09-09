import os

from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

client = TelegramClient(
    "ps5_monitor",
    api_id,
    api_hash
)


async def main():
    me = await client.get_me()

    print(f"Conectado como: {me.first_name}")
    print(f"Username: @{me.username}")


with client:
    client.loop.run_until_complete(main())