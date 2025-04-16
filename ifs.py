#Apuntes
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

bebida = 'cocacola'
bebida == 'COCACOLA'
bebida.upper() == 'COCACOLA'
if bebida.upper() == 'COCACOLA':
    print("Anashe")
else:
    print("Me parece un poco desubicado")

if bebida != 'cocacola':
    print("No se no se")
else:
    print("Boeeee")

# age = 19
# age < 21
# age <= 21
# age > 21
# age >= 21

# age_0 = 22 
# age_1 = 18 
# age_0 >= 21 and age_1 >= 21 
 

# age_1 = 22 
# age_0 >= 21 and age_1 >= 21 

# (age_0 >= 21) and (age_1 >= 21)

# age_0 = 22 
# age_1 = 18 
# age_0 >= 21 or age_1 >= 21 
 
# age_0 = 18 
# age_0 >= 21 or age_1 >= 21 

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# 'mushrooms' in requested_toppings
# 'pepperoni' in requested_toppings

lista_de_baneados = ['momo', 'El Ingeniero', 'Gerypad']
user = 'juanceto01'
if user not in lista_de_baneados:
    print(user.title() + ", vos sabes que vas ser el primer baneado?")
else:
    print("Te vas perma SabeSSSS")


#Act 5-1
equipo_ganador = 'Real Madrid'
print("¿El equipo ganador va a ser el Real Madrid? Yo digo que sí.")
print(equipo_ganador == 'Real Madrid')

print("\nEl equipo ganador será el Arsenal? Yo creo que no.")
print(equipo_ganador == 'Arsenal')

# Goat
# raza_teddy = ['Yorkshire']
# razas = raza_teddy[:]
# print(razas)

# pregunta_raza_perro = input("¿Cuál es la raza de tu perro? ")
# if pregunta_raza_perro == raza_teddy:
#     print("Anda! igual que el mío, pero seguro que el tuyo se porta mejor.")
# elif pregunta_raza_perro not in razas:
#     print("Ohh, debe ser encantador")
#     razas.append(pregunta_raza_perro)
# else:
#     print("Ahh, conozco esa raza, me gusta.")

# print(razas)


# edad_fiesta = int(input("¿Cuántos años tienes máquina? "))
# if edad_fiesta < 18:
#     print("Uff, aún eres chiquitín para entrar aquí, veulve caundo cumplas 18.")
# else:
#     print("Espero que disfrutes, entra.")

# altura_parque_acuatico = int(input("¿Cuánto mides? Dime tu altura en cms: "))
# if altura_parque_acuatico < 150:
#     print("Vaya, pues lo tendrás complicado para subirte a según qué atracciones.")
# elif altura_parque_acuatico < 160:
#     print("Creo que te podrás subir a casi todas las atracciones.")
# else:
#     print("No creo que tengas problemas para subirte a la atracción que te dé la gana.")

# Act 5-3; Act 5-4; Act 5-5
alien_color = ['green', 'yellow', 'red']
color_momo_alien = 'green'
color_virgo_alien = 'yellow'
color_detonado_alien = 'red'

if color_momo_alien == 'green':
    print("Acabas de ganar 5 puntos por virgo.")
elif color_momo_alien == 'yellow':
    print("Acabas de ganar 10 puntos por virgo.")
else:
    print("Te vas baneado por virgo.")

if color_virgo_alien == 'green':
    print("Acabas de ganar 5 puntos por virgo.")
elif color_virgo_alien == 'yellow':
    print("Acabas de ganar 10 puntos por virgo.")
else:
    print("Te vas baneado por virgo.")

if color_detonado_alien == 'green':
    print("Acabas de ganar 5 puntos por virgo.")
elif color_detonado_alien == 'yellow':
    print("Acabas de ganar 10 puntos por virgo.")
else:
    print("Te vas baneado por virgo.")

# Act 5-6
# etapa_de_vida = int(input("¿Qué edad tienes? "))
# if epa_de_vida < 2:
#     print("Bebesitaaa")
# elif etapa_de_vida < 4:
#     print("Uff nene lo siento si")
# elif etapa_de_vida < 13:
#     print("Eres un niño")
# elif etapa_de_vida < 20:
#     print("Eres un adolescente")
# elif etapa_de_vida < 65:
#     print("Eres un adulto")
# else:
#     print("Se ve que eres un tigre recto.")

# Act 5-7
# frutas_favs = ['kiwi', 'banana', 'piña', 'frambuesa', 'mango']
# adivina_fruta = input("Di una fruta y te diré si es de mis favoritas o no \n")
# if adivina_fruta in frutas_favs:
#     print("Has adivinado!")
# elif adivina_fruta not in frutas_favs:
#     print("No has acertado.")

# colores_frutas = ['verde', 'amarillo', 'naranja']
# adivina_color_fruta = input("Adivina el color de alguna de mis frutas favoritas: \n")
# if adivina_color_fruta in colores_frutas:
#     print("Lo has adivinado!")
# elif adivina_color_fruta == 'marron':
#     print("Casi, el marrón es el color de su piel.")
# else:
#     print("No has adivinado.")

