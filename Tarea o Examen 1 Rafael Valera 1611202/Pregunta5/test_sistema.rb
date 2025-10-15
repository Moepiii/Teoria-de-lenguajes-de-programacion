require 'simplecov'
SimpleCov.start
require 'minitest/autorun'
require_relative 'sistema'

class SistemaTest < Minitest::Test
  def setup
    @s = Sistema.new
    @s.definir('PROGRAMA','P1','PYTHON')
    @s.definir('INTERPRETE','LOCAL','PYTHON')
    @s.definir('TRADUCTOR','LOCAL','PYTHON','LOCAL')
  end

  def test_programa_definido
    assert @s.programas.key?('P1')
    assert_equal 'PYTHON', @s.programas['P1'][:lenguaje]
  end

  def test_interprete_definido
    assert @s.interpretes['LOCAL'].key?('PYTHON')
  end

  def test_traductor_definido
    assert_equal 'LOCAL', @s.traductores['LOCAL']['PYTHON']
  end

  def test_ejecutable_existe
    out = capture_io { @s.ejecutable('P1') }.first
    assert_match /Ejecutando/, out
  end

  def test_ejecutable_no_existe
    out = capture_io { @s.ejecutable('NOEXISTE') }.first
    assert_match /no definido/, out
  end

  def test_ejecutable_local
  @s.definir('PROGRAMA','P2','LOCAL')
  out = capture_io { @s.ejecutable('P2') }.first
  assert_match /directamente en LOCAL/, out
end

def test_ejecutable_traductor_sin_interprete
  # Traductor a un lenguaje sin intérprete disponible
  @s.definir('PROGRAMA','P3','RUBY')
  @s.definir('TRADUCTOR','LOCAL','RUBY','JAVA')
  out = capture_io { @s.ejecutable('P3') }.first
  assert_match /No hay intérprete/, out
end

def test_ejecutable_interprete_no_local
  # Intérprete en base diferente de LOCAL
  @s.definir('PROGRAMA','P4','LISP')
  @s.definir('INTERPRETE','PYTHON','LISP')
  out = capture_io { @s.ejecutable('P4') }.first
  assert_match /Necesitaríamos intérprete para PYTHON/, out
end

end
