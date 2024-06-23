from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton("1-dars"), KeyboardButton("2-dars"), KeyboardButton("3-dars"), KeyboardButton("4-dars")],
    [KeyboardButton("5-dars"), KeyboardButton("6-dars"), KeyboardButton("7-dars"), KeyboardButton("8-dars")],
    [KeyboardButton("Qo'shimcha dars")],
    [KeyboardButton("Qo'shimcha dars")]],

    resize_keyboard=True,
    input_field_placeholder="KERAKLI DARSNI TANLANG...")



address_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

address_keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True)
address_keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)
address_keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True)
address_keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True)
address_keyboard5 = ReplyKeyboardMarkup(resize_keyboard=True)
address_keyboard6 = ReplyKeyboardMarkup(resize_keyboard=True)
address_keyboard7 = ReplyKeyboardMarkup(resize_keyboard=True)
address_keyboard8 = ReplyKeyboardMarkup(resize_keyboard=True)

address_keyboard1.add(KeyboardButton("dars haqida"))
address_keyboard2.add(KeyboardButton("dars haqida"))
address_keyboard3.add(KeyboardButton("dars haqida"))
address_keyboard4.add(KeyboardButton("dars haqida"))
address_keyboard5.add(KeyboardButton("dars haqida"))
address_keyboard6.add(KeyboardButton("dars haqida"))
address_keyboard7.add(KeyboardButton("dars haqida"))
address_keyboard8.add(KeyboardButton("dars haqida"))

address_keyboard1.add(KeyboardButton("qoshimcha malumot"))
address_keyboard2.add(KeyboardButton("qoshimcha malumot"))
address_keyboard3.add(KeyboardButton("qoshimcha malumot"))
address_keyboard4.add(KeyboardButton("qoshimcha malumot"))
address_keyboard5.add(KeyboardButton("qoshimcha malumot"))
address_keyboard6.add(KeyboardButton("qoshimcha malumot"))
address_keyboard7.add(KeyboardButton("qoshimcha malumot"))
address_keyboard8.add(KeyboardButton("qoshimcha malumot"))

address_keyboard.add(KeyboardButton("Back"))
