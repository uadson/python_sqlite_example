from sqlite3 import connect
from settings import sqlset

def conn():
    return connect(sqlset.database)
