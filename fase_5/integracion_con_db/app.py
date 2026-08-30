from flask import Flask, jsonify, request
import storage
from psycopg2 import errors
app = Flask(__name__)
app.json.ensure_ascii = False

@app.route("/tareas",methods=["GET"])
def listar_tareas():
    orden = request.args.get('orden')
    completada = request.args.get('completada')
    direccion = request.args.get('direccion')
    try:
        lista_tareas = storage.listar_tareas(orden,direccion,completada)
        return lista_tareas,200
    except errors.Error as error:
        return jsonify({"error": f"{error}"}),500

@app.route("/tareas/<int:id>",methods=["GET"])
def traer_tarea(id):
    try:
        tarea = storage.traer_tarea(id)
        if tarea is None:
            return jsonify({"error": "La tarea no existe"}),404
        return tarea,200
    except errors.Error as error:
        return jsonify({"error": f"{error}"}),500

@app.route("/tareas",methods=["POST"])
def crear_tarea():
    respuesta = request.get_json()
    if not respuesta or "titulo" not in respuesta:
        return {"error": "Datos faltantes"},400
    try:
        nueva_tarea = storage.crear_tarea(respuesta)
        return jsonify(nueva_tarea),201
    except errors.Error as error:
        return jsonify({"error": f"{error}"}),500

@app.route("/tareas/<int:id>",methods=["PUT"])
def editar_tarea(id):
    respuesta = request.get_json()
    if not respuesta or "titulo" not in respuesta or "completada" not in respuesta:
        return {"error": "Datos faltantes"},400
    try:
        tarea_editada = storage.editar_tarea(id,respuesta)
        if tarea_editada is None:
            return {"error":"La tarea no existe"},404
        return jsonify(tarea_editada),200
    except errors.Error as error:
        return {"error":f"{error}"},500

@app.route("/tareas/<int:id>",methods=["DELETE"])
def eliminar_tarea(id):
    try:
        tarea_eliminada = storage.eliminar_tarea(id)
        if tarea_eliminada is None:
            return {"error":"La tarea no existe"},404
        return tarea_eliminada,204
    except errors.Error as error:
        return {"error":f"{error}"},500

@app.route("/tareas/stats",methods=["GET"])
def obtener_stats():
    try:
        stats = storage.obtener_stats()
        if stats is None:
            return {"error": "No existen tareas"},404
        return jsonify({
            "tareas" : stats[0],
            "tareas_completadas": stats[1],
            "tareas_pendientes": stats[2]
        }),200
    except errors.Error as error:
        return {"error":f"{error}"},500

if __name__ == "__main__":
    app.run(debug=True)
