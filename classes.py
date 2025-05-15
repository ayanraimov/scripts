
"""
class Restaurant():
    def __init__(self, name, ctype):
        self.name = name
        self.ctype = ctype

    def ask_howmany(self):
        print(f"Welcome to {self.name.title()}!\n")
        amount = int(input("How many people will you be?\n"))
        print(f"Total of people into the restaurant: {amount}")
    
    def cook(self):
        list_order = []
        while True:
            order = input("What do you want to order?\n")
            if order.lower() in ['no', 'q', 's', '', 'salir', 'quit']:
                break
            list_order.append(order)
        print(f"\n\nThe chief is cooking your order:\n")
        for meal in list_order:
            print(f"\t- {meal.title()}.")

kebab_amigo = Restaurant('Kebab Amigo', 'Kebab')
kebab_amigo.ask_howmany()
kebab_amigo.cook()

hamburgueseria = Restaurant('Hamburguesería La Amistad', 'Universal')
hamburgueseria.ask_howmany()
hamburgueseria.cook()

"""

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
    def increment_login_attempts(self, login_attempts):
        self.attempts += login_attempts
        print(f"Login attempts: {self.attempts}")
    def restart_attempts(self):
        self.attempts = 0
        print(f"Log in attempts: {self.attempts}")
        


daniil = User('daniil', 'kopach')
daniil.description()
daniil.greeting()
daniil.update_login_att(3)
daniil.increment_login_attempts(3)
daniil.increment_login_attempts(1)
daniil.restart_attempts()

class Admin(User):
    def __init__(self, f_name, l_name, has_privileges = True):
        super().__init__(f_name, l_name)
        self.privileges = privileges(has_privileges)
        
class privileges():
    def __init__(self, has_privileges = True):
        if not has_privileges:
            self.ban_users = False
            self.add_users = False
            print("This admin doesn't have admin's privileges yet.")
    def show_privileges(self):
        print(f"Here are the permits status of this user: \nBan Users: {self.ban_users}\nAdd Users: {self.add_users}")
    def set_privileges(self, has_privileges):  # Nuevo método para modificar privilegios
        self.ban_users = has_privileges
        self.add_users = has_privileges
        if not has_privileges:
            print("Privileges have been revoked.")
        else:
            print("Privileges have been granted.")

ayan = Admin('Ayan', 'Ronaldo', has_privileges=False)
ayan.description()
ayan.update_login_att(7)
ayan.increment_login_attempts(0)
ayan.privileges.show_privileges()
ayan.privileges.set_privileges(True)
ayan.privileges.show_privileges()