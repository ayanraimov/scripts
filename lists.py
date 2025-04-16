#Act 3-4
invitados = ['Fary', 'Cristiano Ronaldo', 'Muhammad Ali']
print("Hola " + invitados[0] + ", te mando este mensaje porque quisiera que vengas a mi cumpleaños.")
print("Hola " + invitados[1] + ", te mando este mensaje porque quisiera que vengas a mi cumpleaños.")
print("Hola " + invitados[2] + ", te mando este mensaje porque quisiera que vengas a mi cumpleaños.")
#Act 3-5
print("Hola, lamento informar que " + invitados[2] + " no podrá venir a la fiesta.")
invitados[2] = 'Diddy'
print("Hola " + invitados[0] + ", ¿Qué tal? Te quería comunicar que al final vendrá a la fiesta otra persona. Se llama " + invitados[2] + ", seguro que haréis buenas migas!")
print("Hola " + invitados[1] + ", ¿Qué tal? Te quería comunicar que al final vendrá a la fiesta otra persona. Se llama " + invitados[2] + ", seguro que haréis buenas migas!")
print("Hola " + invitados[2] + ", te mando este mensaje porque quisiera que vengas a mi cumpleaños.")
#Act 3-6
print("Hola " + invitados[0] + ", te escribo para comunicarte que he encontrado un sitio donde tendremos más espacio para celebrar la fiesta. Por tanto tendremos más invitados")
print("Hola " + invitados[1] + ", te escribo para comunicarte que he encontrado un sitio donde tendremos más espacio para celebrar la fiesta. Por tanto tendremos más invitados")
print("Hola " + invitados[2] + ", te escribo para comunicarte que he encontrado un sitio donde tendremos más espacio para celebrar la fiesta. Por tanto tendremos más invitados")
invitados.insert(3, 'Ilia Topuria')
invitados.insert(4, 'Gloosito')
invitados.append('Maloyski')
print(invitados)
print("Hola " + invitados[0] + ", te mando este mensaje para comunicarte que estás (o sigues) invitado a mi cumpleaños.")
print("Hola " + invitados[1] + ", te mando este mensaje para comunicarte que estás (o sigues) invitado a mi cumpleaños.")
print("Hola " + invitados[2] + ", te mando este mensaje para comunicarte que estás (o sigues) invitado a mi cumpleaños.")
print("Hola " + invitados[3] + ", te mando este mensaje para comunicarte que estás (o sigues) invitado a mi cumpleaños.")
print("Hola " + invitados[4] + ", te mando este mensaje para comunicarte que estás (o sigues) invitado a mi cumpleaños.")
#Act 3-7
print("Hola " + invitados[0] + ", te mando este mensaje para comunicarte que al final sólo podrán venir dos personas a mi cumpleaños.")
print("Hola " + invitados[1] + ", te mando este mensaje para comunicarte que al final sólo podrán venir dos personas a mi cumpleaños.")
print("Hola " + invitados[2] + ", te mando este mensaje para comunicarte que al final sólo podrán venir dos personas a mi cumpleaños.")
print("Hola " + invitados[3] + ", te mando este mensaje para comunicarte que al final sólo podrán venir dos personas a mi cumpleaños.")
print("Hola " + invitados[4] + ", te mando este mensaje para comunicarte que al final sólo podrán venir dos personas a mi cumpleaños.")
cocinados = invitados.pop()
print("Hola " + cocinados.title() + ", lo siento, pero al final no puedo traerte a la fiesta.")
cocinados = invitados.pop()
print("Hola " + cocinados.title() + ", lo siento, pero al final no puedo traerte a la fiesta.")
cocinados = invitados.pop()
print("Hola " + cocinados.title() + ", lo siento, pero al final no puedo traerte a la fiesta.")
print("Hola " + invitados[0] + ", eres de los únicos dos que podréis venir a la fiesta. Pasaremos un buen rato con " + invitados[1] + ", nos vemos pronto!")
print("Hola " + invitados[1] + ", eres de los únicos dos que podréis venir a la fiesta. Pasaremos un buen rato con " + invitados[0] + ", nos vemos pronto!")
del invitados[2]
del invitados[1]
del invitados[0]
print(invitados)
len(invitados)
#Act 3-8
lugares = ['Italia', 'Tailandia', 'Irlanda', 'Egipto', 'Cáucaso']
print(lugares)
print(sorted(lugares))
print(lugares)
lugares.reverse()
print(lugares)
lugares.reverse()
print(lugares)
lugares.sort()
print(lugares)
lugares.sort(reverse=True)
print(lugares)
#Act 3-9
print(len(invitados)) #(No hay nadie)
print(len(lugares))
#Act 3-10
baja_wacho = ['David', 'Daniil', 'Didi', 'Marc', 'Xisco', 'Ayan']
trespuntos = [baja_wacho[0], baja_wacho[1], baja_wacho[-1]]
print(trespuntos)
coches_voladores = [baja_wacho[0], baja_wacho[2], baja_wacho[3]]
print(coches_voladores)
print(sorted(coches_voladores))
baja_wacho.sort()
print(baja_wacho)
trespuntos.sort(reverse=True)
print(trespuntos)
for x in baja_wacho:
    print("Hola " + x + ".")
    print("¿Qué es de ti, " + x + "?\n")

