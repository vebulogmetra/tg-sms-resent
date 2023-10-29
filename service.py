import re
from datetime import datetime

import pytz

from db import fetch_where, fetchall, insert
from settings import EXPENSES_TABLE, EXPENSES_TABLE_COLUMNS


def get_now_moscow_time():
    return datetime.now(pytz.timezone("Europe/Moscow"))


def only_summ(input_text: str) -> str:
    reg = re.compile("[^0-9.]")
    return reg.sub("", input_text)


def add_expense(db_data: dict):
    insert(table=EXPENSES_TABLE, column_values=db_data)


def get_expenses(conditions: list[str] = None, limit: int = None):
    if not conditions:
        result = fetchall(table=EXPENSES_TABLE, columns=EXPENSES_TABLE_COLUMNS)
    else:
        print(f"condition_select: {conditions[0]}")
        result = fetch_where(
            table=EXPENSES_TABLE,
            columns=EXPENSES_TABLE_COLUMNS,
            condition_select=conditions[0],
        )
    return result
