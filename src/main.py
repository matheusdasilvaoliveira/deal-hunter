import os

from dotenv import load_dotenv
from telethon import TelegramClient, events

from config import PROMOTION_GROUP_IDS
from services.ps5_detector import is_ps5_message

load_dotenv()

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

client = TelegramClient(
    "ps5_monitor",
    api_id,
    api_hash
)

@client.on(events.NewMessage(chats=PROMOTION_GROUP_IDS))
async def handle_new_message(event):
    message = event.message.text or ""

    if not is_ps5_message(message):
        return

    print("\n" + "=" * 50)
    print(f"Grupo: {event.chat.title}")
    print(f"Mensagem: {message.text}")
    print("=" * 50)

async def main():
    print("🎯 PS5 Deal Hunter iniciado.")
    print(f"Monitorando {len(PROMOTION_GROUP_IDS)} grupos...")
    
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())