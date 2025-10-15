# sistema.rb

class Sistema
  attr_reader :programas, :interpretes, :traductores

  def initialize
    @programas = {}      # nombre => { lenguaje }
    @interpretes = {}    # lenguaje_base => { lenguaje => true }
    @traductores = {}    # lenguaje_base => { origen => destino }
  end

  # Definir un objeto
  def definir(tipo, *args)
    case tipo.upcase
    when 'PROGRAMA'
      nombre, lenguaje = args
      raise "Argumentos inválidos para PROGRAMA" unless nombre && lenguaje
      @programas[nombre] = { lenguaje: lenguaje.upcase }
      puts "Programa '#{nombre}' definido en lenguaje #{lenguaje}."
    when 'INTERPRETE'
      lenguaje_base, lenguaje = args
      raise "Argumentos inválidos para INTERPRETE" unless lenguaje_base && lenguaje
      @interpretes[lenguaje_base.upcase] ||= {}
      @interpretes[lenguaje_base.upcase][lenguaje.upcase] = true
      puts "Intérprete de #{lenguaje} sobre #{lenguaje_base} definido."
    when 'TRADUCTOR'
      lenguaje_base, origen, destino = args
      raise "Argumentos inválidos para TRADUCTOR" unless lenguaje_base && origen && destino
      @traductores[lenguaje_base.upcase] ||= {}
      @traductores[lenguaje_base.upcase][origen.upcase] = destino.upcase
      puts "Traductor de #{origen} a #{destino} sobre #{lenguaje_base} definido."
    else
      raise "Tipo desconocido: #{tipo}"
    end
  end

  # Ejecutar un programa
  def ejecutable(nombre)
    prog = @programas[nombre]
    unless prog
      puts "Programa #{nombre} no definido."
      return
    end

    lenguaje = prog[:lenguaje]

    puts "Intentando ejecutar '#{nombre}' en #{lenguaje}..."

    if lenguaje == "LOCAL"
      puts "Ejecutando #{nombre} directamente en LOCAL."
      return
    end

    # Intentar intérprete directo
    @interpretes.each do |base, langs|
      if langs[lenguaje]
        puts "Usando intérprete de #{lenguaje} sobre #{base}."
        if base == "LOCAL"
          puts "Ejecutando #{nombre} sobre #{base}."
        else
          puts "Necesitaríamos intérprete para #{base}..."
        end
        return
      end
    end

    # Intentar traductor
    @traductores.each do |base, map|
      if map[lenguaje]
        destino = map[lenguaje]
        puts "Traduciendo #{nombre} de #{lenguaje} a #{destino} usando base #{base}."
        if destino == "LOCAL" || @interpretes[base]&.[](destino)
          puts "Ejecutando #{nombre} en #{destino}."
        else
          puts "No hay intérprete para #{destino}."
        end
        return
      end
    end

    puts "No se puede ejecutar #{nombre}: falta intérprete o traductor."
  end
end
