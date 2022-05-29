import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=message.chat.id, text="Got your id")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="Пора спать!")


async def wake_up():
    file = open("media/cat.jpg", "rb")
    await bot.send_photo(chat_id=chat_id, photo=file, caption="Вствай!!!!")


async def mem_nigth():
    file = open("media/mem_nigth.jpg", "rb")
    await bot.send_photo(chat_id=chat_id, photo=file, caption="Интерестно")


async def scheduler():
    aioschedule.every().day.at("18:35").do(go_to_sleep)
    aioschedule.every().day.at("18:40").do(wake_up)
    aioschedule.every().friday.at("00:00").do(mem_nigth)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'разбуди' in word.text)
