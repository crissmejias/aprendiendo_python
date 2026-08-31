from db import conectar_a_bd
from psycopg2 import errors

def crear_tabla():
    conn = None
    try:
        conn, cursor = conectar_a_bd("testing_tareas",False)
        sql ='''CREATE TABLE IF NOT EXISTS tareas (
                id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
                titulo text NOT NULL,
                completada boolean NOT NULL DEFAULT false,
                PRIMARY KEY(id)
            )'''
        cursor.execute(sql)
    except errors.OperationalError:
        print("Ocurrió un error en el servidor de bases de datos")
    finally:
        if conn:
            conn.commit()
            print("Se ha creado la tabla 'tareas'")
            conn.close()
def eliminar_tabla():
    conn = None
    try:
        conn,cursor = conectar_a_bd("testing_tareas",False)
        sql = '''DROP TABLE IF EXISTS tareas'''
        cursor.execute(sql)
    except errors.OperationalError:
        print("Ocurrió un error en el servidor de bases de datos")
    finally:
        if conn:
            conn.commit()
            print("Se ha eliminado la tabla 'tareas'")
            conn.close()

def alterar_tabla():
    conn = None
    try:
        conn, cursor = conectar_a_bd("testing_tareas",False)
        sql = '''ALTER TABLE tareas ADD COLUMN fecha_creacion TIMESTAMP DEFAULT NOW(),
        ADD CONSTRAINT titulo_no_vacio CHECK (titulo <> '')'''
        cursor.execute(sql)
        conn.commit()
        print("Se ha modificado la tabla 'tareas'")
    except errors.Error:
        print("Ocurrió un error en el servidor")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    alterar_tabla()
