from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def key_start():
    builder_inline = InlineKeyboardBuilder()

    builder_inline.row(
        types.InlineKeyboardButton(text='раздел №1', callback_data='first_block'),
        types.InlineKeyboardButton(text='раздел №2', callback_data='second_block')
    )
    builder_inline.row(
        types.InlineKeyboardButton(text='раздел №3', callback_data='three_block'),
        types.InlineKeyboardButton(text='раздел №5', callback_data='thour_block')
    )
    builder_inline.row(
        types.InlineKeyboardButton(text='обратиться в поддержку', callback_data='call_support')
    )

    return builder_inline