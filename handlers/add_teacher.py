from aiogram import types
from aiogram.dispatcher import FSMContext

from utils import dp, AddTeacherGroup, admin
from database import Session, Base, Teacher


@dp.message_handler(commands="add_teacher", state=admin)
async def add_teacher(message: types.Message):
    if True: #message.from_user.username
        await message.answer("Напишите полное имя учителя.")
        await AddTeacherGroup.full_name.set()
    return


@dp.message_handler(state=AddTeacherGroup.full_name, content_types=types.ContentTypes.TEXT)
async def teacher_name(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply("Пожалуйста, введите имя учителя")
        return
    await state.update_data(full_name=message.text)
    await AddTeacherGroup.next()
    await message.answer("Введите telegram-username (без @) преподавателя.")


@dp.message_handler(state=AddTeacherGroup.telegram_id, content_types=types.ContentTypes.TEXT)
async def select_type(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply("Пожалуйста, telegram-username (без @) преподавател.")
        return
    await state.update_data(telegram_id=message.text)
    teacher_data = await state.get_data()
    await message.answer(str(teacher_data))
    await state.finish()

'''
@dp.message_handler(state=AddTeacherGroup.full_name1, content_types=types.ContentTypes.TEXT)
async def add_teacher_db(message: types.Message):
    session = Session()
    teacher = Teacher(telegram_id=str(message.date), name='Федоров Иван')
    try:
        session.add(teacher)
        session.commit()
    except Exception as e:
        print('dssads')
    finally:
        session.close()
        result = session.query(Teacher).all()
        output = ''
        for i in result:
            output += i.name + ' ' + i.telegram_id + '\n'
        await message.reply(str(len(result)))
        await message.reply(output)

###################

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


'''

