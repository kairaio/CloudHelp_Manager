from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("settings"))
async def settings_handler(message: Message):
    await message.answer(
        "⚙️ Halaman settings masih dalam tahap pengembangan.\n"
        "Nanti di sini kamu bisa atur fitur bot."
    )
