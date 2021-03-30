from aiogram.types import Message
from aiogram import executor
from settings import setMyCommands
from config import adminId
from loader import dp, bot

@dp.message_handler(commands=['start', 'help'])
async def sendWelcome(message: Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot")
    
    
@dp.message_handler()
async def echo(message: Message):
    """
    This echo handler
    """
    await message.answer(message.text)


async def onStartup(dp):
    await setMyCommands(dp)
    await bot.send_message(chat_id=adminId, text="Bot activated")


async def onShutdown(dp):
    await bot.close()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=onStartup, on_shutdown=onShutdown)
