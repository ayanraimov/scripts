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