ingredietes_disponibles = ['Queso Parmeggiano Reggiano', 'Jamón ibérico curado', 'Rúcula fresca', 'Champiñones', 'Yema de huevo', 'Pimiento troceado', "queso mozzarella",
    "queso cheddar",
    "queso gorgonzola",
    "pepperoni",
    "jamón york",
    "salchicha italiana",
    "pollo asado",
    "bacon",
    "champiñones",
    "pimientos verdes",
    "cebolla",
    "aceitunas negras",
    "tomates cherry",
    "espinacas",
    "albahaca fresca",
    "maíz",
    "anchoas",
    "piña"]

ingredientes_requeridos = ['Queso Parmeggiano Reggiano', 'Jamón ibérico curado', 'Rúcula fresca', 'Champiñones', 'Yema de huevo', 'Pimiento troceado', "queso mozzarella", 'Coca-Cola']

if ingredientes_requeridos:
    for ingrediente in ingredientes_requeridos:
        if ingrediente in ingredietes_disponibles:
            print("Añadiendo " + ingrediente + " a la pizza...")
        elif ingrediente not in ingredietes_disponibles:
            print("Lo siento, no podemos añadirle " + ingrediente + " a tu pizza ahora mismo.")
    print("\nTu pizza está lista!\n\n")
else:
    print("¿Estás seguro de que quieres una pizza sin nada?")

# Act 5-8
# usernames = ['ayan', 'admin', 'momo', 'teddy', 'joe']
# for username in usernames:
#     if username == 'admin':
#         print("Hola admin, quieres ver un reporte del estado de la empresa?")
#     else:
#         print("Hola " + username + ".")

# Act 5-9

# usuarios = []

# if usuarios:
#     for usuario in usuarios:
#         print("Hola " + usuario + ", recuerda que eres genial!")
#     print("\nSesión iniciada.")
# else:
#     print("No hay usuarios crack.")

# Act 5-10
usernames = ['ayan', 'admin', 'momo', 'teddy', 'joe']
new_usernames = ['cocodrilo bombardino', 'momo', 'gerypad', 'cristiano ronaldo', 'ayan']
# for username in new_usernames:
#     if username not in usernames:
#         print("Bienvenido, " + username + ".")
#         usernames.append(username.lower())
#     elif username in usernames:
#             elige_otro_usuario = input(username + " ya ha sido usado por otro usuario, por favor utiliza otro nombre que aún no haya sido usado: \n")
#             print(elige_otro_usuario)
#             if elige_otro_usuario not in usernames:
#                 for segundo_intento in elige_otro_usuario:
#                     print("Usuario creado con éxito. Bienvenido, "+ segundo_intento + ".")
#                     usernames.append(segundo_intento.lower)
#             elif elige_otro_usuario in usernames:
#                 for usuario_cogido in elige_otro_usuario:
#                     elige_otro_usuario = input(usuario_cogido + " ya ha sido usado por otro usuario, por favor utiliza otro nombre que aún no haya sido usado: \n")
#                     print(elige_otro_usuario)
#                     if elige_otro_usuario not in usernames:
#                         for tercer_intento in elige_otro_usuario:
#                             print("Usuario creado con éxito")
#                             usernames.append(tercer_intento.lower)
#                     elif elige_otro_usuario in usernames:
#                         for usuario_cogido_otravez in elige_otro_usuario:
#                             elige_otro_usuario = input(usuario_cogido_otravez + " ya ha sido usado por otro usuario, por favor utiliza otro nombre que aún no haya sido usado: \n")
#                             print(elige_otro_usuario)
#                             if elige_otro_usuario not in usernames:
#                                 for caurto_intento in elige_otro_usuario:
#                                     print("Usuario creado con éxito")
#                                     usernames.append(caurto_intento.lower)
#                             elif elige_otro_usuario in usernames:
#                                 for usuario_cogido_otravez in elige_otro_usuario:
#                                     print("Estás acabado.")
                        
# código corregido sin copiar
# usernames = ['ayan', 'admin', 'momo', 'teddy', 'joe']
# new_usernames = ['cocodrilo bombardino', 'momo', 'gerypad', 'cristiano ronaldo', 'ayan']
# for username in new_usernames:
#     if username.lower() not in usernames:
#         print("Bienvenido, " + username.lower() + ".")
#         usernames.append(username.lower())
#     elif username.lower() in usernames:
#             elige_otro_usuario = input(username.lower() + " ya ha sido usado por otro usuario, por favor utiliza otro nombre que aún no haya sido usado: \n")
#             if elige_otro_usuario.lower() not in usernames:
#                 print("Bienvenido, " + elige_otro_usuario.lower() + ".")
#                 usernames.append(elige_otro_usuario.lower())
#             else:
#                 print("Se te acabaron los intentos")
# print(usernames)

# Act 5-11
act_5_11 = list(range(1,10))
print(act_5_11)
for value in act_5_11:
    if value == 1:
        print("1st")
    elif value == 2:
        print("2nd")
    elif value == 3:
        print("3rd")
    else:
        print(str(value) + "th")

