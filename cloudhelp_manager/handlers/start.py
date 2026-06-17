from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main_menu import get_language_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    text = (
        "🌍 Welcome / Selamat datang\n\n"
        "Please choose your language:\n"
        "Silakan pilih bahasa:"
    )
    await message.answer(text, reply_markup=get_language_keyboard())
