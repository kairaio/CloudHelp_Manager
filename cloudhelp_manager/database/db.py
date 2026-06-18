"""
Database Connection Module - PostgreSQL
Provides async connection pool for database operations
"""

import os
import asyncio
from typing import Optional
import asyncpg
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


class DatabasePool:
    """PostgreSQL async connection pool manager"""
    
    _instance: Optional[asyncpg.Pool] = None
    
    @classmethod
    async def get_pool(cls) -> asyncpg.Pool:
        """
        Get or create the database connection pool
        
        Returns:
            asyncpg.Pool: Async connection pool
        """
        if cls._instance is None:
            cls._instance = await asyncpg.create_pool(
                DATABASE_URL,
                min_size=5,
                max_size=20,
                command_timeout=60,
            )
        return cls._instance
    
    @classmethod
    async def close_pool(cls):
        """Close the database connection pool"""
        if cls._instance is not None:
            await cls._instance.close()
            cls._instance = None


async def get_connection():
    """
    Get a single database connection from the pool
    
    Returns:
        asyncpg.Connection: Database connection
    """
    pool = await DatabasePool.get_pool()
    return await pool.acquire()


async def execute_query(query: str, *args):
    """
    Execute a query and return results
    
    Args:
        query (str): SQL query string
        *args: Query parameters
        
    Returns:
        list: Query results
    """
    pool = await DatabasePool.get_pool()
    async with pool.acquire() as conn:
        return await conn.fetch(query, *args)


async def execute_update(query: str, *args):
    """
    Execute an update/insert/delete query
    
    Args:
        query (str): SQL query string
        *args: Query parameters
        
    Returns:
        str: Number of affected rows
    """
    pool = await DatabasePool.get_pool()
    async with pool.acquire() as conn:
        return await conn.execute(query, *args)


async def execute_one(query: str, *args):
    """
    Execute a query and return single result
    
    Args:
        query (str): SQL query string
        *args: Query parameters
        
    Returns:
        Record: Single query result
    """
    pool = await DatabasePool.get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(query, *args)


# Export connection pool
pool = DatabasePool
