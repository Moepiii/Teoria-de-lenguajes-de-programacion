def mergesort(arr):
    # parte 1
    # Comprobamos si la lista tiene más de un elemento si tiene 0 o 1, es el caso base es decir esta ordenado.
    if len(arr) > 1:
        # vamos a encontrar el punto medio con:
        medio = len(arr) // 2

        # Dividimo la lista en dos mitades usando.
        mitad_izquierda = arr[:medio]
        mitad_derecha = arr[medio:]

        # parte 2
        # Llamada recursiva de la primera mitad
        mergesort(mitad_izquierda)
        # Llamada recursiva de la segunda mitad
        mergesort(mitad_derecha)

        # parte 3
        i = 0  # Un puntero para la izquierda
        j = 0  # Un puntero para la derecha
        k = 0  # Un puntero para la lista original arr

        # Combinamos las dos mitades que ya están ordenadas en la lista original arr.

        # Bucle que compara elementos de ambas mitades
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] <= mitad_derecha[j]:
                # El elemento de la izquierda es menor
                arr[k] = mitad_izquierda[i]
                i += 1
            else:
                # El elemento de la derecha es menor
                arr[k] = mitad_derecha[j]
                j += 1
            k += 1  # Mover el puntero de la lista principal

        # Si la mitad_derecha se acabó primero, copiar los elementos restantes de la mitad_izquierda.
        while i < len(mitad_izquierda):
            arr[k] = mitad_izquierda[i]
            i += 1
            k += 1

        # Si la mitad_izquierda se acabó primero, copiar los elementos restantes de la mitad_derecha.
        while j < len(mitad_derecha):
            arr[k] = mitad_derecha[j]
            j += 1
            k += 1

# fin aqui puede poner los ejemplos para probar profe
if __name__ == "__main__":

    lista_ejemplo = [38, 27, 43, 3, 9, 82, 10, -5, 100, 1]

    print(f"Lista original: {lista_ejemplo}")
    mergesort(lista_ejemplo)
    print(f"Lista ordenada: {lista_ejemplo}")
