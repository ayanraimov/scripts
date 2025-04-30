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
"""



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

# Mierdon
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
"""

"""
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
     break
    else:
        print("I'd love to go to " + city.title() + "!")
"""
# Act 7-4
"""
ingredientes = []
prompt = "\nDime qué ingrediente quieres añadirle a tu pizza:"
prompt += "\nPuedes salir poniendo 'salir'.\n"

mensaje = ""

while mensaje.lower() not in ['salir', 's', 'exit', 'quit', 'nada', 'nada más']:
    mensaje = input(prompt)
    if mensaje.lower() in ['salir', 's', 'exit', 'quit', 'nada', 'nada más']:
        print("Hasta la próxima!")
        break
    elif mensaje.strip() != "" and mensaje.isalpha() and mensaje not in ingredientes:
        ingredientes.append(mensaje)
        print(f"\nAñadiendo {mensaje.lower()} a tu pizza...\n")
    else:
        print("Por favor, añade un ingrediente que sea válido")



activo = True

while activo:
    confirmacion = input(f"Los ingredientes de tu pizza son los siguientes: {ingredientes}\n\t¿Quieres confirmar tu elección (s/n)?")

    if confirmacion.lower() == "s":
        print("Aquí tienes tu pizza!")
        activo = False
    elif confirmacion.lower() == "n":
        print("Es una pena, vuelve pronto!")
        activo = False
    else:
        print("Por favor, pon una respuesta válida.")
"""


# Act 7-5
"""
mensaje = int(input("Dime tu edad para determinar cuánto te va a costar la entrada:\n"))

if mensaje < 3:
    print("Tú entras gratis pequeñín!")
elif mensaje <= 12:
    print(" El tíquet te costaría 10€.")
elif mensaje > 12:
    print("El tíquet te costaría 15€.")
"""



# Act 7-6
"""
respuesta = ""
estado = True
while respuesta != 'quit':
    respuesta = input("¿Q pasa maquina?")
    if respuesta == 'quit':
        estado = False
        print("Adios!")
        break
    else:
        print("Dime 'quit' coño")
"""


# Act 7-7
"""
x = 10
while x != 0:
    print(x)
"""

"""
usuarios_no_verificados = ['David', 'Daniil', 'Didi', 'Marc', 'Xisco', 'Ayan']
usuarios_verificados = []

while usuarios_no_verificados:
    actual_usuario = usuarios_no_verificados.pop()
    print(f"Verificando a {actual_usuario}...")
    usuarios_verificados.append(actual_usuario)

print(f"\nAquí tienes la lista de los usuarios no verificados:\n\t{usuarios_no_verificados}")
print(f"\nY aquí tienes la lista de los usuarios verificados:\n\t{usuarios_verificados}")
"""

personas = {}

encuesta_activa = True



while encuesta_activa:
    nombre = input("¿Cómo te llamas?\n")
    edad = int(input("Qué edad tienes\n"))

    personas[nombre] = edad

    repetir = input("¿Quieres que otra persona responda?\n")
    if repetir.lower() == 'no':
        encuesta_activa = False

#print(f"Esta es la gente que ha participado en la encuesta y su edad: {personas}")

for nombre, edad in personas.items():
    print(f"{nombre.title()} tiene {edad} años.")