from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.routes import router
from aiogram.fsm.context import FSMContext
from states import UserState
from aiogram.types import Message

@router.callback_query(F.data == 'monoblocks')
async def check_balance_button(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserState.select_monoblocks)
    await callback.answer(text='Раздел моноблоков.')

    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text='Apple', callback_data='Apple'),
        types.InlineKeyboardButton(text='Windows', callback_data='Windows')
    )
    builder.row(
        types.InlineKeyboardButton(text='◀️назад', callback_data='back'),
    )
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())
