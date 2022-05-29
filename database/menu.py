import sqlite3
import random
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("menu.sqlite3")
    cursor = db.cursor()

    if db:
        db.execute("CREATE TABLE IF NOT EXISTS anketa_menu "
                   "(name TEXT PRIMARY KEY, description TEXT, "
                   "photo TEXT, price INTEGER)")
        db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa_menu VALUES "
                       "(?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random_menu(message):
    result = cursor.execute("SELECT * FROM anketa_menu").fetchall()
    random_user = random.randint(0, len(result) -1)
    await bot.send_photo(message.from_user.id,
                         result[random_user][2],
                         caption=f"Name: {result[random_user][0]}\n"
                                 f"Description: {result[random_user][1]}\n"
                                 f"Price: {result[random_user][3]}\n"
                                 )


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa_menu").fetchall()

