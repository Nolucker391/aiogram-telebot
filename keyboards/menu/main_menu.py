from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def key_start():
    builder_inline = InlineKeyboardBuilder()

    builder_inline.row(
        types.InlineKeyboardButton(text='🛍️Каталог', callback_data='first_block'),
        types.InlineKeyboardButton(text='🛒Корзина', callback_data='second_block')
    )
    builder_inline.row(
        types.InlineKeyboardButton(text='🙋FAQ', callback_data='third_block'),
    )
    builder_inline.row(
        types.InlineKeyboardButton(text='🔰бонусный раздел', callback_data='fourth_block')
    )
    return builder_inline