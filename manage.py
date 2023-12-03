import asyncio
import logging
import sys
from bot.config import tg_bot, dp


async def main() -> None:
    await dp.start_polling(tg_bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
