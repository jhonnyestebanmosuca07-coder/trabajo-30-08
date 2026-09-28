import sqlite3

DATABASE_NAME = 'sistema_aprendices.db'

def obtener_conexion():
    conexion = sqlite3.connect(DATABASE_NAME)
    conexion.row_factory = sqlite3.Row
    return conexion

def inicializar_db():
    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS aprendiz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        documento TEXT UNIQUE NOT NULL,
        programa TEXT NOT NULL
    )
        """)
        conexion.commit()