from aiogram.types import BotCommand


async def setMyCommands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand("start", "What is Bot"),
            BotCommand("help", "Show help")
        ]
    )