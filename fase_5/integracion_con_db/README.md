# API de Tareas — Flask + PostgreSQL + Docker

API REST para gestión de tareas, construida con Flask y SQL crudo sobre PostgreSQL (sin ORM), completamente dockerizada para desarrollo.

## Tecnologías

- **Python 3.13** + **Flask**
- **PostgreSQL 16**
- **psycopg2** (conexión y queries SQL crudo)
- **Docker** + **docker-compose**

## Estructura del proyecto

```
.
├── app.py              # Rutas de la API (capa HTTP)
├── storage.py           # Lógica de acceso a datos (queries SQL)
├── db.py                # Conexión a PostgreSQL
├── schema.py             # Script de creación de tabla/esquema
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── .env                 # Variables de entorno (no versionado)
```

## Requisitos previos

- Docker y el plugin de Compose (`docker compose`, con espacio — no el binario standalone `docker-compose`)

## Configuración

Crea un archivo `.env` en la raíz del proyecto con:

```
DB_PASSWORD=tu_clave_aqui
```

Este valor se usa tanto para levantar el contenedor de PostgreSQL como para que la API se autentique contra él.

## Levantar el proyecto

```bash
docker compose up --build
```

Esto levanta dos servicios:

| Servicio | Descripción | Puerto |
|---|---|---|
| `db` | PostgreSQL 16, con volumen persistente `datos_postgres` | `5432` |
| `api` | La API de Flask, en modo debug con auto-reload | `5000` |

El servicio `api` espera a que `db` esté realmente listo para aceptar conexiones (vía `healthcheck` con `pg_isready`) antes de arrancar — no solo a que el contenedor exista.

### Primera vez: crear la base de datos y la tabla

Si el volumen de Postgres es nuevo, hay que crear la base y la tabla manualmente la primera vez:

```bash
docker exec -it postgres_db psql -U postgres -c "CREATE DATABASE testing_tareas;"
docker compose exec api python3 schema.py
```

### Desarrollo en vivo

El código local está montado como volumen dentro del contenedor `api` (`.:/app`), así que los cambios que hagas en tu editor se reflejan de inmediato — Flask detecta el cambio y recarga solo, sin necesidad de reconstruir la imagen.

## Variables de entorno

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `DB_PASSWORD` | Contraseña del usuario `postgres` | — (requerida) |
| `DB_HOST` | Host de conexión a la base de datos | `localhost` (se sobreescribe a `db` dentro de docker-compose) |

## Endpoints

### `GET /tareas`

Lista tareas, con filtros y ordenamiento opcionales vía query params.

| Query param | Descripción | Valores válidos |
|---|---|---|
| `completada` | Filtra por estado | `true` / `false` |
| `orden` | Columna para ordenar | `id`, `titulo`, `fecha_creacion` |
| `direccion` | Dirección del orden | `ASC`, `DESC` (insensible a mayúsculas) |
| `fecha_inicio` | Fecha mínima de creación (inclusive) | `YYYY-MM-DD` |
| `fecha_fin` | Fecha máxima de creación (inclusive, incluye el día completo) | `YYYY-MM-DD` |

Ejemplo:
```
GET /tareas?completada=false&orden=fecha_creacion&direccion=DESC&fecha_inicio=2026-08-25&fecha_fin=2026-08-30
```

Respuesta `200`:
```json
[
  {
    "id": 1,
    "titulo": "Tarea nueva",
    "completada": false,
    "fecha_creacion": "Mon, 31 Aug 2026 02:28:40 GMT"
  }
]
```

### `GET /tareas/<id>`

Devuelve una tarea por id.

- `200` con la tarea si existe.
- `404` con `{"error": "La tarea no existe"}` si no.

### `POST /tareas`

Crea una tarea nueva. Body requerido:
```json
{ "titulo": "Nombre de la tarea" }
```

- `201` con la tarea creada.
- `400` con `{"error": "Datos faltantes"}` si falta `titulo`.
- `completada` se inicializa en `false` y `fecha_creacion` toma la fecha/hora actual automáticamente.

### `PUT /tareas/<id>`

Edita una tarea existente. Body requerido:
```json
{ "titulo": "Nuevo título", "completada": true }
```

- `200` con la tarea editada.
- `400` si falta `titulo` o `completada`.
- `404` si el id no existe.

### `DELETE /tareas/<id>`

Elimina una tarea.

- `204` si se eliminó correctamente.
- `404` si el id no existe.

### `GET /tareas/stats`

Devuelve conteos agregados.

```json
{
  "tareas": 44,
  "tareas_completadas": 12,
  "tareas_pendientes": 32
}
```

## Esquema de la tabla `tareas`

| Columna | Tipo | Restricciones |
|---|---|---|
| `id` | `integer` | `PRIMARY KEY` |
| `titulo` | `text` | `NOT NULL`, `CHECK (titulo <> '')` |
| `completada` | `boolean` | default `false` |
| `fecha_creacion` | `timestamp` | default `NOW()` |

## Notas de diseño

- Las queries usan SQL crudo (sin ORM) con parámetros vía `%s` para evitar SQL injection en filtros normales.
- `orden` y `direccion` se validan contra listas blancas (`{"id", "titulo", "fecha_creacion"}` y `{"ASC", "DESC"}`) antes de interpolarse en el `ORDER BY`, ya que esa cláusula no acepta parámetros `%s`.
- El filtro `fecha_fin` usa `< %s::date + INTERVAL '1 day'` en vez de un cast sobre la columna (`fecha_creacion::date <= ...`), para mantener la condición sargable y aprovechable por un futuro índice sobre `fecha_creacion`.
- `SUM(...)` en `/tareas/stats` está envuelto en `COALESCE(..., 0)` porque `SUM` devuelve `NULL` (no `0`) cuando no hay filas que sumar.

## Comandos útiles de Docker

| Acción | Comando |
|---|---|
| Levantar todo | `docker compose up --build` |
| Detener | `docker compose down` |
| Ver logs en vivo | `docker compose logs -f` |
| Ejecutar un comando dentro de `api` | `docker compose exec api <comando>` |
| Entrar a `psql` dentro de `db` | `docker exec -it postgres_db psql -U postgres` |

## Pendiente / roadmap

- Proyecto B: carga de datos masivos con Faker e índices, comparando planes de ejecución con `EXPLAIN ANALYZE`.
- Manejo más específico de errores de restricciones de base de datos (ej. `CHECK`) con respuestas `400` en vez de `500` genérico.
- Validación de formato de fechas en query params antes de llegar a la base de datos.
- Revisión de principios SOLID / clean code sobre el código actual (candidato ya identificado: la función de `GET /tareas` es extensa y podría segmentarse).