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

##########################################################################################
persona2 = {
    "nombre": "cesar",
    "apellido ": "Villacis",
    "edad" : 28
}
#iterar es trabajar con cada elemento de una variable estructurada

for valor in persona2: #por defecto tomas las llaves
    print(valor)

for valor in persona2.values(): #iterar valores de un diccionario
    print(valor)

for valor in persona2.keys(): #iterar keys de un diccionario
    print(valor)

for keys, values in persona2.items(): #itera a la vez key, values
    print(keys,values)

##################################################
#unir o variables mixtas
personas = [{
        "nombre": "cesar",
        "apellido": "Villacis"
    },
    {
        "nombre": "Xavier",
        "apellido": "Alvia"
    },
    {
        "nombre": "Gabriela",
        "apellido": "Arteaga"
    }
]

#este es el usuario 1 nombre apellido
# este es el usuario 2 nombre apellido

for persona in personas :
    print("El usuario", persona["nombre"], persona["apellido"])


usuario = {
    "nombre": "Cesar",
    "Apellido": "Villacis",
    "hobbie" : ["futbol","videojuegos","musica"],
    "titulos" : ["ingeniero de software","gamer"]
}

for llave, valor in usuario.items() :
    if llave == "hobbie" :
        for hobbie in valor :
            print(hobbie)
    elif llave == "titulos" :
        for titulo in valor :
            print(titulo)
    else:
        print(llave,valor)