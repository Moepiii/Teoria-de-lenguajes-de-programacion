import sys

# como python hace cosas medio raras estara en mi documento del examen hablando mas del tema
#tengo un limite de recursion alto para calcular valores de n altos
sys.setrecursionlimit(20000)


def _G_k_tail_helper(m_target, m_current, v0, v1, v2, v3, v4):

    # Si m_current es mayor que el m objetivo, termina.
    if m_current > m_target:
        return v4

    # Calcular G_k(m_current) como la suma de los 5 valores previos
    new_v = v0 + v1 + v2 + v3 + v4

    # Llamada de cola: La función se llama a sí misma para la siguiente iteración.
    return _G_k_tail_helper(m_target, m_current + 1, v1, v2, v3, v4, new_v)


def F_recursiva_cola(n):

    if 0 <= n < 25:
        return n
    elif n < 0:
        raise ValueError("n debe ser no negativo")
    #pasitos 
    # Definir k y m_target
    k = n % 5  # Secuencia particular (0, 1, 2, 3, 4)
    m_target = n // 5  # El índice m que en principio se calcula

    # Establecer el estado inicial (Casos base G_k(0) a G_k(4))
    v0 = k  # G_k(0) = 5*0 + k
    v1 = 5 + k  # G_k(1) = 5*1 + k
    v2 = 10 + k  # G_k(2) = 5*2 + k
    v3 = 15 + k  # G_k(3) = 5*3 + k
    v4 = 20 + k  # G_k(4) = 5*4 + k

    #Iniciar la recursión de cola desde m = 5
    return _G_k_tail_helper(m_target, 5, v0, v1, v2, v3, v4)


# Ejemplos para que use profesor
print("Resultados de F_recursiva_cola(n)")

# Caso Base
n1 = 20
resultado1 = F_recursiva_cola(n1)
print(f"F_recursiva_cola({n1}): {resultado1}")

# Caso para n valor más grande como n = 50
n3 = 50
resultado3 = F_recursiva_cola(n3)
print(f"F_recursiva_cola({n3}): {resultado3}")
