from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from aiogram import Bot

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class TaskStateGroup(StatesGroup):
    teacher = State()
    course = State()
    subject = State()
    type = State()


class AddTeacherGroup(StatesGroup):
    full_name = State()
    telegram_id = State()


admin = State()
