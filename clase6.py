# feedback
# variables estructuradas


#Listas ["Cesar",7,450.2]
# puede obtener info por posiciones [ordenadas]
#puede cambiar la info [mutables]


#tuplas ("Cesar",7,450.2) ordenadas pero no mutables
#set conjuntos {"Cesar",7,450.2} mutables pero no ordenadas , no permite elementos repetidos y simula operaciones matematicas
#se puede pasar entre estos tipos de datos

# lista = > conjunto o tupla
lista = [1,2,3,4]
set1 =set(lista) #convertir a conjunto
tupla = tuple (lista) # convertir a tupla
lista2 = list(set1) #convertir a lista

#crear una lista de frutas vamos 5 frutas por teclado y al final mostrar la lista a comprar

lista_frutas = []
for item in range (1,6):
    fruta = input("ingrese la fruta que desea: ") #creando la fruta
    lista_frutas.append(fruta)
print("estas son las frutas a comprar")
lista_final = list(set(lista_frutas))
print(lista_final)


# diccionarios
persona1 = ["cesar", "Villacis", "it", 28, 450.50, "0926032236"]
#son ordenados pero se ordena en base a una key o nombre guia
#son mutables
# {} se escriben con llaves
persona2 = {
    "nombre": "cesar",
    "apellido ": "Villacis",
    "edad" : 28
}
#agregar un valor
persona2["cedula"] = "0926032236"
persona2["sueldo"] = 450.50
print(persona2)

#leer valor
print(persona2["nombre"])
print(persona2.get("hobbie")) #esta forma no me da error 
print(persona2.get("Estado civil", "desconocido")) #puedo colocar un valor por defecto

#actualizar un valor
persona2["nombre"] = "xavier"
persona2.update({"edad" : 29})
print(persona2)

#borrar un valor
del persona2["sueldo"]
print(persona2)

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


#iterar es trabajar con cada elemento de una variable estructurada

for valor in persona2:
    print(valor)