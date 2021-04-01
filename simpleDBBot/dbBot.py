from aiogram import executor
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message
from config import ADMIN_ID
from loader import dp, bot
from db import *
from misc.settings import setMyCommands


@dp.message_handler(commands='add')
async def addItem(msg: Message):
    try:
        vals = msg.text[5:].split(" ")
        tmp = await add_item(int(vals[0]), vals[1], int(vals[2]))
        if tmp:
            await msg.answer("Item was added")
    except:
        await msg.answer("FAIL Check Input")


@dp.message_handler(commands='del')
async def removeItem(msg: Message):
    try:
        val = msg.text[5:]
        tmp = await remove_item(int(val))
        if tmp:
            await msg.answer("Item was deleted")
    except:
        await msg.answer("FAIL Have some problem")


@dp.message_handler(commands='show')
async def showItems(msg: Message):
    table = await show_items()
    await msg.answer("Items:\n" + table)


@dp.message_handler(commands="help")
async def commandHelp(msg: Message):
        text = "List of commands:\n" \
               "/add - to add item write '/add id name price'\n" \
               "/del - to delete item write '/del id'\n" \
               "/show - to show all items ids, names and quantities"
        await msg.answer(text)


@dp.message_handler(CommandStart())
async def sendWelcome(msg: Message):
    await msg.answer(f"Hi! {msg.chat.first_name}"
                     f"\nI'm DB Bot, work with some database"
                     f"\nWrite /help to get some info about command")


async def onStartup(dp):
    await setMyCommands(dp)
    await create_table()
    await bot.send_message(chat_id=ADMIN_ID, text="Bot activated")


async def onShutdown(dp):
    await close_con()
    await bot.close()


if __name__=="__main__":
    executor.start_polling(dp, on_startup=onStartup, on_shutdown=onShutdown)