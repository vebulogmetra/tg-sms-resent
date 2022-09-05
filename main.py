import logging
import pytz
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

from permissions import AccessMiddleware
from settings import BOT_TOKEN, ADMIN_ID


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(ADMIN_ID))
logging.basicConfig(level=logging.INFO)





@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply("Бот для приёма и парсинга смс сообщений пересланных приложением на андроид")


@dp.message_handler()
async def sms_text_message(message: types.Message):
    if message.text.startswith("Покупка, карта *5489"):
        bank = "tinkoff"
        words_list = message.text.split(". ")
        # ['Покупка, карта *5489', '179.98 RUB', 'PEREKRESTO', 'Доступно 1019.49 RUB']
        summ = words_list[1]
        shop_name = words_list[2]
        remains = words_list[3]
    await message.answer(message.text)



if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)