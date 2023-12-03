from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from bot_dir.config import dp
from keyboard.key_board import first_button, settings
from aiogram import F, types


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    start_message = (f"Hello, {hbold(message.from_user.full_name)}!\n"
                     f"I am your assistant for finding an apartment in Baku!\n"
                     f"Tell me what kind of apartment you are looking for")
    await message.answer(start_message, reply_markup=first_button())


