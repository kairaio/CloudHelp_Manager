from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.main_menu import get_main_menu

router = Router()


@router.callback_query(F.data == "menu_help")
async def callback_help(callback: CallbackQuery):
    await callback.message.answer(
        "📘 Bantuan:\n"
        "/start - Menu utama\n"
        "/help - Bantuan\n"
        "/settings - Pengaturan"
    )
    await callback.answer()


@router.callback_query(F.data == "menu_settings")
async def callback_settings(callback: CallbackQuery):
    await callback.message.answer(
        "⚙️ Menu settings akan segera tersedia.\n"
        "Di sini nanti kamu bisa atur fitur bot."
    )
    await callback.answer()


@router.callback_query(F.data == "lang_id")
async def set_lang_id(callback: CallbackQuery):
    await callback.message.answer("✅ Bahasa Indonesia dipilih.")
    await callback.message.answer(
        "Gunakan menu di bawah:",
        reply_markup=get_main_menu()
    )
    await callback.answer()


@router.callback_query(F.data == "lang_en")
async def set_lang_en(callback: CallbackQuery):
    await callback.message.answer("✅ English selected.")
    await callback.message.answer(
        "Use the menu below:",
        reply_markup=get_main_menu()
    )
    await callback.answer()
