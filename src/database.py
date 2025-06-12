import asyncio
import asyncpg
import json

from settings import settings


url = settings.DB_URL()

async def call_stored_proc():
    params = '{"title": " Мармарис", "location": "Мармарис, ул. Южная, 15"}'
    conn = await asyncpg.connect(url)
    res = await conn.fetch('''SELECT "sch_hotels"."f_add_hotels"($1)''', params)
    print(res)
    await conn.close()

asyncio.run(call_stored_proc())
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
#
# Настройка работы с JSON типом
# await conn.set_type_codec(
#     'json',
#     encoder=json.dumps,
#     decoder=json.loads,
#     schema='pg_catalog'
# )
#
#
