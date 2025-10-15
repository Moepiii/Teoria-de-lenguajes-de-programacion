# Definición de la función 'rotar' 
def rotar(w, k)

  # 1. Caso Base: si k = 0 o la cadena está vacía (|w| = 0)
  if k == 0 || w.empty?
    return w
  end

  # Ajuste para rotaciones mayores a la longitud de la cadena:
  k_efectivo = k % w.length
  
  if k_efectivo == 0
    return w
  end

  
  # 2. Caso Recursivo: si k > 0 y w = a + x (donde 'a' es el primer caracter)
  #    rotar(w, k) = rotar(x + [a], k - 1)

  
  a = w[0] 
  
  x = w[1..-1] 
  
  # Se forma la nueva cadena rotada un paso: x + [a]
  # Se hace la llamada recursiva: rotar(x + a, k_efectivo - 1)
  return rotar(x + a, k_efectivo - 1)
end

# --- Ejemplos del profe ---

puts "--- Pruebas de rotación ---"


puts "rotar('hola', 0) = #{rotar('hola', 0)}"

puts "rotar('hola', 1) = #{rotar('hola', 1)}"

puts "rotar('hola', 2) = #{rotar('hola', 2)}"

puts "rotar('hola', 3) = #{rotar('hola', 3)}"

puts "rotar('hola', 4) = #{rotar('hola', 4)}"

puts "rotar('hola', 5) = #{rotar('hola', 5)}"
puts "------------------------------"