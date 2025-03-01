from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import key_start
from handlers.routes import router
from aiogram.fsm.context import FSMContext

@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    builder_menu = key_start()

    await message.answer(
        "Привет, я - БОТан:",
             reply_markup=builder_menu.as_markup())

