"""
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
"""

import threading
import multiprocessing
import re
import inspect
import functools
import asyncio
import platform
from collections import defaultdict, OrderedDict
from types import FunctionType
from typing import Callable, Any

# Metaclase con comportamiento dinámico
class DynamicMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['mutate'] = lambda self: setattr(self, 'state', self.state * 2)
        for key, value in attrs.items():
            if callable(value):
                attrs[key] = cls._wrap_method(value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def _wrap_method(method):
        def wrapper(*args, **kwargs):
            print(f"Executing {method.__name__}")
            return method(*args, **kwargs)
        return wrapper

# Decoradores múltiples
def thread_safe(func):
    lock = multiprocessing.Lock()  # Cambiado a multiprocessing.Lock
    def wrapper(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)
    return wrapper

def retry_on_failure(max_attempts: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
            raise RuntimeError(f"Failed after {max_attempts} attempts")
        return wrapper
    return decorator

# Clase con metaclase y generadores
class Processor(metaclass=DynamicMeta):
    def __init__(self, initial_state: int):
        self.state = initial_state

    @thread_safe
    @retry_on_failure(3)
    def generate_sequence(self):
        def inner_gen():
            current = self.state
            while True:
                yield current
                current += self.state
        return inner_gen()

# Corrutina asíncrona
async def async_processor(coro_input: str):
    pattern = re.compile(r'(?:\w{2,})|[\d]+')
    iterations = 0
    while iterations < 2:  # Limitado a 2 iteraciones
        await asyncio.sleep(0.1)
        matches = pattern.findall(coro_input)
        yield matches
        iterations += 1

# Concurrencia con threading y multiprocessing
def concurrent_task(shared_data: list, lock: multiprocessing.Lock, queue: multiprocessing.Queue):
    with lock:
        shared_data.append(threading.current_thread().name)
    queue.put(len(shared_data))  # Siempre usamos longitud porque son strings

# Reflexión y metaprogramación
def create_dynamic_function(code_str: str) -> Callable:
    namespace = {}
    exec(code_str, namespace)
    return namespace['dynamic_func']

# Estructura principal
async def main():
    # Inicialización
    manager = multiprocessing.Manager()
    lock = multiprocessing.Lock()
    shared_data = manager.list()  # Usamos Manager.list para compartir entre procesos
    queue = multiprocessing.Queue()

    # Concurrencia
    threads = [threading.Thread(target=concurrent_task, args=(shared_data, lock, queue)) for _ in range(4)]
    processes = [multiprocessing.Process(target=concurrent_task, args=(shared_data, lock, queue)) for _ in range(2)]

    for t in threads:
        t.start()
    for p in processes:
        p.start()

    for t in threads:
        t.join()
    for p in processes:
        p.join()

    # Procesamiento de resultados
    results = [queue.get() for _ in range(6)]
    print(f"Concurrent results: {results}")

    # Uso de Processor
    proc = Processor(5)
    gen = proc.generate_sequence()
    seq = [next(gen) for _ in range(5)]
    print(f"Generated sequence: {seq}")

    # Corrutina
    async_gen = async_processor("hello123world456")
    async_result = [result async for result in async_gen]
    print(f"Async results: {async_result}")

    # Estructuras avanzadas
    dd = defaultdict(lambda: OrderedDict())
    dd['x']['first'] = 1
    dd['x']['second'] = 2
    dd['y']['third'] = 3
    print(f"DefaultDict with OrderedDict: {dict(dd)}")

    # Reflexión
    dynamic_code = """
def dynamic_func():
    return sum([i * i for i in range(5)])
"""
    dyn_func = create_dynamic_function(dynamic_code)
    print(f"Dynamic function result: {dyn_func()}")

    # Excepciones anidadas
    try:
        try:
            raise ValueError("Nested error")
        except ValueError as e:
            raise RuntimeError("Outer error") from e
    except RuntimeError as re:
        print(f"Caught: {re}")

    # Lambdas y comprensiones
    matrix = [[1, 2], [3, 4]]
    transform = lambda x: x * 2
    flattened = [transform(x) for row in matrix for x in row if x % 2 == 0]
    print(f"Transformed and flattened: {flattened}")

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())