import logging
from db import Database
from Button import (menu_keyboard, address_keyboard, address_keyboard1, address_keyboard2,
                    address_keyboard3, address_keyboard4, address_keyboard5, address_keyboard6,
                    address_keyboard7, address_keyboard8)
from inline_button import keyboard

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "7247111795:AAE8vC54W0Cxrtw9CL5xmo1L5R22FOqkyvM"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users (username, full_name, user_id) VALUES ('{username}', '{full_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"yana bir bor salom @{full_name}", reply_markup=menu_keyboard)
    else:
        await Database.connect(query, "insert")
        await message.reply(f"salom @{full_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "MENU")
async def menu(message: types.Message):
    await message.answer("Darslarni birini tanlang ", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "MENU")
async def menu(message: types.Message):
    await message.answer("DARSLAR", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "1-dars")
async def menu(message: types.Message):
    await message.answer("hozircha video yoq", reply_markup=address_keyboard1)


@dp.message_handler(lambda message: message.text == "2-dars")
async def menu(message: types.Message):
    await message.answer("hozircha video yoq", reply_markup=address_keyboard2)


@dp.message_handler(lambda message: message.text == "3-dars")
async def menu(message: types.Message):
    await message.answer("hozircha video yoq", reply_markup=address_keyboard3)


@dp.message_handler(lambda message: message.text == "4-dars")
async def menu(message: types.Message):
    await message.answer("hozircha video yoq", reply_markup=address_keyboard4)


@dp.message_handler(lambda message: message.text == "5-dars")
async def menu(message: types.Message):
    await message.answer("hozircha video yoq", reply_markup=address_keyboard5)


@dp.message_handler(lambda message: message.text == "6-dars")
async def menu(message: types.Message):
    await message.answer("hozircha video yoq", reply_markup=address_keyboard6)


@dp.message_handler(lambda message: message.text == "7-dars")
async def menu(message: types.Message):
    await message.answer("hozircha video yoq", reply_markup=address_keyboard7)


@dp.message_handler(lambda message: message.text == "8-dars")
async def menu(message: types.Message):
    await message.answer("hozircha video yoq", reply_markup=address_keyboard8)


@dp.message_handler(lambda message: message.text == "dars haqida")
async def menu(message: types.Message):
    await message.answer("hozircha malumot yoq", reply_markup=address_keyboard1)


@dp.message_handler(lambda message: message.text == "qoshimcha malumot")
async def menu(message: types.Message):
    await message.answer("hozircha malumot yoq", reply_markup=address_keyboard1)


@dp.message_handler(lambda message: message.text == "orqaga")
async def menu(message: types.Message):
    await message.answer("darslar", reply_markup=menu_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)