from database import conn

TBLNAME = 'customers'

connection = conn()
cursor = connection.cursor()
cursor.execute(
    f"""
        CREATE TABLE IF NOT EXISTS {TBLNAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            phone TEXT
        )
    """
)
connection.commit()
connection.close()
