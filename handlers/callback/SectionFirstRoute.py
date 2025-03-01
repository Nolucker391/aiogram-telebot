from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.routes import router
from aiogram.fsm.context import FSMContext
from states import UserState
from aiogram.types import Message

@router.callback_query(F.data == 'first_block')
async def check_balance_button(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserState.first_section)
    await callback.answer(text='Вы выбрали раздел просмотра баланса скиллкоинов')
    await callback.message.edit_text(text='information-for-section')

    builder_for_first_button = InlineKeyboardBuilder()
    builder_for_first_button.add(
        types.InlineKeyboardButton(text='<< назад', callback_data='back'),
    )

    await callback.message.edit_reply_markup(reply_markup=builder_for_first_button.as_markup())


@router.message(UserState.first_section)
async def menu(message: Message, state: FSMContext):
    await message.delete()
    show_alert = True
    print("show_alert =", show_alert)
    await message.answer(text='Выберите действие из списка!', show_alert=True)
