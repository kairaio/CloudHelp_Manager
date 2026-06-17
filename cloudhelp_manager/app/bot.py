import asyncio

from aiogram import Bot, Dispatcher

from app.config import BOT_TOKEN
from app.loader import register_handlers
from middlewares.rate_limit import RateLimitMiddleware
from utils.logger import setup_logger


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
