"""
def insaneada():
    print("cashate xokas")

cien = list(range(1,101))

for i in cien:
    insaneada()

def sandrokas():
    nombre = input("¿Cómo te llamas?\n")
    hay = input("\nTienes dinero?\n")
    if hay.lower() == 'si':
        print("Hermano dame un poco que solo hay pan en casa jodir")
    else:
        print(f"Ponti a trabajar {nombre.title()} jodir")

sandrokas()
"""

"""
try:
    number_1 = int(input("Dime un número:\n"))
except ValueError:
    print("\nPon un número, por favor.\n")

try:
    number_2 = int(input("\nPon otro número, y así lo sumamos con el anterior:\n"))
except ValueError:
    print("Pon un número, por favor")
"""


"""
def sumardosnumeros():
    while True:
        try:
            pedir_num1 = int(input("Dime un número que quieras sumar con otro, luego te preguntaré el otro número:\n"))
        except ValueError:
            print("Pon un número, por favor")
        else:
            break

    while True:
        try:
            pedir_num2 = int(input("Dime el otro número:\n"))
        except ValueError:
            print("Pon un número, por favor")
        else:
            break

    suma = pedir_num1 + pedir_num2
    print(f"\nEl resultado es: {suma}")
"""

"""
def sumardosnumeros():
    while True:
        try:
            pedir_num1 = int(input("Dime un número que quieras sumar con otro, luego te preguntaré el otro número:\n"))
        except ValueError:
            print("Pon un número, por favor")
        else:
            break

    while True:
        try:
            pedir_num2 = int(input("Dime el otro número:\n"))
        except ValueError:
            print("Pon un número, por favor")
        else:
            break

    suma = pedir_num1 + pedir_num2
    print(f"\nEl resultado es: {suma}")

sumardosnumeros()
"""


"""
import json
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
"""



def count(s):
    lista_caracteres = {}
    for char in s:
        if char in lista_caracteres:
            lista_caracteres[char] += 1
        else:
            lista_caracteres[char] = 1
    return lista_caracteres

def max_sequence(arr):
    if not arr: 
        return 0
    
    suma_maxima = 0  
    suma_actual = 0

    for numero in arr:
        if numero > suma_actual + numero:
            suma_actual = numero
        else:
            suma_actual = suma_actual + numero
            
        if suma_actual > suma_maxima:
            suma_maxima = suma_actual

    return suma_maxima

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])

