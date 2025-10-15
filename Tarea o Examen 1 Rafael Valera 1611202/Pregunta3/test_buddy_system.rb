require 'simplecov'
SimpleCov.start
require "minitest/autorun"
require_relative "buddy_system"

class TestBuddySystem < Minitest::Test
  def setup
    @sistema = BuddySystem.new(8)
  end

  def test_reservar_y_mostrar
    @sistema.reservar(3, "A")
    assert_includes @sistema.allocated.keys, "A"
  end

  def test_liberar
    @sistema.reservar(2, "B")
    @sistema.liberar("B")
    refute_includes @sistema.allocated.keys, "B"
  end

  def test_error_nombre_repetido
    @sistema.reservar(1, "X")
    assert_raises(RuntimeError) { @sistema.reservar(1, "X") }
  end

  def test_error_sin_memoria
    @sistema.reservar(8, "X")
    assert_raises(RuntimeError) { @sistema.reservar(1, "Y") }
  end

  def test_error_liberar_inexistente
    assert_raises(RuntimeError) { @sistema.liberar("Z") }
  end
end
