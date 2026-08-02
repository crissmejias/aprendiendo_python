estudiantes = ["Ana", "Luis", "Camila"]
materias = ["Matemáticas", "Física"]

# Con dict comprehension anidado

estudiante_materias = {estudiante : {materia : 0 for materia in materias} for estudiante in estudiantes }


# Con for anidado 

# for e in estudiantes:
#     for m in materias:
#         estudiante_materias.setdefault(e,{}).setdefault(m,0)

print(estudiante_materias)
