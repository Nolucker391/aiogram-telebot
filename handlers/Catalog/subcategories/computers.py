from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.routes import router
from aiogram.fsm.context import FSMContext
from states import UserState
from aiogram.types import Message

@router.callback_query(F.data == 'computers')
async def check_balance_button(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Catalog.select_computer)
    await callback.answer(text='Раздел компьютеров.')

    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text='Игровые', callback_data='gaming'),
        types.InlineKeyboardButton(text='Офисные', callback_data='office')
    )
    builder.row(
        types.InlineKeyboardButton(text='Для работы', callback_data='workpc'),
    )
    builder.row(
        types.InlineKeyboardButton(text='◀️назад', callback_data='back'),
    )
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())
