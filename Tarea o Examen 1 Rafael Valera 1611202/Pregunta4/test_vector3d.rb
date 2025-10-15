# test_vector3d.rb
require 'simplecov'
SimpleCov.start
require 'minitest/autorun'
require_relative 'vector3d'

class Vector3DTest < Minitest::Test
  def setup
    @a = Vector3D.new(1, 2, 3)
    @b = Vector3D.new(3, 2, 1)
    @c = Vector3D.new(0, 1, 2)
  end

  def test_suma
    assert_equal Vector3D.new(4, 4, 4), @a + @b
    assert_equal Vector3D.new(4, 5, 6), @a + 3
  end

  def test_resta
    assert_equal Vector3D.new(-2, 0, 2), @a - @b
    assert_equal Vector3D.new(-2, -1, 0), @a - 3
  end

  def test_producto_cruz
    assert_equal Vector3D.new(-4, 8, -4), @a * @b
    assert_equal Vector3D.new(3, 6, 9), @a * 3
  end

  def test_producto_punto
    assert_equal 10, @a % @b
  end

  def test_norma
    assert_in_delta 3.741657, @a.norm, 1e-6
  end

  def test_combinaciones
    assert_equal Vector3D.new(-4, 9, -2), (@a * @b) + @c
    assert_equal Vector3D.new(12, 8, 4), (@b + @b) * 2
  end
end
