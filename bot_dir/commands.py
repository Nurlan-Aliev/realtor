from asyncio import sleep

from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from bot_dir.config import dp, bot
from keyboard import key_board
from aiogram import F, types
from parser.parser import parse_bina
from bot_dir.bot_setting import params


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    start_message = (f"Hello, {hbold(message.from_user.full_name)}!\n"
                     f"I am your assistant for finding an apartment in Baku!\n"
                     f"Tell me what kind of apartment you are looking for")
    await message.answer(start_message, reply_markup=key_board.first_button())


@dp.message(F.text.lower() == 'refresh')
async def refresh(message: types.Message) -> None:
    """
    Updating data
    """
    await message.reply("")


@dp.message(F.text.lower() == 'setting')
async def setting(message: types.Message) -> None:
    """
    Displaying the keyboard with data settings
    """
    await message.answer('What do you want to change?', reply_markup=key_board.settings())
