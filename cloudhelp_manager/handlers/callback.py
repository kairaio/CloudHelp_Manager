"""Callback handler for CloudHelp Manager"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query()
async def callback_handler(query: CallbackQuery):
    """Handle callback queries"""
    await query.answer("Callback handler aktif", show_alert=False)
