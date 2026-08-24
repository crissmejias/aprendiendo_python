import requests

respuesta = requests.get("https://countries.dev/countries",params={"fields":"name,population,region"})
print(respuesta.status_code)

datos = respuesta.json()

datos_filtrados = [pais for pais in datos if pais["region"] == "Americas" and pais["population"] > 50_000_000 ]

for pais in datos_filtrados:
   print(f"{pais["name"]}: {pais["population"]} habitantes. Región: {pais["region"]}")

nuevo_filtro = [pais for pais in datos if pais["population"] < 1_000_000]

for n in nuevo_filtro:
    print(f"{n["name"]}, {n["region"]}: {n["population"]}")
print("--------------------------------------")
filtro_asia = [pais for pais in datos if pais["region"] == "Asia"]

for n in filtro_asia:
    print(f"{n["name"]}, {n["region"]}: {n["population"]}")

solo_nombres = [pais["name"] for pais in datos_filtrados]
print(solo_nombres)
