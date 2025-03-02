from aiogram.types import Message, FSInputFile, InputMediaPhoto
from aiogram.filters import CommandStart, Command
from keyboards.menu.main_menu import key_start
from handlers.routes import router
from aiogram.fsm.context import FSMContext

from states.states import UserState
from states.history_static import set_user_state

@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.update_data(history=[])  # Очищаем историю при старте
    await set_user_state(state, UserState.start_section)  # Сохраняем состояние

    builder_menu = key_start()
    file_path = "assets/images/menu.png"
    try:
        await message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(file_path),  # Новый путь к фото
                caption="Привет 👋, Я - <b>БОТ</b>ан.🤖\n"
                        "\n<b>Вы</b> - 💁‍♂️можете просматривать доступные товары, заполнять корзину и самое главное - приобрести интересующий <b>Вам</b> - продукт.⤵️️",
            ),
            reply_markup=builder_menu.as_markup()  # Обновленные кнопки (если нужны)
        )
    except Exception:
        await message.answer_photo(
            photo=FSInputFile(file_path),
            caption="Привет 👋, Я - <b>БОТ</b>ан.🤖\n"
                    "\n<b>Вы</b> - 💁‍♂️можете просматривать доступные товары, заполнять корзину и самое главное - приобрести интересующий <b>Вам</b> - продукт.⤵️️",
            reply_markup=builder_menu.as_markup()
        )




@router.message(Command("history"))
async def show_history(message: Message, state: FSMContext):
    data = await state.get_data()
    history = data.get("history", [])  # Получаем историю состояний

    print(history)
