from aiogram import Dispatcher

from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.settings import router as settings_router
from handlers.callback import router as callback_router


def register_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(settings_router)
    dp.include_router(callback_router)
