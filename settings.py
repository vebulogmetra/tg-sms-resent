import os

import dotenv

ENVFILE_PATH = os.path.join(".env")
dotenv.load_dotenv(ENVFILE_PATH)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = os.environ.get("ADMIN_ID")

EXPENSES_TABLE = "expense"
EXPENSES_TABLE_COLUMNS = ["bank", "summ", "shop_name", "created_at"]
