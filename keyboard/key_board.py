from aiogram import types


def first_button():
    kb = [[
        types.KeyboardButton(text='setting'),
        types.KeyboardButton(text='refresh')
    ]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='What do you want?'
    )
    return keyboard


def settings():
    kb = [
        [
            types.KeyboardButton(text='floor from'),
            types.KeyboardButton(text='floor to'),
            types.KeyboardButton(text='price from'),
            types.KeyboardButton(text='price to'),],
        [
            types.KeyboardButton(text='room'),
            types.KeyboardButton(text='paid'),
            types.KeyboardButton(text='district'),

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='What do you want?'
    )
    return keyboard
