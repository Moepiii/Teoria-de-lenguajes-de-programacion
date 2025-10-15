# vector3d.rb
class Vector3D
  attr_accessor :x, :y, :z

  def initialize(x, y, z)
    @x = x.to_f
    @y = y.to_f
    @z = z.to_f
  end

  # Suma
  def +(other)
    if other.is_a?(Vector3D)
      Vector3D.new(@x + other.x, @y + other.y, @z + other.z)
    else
      Vector3D.new(@x + other, @y + other, @z + other)
    end
  end

  # Resta
  def -(other)
    if other.is_a?(Vector3D)
      Vector3D.new(@x - other.x, @y - other.y, @z - other.z)
    else
      Vector3D.new(@x - other, @y - other, @z - other)
    end
  end

  # Producto cruz
  def *(other)
    if other.is_a?(Vector3D)
      Vector3D.new(
        @y * other.z - @z * other.y,
        @z * other.x - @x * other.z,
        @x * other.y - @y * other.x
      )
    else
      Vector3D.new(@x * other, @y * other, @z * other)
    end
  end

  # Producto punto
  def %(other)
    raise "Producto punto requiere un vector" unless other.is_a?(Vector3D)
    @x * other.x + @y * other.y + @z * other.z
  end

  # Norma
  def norm
    Math.sqrt(@x**2 + @y**2 + @z**2)
  end

  def to_s
    "(#{@x}, #{@y}, #{@z})"
  end

  def ==(other)
    return false unless other.is_a?(Vector3D)
    @x == other.x && @y == other.y && @z == other.z
  end
end
