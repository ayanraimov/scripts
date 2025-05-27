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

def nombre_completo():
    while True:
        print("Para salir, pon 'q'\n")
        nombre = input("Dime tu nombre:\n")
        if nombre == 'q':
            break
        apellido = input("Dime tu apellido:\n")
        if apellido == 'q':
            break
        nombre_y_apellido = (f"{nombre.title()} {apellido.title()}")
        print(f"\nHola, {nombre_y_apellido}")
    
nombre_completo()


"""
conseguir_nombre_completo('ayan', 'reyhanov')

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
"""

def crear_artista(nombre, album_destacado, oyentes):
    info_artista = {'Nombre': nombre, 'Álbum destacado': album_destacado, 'Oyentes': oyentes}
    return info_artista
grupo_artistas = {}
grupo_artistas['Ejemplo'] = crear_artista('Ejemplo', 'Ejemplo', 7777777)


# PRIMERO
"""
def bienvenido(nombre):
    return f"Hola {nombre.title()}!"

nombres = ['ayan', 'daniil', 'teddy']

for nombre in nombres:
    print(bienvenido(nombre))

"""

# SEGUNDO
"""
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
"""

# Act 8-9
def nombres_magos(lista_nombres, lista_magos):
    for nombre in lista_nombres:
        lista_magos.append(nombre)
    for mago in lista_magos:
        print(f"The Great: {mago.title()}")
    
nombres = ['ayan', 'daniil', 'teddy']
magos_guapos = []

nombres_magos(nombres[:], magos_guapos)

def crear_sandwich():
    ingredientes = []
    pan = input("¿Qué tipo de pan quieres?\n")
    ingrediente1 = input("¿Qué quieres de primer ingrediente?\n")
    ingrediente2 = input("¿Qué quieres de segundo ingrediente?\n")
    ingredientes.append(pan)
    ingredientes.append(ingrediente1)
    ingredientes.append(ingrediente2)
    
    nuevos_ingredientes = []  # Lista fuera del bucle para no reiniciarla
    while True:
        nuevo_ingrediente = input("¿Quieres añadir algo más? Si es así, dime el qué (o 'no' para terminar):\n")
        if nuevo_ingrediente.lower() in ['no', 'q', 's', '', 'salir', 'quit']:
            break
        nuevos_ingredientes.append(nuevo_ingrediente)
    
    print("\n\nGracias por tu compra, los ingredientes que has seleccionado son los siguientes:\n")
    for ingrediente in ingredientes:
        print(ingrediente)
    for ingrediente in nuevos_ingredientes:
        print(ingrediente)


crear_sandwich()

from corrigiendo_al_libro import nombre_completo as full

full()

class cocinar():
    def __init__(self, username, name, last_name):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.login_attempts = 0
        print(f"Username: {self.username.lower()}\nName: {self.name.title()}\nLast name: {self.last_name.title()}")
    def login_attempts(self, attempts):
        self.login_attempts += attempts
    def reset_attempts(self):
        self.login_attempts = 0

class User():
    def __init__(self, f_name, l_name):
        self.name = f_name
        self.surname = l_name
        self.attempts = 0
    def description(self):
        print(f"First name: {self.name.title()} \nLast name: {self.surname.title()}")
        return f"First name: {self.name.title()} \nLast name: {self.surname.title()}"
    def greeting(self):
        full_name = f"{self.name.title()} {self.surname.title()}"
        greeting = f"Hello, {full_name}!"
        print(greeting)
        return greeting
    def update_login_att(self, att):
        if att >= self.attempts:
            self.attempts = att
        else:
            print("Qué digooo")
    def increment_login_att(self):
        self.attempts += 1
        print(f"Login attempts: {self.attempts}")
    def restart_attempts(self):
        self.attempts = 0
        print(f"Log in attempts: {self.attempts}")
        

class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privilegies = privilegies()
        
class privilegies():
    def __init__(self, prvlgs = True):
        if prvlgs == True:
            self.ban_users = True
            self.add_users = True
        else:
            self.ban_users = False
            self.add_users = False
            print("This admin doesn't have admin's privilegies yet.")
    def show_privilegies(self):
        print(f"Here are the permits status of this user: \nBan Users: {self.ban_users}\nAdd Users: {self.add_users}")

ayan = Admin('Ayan', 'Ronaldo')
ayan.description()
ayan.update_login_att(7)
ayan.increment_login_att()
ayan.privilegies.show_privilegies()

