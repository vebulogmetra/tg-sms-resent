from datetime import datetime
import pytz


def get_now_moscow_time():
    return datetime.now(pytz.timezone('Europe/Moscow'))
