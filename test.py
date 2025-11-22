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