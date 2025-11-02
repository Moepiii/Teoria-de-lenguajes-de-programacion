import unittest

# Primero importamos un monto de cosas 
from expresiones import (
    process_line,
    NumberNode,
    OperatorNode,
    parse_prefix,
    parse_postfix,
    build_ast,
)


class TestExpresiones(unittest.TestCase):

    def test_eval_pre_ejemplo(self):
        # EVAL PRE + * + 3 4 5 7 deberá imprimir 42
        linea = "EVAL PRE + * + 3 4 5 7"
        self.assertEqual(process_line(linea), 42)

    def test_eval_post_ejemplo(self):
        # EVAL POST 8 3 - 8 4 4 + * + deberá imprimir 69
        linea = "EVAL POST 8 3 - 8 4 4 + * +"
        self.assertEqual(process_line(linea), 69)

    def test_mostrar_pre_ejemplo(self):
        # MOSTRAR PRE + * + 3 4 5 7 deberá imprimir (3 + 4) * 5 + 7
        linea = "MOSTRAR PRE + * + 3 4 5 7"
        self.assertEqual(process_line(linea), "(3 + 4) * 5 + 7")

    def test_mostrar_post_ejemplo(self):
        # MOSTRAR POST 8 3 - 8 4 4 + * + deberá imprimir 8 - 3 + 8 * (4 + 4)
        linea = "MOSTRAR POST 8 3 - 8 4 4 + * +"
        self.assertEqual(process_line(linea), "8 - 3 + 8 * (4 + 4)")

    def test_eval_division_entera(self):
        linea = "EVAL PRE / 10 3"
        self.assertEqual(process_line(linea), 3)

    def test_eval_resta_simple(self):
        linea = "EVAL POST 10 5 -"
        self.assertEqual(process_line(linea), 5)

    def test_eval_division_cero(self):
        linea = "EVAL POST 10 0 /"
        # Prueba que levanta un error de ValueError
        with self.assertRaisesRegex(ValueError, "División por cero"):
            process_line(linea)

    def test_mostrar_precedencia_1(self):
        # * + 1 2 3 -> (1 + 2) * 3
        linea = "MOSTRAR PRE * + 1 2 3"
        self.assertEqual(process_line(linea), "(1 + 2) * 3")

    def test_mostrar_precedencia_2(self):
        # + 1 * 2 3 -> 1 + 2 * 3 
        linea = "MOSTRAR POST 1 2 3 * +"
        self.assertEqual(process_line(linea), "1 + 2 * 3")

    def test_mostrar_asociatividad_resta(self):
        # - - 8 3 2 -> (8 - 3) - 2
        linea = "MOSTRAR PRE - - 8 3 2"
        self.assertEqual(
            process_line(linea), "8 - 3 - 2"
        ) 

    def test_mostrar_asociatividad_resta_forzada(self):
        # - 8 - 3 2 -> 8 - (3 - 2)
        linea = "MOSTRAR PRE - 8 - 3 2"
        self.assertEqual(process_line(linea), "8 - (3 - 2)")

    def test_mostrar_asociatividad_division(self):
        # / 8 - 4 2 -> 8 / (4 - 2)
        linea = "MOSTRAR POST 8 4 2 - /"
        self.assertEqual(process_line(linea), "8 / (4 - 2)")

    def test_comando_salir(self):
        self.assertEqual(process_line("SALIR"), "SALIR")
        self.assertEqual(process_line("salir"), "SALIR") 

    def test_comando_vacio(self):
        self.assertIsNone(process_line("   "))

    def test_comando_desconocido(self):
        with self.assertRaisesRegex(ValueError, "Comando no reconocido"):
            process_line("INVENTADO 1 2 3")

    def test_comando_incompleto(self):
        with self.assertRaisesRegex(ValueError, "Comando 'EVAL' incompleto"):
            process_line("EVAL PRE")

    def test_formato_desconocido(self):
        with self.assertRaisesRegex(ValueError, "Formato desconocido"):
            process_line("EVAL INFIX + 1 2")

    def test_expresion_post_malformada_faltan_operandos(self):
        with self.assertRaisesRegex(ValueError, "faltan operandos"):
            process_line("EVAL POST 1 + +")

    def test_expresion_post_malformada_sobran_operandos(self):
        with self.assertRaisesRegex(ValueError, "sobran operandos"):
            process_line("EVAL POST 1 2 3 +")

    def test_expresion_pre_malformada_incompleta(self):
        with self.assertRaisesRegex(ValueError, "PRE-FIJA incompleta"):
            process_line("EVAL PRE + 1")

    def test_expresion_pre_malformada_sobran_tokens(self):
        with self.assertRaisesRegex(ValueError, "sobran tokens"):
            process_line("EVAL PRE + 1 2 3")

    def test_token_no_numerico(self):
        with self.assertRaisesRegex(ValueError, "Token no numérico"):
            process_line("EVAL PRE + 1 A")

    def test_operador_desconocido(self):
        with self.assertRaisesRegex(ValueError, "Operador desconocido"):
            process_line("EVAL PRE % 1 2")

if __name__ == "__main__":
    unittest.main()
