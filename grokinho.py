# Inicializa estructuras
productos = []
cantidades = []

# Bucle para pedir datos
cliente_comprando = True
while cliente_comprando:
    producto = input("¿Qué quieres comprar?\n")
    if producto.lower() in ['salir', 's', 'exit', 'quit', 'nada', 'nada más']:
        cliente_comprando = False
        print("Gracias por venir a comprar!")
    else:
        # Valida y pide cantidad
        while True:
            entrada = input("¿Cuántas unidades quieres?\n")
            if entrada.isdigit() and int(entrada) > 0:
                cantidad = int(entrada)
                break
            print("Por favor, ingresa un número entero positivo")
        productos.append(producto)
        cantidades.append(cantidad)

# Calcula resultados
# 1. Productos únicos
productos_unicos = []
for prod in productos:
    if prod not in productos_unicos:
        productos_unicos.append(prod)

# 2. Suma total
total = 0
for cantidad in cantidades:
    total += cantidad

# 3. Producto más pedido
cantidades_por_producto = {}
for i in range(len(productos)):
    prod = productos[i]
    cant = cantidades[i]
    if prod in cantidades_por_producto:
        cantidades_por_producto[prod] += cant
    else:
        cantidades_por_producto[prod] = cant

max_cantidad = 0
max_producto = ""
for prod, cant in cantidades_por_producto.items():
    if cant > max_cantidad:
        max_cantidad = cant
        max_producto = prod

# Imprime resultados
print("Productos únicos:", productos_unicos)
print("Cantidad total:", total)
print(f"Producto más pedido: {max_producto} ({max_cantidad} unidades)")