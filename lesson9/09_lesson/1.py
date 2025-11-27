from sqlalchemy import create_engine
from DataBaseClass import StudentTable

db_connection_string = \
    "postgresql://postgres:YV1018sql@localhost:5432/python_db"

db = create_engine(db_connection_string)
