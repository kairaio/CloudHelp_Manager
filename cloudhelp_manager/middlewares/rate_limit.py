"""Rate limiting middleware for CloudHelp Manager"""
from aiogram import BaseMiddleware


class RateLimitMiddleware(BaseMiddleware):
    """Middleware for rate limiting"""
    
    async def __call__(self, handler, event, data):
        # Implement rate limiting logic here if needed
        return await handler(event, data)
