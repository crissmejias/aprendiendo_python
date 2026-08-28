from db import conectar_a_bd

def listar_tareas():
    conn = None
    try:
        conn,cursor = conectar_a_bd("testing_tareas",False)
        sql = '''SELECT id,titulo,completada FROM tareas'''
        cursor.execute(sql)
        datos = cursor.fetchall()
        lista_tareas =[]
        for dato in datos:
            tarea_dict = {"id": dato[0], 
                          "titulo": dato[1], 
                          "completada": dato[2]
                          }
            lista_tareas.append(tarea_dict)
        return lista_tareas
    finally:
        if conn:
            conn.close()

def traer_tarea(id):
    conn = None
    try:
        conn,cursor = conectar_a_bd("testing_tareas",False)
        sql='''SELECT id, titulo, completada FROM tareas WHERE id = %s'''
        cursor.execute(sql,(id,))
        datos = cursor.fetchone()
        if datos is None:
            return None
        tarea_dict = {
                      "id" : datos[0],
                      "titulo": datos[1],
                      "completada":datos[2]
                      }
        return tarea_dict
    finally:
        if conn:
            conn.close()

def crear_tarea(respuesta):
    conn = None
    try:
        conn,cursor = conectar_a_bd("testing_tareas",False)
        sql = "INSERT INTO tareas (titulo) VALUES (%s) RETURNING id, titulo, completada"
        cursor.execute(sql,(respuesta["titulo"],))
        id,titulo,completada = cursor.fetchone()
        conn.commit()
        nueva_tarea = {"id": id, "titulo":titulo,"completada":completada}
        return nueva_tarea
    finally:
        if conn:
            conn.close()

def editar_tarea(id,respuesta):
    conn = None
    try:
        conn, cursor = conectar_a_bd("testing_tareas",False)
        sql = "UPDATE tareas SET titulo = %s, completada = %s WHERE id = %s RETURNING id, titulo, completada"
        cursor.execute(sql,(respuesta["titulo"],bool(respuesta["completada"]),id))
        if cursor.rowcount == 0:
            return None
        id,titulo,completada = cursor.fetchone()
        tarea_editada = {
            "id":id,
            "titulo":titulo,
            "completada":completada
        }
        conn.commit()
        return tarea_editada
    finally:
        if conn:
            conn.close()

def eliminar_tarea(id):
    conn = None
    try:
        conn, cursor = conectar_a_bd("testing_tareas",False)
        sql = "DELETE FROM tareas WHERE id = %s"
        cursor.execute(sql,(id,))
        conn.commit()
        if cursor.rowcount == 0:
            return None
        return ""
    finally:
        if conn:
            conn.close()
