import asyncio
import logging
import sys
from bot_dir.config import bot, dp
import bot_dir.commands


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
