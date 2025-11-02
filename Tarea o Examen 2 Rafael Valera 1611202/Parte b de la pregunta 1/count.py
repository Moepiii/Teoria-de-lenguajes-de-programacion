def count(n):
    # n debe ser un entero positivo > 0 para que funcione si no dara error posiblemente.
    # Si n ya es 1, el bucle no se ejecutará y devolverá 0 pasos.

    # 1. Inicializamos el contador de pasos
    pasos = 0

    # 2. Iteramos mientras n sea diferente de 1
    while n != 1:
        # 3. Aplicamos la lógica de la función f(n) 
        if n % 2 == 0:
            # n es par
            n = n // 2
        else:
            # n es impar
            n = (3 * n) + 1
        # 4. Incrementamos el contador por cada paso
        pasos += 1
    # 5. Cuando n == 1, el bucle termina y devolvemos el total de pasos
    return pasos


# Parte principal

try:
    # Se pide un numero entero y positivo
    numero_n = int(input("Introduce un entero n positivo: "))

    if numero_n <= 0:
        print("El número debe ser un entero positivo.")
    else:
        # Se Llama a la función para calcular la distancia
        distancia = count(numero_n)

        # Imprimimos el resultado
        print(f"count({numero_n}) = {distancia}")

except ValueError:
    print("Error: Debes introducir un número entero válido.")
