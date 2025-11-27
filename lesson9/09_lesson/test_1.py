import pytest
from sqlalchemy import create_engine
from sqlalchemy import inspect
from DataBaseClass import StudentTable

db_connection_string = "postgresql://postgres:YV1018sql@localhost:5432/python_db"

db = create_engine(db_connection_string)
def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'student' in names