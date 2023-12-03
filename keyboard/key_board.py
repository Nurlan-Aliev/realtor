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
            types.KeyboardButton(text='Floor'),
            types.KeyboardButton(text='Price'),
            types.KeyboardButton(text='Room'),
            types.KeyboardButton(text='Paid'),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='What do you want?'
    )
    return keyboard
