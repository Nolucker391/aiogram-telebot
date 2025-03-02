from aiogram import F
from aiogram.types import CallbackQuery

from handlers.DefaultCommands.StartCommand import start_command
from handlers.Catalog.categories import check_balance_button
from keyboards.menu.main_menu import key_start
from handlers.routes import router
from aiogram.fsm.context import FSMContext
from handlers.Catalog.subcategories.laptops import check_laptops

from states import UserState


@router.callback_query(F.data == 'back')
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    previous_state = user_data.get('previous_state', UserState.start_section)  # Достаем предыдущее состояние

    if previous_state == UserState.start_section:
        await start_command(callback.message, state)  # Возвращаем в главное меню
    elif previous_state == UserState.first_section:
        await check_balance_button(callback, state)  # Возвращаем в каталог
    elif previous_state == UserState.select_laptops:
        await check_laptops(callback, state)  # Возвращаем в ноутбуки

    await state.set_state(previous_state)  # Восст

    builder_menu = key_start()
    print(state)
    await callback.answer(text='Вы вернулись в главное меню.')

    await callback.message.edit_text(text="Привет, я - БОТан:")

    await callback.message.edit_reply_markup(reply_markup=builder_menu.as_markup())

