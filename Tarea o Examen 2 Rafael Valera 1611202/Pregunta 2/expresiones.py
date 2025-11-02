import sys

# Para facilita esto lo voy hacer con un AST 
class NumberNode:

    def __init__(self, value):
        # Todo esto es para tener seguridad de que se almacena como entero
        try:
            self.value = int(value)
        except ValueError:
            raise ValueError(f"Token no numérico: '{value}'")

    def eval(self):
        # Evalua un nodo numérico simplemente devolvera su valor.
        return self.value

    def to_infix(self, parent_prec=0):
        # Convertir un nodo numérico a infijo es devolvera su string.
        return str(self.value)


class OperatorNode:

    # Las reglas de precedencia de operadores
    PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}

    def __init__(self, operator, left, right):
        if operator not in self.PRECEDENCE:
            raise ValueError(f"Operador desconocido: '{operator}'")
        self.operator = operator
        self.left = left
        self.right = right
        self.precedence = self.PRECEDENCE[operator]

    def eval(self):
        
        #Evalua recursivamente los hijos y aplica el operador.
        left_val = self.left.eval()
        right_val = self.right.eval()

        if self.operator == "+":
            return left_val + right_val
        elif self.operator == "-":
            return left_val - right_val
        elif self.operator == "*":
            return left_val * right_val
        elif self.operator == "/":
            if right_val == 0:
                raise ValueError("División por cero")
            return left_val // right_val

    def to_infix(self, parent_prec=0):

        # se pasa la precedencia como parent_prec a los hijos.
        left_str = self.left.to_infix(self.precedence)
        right_str = self.right.to_infix(self.precedence)

        # aqui de dice si los hijos necesitan paréntesis
        # Hijo izquierdo
        if (
            isinstance(self.left, OperatorNode)
            and self.left.precedence < self.precedence
        ):
            left_str = f"({left_str})"

        # Hijo derecho
        if isinstance(self.right, OperatorNode):
            if self.right.precedence < self.precedence:
                right_str = f"({right_str})"
            elif self.right.precedence == self.precedence and self.operator in [
                "-",
                "/",
            ]:
                right_str = f"({right_str})"

        # pone la expresión actual
        my_str = f"{left_str} {self.operator} {right_str}"

        return my_str

# Ahora el parsers que bueno convierte la entrada de texto en el AST

def parse_prefix(tokens):

    if not tokens:
        raise ValueError("Expresión Pre-Fija incompleta")

    token = tokens.pop(0)  # Tomar el primer token

    if token in OperatorNode.PRECEDENCE:
        # Es un operador, necesita dos operandos 
        left_child = parse_prefix(tokens)
        right_child = parse_prefix(tokens)
        return OperatorNode(token, left_child, right_child)
    else:
        # Es un operando 
        return NumberNode(token)


def parse_postfix(tokens):

    stack = []
    for token in tokens:
        if token in OperatorNode.PRECEDENCE:
            # si es un operador, saca dos operandos del stack
            if len(stack) < 2:
                raise ValueError("Expresión Post-Fija mal formada, faltan operandos")

            # El orden es importante
            right_child = stack.pop()
            left_child = stack.pop()

            node = OperatorNode(token, left_child, right_child)
            stack.append(node)
        else:
            # Es un operando, lo mete al stack
            stack.append(NumberNode(token))

    # Al final, segun yo quedara un solo elemento en el stack que es el nodo raíz
    if len(stack) != 1:
        raise ValueError("Expresión Post-Fija mal formada, sobran operandos")

    return stack[0]


def build_ast(formato, tokens):

    if formato == "PRE":
        # Copiamos la lista porque parse_prefix la muta
        tokens_list = list(tokens)
        ast = parse_prefix(tokens_list)
        # Si sobran tokens, la expresión esta mal formada
        if tokens_list:
            raise ValueError("Expresión Pre-Foja mal formada, sobran tokens")
        return ast

    elif formato == "POST":
        ast = parse_postfix(tokens)
        return ast

    else:
        raise ValueError("Formato desconocido. Use PRE o POST.")


# con esto voy a manejar comandos si sale todo bien

def process_line(line):

    parts = line.strip().split()
    if not parts:
        return None  # Línea vacía, no hace nada

    command = parts[0].upper()

    if command == "SALIR":
        return "SALIR"

    if command in ("EVAL", "MOSTRAR"):
        if len(parts) < 3:
            raise ValueError(
                f"Comando '{command}' incompleto. Falta formato y/o expresión."
            )

        formato = parts[1].upper()
        exp_tokens = parts[2:]

        # Construye el arbol
        ast = build_ast(formato, exp_tokens)

        if command == "EVAL":
            # Evalua el arbol
            return ast.eval()
        elif command == "MOSTRAR":
            # Convertir a infijo
            return ast.to_infix()

    else:
        raise ValueError(f"Comando no reconocido: '{command}'")

# mi main que hace cosas principalmente tirar comandos
def main():

    print("Programa de Expresiones Aritméticas (PRE/POST)")
    print("Comandos: EVAL, MOSTRAR, SALIR")

    while True:
        try:
            linea = input("ACCION> ")

            resultado = process_line(linea)

            if resultado == "SALIR":
                print("Adios.")
                break
            elif resultado is not None:
                print(resultado)

        except EOFError:
            print("\nAdios.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
