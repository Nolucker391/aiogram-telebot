from aiogram import types, F
from aiogram.types import CallbackQuery

from keyboards import key_start
from handlers.routes import router
from aiogram.fsm.context import FSMContext

@router.callback_query(F.data == 'back')
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    builder_menu = key_start()
    await callback.answer(text='Вы вернулись в главное меню.')

    await callback.message.edit_text(text="Привет, я - БОТан:")

    await callback.message.edit_reply_markup(reply_markup=builder_menu.as_markup())

