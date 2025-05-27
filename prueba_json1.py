import json

def get_stored_usernames():
    """Recupera la lista de nombres de usuario del archivo JSON."""
    filename = 'usernames.json'
    try:
        with open(filename) as f_obj:
            usernames = json.load(f_obj)
    except FileNotFoundError:
        return []
    else:
        return usernames

def add_new_username():
    """Pide un nuevo nombre y lo añade a la lista de usuarios."""
    username = input("What is your name? ")
    usernames = get_stored_usernames()
    if username not in usernames:  # Evita duplicados
        usernames.append(username)
        filename = 'usernames.json'
        with open(filename, 'w') as f_obj:
            json.dump(usernames, f_obj)
        print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}! You're already in our system.")
    return username

def greet_user():
    """Saluda al usuario y gestiona el almacenamiento."""
    username = input("What is your name? ")  # Pedimos el nombre primero
    usernames = get_stored_usernames()
    if username in usernames:
        print(f"Welcome back, {username}!")
    else:
        add_new_username()

greet_user()