for x in baja_wacho:
    print("Hola")

#Act 4-1
pizzas = ['Napoli', '4 quesos', 'Calzone']

for pizza in pizzas:
    print("La pizza " + pizza + " es de mis favoritas.")

print("\nMe gustan tanto las pizzas que este año iré a Italia!\n\n")

#Act 4-2
animales = ['Perro', 'Gato', 'Pez']

for animal in animales:
    print("El " + animal + " es muy bonito.")

print("\nSon todos muy guapos.")

#Prueba
# nums_elevados = []
# nums_a_elevar = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for elevacion in nums_a_elevar:
#     elevacion=elevacion**2
#     nums_elevados.append(elevacion)
#     print(elevacion)

# print(nums_elevados)

#Prueba 
rango_de_nums = list(range(1, 12))  # Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(rango_de_nums)  # Verificamos la lista

nums_impares = []  # Lista vacía para impares
nums_pares = []    # Lista vacía para pares

for num in rango_de_nums:  # Recorremos cada número
    if num % 2 == 0:       # Si el número es divisible entre 2 (par)
        nums_pares.append(num)
    else:                  # Si no es divisible entre 2 (impar)
        nums_impares.append(num)

print("Números pares: ", nums_pares)    # [2, 4, 6, 8, 10]
print("Números impares: ", nums_impares)  # [1, 3, 5, 7, 9, 11]


rango_impares = list(range(1,16,2))
print(rango_impares)


#Act 4-3
act4_3 = list(range(1,20))
for value in act4_3:
    print(value)

#Act 4-4
# act4_4 = list(range(1,1000000))
# for value in act4_4:
#     print(value)


#Act 4-5
act4_5 = list(range(1,1000000))

print(min(act4_5))
print(max(act4_5))
print(sum(act4_5))

#Act 4-6
act4_6 = list(range(1,20,2))
for value in act4_6:
    print(value)

#Act 4-7
act4_7 = list(range(3,31,3))
for value in act4_7:
    print(value)

#Act 4-8 y 4-9
numeros_elevados = []
numeros_a_elevar = list(range(1,11))
for cubo in numeros_a_elevar:
    cubo = cubo**3
    numeros_elevados.append(cubo)
    print(cubo)

#Act 4-10

print("The fist three items in the list are: ")
print(numeros_elevados[:3])

print("\nThree items in the middle of the list are: ")
print(numeros_elevados[4:7])

print("\nThe last three items in the list are: ")
print(numeros_elevados[-3:])


#Act 4-11
pizzas_amigo = pizzas[:]

pizzas_amigo.append('margarita')
pizzas.append('4 quesos')

for pizza in pizzas:
    print("\nMe gusta la " + pizza + ".")

for pizza in pizzas_amigo:
    print("\nA mi amigo le gusta la " + pizza + ".")

#Act 4-13
menu_buffet = ('maki', 'niguiri', 'pan de gamba', 'gyozas', 'sushi especial')
for platos in menu_buffet:
    print(platos)

#menu_buffet[2] = 'paella' #No funciona

menu_buffet = ('bocata lomo', 'paella', 'macarrones', 'mariscada', 'albondigas')
for platos in menu_buffet:
    print(platos)

#coña
crazy_question = input("If you had to choose between YoungBoy (1) and your girlfriend (2), who would you choose (1/2)? ")
if crazy_question == "1":
    print("YoungBoy! Fuck that bitch!")
else:
    print("Nahh I'm not real")

