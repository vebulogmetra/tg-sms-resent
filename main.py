import logging
from venv import create
from aiogram import Bot, Dispatcher, executor, types

from permissions import AccessMiddleware
from settings import BOT_TOKEN, ADMIN_ID
from service import get_now_moscow_time


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(ADMIN_ID))
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply("Бот для приёма и парсинга смс сообщений пересланных приложением на андроид")


@dp.message_handler()
async def sms_text_message(message: types.Message):
    now_time = get_now_moscow_time()
    if message.text.startswith("Покупка, карта *5489"):
        words_list = message.text.split(". ")
        # ['Покупка, карта *5489', '179.98 RUB', 'PEREKRESTO', 'Доступно 1019.49 RUB']
        db_data = {"bank": "tinkoff",
                   "summ": words_list[1],
                   "shop_name": words_list[2],
                   "remains": words_list[3],
                   "created_at": now_time}
    await message.answer(message.text)



if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)