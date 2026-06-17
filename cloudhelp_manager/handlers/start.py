"""Start handler for CloudHelp Manager"""
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    """Handle /start command"""
    await message.answer(
        "🤖 Selamat datang di CloudHelp Manager!\n"
        "Bot Telegram enterprise-grade untuk manajemen supergroup."
    )
