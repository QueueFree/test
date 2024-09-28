from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
load_dotenv()

bot = Bot(os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

staff = [5512032771, ]
