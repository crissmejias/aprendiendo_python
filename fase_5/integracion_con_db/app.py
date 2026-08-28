from flask import Flask, jsonify, request
from db import conectar_a_bd
from psycopg2 import errors
app = Flask(__name__)
app.json.ensure_ascii = False

@app.route("/tareas",methods=["GET"])
def listar_tareas():
    conn = None
    try:
        conn,cursor = conectar_a_bd("testing_tareas",False)
        sql = '''SELECT id,titulo,completada FROM tareas'''
        cursor.execute(sql)
        datos = cursor.fetchall()
        if len(datos) == 0:
            return [],200
        lista_tareas =[]
        for dato in datos:
            tarea_dict = {"id": dato[0], "titulo": dato[1], "completada": dato[2]}
            lista_tareas.append(tarea_dict)
        return jsonify(lista_tareas),200
    except errors.Error as error:
        return {"error": f"{error}" },500
    finally:
        if conn:
            conn.close()

@app.route("/tareas/<int:id>",methods=["GET"])
def traer_tarea(id):
    conn = None
    try:
        conn,cursor = conectar_a_bd("testing_tareas",False)
        sql='''SELECT id, titulo, completada FROM tareas WHERE id = %s'''
        cursor.execute(sql,(id,))
        datos = cursor.fetchone()
        if datos is None:
            return jsonify({"error":"La tarea no existe"}),404 
        tarea_dict = {
                      "id" : datos[0],
                      "titulo": datos[1],
                      "completada":datos[2]
                      }
        return jsonify(tarea_dict),200
    except errors.Error as error:
        return {"error":f"{error}"},500
    finally:
        if conn:
            conn.close()

@app.route("/tareas",methods=["POST"])
def crear_tarea():
    conn = None
    respuesta = request.get_json()
    if not respuesta or "titulo" not in respuesta:
        return {"error": "Datos faltantes"},400
    try:
        conn,cursor = conectar_a_bd("testing_tareas",False)
        sql = "INSERT INTO tareas (titulo) VALUES (%s) RETURNING id, titulo, completada"
        cursor.execute(sql,(respuesta["titulo"],))
        id,titulo,completada = cursor.fetchone()
        conn.commit()
        nueva_tarea = {"id": id, "titulo":titulo,"completada":completada}
        return jsonify(nueva_tarea),201
    except errors.Error as error:
        return {"error":f"{error}"},500
    finally:
        if conn:
            conn.close()

@app.route("/tareas/<int:id>",methods=["PUT"])
def editar_tarea(id):
    conn = None
    respuesta = request.get_json()
    if not respuesta or "titulo" not in respuesta or "completada" not in respuesta:
        return {"error": "Datos faltantes"},400
    try:
        conn, cursor = conectar_a_bd("testing_tareas",False)
        sql = "UPDATE tareas SET titulo = %s, completada = %s WHERE id = %s RETURNING id, titulo, completada"
        cursor.execute(sql,(respuesta["titulo"],bool(respuesta["completada"]),id))
        if cursor.rowcount == 0:
            return {"error":"La tarea no existe"},404
        id,titulo,completada = cursor.fetchone()
        nueva_tarea = {
            "id":id,
            "titulo":titulo,
            "completada":completada
        }
        conn.commit()
        return jsonify(nueva_tarea),200
    except errors.Error as error:
        return {"error":f"{error}"},500
    finally:
        if conn:
            conn.close()

@app.route("/tareas/<int:id>",methods=["DELETE"])
def eliminar_tarea(id):
    conn = None
    try:
        conn, cursor = conectar_a_bd("testing_tareas",False)
        sql = "DELETE FROM tareas WHERE id = %s"
        cursor.execute(sql,(id,))
        conn.commit()
        if cursor.rowcount == 0:
            return {"error":"La tarea no existe"},404
        return "",204
    except errors.Error as error:
        return {"error":f"{error}"},500
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run(debug=True)
