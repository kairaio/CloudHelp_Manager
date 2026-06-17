from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def help_handler(message: Message):
    text = (
        "📘 Help Menu\n\n"
        "/start - Menu utama\n"
        "/help - Bantuan\n"
        "/settings - Pengaturan"
    )
    await message.answer(text)


@router.message(F.text)
async def unknown_handler(message: Message):
    await message.answer("❓ Perintah tidak dikenali. Gunakan /help ya.")
