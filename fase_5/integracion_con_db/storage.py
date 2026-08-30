from db import conectar_a_bd

def listar_tareas(orden=None,direccion=None,completada=None):
    conn = None
    try:
        conn,cursor = conectar_a_bd("testing_tareas",False)
        columnas_validas = {"id","titulo"}
        direcciones ={"ASC","DESC"}
        sql = '''SELECT id,titulo,completada FROM tareas'''
        params = []
        condiciones = []
        if completada is not None:
            condiciones.append("completada = %s")
            params.append(completada)
        if condiciones:
            sql += " WHERE " + " AND ".join(condiciones)
        if direccion is not None:
            direccion = direccion.upper()
        if orden in columnas_validas and direccion in direcciones:
            sql += f" ORDER BY {orden} {direccion}"
        cursor.execute(sql,params)
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

def obtener_stats():
    conn = None
    try:
        conn, cursor = conectar_a_bd("testing_tareas",False)
        sql = '''
        SELECT 
            COUNT(*) AS total_tareas,
            COALESCE(SUM(CASE WHEN completada THEN 1 ELSE 0 END),0) AS completadas,
            COALESCE(SUM (CASE WHEN NOT completada THEN 1 ELSE 0 END),0) AS pendientes
        FROM tareas
        '''
        cursor.execute(sql)
        stats = cursor.fetchone()
        if stats is None:
            return None
        return stats
    finally:
        if conn:
            conn.close()
        
