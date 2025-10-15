# main_sistema.rb
require_relative 'sistema'

s = Sistema.new

puts "Bienvenido al simulador de programas/intérpretes/traductores."
loop do
  print "> "
  input = gets.chomp.strip
  break if input.upcase == "SALIR"
  next if input.empty?

  comando, *args = input.split
  begin
    case comando.upcase
    when "DEFINIR"
      tipo = args.shift
      s.definir(tipo, *args)
    when "EJECUTABLE"
      nombre = args.first
      s.ejecutable(nombre)
    else
      puts "Comando desconocido: #{comando}"
    end
  rescue => e
    puts "Error: #{e.message}"
  end
end

puts "Saliendo..."
