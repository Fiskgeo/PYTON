import pytest
from sqlalchemy import create_engine
from DataBaseClass import TeacherTable
from sqlalchemy.orm import sessionmaker
db_connection_string = "postgresql://postgres:YV1018sql@localhost:5432/python_db"

db = create_engine(db_connection_string)
Session = sessionmaker(bind=db)
session = Session()

@pytest.fixture()
def db_connection():
    #db = create_engine(db_connection_string)
    #session = db.connect()
    transaction = session.begin()   # Начало транзакции
    yield session
    transaction.rollback()    # Откат изменений
    session.close()


def test_insert_and_delete_and_update(db_connection):
    repo = TeacherTable()
    initial_count = repo.get_count(db_connection)
    teacher_email = "new@gmail.com"
    new_teacher_email = "Updated@gmail.com"

    # Добавление
    repo.insert_teacher(db_connection, teacher_email)
    assert repo.get_count(db_connection) == initial_count + 1

    # Получение ID добавленного учителя
    teacher_id = repo.find_teacher_by_email(db_connection, teacher_email)
    assert teacher_id is not None

    # Изменение
    repo.update_teacher_email(db_connection, teacher_id, new_teacher_email)
    update_teacher = repo.get_teacher_by_id(db_connection, teacher_id)
    assert update_teacher.email == new_teacher_email

    # Удаление
    repo.delete_teacher(db_connection, new_teacher_email)
    assert repo.get_count(db_connection) == initial_count