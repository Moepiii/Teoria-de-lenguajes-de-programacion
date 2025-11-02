import timeit
import matplotlib.pyplot as plt
import numpy as np
import sys

# límite de recursión alto para la prueba (b)
sys.setrecursionlimit(20000)


# (a) Subrutina Recursiva Directa 
def F_recursiva_directa(n):
    if 0 <= n < 25:
        return n
    elif n >= 25:
        sum_val = 0
        for i in range(1, 6):  # i = 1, 2, 3, 4, 5
            sum_val += F_recursiva_directa(n - 5 * i)
        return sum_val
    return 0


# (b) Subrutina Recursiva de Cola 
def _G_k_tail_helper(m_target, m_current, v0, v1, v2, v3, v4):
    if m_current > m_target:
        return v4
    new_v = v0 + v1 + v2 + v3 + v4
    return _G_k_tail_helper(m_target, m_current + 1, v1, v2, v3, v4, new_v)


def F_recursiva_cola(n):
    if 0 <= n < 25:
        return n
    elif n < 0:
        raise ValueError("n debe ser no negativo")
    k = n % 5
    m_target = n // 5
    v0, v1, v2, v3, v4 = k, 5 + k, 10 + k, 15 + k, 20 + k
    return _G_k_tail_helper(m_target, 5, v0, v1, v2, v3, v4)


# (c) Subrutina Iterativa 
def F_iterativa(n):
    if 0 <= n < 25:
        return n
    elif n < 0:
        raise ValueError("n debe ser no negativo")
    k = n % 5
    m_target = n // 5

    g_m_minus_5 = k
    g_m_minus_4 = 5 + k
    g_m_minus_3 = 10 + k
    g_m_minus_2 = 15 + k
    g_m_minus_1 = 20 + k
    current_g_m = 0

    for m_current in range(5, m_target + 1):
        current_g_m = (
            g_m_minus_1 + g_m_minus_2 + g_m_minus_3 + g_m_minus_4 + g_m_minus_5
        )

        # Desplazamiento
        g_m_minus_5, g_m_minus_4, g_m_minus_3, g_m_minus_2 = (
            g_m_minus_4,
            g_m_minus_3,
            g_m_minus_2,
            g_m_minus_1,
        )
        g_m_minus_1 = current_g_m

    return current_g_m


# --- Definición de Valores de Entrada para Pruebas ---

# (a) Solo valores muy pequeños, pues el tiempo crece muy rápido.
n_directa = list(range(25, 46, 5))
times_directa = []

# (b) y (c) Valores más grandes para ver el comportamiento lineal.
n_lineal = list(range(100, 4001, 500))
times_cola = []
times_iterativa = []

# Medición de Tiempos
print("Iniciando análisis de tiempos...")

#  Medir (a) F_recursiva_directa
for n in n_directa:
    t = timeit.timeit(lambda: F_recursiva_directa(n), number=1)
    times_directa.append(t)
print(f"Prueba (a) completada para n={n_directa[-1]}.")

#  Medir (b) F_recursiva_cola
for n in n_lineal:
    # Promedio de 10 ejecuciones
    t = timeit.timeit(lambda: F_recursiva_cola(n), number=10) / 10
    times_cola.append(t)
print(f"Prueba (b) completada para n={n_lineal[-1]}.")

#  Medir (c) F_iterativa
for n in n_lineal:
    # Promedio de 100 ejecuciones (es muy rápida)
    t = timeit.timeit(lambda: F_iterativa(n), number=100) / 100
    times_iterativa.append(t)
print(f"Prueba (c) completada para n={n_lineal[-1]}.")


# Esta parte son solo cosas de la grafica no detallare mucho profe
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfica 1: Comportamiento Exponencial vs Lineal =
ax1.plot(n_directa, times_directa, "ro-", label="(a) Recursiva Directa (Exp)")
ax1.set_title("Gráfico 1: Rendimiento para n Pequeños")
ax1.set_xlabel("Valor de n")
ax1.set_ylabel("Tiempo de ejecución (segundos)")
ax1.legend()
ax1.grid(True)

# Gráfica 2: Comportamiento Lineal (b) y (c)
ax2.plot(n_lineal, times_cola, "bo--", label="(b) Recursiva de Cola (Lineal)")
ax2.plot(n_lineal, times_iterativa, "g^-", label="(c) Iterativa (Lineal)")
ax2.set_title("Gráfico 2: Comparación de Implementaciones Eficientes")
ax2.set_xlabel("Valor de n")
ax2.set_ylabel("Tiempo de ejecución (segundos)")
ax2.legend()
ax2.grid(True)

plt.suptitle("Análisis de Eficiencia de F(5, 5, n) - Implementaciones", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

