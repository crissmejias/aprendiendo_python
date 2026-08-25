# API de Tareas — Flask

API REST simple para gestionar una lista de tareas, construida con Flask como proyecto de práctica (día 2 aprendiendo Flask). Implementa un CRUD completo con persistencia en un archivo JSON.

## Estructura del proyecto

```
empezando_con_flask/
├── app.py          # Rutas de la API
├── storage.py       # Capa de persistencia (lectura/escritura de tareas.json)
├── tareas.json       # "Base de datos" en archivo JSON (se crea automáticamente)
└── venv/
```

## Características

- CRUD completo sobre el recurso `tareas`: crear, listar, obtener una, editar y eliminar.
- Persistencia en disco mediante un archivo `tareas.json`, leído en cada request.
- Capa de persistencia separada de las rutas (`storage.py`), lo que permite reemplazar el archivo JSON por una base de datos real (ej. PostgreSQL) sin tocar la lógica de las rutas.
- Manejo de errores: validación de campos obligatorios, tareas no encontradas, y creación automática del archivo `tareas.json` si no existe.
- Códigos de estado HTTP correctos en cada respuesta (200, 201, 204, 400, 404).

## Endpoints

| Método | Ruta            | Descripción                          | Código de éxito |
|--------|-----------------|---------------------------------------|------------------|
| GET    | `/tareas`       | Lista todas las tareas                | 200              |
| GET    | `/tareas/<id>`  | Obtiene una tarea por id              | 200 / 404        |
| POST   | `/tareas`       | Crea una tarea nueva                  | 201 / 400        |
| PUT    | `/tareas/<id>`  | Edita una tarea existente             | 200 / 400 / 404  |
| DELETE | `/tareas/<id>`  | Elimina una tarea                     | 204 / 404        |

### Formato de una tarea

```json
{
  "id": 1,
  "titulo": "Practicando Flask",
  "completada": false
}
```

### Ejemplo — crear una tarea (POST /tareas)

Body de la petición:

```json
{
  "titulo": "Aprender SQL"
}
```

Respuesta (201):

```json
{
  "id": 3,
  "titulo": "Aprender SQL",
  "completada": false
}
```

### Ejemplo — editar una tarea (PUT /tareas/1)

Body de la petición:

```json
{
  "titulo": "Aprender SQL",
  "completada": true
}
```

## Cómo correr el proyecto

```bash
python -m venv venv
source venv/bin/activate
pip install flask
python app.py
```

La API queda disponible en `http://127.0.0.1:5000`.

## Cómo funciona la persistencia (`storage.py`)

- **`cargar_tareas()`**: lee `tareas.json`. Si el archivo no existe todavía (primera ejecución), lo crea con una lista vacía y la devuelve, en vez de fallar.
- **`guardar_tareas(tareas)`**: sobreescribe `tareas.json` con la lista de tareas actualizada.

Cada ruta llama a estas dos funciones en vez de manejar archivos directamente, lo que mantiene `app.py` enfocado solo en la lógica de cada endpoint (validación de datos, búsqueda de la tarea, código de estado a devolver).

## Historial de desarrollo

Este proyecto se hizo dos veces:

1. Primera versión: CRUD funcionando en memoria (la lista de tareas se perdía al reiniciar el servidor).
2. Segunda versión (esta, desde cero y sin ayuda): mismo CRUD + persistencia en archivo JSON + capa de almacenamiento separada, para practicar manejo de archivos en Python y buenas prácticas de organización de código.

## Próximos pasos

Migrar `storage.py` para que use PostgreSQL con SQL crudo en vez de un archivo JSON, manteniendo la misma interfaz (`cargar_tareas`, `guardar_tareas`) para que las rutas en `app.py` no necesiten cambios.
