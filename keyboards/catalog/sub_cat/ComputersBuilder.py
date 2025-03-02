from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

def computer_builder():
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text='Игровые', callback_data='gaming'),
        types.InlineKeyboardButton(text='Офисные', callback_data='office')
    )
    builder.row(
        types.InlineKeyboardButton(text='Для работы', callback_data='workpc'),
    )
    builder.row(
        types.InlineKeyboardButton(text='<< назад', callback_data='back'),
    )

    return builder