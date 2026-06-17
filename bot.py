import asyncio
import sys
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent))

from cloudhelp_manager.app.config import BOT_TOKEN
from cloudhelp_manager.app.loader import register_handlers
from cloudhelp_manager.middlewares.rate_limit import RateLimitMiddleware
from cloudhelp_manager.utils.logger import setup_logger

from aiogram import Bot, Dispatcher


async def main():
    logger = setup_logger()

    print("🚀 CloudHelp Manager starting...")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    register_handlers(dp)
    dp.message.middleware(RateLimitMiddleware())

    logger.info("Bot started successfully ✅")

    await dp.start_polling(bot, timeout=60)


if __name__ == "__main__":
    asyncio.run(main())
