from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.routes import router
from aiogram.fsm.context import FSMContext
from states import UserState
from aiogram.types import Message

@router.callback_query(F.data == 'first_block')
async def check_balance_button(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(previous_state=UserState.start_section)  # Сохраняем предыдущее состояние
    await state.set_state(UserState.first_section)  # Устанавливаем состояние "first_section"

    await callback.answer(text='Раздел покупки')
    await callback.message.edit_text(
        text='В данном разделе - <b>Вы</b>, можете ознакомиться с доступными товарами магазина.'
    )

    builder_for_first_button = InlineKeyboardBuilder()
    builder_for_first_button.row(
        types.InlineKeyboardButton(text='Ноутбуки', callback_data='laptops'),
        types.InlineKeyboardButton(text='Моноблоки', callback_data='monoblocks')
    )
    builder_for_first_button.row(
        types.InlineKeyboardButton(text='Компьютеры', callback_data='computers')
    )
    builder_for_first_button.row(
        types.InlineKeyboardButton(text='◀️назад', callback_data='back'),
    )

    await callback.message.edit_reply_markup(reply_markup=builder_for_first_button.as_markup())


# @router.message(UserState.first_section)
# async def menu(message: Message, state: FSMContext):
#     await message.delete()
#     await message.answer(text='Выберите действие из списка!', show_alert=True)
