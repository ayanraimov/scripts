"""
def activity():
    ask_number = int(input("Dime un número:\n"))
    print(f"{int(ask_number)} --> {str(ask_number)}")
    print(ask_number)
"""


"""
def activity():
    str_number = ""
    ask_number = int(input("Dime un número:\n"))
    if ask_number == int():
        ask_number = str_number
        ask_number = int()
        str_number = str()
    print(f"{ask_number} --> {str(str_number)}")
"""


# activity()
"""
def even_or_odd(number):
    if number % 2 == 0:
        return("Even")
    else:
        return("Odd")

even_or_odd(3)

even_or_odd(7)

even_or_odd(8)
"""

"""
# fail
lista = [1,2,2,3,3,3,4,3,3,3,2,2,1]
for number in lista:
    if len(number) % 2 != 0:
        print(number)
"""

"""
def multiply(a, b):
    print(a * b)

multiply(3, 7)
"""

def besico(persona1, persona2):
    print(f"{persona1.title()} y {persona2.title()} se besan.\n")

besico('macías', 'daniil')

personas = {}
def describir_persona(nombre, edad, estudia, trabaja, soltero):
    descripcion = {
        'nombre': nombre, 
        'edad': edad, 
        '¿Está estudiando?': estudia, 
        '¿Está trabajando?': trabaja, 
        '¿Está soltero?': soltero
        }
    return(descripcion)


grupo = {}
grupo['Ayan'] = describir_persona('Ayan', 19, True, True, True)
grupo['Daniil'] = describir_persona('Daniil', 18, True, False, True)
print(grupo)
