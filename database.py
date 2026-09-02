import sqlite3

connection = sqlite3.connect("dbdreams.db")
connection.row_factory = sqlite3.Row

CREA_TABLA = """CREATE TABLE IF NOT EXISTS dreams (
    dream TEXT,
    fecha TEXT
);"""


def create_tables():
    with connection:
        connection.execute(CREA_TABLA)


def add_dream(dream, fecha):
    with connection:
        connection.execute(
            "INSERT INTO dreams (dream, fecha) VALUES (?, ?);",
            (dream, fecha)
        )


def get_dreams():
    cursor = connection.execute(
        "SELECT dream, fecha FROM dreams ORDER BY fecha DESC;"
    )
    return cursor.fetchall()


def buscar_dream_por_palabra(palabra_clave):
    cursor = connection.execute(
        "SELECT dream, fecha FROM dreams WHERE dream LIKE ?;",
        (f"%{palabra_clave}%",)
    )
    return cursor.fetchall()


def buscar_dream_por_fecha(fecha):
    cursor = connection.execute(
        "SELECT dream, fecha FROM dreams WHERE fecha = ?;",
        (fecha,)
    )
    return cursor.fetchall()


def close_connection():
    connection.close()
