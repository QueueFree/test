from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_buttons = KeyboardButton('/start')
info_buttons = KeyboardButton('/info')
store_buttons = KeyboardButton('/store')
product_buttons = KeyboardButton('/products')
client_buttons = KeyboardButton('/client')
# mem_buttons = KeyboardButton('/mem_handler')
# mem_all_buttons = KeyboardButton('/mem_all')
# music_buttons = KeyboardButton('/music')
# quiz_buttons = KeyboardButton('/quiz')
# dice_buttons = KeyboardButton('/dice')
# games_buttons = KeyboardButton('/games')


start.add(start_buttons, info_buttons, store_buttons, product_buttons, client_buttons)

start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    ).add(
    KeyboardButton('/start'),
    KeyboardButton('/info'),
    KeyboardButton('/store'),
    KeyboardButton('/products'),
    KeyboardButton('/client')
)

cancel_button = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))

submit_button = ReplyKeyboardMarkup(resize_keyboard=True,
                                    row_width=2).add(KeyboardButton('Да'), KeyboardButton('Нет'))
