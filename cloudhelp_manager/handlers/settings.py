"""Settings handler for CloudHelp Manager"""
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("settings"))
async def settings_handler(message: Message):
    """Handle /settings command"""
    await message.answer(
        "⚙️ Pengaturan CloudHelp Manager\n\n"
        "Fitur pengaturan masih dalam pengembangan."
    )
