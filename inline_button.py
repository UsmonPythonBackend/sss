from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="1-dars", callback_data="1-dars")
button2 = InlineKeyboardButton(text="2-dars", callback_data="2-dars")
button3 = InlineKeyboardButton(text="3-dars", callback_data="3-dars")
button4 = InlineKeyboardButton(text="4-dars", callback_data="4-dars")
keyboard.add(button1, button2, button3, button4)