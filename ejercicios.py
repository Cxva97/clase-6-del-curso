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

################################################################################################################################
# Crear una nueva lista solo con números mayores a 20
# Ingresados por consola se piden 5
lista = []
for numero in range (1,6):
    numeros = int(input(f"Ingrese el numero {numero}: "))
    if numeros >= 20:
        lista.append(numeros)
print(lista)


################################################################################################################################

# En base a lista de notas
notas = [7,8.5,2,9]
nombre = ["Felipe","Carlos","Hector","Juan"]
#mostrar el mensaje el nombre su nota y si aprobo

for posicion in range (0,len(notas)):
    if notas[posicion] >= 7:
        estado = "aprobado"
    else:
        estado = "reprobado"
    print(f"El estudiante {nombre[posicion]} su nota es {notas[posicion]}, {estado}")


################################################################################################################################
#Simular que somos un sistema de inventario y registraremos 3 productos
# id,nombre,cantidad
# mostrar los productos con mas de 3 elementos
inventario = []
for elemento in range (3):
    id = input("ingrese el ID: ")
    nombre = input("ingrese el producto: ")
    cantidad = int(input("ingrese la cantidad: "))
    item = {
        "id" : id,
        "nombre" : nombre,
        "cantidad" : cantidad    
    }
    inventario.append(item)
print(inventario)

for item in inventario:
    if item["cantidad"] > 3:
        print(item["nombre"])

################################################################################################################################
