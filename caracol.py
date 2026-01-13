def caracol(distancia_recorrida_diaria, distancia_perdida_diaria, distancia_objetivo):
    if distancia_perdida_diaria >= distancia_recorrida_diaria:
        print("Eres autista")
    else:
        distancia_recorrida = 0
        dias = 0
        while distancia_recorrida < distancia_objetivo:
            dias += 1
            distancia_recorrida += distancia_recorrida_diaria
            if distancia_recorrida >= distancia_objetivo:
                break
            distancia_recorrida -= distancia_perdida_diaria
        print(f"El caracol ha tardado {dias} dias en salir del pozo")

caracol(271000, 88, 6000000)

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    
    # Solo verificar impares hasta la raíz cuadrada
    for divisor in range(3, int(num**0.5) + 1, 2):
        if num % divisor == 0:
            return False
    
    return True

