from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import asyncio
from config.config_reader import config
from handlers.routes import router

async def main():
    bot = Bot(config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    dp.include_routers(
        router
    )

    await bot.delete_webhook(drop_pending_updates=True) #Удаляем накопленные сообщения, если бот был выкл, а его пытались использовать
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())