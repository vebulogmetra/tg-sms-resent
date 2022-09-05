import pytz
import re
from datetime import datetime

from db import fetchall, insert


def get_now_moscow_time():
    return datetime.now(pytz.timezone('Europe/Moscow'))


def only_summ(input_text: str) -> str:
    reg = re.compile('[^0-9.]')
    return reg.sub('', input_text)


def add_expense(db_data: dict):
    insert(table="expense", column_values=db_data)


def get_expenses(conditions: list[str] = None):
    if not conditions:
        result = fetchall(table="expense")
