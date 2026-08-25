import json

def cargar_tareas():
    try:
        with open("tareas.json", "r",encoding="utf-8") as f:
            tareas = json.load(f)
            return tareas
    except FileNotFoundError:
        with open("tareas.json", "x",encoding="utf-8") as f:
            nuevas_tareas = []
            json.dump(nuevas_tareas,f,indent=2)
            return nuevas_tareas

def guardar_tareas(tareas):
    with open("tareas.json","w",encoding="utf-8") as f:
        json.dump(tareas,f,indent=2)
