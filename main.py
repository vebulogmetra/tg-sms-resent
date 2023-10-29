import logging

from aiogram import Bot, Dispatcher, executor, types
from dateutil import parser as dtparser

import service as utils_service
from permissions import AccessMiddleware
from settings import ADMIN_ID, BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(ADMIN_ID))
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply(
        "Бот для приёма и парсинга смс сообщений пересланных приложением на андроид"
    )


@dp.message_handler(commands="list")
async def cmd_start(message: types.Message):
    response_msgs: list[dict] = utils_service.get_expenses()
    answer_message = ""
    sum_all = 0
    for msg in response_msgs:
        # date_rus = datetime.strptime(, "%Y-%m-%d %H:%M:%S")
        date_rus = dtparser.parse(msg.get("created_at"))
        date_rus_str = date_rus.strftime("%Y-%m-%d %H:%M:%S")
        answer_message += f"{msg.get('bank')}, {msg.get('shop_name')}, {msg.get('summ')}, {date_rus_str}\n"
        sum_all += float(msg.get("summ"))
    # now_time = utils_service.get_now_moscow_time()
    # По дефолту результат за последние 3 дня
    # target_date = now_time - timedelta(days=3)
    await message.reply(answer_message)
    sum_all = round(sum_all, 2)
    await message.reply(f"Сумма: {sum_all}")


@dp.message_handler()
async def sms_text_message(message: types.Message):
    now_time = utils_service.get_now_moscow_time()
    if message.text.startswith("Покупка, карта *5489"):
        words_list = message.text.split(". ")
        bank = "tinkoff"
        # ['Покупка, карта *1234', '179.98 RUB', 'PEREKRESTO', 'Доступно 1019.49 RUB']
        db_data = {
            "bank": bank,
            "summ": utils_service.only_summ(input_text=words_list[1]),
            "shop_name": words_list[2],
            "remains": utils_service.only_summ(input_text=words_list[3]),
            "created_at": now_time,
            "raw_text": message.text,
        }
        print(f"db_data: {db_data}")
        utils_service.add_expense(db_data=db_data)
        await message.answer(f"Расход добавлен. ({bank} - {words_list[2]})")
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
