from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, staff
import buttons
from aiogram.types import ReplyKeyboardRemove


class FSM_Store(StatesGroup):
    name_products = State()
    size = State()
    product_id = State()
    quantity = State()
    phone_number = State()
    submit = State()


async def start_fsm(message: types.Message):
    await message.answer('Укажите название или бренд товара: ', reply_markup=buttons.cancel_button)
    await FSM_Store.name_products.set()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_products'] = message.text

    await message.answer('Введите название товара: ')
    await FSM_Store.next()


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('Введите размер товара: ')
    await FSM_Store.next()


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('введите артикул товара: ')
    await FSM_Store.next()


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await message.answer('введите количество товара которое хотите заказать:')
    await FSM_Store.next()


async def load_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    await message.answer('введите свой номер телефона:')
    await FSM_Store.next()


async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'Да':
        async with state.proxy() as data:
            await message.answer('Отлично, Данные в отправлены!', reply_markup=kb)
            await bot.send_message(chat_id=7040928654, text=
                f"название: - {data['name_products']}\n"
                f"Размер: - {data['size']}\n"
                f"Артикул: - {data['product_id']}\n"
                f"количество: - {data['quantity']}\n"
                f"номер мобилы: - {data['phone_number']}"
            )
            await state.finish()

    elif message.text == 'Нет':
        await message.answer('Хорошо', reply_markup=kb)
        await state.finish()

    else:
        await message.answer('Выберите "Да" или "Нет"')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    kb = ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=kb)

def register_client(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state='*')

    dp.register_message_handler(start_fsm, commands=['client'])
    dp.register_message_handler(load_name, state=FSM_Store.name_products)
    dp.register_message_handler(load_size, state=FSM_Store.size)
    dp.register_message_handler(load_quantity, state=FSM_Store.quantity)
    dp.register_message_handler(load_product_id, state=FSM_Store.product_id)
    dp.register_message_handler(load_phone_number, state=FSM_Store.phone_number)
    dp.register_message_handler(submit, state=FSM_Store.submit)

