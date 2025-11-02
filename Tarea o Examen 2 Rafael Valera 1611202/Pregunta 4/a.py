# Recordando que mis nuemros son X=2 Y=0 Z=2
def Frecursivadirecta(n):

    if 0 <= n < 25:
        # Caso base: F(n) = n
        return n
    elif n >= 25:
        # Caso recursivo: F(n) = sumatoria con cosas
        sum_val = 0
        for i in range(1, 6): 
            sum_val += Frecursivadirecta(n - 5 * i)
        return sum_val
    else:
        # por definicion
        raise ValueError("n debe ser no negativo")

# ejemplo caso base
n_base = 20
resultado_base = Frecursivadirecta(n_base)
print(f"Frecursivadirecta({n_base}) retorna: {resultado_base}")

# ejemplo caso recursivo
n_rec = 25
resultado_rec = Frecursivadirecta(n_rec)
print(f"Frecursivadirecta({n_rec}) retorna: {resultado_rec}")
