
def iterador_ordenado(lista_original):
  # Hace una copia de la lista para no modificar la original
  items = list(lista_original)
  
  # Mientras la copia no esté vacía
  while items:
    # Encuentra el elemento más pequeño
    min_val = min(items)
    
    # Producir (yield) ese elemento
    yield min_val
    
    # Eliminar la primera aparición de ese elemento
    items.remove(min_val)

# si lo quiere usar profe cambie valores aqui
lista_ejemplo = [1, 3, 3, 2, 1]

print(f"Lista original: {lista_ejemplo}")
print("Elementos producidos por el iterador:")

for elemento in iterador_ordenado(lista_ejemplo):
  print(elemento, end=" ")

