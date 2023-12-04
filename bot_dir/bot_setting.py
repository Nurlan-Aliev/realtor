from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from bot_dir.config import dp
from keyboard import key_board
from aiogram import F, types

params = {}


class Form(StatesGroup):
    floor_from = State()
    price_from = State()
    floor_to = State()
    price_to = State()
    room = State()


@dp.message(F.text.lower() == 'floor from')
async def lower_floor(message: types.Message, state: FSMContext) -> None:
    """
    Changing the lower floor parameter
    """
    await state.set_state(Form.floor_from)
    await message.answer('from which floor?', reply_markup=ReplyKeyboardRemove())


@dp.message(Form.floor_from)
async def lower_floor_update(message: types.Message, state: FSMContext) -> None:
    """
    Setting the lower floor parameter
    """
    params['floor_from'] = message.text

    await state.clear()

    await message.answer('Update floor', reply_markup=key_board.first_button())


@dp.message(F.text.lower() == 'floor to')
async def upper_floor(message: types.Message, state: FSMContext) -> None:
    """
    Changing the upper floor parameter
    """
    await state.set_state(Form.floor_to)
    await message.answer('to which floor?', reply_markup=ReplyKeyboardRemove())


@dp.message(Form.floor_to)
async def upper_floor_update(message: types.Message, state: FSMContext) -> None:
    """
    Setting the upper floor parameter
    """
    params['floor_to'] = message.text
    await state.clear()
    await message.answer('Update floor', reply_markup=key_board.first_button())


@dp.message(F.text.lower() == 'room')
async def rooms(message: types.Message, state: FSMContext) -> None:
    """
    Changing rooms parameter
    """
    await state.set_state(Form.room)
    await message.answer('How many rooms?', reply_markup=ReplyKeyboardRemove())


@dp.message(Form.room)
async def room_update(message: types.Message, state: FSMContext) -> None:
    """
    Setting the rooms parameter
    """
    number_of_rooms = message.text

    # number_of_rooms.split()
    params['room_ids%5B%5D'] = number_of_rooms
    await state.clear()
    await message.answer('Update rooms', reply_markup=key_board.first_button())


@dp.message(F.text.lower() == 'price from')
async def lower_price_(message: types.Message, state: FSMContext) -> None:
    """
    Changing the lower price parameter
    """
    await state.set_state(Form.price_from)
    await message.answer('from which price?', reply_markup=ReplyKeyboardRemove())


@dp.message(Form.price_from)
async def lower_price_update(message: types.Message, state: FSMContext) -> None:
    """
    Setting the lower floor parameter
    """
    params['price_from'] = message.text
    await state.clear()

    await message.answer('Update price', reply_markup=key_board.first_button())


@dp.message(F.text.lower() == 'price to')
async def upper_price(message: types.Message, state: FSMContext) -> None:
    """
    Changing the upper price parameter
    """
    await state.set_state(Form.price_to)
    await message.answer('To which price?', reply_markup=ReplyKeyboardRemove())


@dp.message(Form.price_to)
async def upper_price_update(message: types.Message, state: FSMContext) -> None:
    """
    Setting the upper price parameter
    """
    params['price_to'] = message.text
    await state.clear()
    await message.answer('Update price', reply_markup=key_board.first_button())
