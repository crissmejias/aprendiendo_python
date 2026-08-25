from flask import Flask, request, jsonify
from storage import cargar_tareas,guardar_tareas
app = Flask(__name__)
app.json.ensure_ascii = False

@app.route("/tareas",methods=["GET"])
def listar_tareas():
    tareas = cargar_tareas()
    return jsonify(tareas),200

@app.route("/tareas/<int:id>",methods=["GET"])
def listar_tarea(id):
    tareas = cargar_tareas()
    for tarea in tareas:
        if  tarea["id"] == id:
            return tarea,200
    return {"error":"Tarea no encontrada"},404

@app.route("/tareas",methods=["POST"])
def crear_tarea():
    datos = request.get_json()
    if not datos or "titulo" not in datos:
        return {"error":"Información faltante"},400
    tareas = cargar_tareas()
    nuevo_id = max([tarea["id"] for tarea in tareas],default=0) + 1
    nueva_tarea = {"id":  nuevo_id, "titulo": datos["titulo"],"completada":False}
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    return nueva_tarea,201

@app.route("/tareas/<int:id>",methods=["PUT"])
def editar_tarea(id):
    datos = request.get_json()
    if not datos or "titulo" not in datos or "completada" not in datos:
        return {"error":"Datos faltantes"},400
    tareas = cargar_tareas()
    for index,tarea in enumerate(tareas):
        if tarea["id"] == id:
            tarea["titulo"] = datos["titulo"]
            tarea["completada"] = datos["completada"]
            tareas[index] = tarea
            guardar_tareas(tareas)
            return tarea,200
    return {"error":"Tarea no encontrada"},404

@app.route("/tareas/<int:id>",methods=["DELETE"])
def eliminar_tarea(id):
    tareas = cargar_tareas()
    for index,tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas.pop(index)
            guardar_tareas(tareas)
            return "",204
    return {"error": "Tarea no encontrada"},404

if __name__ == "__main__":
    app.run(debug=True)
