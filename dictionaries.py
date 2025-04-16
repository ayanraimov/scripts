# alien_0 = {'color': 'green', 'points': 5}

# print("You just earned " + str(alien_0['points']) + " points!")



# abecedariokas = {'a':0, 'b':0, 'c':0}
# abecedario2 = {'a':0}
# lista_abecedario = [abecedariokas, abecedario2]

#EJERCICIO ÉPICO
# pregunta = input("Pon lo que quieras: \n")
# for letra in pregunta:
#     if letra == 'a':
#         if abecedariokas['a'] <= 4:
#             abecedariokas['a'] = abecedariokas['a'] + 1
#             if abecedariokas['a'] > 4:
#                 abecedariokas['a'] = abecedariokas['a'] - 1
#                 abecedario2['a'] = abecedario2['a'] + 1
#     elif letra == 'b':
#         abecedariokas['b'] = abecedariokas['b'] + 1
#     elif letra == 'c':
#         abecedariokas['c'] = abecedariokas['c'] + 1

# print(lista_abecedario)


# def contar_letras(cadena):
#     diccionario = {}
#     for letra in cadena:
#         if letra in diccionario:
#             diccionario[letra] += 1
#         else:
#             diccionario[letra] = 1
#     return diccionario

# resultado = contar_letras(input("pon lo q quieras"))
# print(resultado)

# Act 6-1
perro_0 = {'raza':'Yorkshire', 'nombre': 'Teddy', 'edad': 4, 'color': 'negro', 'animado':True, 'fecha de nacimiento': '14/4/2020', 'comportamiento': 'bueno'}
print("Mi perro se llama " + perro_0['nombre'] + ".")
perro_0['edad'] = perro_0['edad'] + 1
print("Teddy tiene " + str(perro_0['edad']) + " años.")

if perro_0['comportamiento'] == 'bueno':
    print(perro_0['nombre'] + " se merece una galleta")
else:
    print(perro_0['nombre'] + " se queda sin juguete.")

# Act 6-2
# numeros_favoritos = {'daniil': 14, 'david': 13, 'marc': 8, 'ayan': 7}
# for nombre in numeros_favoritos:
#     print("El número favorito de " + nombre.title() + " es el " + str(numeros_favoritos[nombre]) + ".")

# Act 6-3
# for nombre in numeros_favoritos:
#     print(nombre.title() + ":\n" + str(numeros_favoritos[nombre]))

# for key, value in numeros_favoritos.items():
#     print("\nKey: " + key.title())
#     print("Value: " + str(value))

# for num in numeros_favoritos:
#     print("Hola " + num.title() + ", veo que tu número favorito es el " + str(numeros_favoritos[num]) + ".")


# lista_nums_favs = list()

# for num in set(numeros_favoritos.values()):
#     lista_nums_favs.append(num)

# print(lista_nums_favs)



# Act 6-5
# rivers = {'nile': 'egypt', 'danubio': 'bulgaria', 'amazonas': 'brazil'}

# for key, value in rivers.items():
#     print("The river " + key.title() + " runs through the country of " + value.title())

# for river in set(rivers.keys()):
#     print(river.title())

# for country in set(rivers.values()):
#     print(country.title())

# Act 6-6
numeros_favoritos = {'daniil': 14, 'david': 13, 'marc': 8, 'ayan': 7}
for key, value in numeros_favoritos.items():
    print("Hola " + key.title() + ", tu número favorito sigue siendo el " + str(value) + ", verdad?")

if 'didi' not in numeros_favoritos.keys():
    print("Hola Didi, dime tu número favorito")
else:
    print("Gracias por decirme tu número favorito!")

if 'xisco' not in numeros_favoritos.keys():
    print("Hola Xisco, dime tu número favorito")
else:
    print("Gracias por decirme tu número favorito!")

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
 
# Show the first 5 aliens:
for alien in aliens[:5]:
 print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

pizza_0 = {
    'masa': 'fina', 'extras': ['bacon', 'mozzarella'], 'base': 'queso de cabra', 'ingredientes base': ['pollo', 'champiñones']
}

print("Tu pizza tiene las siguientes características:\n\t" +  "Masa: " +  pizza_0['masa'] + "\n\tBase: " + pizza_0['base'] + "\n\tIngredientes principales: ")

for ingrediente in pizza_0['ingredientes base']:
    print("\t\t- " + ingrediente.title()) 
    
print("\n\tExtras: ")
for extra in pizza_0['extras']:
    print("\t\t- " + extra.title())

print("...\n¿Estás de acuerdo con tu elección?")

# daniil = {
#     'nombre': 'Daniil', 'apellido': 'Kopach', 'edad': 18, 'país': 'Ucrania'
# }
# marc = {
#     'nombre': 'Marc', 'apellido': 'Gómez', 'edad': 18, 'país': 'España'
# }
# david = {
#     'nombre': 'David', 'apellido': 'Macías', 'edad': 18, 'país': 'España'
# }
# xisco = {
#     'nombre': 'Francisco Javier', 'apellido': 'González', 'edad': 20, 'país': 'Holanda'
# }
# didi = {
#     'nombre': 'Didier', 'apellido': 'Nohad', 'edad': 18, 'país': 'Ecuador'
# }
# ayan = {
#     'nombre': 'Ayan', 'apellido': 'Reyhanov', 'edad': 19, 'país': 'Bulgaria'
# }

# users = {
#  'aeinstein': {
#  'first': 'albert',
#  'last': 'einstein',
#  'location': 'princeton',
#  },
#  'mcurie': {
#  'first': 'marie',
#  'last': 'curie',
#  'location': 'paris',
#  },
#  }


baja_wacho_baja = {
    'daniil': {
        'nombre': 'Daniil', 'apellido': 'Kopach', 'edad': 18, 'país': 'Ucrania',
    },
    'marc': {
        'nombre': 'Marc', 'apellido': 'Gómez', 'edad': 18, 'país': 'España',
    },
    'david': {
        'nombre': 'David', 'apellido': 'Macías', 'edad': 18, 'país': 'España',
    },
    'xisco': {
        'nombre': 'Francisco Javier', 'apellido': 'González', 'edad': 20, 'país': 'Holanda',
    },
    'didi': {
        'nombre': 'Didier', 'apellido': 'Nohad', 'edad': 18, 'país': 'Ecuador',
    },
    'ayan': {
        'nombre': 'Ayan', 'apellido': 'Reyhanov', 'edad': 19, 'país': 'Bulgaria',
    },
}


for persona, infopersona in baja_wacho_baja.items():
    print("\nUsuario: " + persona)
    nombre_completo = infopersona['nombre'] + " " + infopersona['apellido']
    print("Nombre completo: " + nombre_completo)

pincho = int(input("Sicrack:\n"))