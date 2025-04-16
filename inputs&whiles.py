# Act 7-1
"""
coche_rent = input("¿Qué coche te interesa?\n")
print("Vale, veré si nos queda algún " + coche_rent + " para dejarte.")
"""

# Act 7-2
"""
asiento = int(input("\n¿Cuántos vais a comer?\n"))
if asiento > 8:
    print("Lo siento pero tendréis que esperar.")
else:
    print("Acompañadme.")
"""

# Act 7-3

"""
multiplokas_10 = ""
while multiplokas_10 != 'quit':
    multiplokas_10 = int(input("\nHola maestro dime un número y te diré si es múltiplo de 10.\n\tEscribe 'quit' sin las comillas para salir:\n"))
    if multiplokas_10 % 10 == 0:
        print("Sí es múltiplo de 10 crack")
    else:
        print("No es múltiplo de 10 cachorro.")
"""

nums_rango = list(range(1,31))
nums_impares = list()
nums_pares = list()
for num in nums_rango:
    if num % 2 == 0:
        nums_pares.append(num)
    else:
        nums_impares.append(num)

print(nums_impares)

total_suma = 0

for num in nums_impares:
    total_suma = total_suma + num
print (total_suma)


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print("xokas")


"""
activo = True
while activo == True:
    preguntokas = input("¿Tanga braga o nada?\n\t")
    if preguntokas == '':
        activo = False
        print("Pon algo euu")
    elif preguntokas == 'tanga':
        activo = False
        print("Puedes mostrar?")
    elif preguntokas == 'braga':
        activo = False
        print("Puedes mostrar?")
    elif preguntokas == 'nada':
        activo = False
        print("Puedes mostrar?")
    elif preguntokas == 'salir':
        activo = False
        print("Nos fuimooossss")
    elif preguntokas == 's':
        activo = False
        print("Nos fuimooossss")
    elif preguntokas == 'exit':
        activo = False
        print("Nos fuimooossss")
    elif preguntokas == 'quit':
        activo = False
        print("Nos fuimooossss")
    else:
        print(preguntokas)
"""


cesta_productos = []
cesta_cantidades = []
cesta = {cesta_productos: cesta_cantidades}
cliente_comprando = True
while cliente_comprando == True:
    producto = input("¿Qué quieres comprar?")
    if producto != 'salir' or 's' or 'exit' or 'quit' 'Nada' or 'Nada más':
        cesta_productos.append(producto)
        cantidad_producto = int(input("¿Cuántas unidades quieres?"))
        cesta_cantidades.append(cantidad_producto)
        print(producto)
    elif producto != 'salir' or 's' or 'exit' or 'quit' 'Nada' or 'Nada más':
        cliente_comprando = False
        print("Gracias por venir a comprar!")
print(cesta)