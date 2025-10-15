require_relative 'buddy_system'

puts "Ingrese el tamaño total de la memoria (potencia de 2):"
tam = gets.to_i
sistema = BuddySystem.new(tam)

loop do
  puts "Acción: RESERVAR <cant> <nombre> | LIBERAR <nombre> | MOSTRAR | SALIR"
  print "> "
  entrada = gets.chomp.split
  comando = entrada[0]&.upcase

  begin
    case comando
    when "RESERVAR"
      cant = entrada[1].to_i
      nombre = entrada[2]
      sistema.reservar(cant, nombre)
    when "LIBERAR"
      nombre = entrada[1]
      sistema.liberar(nombre)
    when "MOSTRAR"
      sistema.mostrar
    when "SALIR"
      puts "Finalizando simulación..."
      break
    else
      puts "Comando no válido."
    end
  rescue => e
    puts "Error: #{e.message}"
  end
end
