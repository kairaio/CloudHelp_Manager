import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# ✅ TOMBOL MENU
def menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⚙️ Menu", callback_data="menu"),
            InlineKeyboardButton(text="❓ Help", callback_data="help")
        ],
        [
            InlineKeyboardButton(text="📊 Stats", callback_data="stats")
        ]
    ])


# ✅ START COMMAND
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "✅ BOT BARU AKTIF",
        reply_markup=menu()
    )


# ✅ BUTTON HANDLER
@dp.callback_query(lambda c: c.data == "menu")
async def menu_btn(callback):
    await callback.message.answer("⚙️ MENU AKTIF")


@dp.callback_query(lambda c: c.data == "help")
async def help_btn(callback):
    await callback.message.answer("❓ HELP AKTIF")


@dp.callback_query(lambda c: c.data == "stats")
async def stats_btn(callback):
    await callback.message.answer("📊 STATS AKTIF")


async def main():
    print("✅ BOT NEW VERSION RUNNING")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
``
