# Función para calcular la transpuesta de una matriz cuadrada A.
def transponer(matriz_a)
  n = matriz_a.length
  # Inicializa la matriz transpuesta con ceros (o nil)
  matriz_at = Array.new(n) { Array.new(n) }
  
  # Llena la matriz transpuesta
  (0...n).each do |i|
    (0...n).each do |j|
      matriz_at[i][j] = matriz_a[j][i]
    end
  end
  
  return matriz_at
end

# Función para calcular el producto de dos matrices cuadradas A y B.
def multiplicar_matrices(matriz_a, matriz_b)
  n = matriz_a.length
  
  # Inicializa la matriz resultado con ceros
  matriz_resultado = Array.new(n) { Array.new(n, 0) }
  
  # Realiza la multiplicación de matrices
  (0...n).each do |i| # Filas de la matriz resultado
    (0...n).each do |j| # Columnas de la matriz resultado
      suma_producto = 0
      
      (0...n).each do |k|
        suma_producto += matriz_a[i][k] * matriz_b[k][j]
      end
      
      matriz_resultado[i][j] = suma_producto
    end
  end
  
  return matriz_resultado
end

# Función principal que calcula A * A^T
def producto_matriz_por_transpuesta(matriz_a)

  matriz_at = transponer(matriz_a)

  matriz_resultado = multiplicar_matrices(matriz_a, matriz_at)
  
  return matriz_resultado
end

# Función de ayuda para mostrar la matriz de forma clara
def imprimir_matriz(matriz)
  matriz.each do |fila|
    puts fila.inspect
  end
end

#               Ejemplo de como usarlo si quiere profe

# Matriz cuadrada A (dimensión N=2)
# A = [[1, 2],
#      [3, 4]]
matriz_a = [[1, 2], [3, 4]]

# Matriz Transpuesta A^T = [[1, 3],
#                           [2, 4]]

# Producto esperado A x A^T = 
# [[(1*1 + 2*2), (1*3 + 2*4)],
#  [(3*1 + 4*2), (3*3 + 4*4)]]
# = [[(1 + 4), (3 + 8)],
#    [(3 + 8), (9 + 16)]]
# = [[5, 11], 
#    [11, 25]]

puts "Matriz A:"
imprimir_matriz(matriz_a)

resultado = producto_matriz_por_transpuesta(matriz_a)

puts "\nResultado de A * A^T:"
imprimir_matriz(resultado)