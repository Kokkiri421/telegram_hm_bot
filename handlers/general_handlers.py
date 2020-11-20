from aiogram import types
from aiogram.types import ContentType
from utils import dp, bot, admin
from database import Session, Base, Teacher
from config import PASSWORD


@dp.message_handler(state='*', commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(str(message))


@dp.message_handler(state='*', commands='admin')
async def set_admin_state(message: types.Message):
    if str(message.text.split()[-1]) == PASSWORD:
        await admin.set()
        await message.answer('Ого, да вы админ!')
    return


@dp.message_handler(content_types=[ContentType.PHOTO, ContentType.DOCUMENT])
async def send_file(message: types.Message):
    if message['photo']:
        await bot.send_photo(message.chat.id, message.photo[2].file_id)
    if message['document']:
        await bot.send_document(message.chat.id, message.document.file_id)

