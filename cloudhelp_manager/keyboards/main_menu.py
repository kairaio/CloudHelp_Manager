from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📘 Help", callback_data="menu_help"),
                InlineKeyboardButton(text="⚙️ Settings", callback_data="menu_settings"),
            ]
        ]
    )
    return keyboard


def get_language_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇮🇩 Indonesia", callback_data="lang_id"),
                InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
            ]
        ]
    )
    return keyboard
