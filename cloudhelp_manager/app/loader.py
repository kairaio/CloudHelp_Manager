from aiogram import Dispatcher

from cloudhelp_manager.handlers.start import router as start_router
from cloudhelp_manager.handlers.help import router as help_router
from cloudhelp_manager.handlers.settings import router as settings_router
from cloudhelp_manager.handlers.callback import router as callback_router


def register_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(settings_router)
    dp.include_router(callback_router)
