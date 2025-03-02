from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.routes import router
from aiogram.fsm.context import FSMContext
from states import UserState
from aiogram.types import Message

@router.callback_query(F.data == 'laptops')
async def check_laptops(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(previous_state=UserState.first_section)  # Сохраняем "Каталог" как предыдущее состояние
    await state.set_state(UserState.select_laptops)
    await callback.answer(text='Раздел ноутбуков.')

    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text='Apple', callback_data='Apple'),
        types.InlineKeyboardButton(text='Huawei', callback_data='Huawei')
    )
    builder.row(
        types.InlineKeyboardButton(text='Lenovo', callback_data='Lenovo'),
    )
    builder.row(
        types.InlineKeyboardButton(text='◀️назад', callback_data='back'),
    )
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())
