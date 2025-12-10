import logging
import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from src.routers.user_router import user_router

load_dotenv()

BOT_TOKEN = str(getenv('TOKEN'))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_routers(user_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())