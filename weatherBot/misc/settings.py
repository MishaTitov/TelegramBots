from aiogram.types import BotCommand


async def setMyCommands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand("weather", "Show Weather"),
            BotCommand("start", "Show help")
        ]
    )