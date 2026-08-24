from flask import Flask, jsonify,request

app = Flask(__name__)
app.json.ensure_ascii = False
tareas = [
    {"id": 1, "titulo": "Aprender Flask", "completada":False},
    {"id": 2, "titulo": "Conectar PostgreSQL", "completada":False}
]

@app.route("/tareas/<int:id>",methods=["DELETE"])
def eliminar_tarea(id):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas.pop(index)
            return "",204
    return {"error":"No se encontró la tarea solicitada"},404

@app.route("/tareas/<int:id>",methods=["PUT"])
def editar_tarea(id):
    datos = request.get_json()
    if not datos or "titulo" not in datos or "completada" not in datos:
        return {"error": "Hay un campo obligatorio faltante"},400
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["titulo"] = datos["titulo"]
            tarea["completada"] = datos["completada"]
            return tarea,200
    return {"error": "Tarea no encontrada"},404

@app.route("/tareas",methods=["POST"])
def crear_tarea():
    datos = request.get_json()
    if not datos or "titulo" not in datos:
        return jsonify({"error": "El campo 'titulo' es obligatorio"}),400
    nuevo_id = max([t["id"] for t in tareas],default=0) + 1
    nueva_tarea = {
        "id": nuevo_id,
        "titulo": datos["titulo"],
        "completada": datos.get("completada",False)
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea),201

@app.route("/tareas", methods=["GET"])
def obtener_tareas():
    return jsonify(tareas), 200

@app.route("/tareas/<int:id>",methods=["GET"])
def obtener_tarea(id):
    tarea = [tarea for tarea in tareas if tarea["id"] == id]
    if len(tarea) == 0:
        return jsonify({"error":"Tarea no encontrada"}), 404
    else:
        return jsonify(tarea[0]),200

if __name__ == "__main__":
    app.run(debug=True)

