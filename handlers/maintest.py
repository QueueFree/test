import logging
from aiogram.utils import executor
from config import bot, staff, dp
import commands
from db import db_main
from buttons import start_test
import send_products
import client_fsm
import fsm

async def on_startup(_):
    for i in staff:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               reply_markup=start_test)
        await db_main.sql_create()

commands.register_commands(dp)
client_fsm.register_client(dp)
fsm.register_store(dp)
send_products.register_send_products_handler(dp)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
