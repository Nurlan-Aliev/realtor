import asyncio
import logging
import sys
from bot_dir.config import bot, dp
from bot_dir import commands, bot_setting


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
