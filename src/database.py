import asyncio
import asyncpg
import json

from src.config import DB_URL


async def call_stored_proc(db_object, params, url = DB_URL):
    conn = await asyncpg.connect(url)
    res = await conn.fetch(db_object, params)
    await conn.close()
    return res

#asyncio.run(call_stored_proc(db_object, params))
#---------------------
# pool = await asyncpg.create_pool(
#     user='postgres',
#     password='secret',
#     database='test_db',
#     host='127.0.0.1'
# )
#
# async with pool.acquire() as conn:
#     try:
#         params = {
#             "title": "val1",
#             "location": "val2"
#         }
#
#         await conn.execute(
#             'CALL "booking"."hotels"( $1 )',
#             params
#         )
#
#     except asyncpg.PostgresError as e:
#         print(f"Произошла ошибка: {e}")

