# Rafael Antonio Valera Pacheco 16-11202
import math

class DataType:
    def __init__(self, name):
        self.name = name

    def get_stats(self, strategy):
        """
        Retorna (tamaño, alineación, desperdicio) basado en la estrategia.
        Strategies: 'naive', 'packed', 'optimal'
        """
        raise NotImplementedError


class AtomicType(DataType):
    def __init__(self, name, size, alignment):
        super().__init__(name)
        self.size = int(size)
        self.alignment = int(alignment)

    def get_stats(self, strategy):
        # Para atómicos, el reordenamiento no aplica.
        align = 1 if strategy == "packed" else self.alignment
        return self.size, align, 0


class StructType(DataType):
    def __init__(self, name, fields):
        super().__init__(name)
        self.fields = fields  # Lista de objetos DataType 

    def get_stats(self, strategy):
        fields_to_process = self.fields[:]

        # Estrategia: Reordenando los campos de manera óptima
        # Se ordenan los campos por su alineación de mayor a menor
        if strategy == "optimal":
            fields_to_process.sort(key=lambda x: x.get_stats("naive")[1], reverse=True)

        current_offset = 0
        max_alignment = 1
        total_waste = 0

        for field in fields_to_process:
            f_size, f_align, f_waste = field.get_stats(strategy)

            # En modo packed, force alineación 1
            effective_align = 1 if strategy == "packed" else f_align
            max_alignment = max(max_alignment, effective_align)

            # Calcular padding necesario antes de este campo
            padding = (
                effective_align - (current_offset % effective_align)
            ) % effective_align

            current_offset += padding
            total_waste += (
                padding + f_waste
            )  # Padding actual + desperdicio interno del hijo
            current_offset += f_size

        # Padding final para alinear la estructura completa
        if strategy != "packed":
            if max_alignment > 0:
                final_padding = (
                    max_alignment - (current_offset % max_alignment)
                ) % max_alignment
            else:
                final_padding = 0
            current_offset += final_padding
            total_waste += final_padding
        else:
            max_alignment = 1

        return current_offset, max_alignment, total_waste


class UnionType(DataType):
    def __init__(self, name, fields):
        super().__init__(name)
        self.fields = fields

    def get_stats(self, strategy):
        # En una unión, todos los campos comienzan en el offset 0.
        # Tamaño = Tamaño del campo más grande (ajustado a alineación).
        # Alineación = Alineación del campo más restrictivo (mayor).

        max_size = 0
        max_align = 1

        # 1. Determinar el tamaño crudo más grande y la alineación más grande
        for field in self.fields:
            f_size, f_align, _ = field.get_stats(strategy)
            effective_align = 1 if strategy == "packed" else f_align

            if f_size > max_size:
                max_size = f_size
            if effective_align > max_align:
                max_align = effective_align

        # 2. Ajustar el tamaño total para que sea múltiplo de la alineación
        total_size = max_size
        padding = 0

        if strategy != "packed":
            if max_align > 0:
                padding = (max_align - (total_size % max_align)) % max_align
            total_size += padding
        else:
            max_align = 1

        # El desperdicio en Union se suele definir como el padding final de alineación.
        return total_size, max_align, padding


class TypeManager:
    def __init__(self):
        self.registry = {}

    def register_atomic(self, name, size, align):
        if name in self.registry:
            raise ValueError(f"El tipo '{name}' ya existe.")
        self.registry[name] = AtomicType(name, size, align)

    def register_struct(self, name, type_names):
        if name in self.registry:
            raise ValueError(f"El tipo '{name}' ya existe.")
        # Busca los tipos en el registro; si no existen, _get_type lanzará error
        fields = [self._get_type(tn) for tn in type_names]
        self.registry[name] = StructType(name, fields)

    def register_union(self, name, type_names):
        if name in self.registry:
            raise ValueError(f"El tipo '{name}' ya existe.")
        fields = [self._get_type(tn) for tn in type_names]
        self.registry[name] = UnionType(name, fields)

    def describe(self, name):
        if name not in self.registry:
            return f"Error: El tipo '{name}' no ha sido definido."

        dtype = self.registry[name]

        # Etiquetas 
        strategies = [
            ("Sin empaquetar", "naive"),
            ("Empaquetado", "packed"),
            ("Reordenando los campos de manera óptima", "optimal"),
        ]

        output = []
        output.append(f"Información del tipo '{name}':")
        for label, strat in strategies:
            size, align, wasted = dtype.get_stats(strat)
            output.append(
                f"  * {label}: Tamaño={size}, Alineación={align}, Desperdicio={wasted}"
            )

        return "\n".join(output)

    def _get_type(self, name):
        if name not in self.registry:
            raise ValueError(f"Tipo desconocido: '{name}'")
        return self.registry[name]
