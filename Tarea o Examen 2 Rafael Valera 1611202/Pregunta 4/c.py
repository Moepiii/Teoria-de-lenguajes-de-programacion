def F_iterativa(n):

    if 0 <= n < 25:
        return n
    elif n < 0:
        raise ValueError("n debe ser no negativo")

    k = n % 5
    m_target = n // 5

    # Casos base
    g_m_minus_5 = k
    g_m_minus_4 = 5 + k
    g_m_minus_3 = 10 + k
    g_m_minus_2 = 15 + k
    g_m_minus_1 = 20 + k 

    # Variable para guardar el valor calculado en el bucle
    current_g_m = 0

    for m_current in range(5, m_target + 1):
        # Calcula
        current_g_m = (
            g_m_minus_1 + g_m_minus_2 + g_m_minus_3 + g_m_minus_4 + g_m_minus_5
        )

        # Actualiza el estado para la siguiente iteración
        g_m_minus_5 = g_m_minus_4
        g_m_minus_4 = g_m_minus_3
        g_m_minus_3 = g_m_minus_2
        g_m_minus_2 = g_m_minus_1
        g_m_minus_1 = current_g_m  

    return current_g_m

#si quiere usar algun ejemplo profe
print("Resultados de F_iterativa(n)")

# Ejemplo caso base
n1 = 24
resultado1 = F_iterativa(n1)
print(f"F_iterativa({n1}): {resultado1}")

# Ejemplo con un valor cualquiera
n2 = 26
resultado2 = F_iterativa(n2)
print(f"F_iterativa({n2}): {resultado2}")
