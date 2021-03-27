from aiogram.types import Message
from aiogram import executor

from config import adminId
from loader import dp, bot


@dp.message_handler()
async def echo(message: Message):
    await message.answer(message.text)


async def onStartup(dp):
    await bot.send_message(chat_id=adminId, text="Bot activated")


async def onShutdown(dp):
    await bot.close()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=onStartup, on_shutdown=onShutdown)
