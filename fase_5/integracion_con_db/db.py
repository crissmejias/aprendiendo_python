import psycopg2
import os
from dotenv import load_dotenv

def conectar_a_bd(bd,autocommit):
    load_dotenv()
    conn = psycopg2.connect(
    database=bd,
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST","localhost"),
    port="5432"
    )
    if autocommit:
        conn.autocommit = True
    cursor = conn.cursor()
    return conn,cursor

def crear_bd(nombre_bd):
    conn = None
    try:
        conn,cursor = conectar_a_bd("postgres",True)
        cursor.execute(f'''DROP DATABASE IF EXISTS {nombre_bd}''')
        sql= f'''CREATE DATABASE {nombre_bd}'''
        cursor.execute(sql)
        print(f"Se ha creado la base de datos '{nombre_bd}'")
    except psycopg2.errors.OperationalError:
        print("Hubo un problema con el servidor de bases de datos")
    except psycopg2.errors.ObjectInUse:
        print("La base de datos está en uso")
    finally:
        if conn:
            conn.close()

def borrar_bd(nombre_bd):
    conn = None
    try:
        conn,cursor = conectar_a_bd("postgres",True)
        sql= f'''DROP DATABASE IF EXISTS {nombre_bd}'''
        cursor.execute(sql)
        print(f"Se ha eliminado la base de datos '{nombre_bd}'")
    except psycopg2.errors.OperationalError:
        print("Hubo un error con el servidor de bases de datos")
    except psycopg2.errors.ObjectInUse:
        print("La base de datos está en uso")
    finally:
        if conn:
            conn.close()
if __name__ == "__main__":
    crear_bd("testing_tareas")

