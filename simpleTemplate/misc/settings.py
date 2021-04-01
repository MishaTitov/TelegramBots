from aiogram.types import BotCommand


async def setMyCommands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand("start", "Start dialogue"),
            BotCommand("help", "Show help")
        ]
    )