from aiogram.types import BotCommand


async def setMyCommands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand("start", "Start bot"),
            BotCommand("show", "Show all items"),
            BotCommand("add", "Add new item"),
            BotCommand("del", "Delete some item"),
            BotCommand("help", "Show info commands")
        ]
    )