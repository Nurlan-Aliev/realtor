from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode


load_dotenv()


TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
tg_bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
router = Router()
