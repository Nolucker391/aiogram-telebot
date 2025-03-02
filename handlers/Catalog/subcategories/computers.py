from aiogram import types, F
from aiogram.types import InputMediaPhoto, FSInputFile

from handlers.routes import router
from aiogram.fsm.context import FSMContext

from states.history_static import set_user_state
from states.states import UserState
from keyboards.catalog.sub_cat.ComputersBuilder import computer_builder

@router.callback_query(F.data == 'computers')
async def computer_selection(callback: types.CallbackQuery, state: FSMContext):
    builder = computer_builder()
    file_path = "assets/images/computers.png"

    await set_user_state(state, UserState.select_computer)
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(file_path),  # Новый путь к фото
            caption="Выберите интересующую модель.🪬"
        ),
        reply_markup=builder.as_markup()  # Обновленные кнопки (если нужны)
    )