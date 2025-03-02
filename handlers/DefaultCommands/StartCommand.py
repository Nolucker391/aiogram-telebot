from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.menu.main_menu import key_start
from handlers.routes import router
from aiogram.fsm.context import FSMContext

from states import UserState


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.update_data(previous_state=None)  # В главном меню нет "предыдущего"
    await state.set_state(UserState.start_section)  # Устанавливаем состояние "Главное меню"
    builder_menu = key_start()

    await message.answer(
        "Привет, я - БОТан:",
             reply_markup=builder_menu.as_markup())

