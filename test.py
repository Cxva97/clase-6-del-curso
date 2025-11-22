
"""
teniando la lista de diccionarios:
pida al usuario el ingrese de un codigo y borre de la lista dicho elemento.
"""
productos=[{
"id":1,
"nombre":"lapiz"
},{
"id":2,
"nombre":"cuadernos"
}
]

print(productos)

id = int(input("ingrese el id a eliminar: "))
for elemento in productos:
    if elemento["id"] == id:
        productos.remove(elemento)
        print("Elemento eliminado")
print(productos)