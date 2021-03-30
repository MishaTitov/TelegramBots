from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


locationKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send location", request_location=True)
        ],
        [
            KeyboardButton(text="Cancel")
        ]
    ], resize_keyboard=True
)