import dotenv
import os


ENVFILE_PATH = os.path.join('.env')
dotenv.load_dotenv(ENVFILE_PATH)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = os.environ.get("ADMIN_ID")