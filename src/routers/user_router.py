from aiogram import Router, types
from aiogram.filters import Command, CommandStart

user_router = Router()

@user_router.message(CommandStart())
async def hello_message(message: types.Message):
    await message.answer(f'Hello {message.from_user.username}!')