from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, message

keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
location = types.KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
keyboard_start.add(location)

options = ['Погода на сегодня', 'Погода на завтра', 'Предпочитаю погоду на неделю']
keyboard_options = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
keyboard_options.add(*options)