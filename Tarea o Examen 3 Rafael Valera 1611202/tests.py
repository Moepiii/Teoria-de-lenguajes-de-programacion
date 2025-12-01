# Rafael Antonio Valera Pacheco 16-11202
import unittest
import sys

from manager import TypeManager


class TestTypeManagerRequirements(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada prueba"""
        self.tm = TypeManager()
        # Configuración base común
        self.tm.register_atomic("char", 1, 1)
        self.tm.register_atomic("int", 4, 4)
        self.tm.register_atomic("double", 8, 8)

    def test_atomico_registro(self):
        # Prueba registro de tipo atómico y error de duplicado
        self.tm.register_atomic("byte", 1, 1)
        self.assertIn("byte", self.tm.registry)

        with self.assertRaises(ValueError):
            self.tm.register_atomic("byte", 1, 1)

    def test_struct_simple_y_estrategias(self):
        # STRUCT test char int
        # Naive: char(1) + pad(3) + int(4) = 8 bytes
        self.tm.register_struct("test", ["char", "int"])

        # 1. Sin empaquetar
        size, align, waste = self.tm.registry["test"].get_stats("naive")
        self.assertEqual(size, 8)
        self.assertEqual(align, 4)

        # 2. Empaquetado (Size = 1+4=5, Align=1)
        size, align, waste = self.tm.registry["test"].get_stats("packed")
        self.assertEqual(size, 5)
        self.assertEqual(align, 1)
        self.assertEqual(waste, 0)

    def test_struct_optimal_reordering(self):
        # STRUCT desordenado: char, double, char
        # Naive: 1 + pad(7) + 8 + 1 + pad(7) = 24 bytes
        # Optimal: double, char, char -> 8 + 1 + 1 + pad(6) = 16 bytes
        self.tm.register_struct("desordenado", ["char", "double", "char"])

        s_naive, _, _ = self.tm.registry["desordenado"].get_stats("naive")
        s_opt, a_opt, w_opt = self.tm.registry["desordenado"].get_stats("optimal")

        self.assertTrue(
            s_opt < s_naive, "La estrategia óptima debería reducir el tamaño"
        )
        self.assertEqual(s_opt, 16)

    def test_union_behavior(self):
        # UNION u int double -> Size max(4,8)=8
        self.tm.register_union("u", ["int", "double"])
        size, align, _ = self.tm.registry["u"].get_stats("naive")
        self.assertEqual(size, 8)
        self.assertEqual(align, 8)

    def test_tipos_anidados(self):
        # STRUCT inner char int (Size 8)
        self.tm.register_struct("inner", ["char", "int"])
        # STRUCT outer char inner
        # char(1) + pad(3) + inner(8) = 12 bytes
        self.tm.register_struct("outer", ["char", "inner"])

        size, _, _ = self.tm.registry["outer"].get_stats("naive")
        self.assertEqual(size, 12)

    def test_manejo_errores(self):
        # Registrar struct con tipo inexistente
        with self.assertRaises(ValueError):
            self.tm.register_struct("fail", ["no_existo"])

        # Describir tipo inexistente
        msg = self.tm.describe("fantasma")
        self.assertTrue("Error" in msg)


if __name__ == "__main__":
    # 1. Cargar las pruebas de la clase
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTypeManagerRequirements)

    # 2. Ejecutar las pruebas usando un Runner que nos permita capturar el resultado
    # verbosity=0 evita para que el cuadro se vea limpio.
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)

    # 3. Calcular Estadísticas
    total = result.testsRun
    errors = len(result.errors)
    failures = len(result.failures)
    passed = total - (errors + failures)

    if total > 0:
        percentage = (passed / total) * 100
    else:
        percentage = 0.0

    # 4. Imprimir el Reporte 
    print("\n" + "=" * 60)
    print("       REPORTE DE PRUEBAS UNITARIAS")
    print("=" * 60)
    print(f"Total de pruebas  : {total}")
    print(f"Pruebas exitosas  : {passed}")
    print(f"Fallos / Errores  : {errors + failures}")
    print("-" * 60)
    print(f"PORCENTAJE DE ÉXITO: {percentage:.2f}%")
    print("=" * 60)
