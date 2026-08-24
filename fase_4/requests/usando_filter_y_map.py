import requests

respuesta = requests.get("https://countries.dev/countries",params={"fields":"name,population,region"})

datos = respuesta.json()

datos_filtrados = list(filter(lambda paises : paises["region"] == "Americas",datos))

nombres_de_paises = list(map(lambda pais : pais["name"],datos_filtrados))
print(nombres_de_paises)
