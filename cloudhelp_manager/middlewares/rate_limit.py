import time

from aiogram import BaseMiddleware
from aiogram.types import Message


class RateLimitMiddleware(BaseMiddleware):
    def __init__(self, limit: float = 1.0):
        super().__init__()
        self.limit = limit
        self.users = {}

    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            user_id = event.from_user.id
            current_time = time.time()
            last_time = self.users.get(user_id, 0)

            if current_time - last_time < self.limit:
                await event.answer("⏳ Jangan spam ya, tunggu sebentar...")
                return

            self.users[user_id] = current_time

        return await handler(event, data)
