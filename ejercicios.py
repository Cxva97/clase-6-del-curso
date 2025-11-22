# crea un diccionario con su informacion persona
# nombre, apellido, edad, hobbie
#imprimir nombre completo
#agregar estado civil por consola
# eliminar hobbie e imprimir

pers1 = {
    "nombre" : "cesar",
    "apellido" : "villacis",
    "edad" : 28,
    "hobbie": "programar"
}

print(f"tu nombre es {pers1['nombre']} {pers1['apellido']}")
estado_civil = input("agrega tu estado civil: ")
pers1["estado"] = estado_civil
del pers1["hobbie"]
print(pers1)