import requests

try:
    respuesta = requests.get("https://countries.dev/countries-no-existe",
                             params={"fields":"name,population,region"},
                             timeout=5)
    respuesta.raise_for_status()
    datos = respuesta.json()
except requests.exceptions.RequestException as error:
    print(f"No se pudieron obtener los datos, error: {error}")
    datos = []


