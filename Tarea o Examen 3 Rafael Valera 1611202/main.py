# Rafael Antonio Valera Pacheco 16-11202
import sys

from manager import TypeManager

def main():
    manager = TypeManager()
    print("--- Simulador de Manejador de Tipos de Datos ---")
    print("Comandos disponibles: ATOMICO, STRUCT, UNION, DESCRIBIR, SALIR")

    while True:
        try:
            # Requisito 
            line = input("> ").strip()
            if not line:
                continue

            parts = line.split()
            command = parts[0].upper()

            # Requisito V: SALIR
            if command == "SALIR":
                print("Saliendo del simulador.")
                break

            # Requisito I: ATOMICO
            elif command == "ATOMICO":
                if len(parts) != 4:
                    print("Error: Uso -> ATOMICO <nombre> <bytes> <alineación>")
                    continue
                try:
                    name, size, align = parts[1], parts[2], parts[3]
                    manager.register_atomic(name, size, align)
                    print(f"Tipo atómico '{name}' definido exitosamente.")
                except ValueError as e:
                    print(f"Error: {e}")

            # Requisito II: STRUCT
            elif command == "STRUCT":
                if len(parts) < 3:
                    print("Error: Uso -> STRUCT <nombre> <tipo> [<tipo>...]")
                    continue
                try:
                    name = parts[1]
                    field_types = parts[2:]
                    manager.register_struct(name, field_types)
                    print(f"Registro (Struct) '{name}' definido exitosamente.")
                except ValueError as e:
                    print(f"Error: {e}")

            # Requisito III: UNION
            elif command == "UNION":
                if len(parts) < 3:
                    print("Error: Uso -> UNION <nombre> <tipo> [<tipo>...]")
                    continue
                try:
                    name = parts[1]
                    field_types = parts[2:]
                    manager.register_union(name, field_types)
                    print(f"Registro variante (Union) '{name}' definido exitosamente.")
                except ValueError as e:
                    print(f"Error: {e}")

            # Requisito IV: DESCRIBIR
            elif command == "DESCRIBIR":
                if len(parts) != 2:
                    print("Error: Uso -> DESCRIBIR <nombre>")
                    continue
                
                print(manager.describe(parts[1]))

            else:
                print(f"Comando '{command}' no reconocido.")

        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
