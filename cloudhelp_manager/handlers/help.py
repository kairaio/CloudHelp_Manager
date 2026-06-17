"""Help handler for CloudHelp Manager"""
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def help_handler(message: Message):
    """Handle /help command"""
    await message.answer(
        "📖 Bantuan CloudHelp Manager:\n\n"
        "/start - Mulai bot\n"
        "/help - Tampilkan bantuan ini\n"
        "/settings - Pengaturan bot\n"
    )
