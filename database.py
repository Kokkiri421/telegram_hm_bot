from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///bot.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String(255), unique=True)


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String(255), unique=True)
    name = Column(String(255))


class Type(Base):
    __tablename__ = "type"
    id = Column(Integer, primary_key=True)
    type = Column(String(255))


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    course = Column(Integer)
    subject = Column(String(255))
    type_id = Column(Integer, ForeignKey('type.id'))
    task_name = Column(String(255))

    UniqueConstraint(teacher_id,course,subject,type_id,task_name)


class File(Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('type.id'))

Base.metadata.create_all(engine)