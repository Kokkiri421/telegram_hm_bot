from aiogram import types
from aiogram.dispatcher import FSMContext

from utils import TaskStateGroup, dp


@dp.message_handler(commands="select_task", state="*")
async def select_teacher(message: types.Message):
    await message.answer("Напишите фамилию учителя.")
    await TaskStateGroup.teacher.set()


@dp.message_handler(state=TaskStateGroup.teacher, content_types=types.ContentTypes.TEXT)
async def select_teacher2(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply("Пожалуйста, введите правильное имя учителя")
        return
    await state.update_data(teacher=message.text)
    await TaskStateGroup.next()
    await message.answer("Пожалуйста, выберите курс")


@dp.message_handler(state=TaskStateGroup.course, content_types=types.ContentTypes.TEXT)
async def select_course(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply("Пожалуйста, введите правильный курс")
        return
    await state.update_data(course=message.text)
    await TaskStateGroup.next()
    await message.answer("Выберите предмет")


@dp.message_handler(state=TaskStateGroup.subject, content_types=types.ContentTypes.TEXT)
async def select_subject(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply("Пожалуйста, введите правильный предмет")
        return
    await state.update_data(subject=message.text)
    await TaskStateGroup.next()
    await message.answer("Выберите тип задания")


@dp.message_handler(state=TaskStateGroup.type, content_types=types.ContentTypes.TEXT)
async def select_type(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply("Пожалуйста, введите правильный тип задания")
        return
    await state.update_data(type=message.text)
    user_data = await state.get_data()
    await message.answer(str(user_data))
    await state.finish()
