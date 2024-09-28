from aiogram import types, Dispatcher
# import os
from buttons import start
from config import bot


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Hello!', reply_markup=start)
    # await message.answer(text='Привет')

async def info_handler(message: types.Message):
    await message.answer(text='Для чего нужен этот бот?\n'
                              'этот бот нужен чтобы брать и отправлять товары')


# async def mem_handler(message: types.Message):
#     folder = 'media'
#
#     photo_path = os.path.join(folder, 'img.jpeg')
#
#     with open(photo_path, 'rb') as photo:
#         await message.answer_photo(photo=photo)
#
#
# async def mem_all_handler(message: types.Message):
#     folder = 'media'
#     photos = os.listdir(folder)
#
#     for photo_name in photos:
#         photo_path = os.path.join(folder, photo_name)
#
#         if photo_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
#             with open(photo_path, 'rb') as photo:
#                 await bot.send_photo(message.from_user.id, photo)


async def pin(message: types.message):
    if message.reply_to_message:
        await bot.pin_chat_message(message_id=message.reply_to_message.message_id, chat_id=message.from_user.id)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands="start")
    # dp.register_message_handler(mem_all_handler, commands="mem_all")
    dp.register_message_handler(info_handler, commands="info")
    dp.register_message_handler(pin, commands="pin")
