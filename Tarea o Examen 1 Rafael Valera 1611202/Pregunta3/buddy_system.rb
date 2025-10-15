class BuddySystem
  attr_reader :size, :free_blocks, :allocated

  def initialize(size)
    raise ArgumentError, "El tamaño debe ser potencia de 2" unless size.positive? && (size & (size - 1)).zero?

    @size = size
    @free_blocks = { size => [0] }  # Hash: tamaño → lista de bloques libres
    @allocated = {}                 # nombre → [posición, tamaño]
  end

  def reservar(cantidad, nombre)
    raise "El nombre '#{nombre}' ya está reservado" if @allocated.key?(nombre)
    raise "Cantidad inválida" unless cantidad.positive?

    bloque = siguiente_potencia_de_2(cantidad)
    size_actual = buscar_bloque_libre(bloque)

    raise "No hay memoria suficiente" if size_actual.nil?

    dividir_hasta(size_actual, bloque)
    pos = @free_blocks[bloque].shift
    @allocated[nombre] = [pos, bloque]
    puts "Bloque '#{nombre}' reservado con #{bloque} unidades (posición #{pos})."
  end

  def liberar(nombre)
    raise "No existe el bloque '#{nombre}'" unless @allocated.key?(nombre)

    pos, bloque = @allocated.delete(nombre)
    @free_blocks[bloque] ||= []
    @free_blocks[bloque] << pos
    fusionar(pos, bloque)
    puts "Bloque '#{nombre}' liberado."
  end

  def mostrar
    puts "\n=== Estado de Memoria ==="
    puts "Bloques libres:"
    @free_blocks.keys.sort.each do |tam|
      puts "  #{tam}: #{@free_blocks[tam].sort}"
    end
    puts "Bloques reservados:"
    @allocated.each { |nom, (pos, tam)| puts "  #{nom}: posición #{pos}, tamaño #{tam}" }
    puts "=========================\n\n"
  end

  private

  def siguiente_potencia_de_2(n)
    2**Math.log2(n).ceil
  end

  def buscar_bloque_libre(min)
    @free_blocks.keys.sort.find { |tam| tam >= min && !@free_blocks[tam].empty? }
  end

  def dividir_hasta(size_actual, size_deseado)
    while size_actual > size_deseado
      pos = @free_blocks[size_actual].shift
      mitad = size_actual / 2
      @free_blocks[mitad] ||= []
      @free_blocks[mitad] << pos
      @free_blocks[mitad] << pos + mitad
      size_actual = mitad
    end
  end

  def fusionar(pos, size)
    buddy = pos ^ size  # XOR para encontrar el “hermano”
    lista = @free_blocks[size]

    if lista.include?(buddy)
      lista.delete(buddy)
      lista.delete(pos)
      nuevo_pos = [pos, buddy].min
      fusionar(nuevo_pos, size * 2)
    else
      @free_blocks[size] ||= []
      @free_blocks[size] << pos
    end
  end
end
