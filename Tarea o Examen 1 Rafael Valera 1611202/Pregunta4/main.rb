# main.rb
require_relative 'vector3d'

a = Vector3D.new(1, 2, 3)
b = Vector3D.new(3, 2, 1)
c = Vector3D.new(0, 1, 2)
d = Vector3D.new(2, 0, -1)

puts "Vectores:"
puts "a = #{a}"
puts "b = #{b}"
puts "c = #{c}"
puts "d = #{d}"
puts "\nOperaciones:"

puts "b + c = #{b + c}"
puts "a * b + c = #{a * b + c}"
puts "(b + b) * (c - a) = #{(b + b) * (c - a)}"
puts "a % (c * b) = #{a % (c * b)}"
puts "b + 3 = #{b + 3}"
puts "a * 3.0 + a.norm = #{a * 3.0 + a.norm}"  # Use .norm
puts "(b + b) * (c % a) = #{(b + b) * (c % a)}"
