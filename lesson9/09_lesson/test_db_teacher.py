import pytest
from sqlalchemy import create_engine, text
from DataBaseClass import TeacherTable
from sqlalchemy.orm import sessionmaker
import uuid

db_connection_string = "postgresql://postgres:YV1018sql@localhost:5432/python_db"


@pytest.fixture()
def db_connection():
    engine = create_engine(db_connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def generate_test_email():
    return f"test_{uuid.uuid4().hex}@gmail.com"


def test_insert_and_delete(db_connection):
    """Простой тест вставки и удаления"""
    repo = TeacherTable()

    # Сохраняем начальное состояние
    initial_count = repo.get_count(db_connection)
    test_email = generate_test_email()

    # Вставляем
    repo.insert_teacher(db_connection, test_email)
    assert repo.get_count(db_connection) == initial_count + 1

    # Удаляем
    repo.delete_teacher(db_connection, test_email)
    assert repo.get_count(db_connection) == initial_count


def test_insert_and_find(db_connection):
    """Тест вставки и поиска"""
    repo = TeacherTable()

    test_email = generate_test_email()

    # Вставляем
    repo.insert_teacher(db_connection, test_email, group_id=5)

    # Ищем
    teacher = repo.get_teacher_by_email(db_connection, test_email)
    assert teacher is not None
    assert teacher["email"] == test_email
    assert teacher["group_id"] == 5

    # Очищаем
    repo.delete_teacher(db_connection, test_email)


def test_update_email(db_connection):
    """Тест обновления email"""
    repo = TeacherTable()

    old_email = generate_test_email()
    new_email = generate_test_email()

    # Вставляем
    repo.insert_teacher(db_connection, old_email)

    # Обновляем
    repo.update_teacher_email(db_connection, old_email, new_email)

    # Проверяем обновление
    teacher = repo.get_teacher_by_email(db_connection, new_email)
    assert teacher is not None
    assert teacher["email"] == new_email

    # Старый email не должен находиться
    old_teacher = repo.get_teacher_by_email(db_connection, old_email)
    assert old_teacher is None

    # Очищаем
    repo.delete_teacher(db_connection, new_email)


def test_all_operations(db_connection):
    """Все операции в одном тесте"""
    repo = TeacherTable()

    initial_count = repo.get_count(db_connection)
    email1 = generate_test_email()
    email2 = generate_test_email()

    # 1. Вставка
    repo.insert_teacher(db_connection, email1, group_id=10)
    assert repo.get_count(db_connection) == initial_count + 1

    # 2. Поиск
    teacher = repo.get_teacher_by_email(db_connection, email1)
    assert teacher["email"] == email1
    assert teacher["group_id"] == 10

    # 3. Обновление
    repo.update_teacher_email(db_connection, email1, email2)
    updated_teacher = repo.get_teacher_by_email(db_connection, email2)
    assert updated_teacher["email"] == email2

    # 4. Удаление
    repo.delete_teacher(db_connection, email2)
    assert repo.get_count(db_connection) == initial_count