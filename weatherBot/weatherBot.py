from aiogram.types import Message, ReplyKeyboardRemove, ContentType
from loader import bot, dp
from aiogram import executor
from config import ADMIN_ID, API_KEY, WEATHER_URL
from keyboards.default.locationKey import locationKey
from misc.settings import setMyCommands
import requests
import json


@dp.message_handler(commands=['start'])
async def sendWelcome(message: Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi! " + message.from_user.first_name + "\n" +\
                        "I'm WeatherBot. To show weather write command /weather\n" +\
                        "Or you can just write name of the city")


@dp.message_handler(commands=["weather"])
async def choiceWay(message: Message):
    await message.answer(text="You can write name of the city or send your location", reply_markup=locationKey)


@dp.message_handler(content_types=ContentType.LOCATION)
async def weatherByLocation(msg: Message):
    params = {"lat": msg.location.latitude, "lon": msg.location.longitude, "appid": API_KEY, "units": "metric"}
    result = requests.get(WEATHER_URL, params=params)
    weather = result.json()
    await bot.send_message(chat_id=msg.chat.id, text=textHelper(weather), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Cancel")
async def todoCancel(msg: Message):
    await msg.answer("Canceled", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(content_types="text")
async def getWeather(message: Message):
    city = message.text
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        result = requests.get(WEATHER_URL, params=params)
        weather = result.json()
        await bot.send_message(message.chat.id, text=textHelper(weather), reply_markup=ReplyKeyboardRemove())
    except:
        await bot.send_message(message.chat.id, "I cannot find " + city + " name city")


def textHelper(weather: json):
    return "In city " + weather["name"] + "\n"\
           "Temperature: " + str(weather["main"]["temp"]) + " °C" + "\n"\
           "Feels like: " + str(weather['main']['feels_like']) + " °C" + "\n"\
           "Description: " + weather['weather'][0]['description']


async def onStartup(dp):
    await setMyCommands(dp)
    await bot.send_message(chat_id=ADMIN_ID, text="Bot activated")


async def onShutdown(dp):
    await bot.close()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=onStartup, on_shutdown=onShutdown)