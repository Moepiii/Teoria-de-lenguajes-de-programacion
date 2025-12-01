Rafael Antonio Valera Pacheco 16-11202
# Simulador de Manejador de Tipos de Datos

Este Ejercicio en Python simula la gestión de memoria de bajo nivel (similar a C/C++). El programa permite definir tipos de datos atómicos, estructuras (structs) y uniones, calculando automáticamente su **tamaño**, **alineación** y **desperdicio (padding)** bajo diferentes estrategias de optimización de memoria.


## Estructura del Proyecto

El proyecto consta de tres archivos principales:

### 1\. `manager.py` (Lógica del Sistema)

 Contiene las clases que modelan los tipos de datos y la lógica matemática para calcular la alineación.

  * **Clases Principales:**
      * `AtomicType`: Maneja tipos primitivos (int, char, double).
      * `StructType`: Maneja registros. Calcula el padding interno y final necesario para mantener la alineación.
      * `UnionType`: Maneja uniones. Calcula el tamaño basándose en el campo más grande.
      * `TypeManager`: Actúa como controlador principal, almacenando los tipos en un diccionario y gestionando su creación.
  * **Funcionalidad Clave:**
      * Implementa el método `get_stats(strategy)` que acepta tres estrategias:
        1.  `naive`: Alineación estándar con padding (como estoy usando python mi simulador va a ser con comportamientos de C).
        2.  `packed`: Elimina todo el padding (alineación = 1).
        3.  `optimal`: Reordena los campos del struct de mayor a menor alineación para minimizar el desperdicio.

### 2\. `main.py` (Interfaz de Usuario)

 Proporciona una interfaz de línea de comandos interactiva.

  * **Funciones:**
      * Inicia un bucle infinito (`while True`) esperando comandos.
      * Parsea la entrada del usuario (`ATOMICO`, `STRUCT`, `UNION`, `DESCRIBIR`).
      * Maneja errores de entrada y excepciones (ej. intentar definir un struct con tipos que no existen).
      * Termina la ejecución con el comando `SALIR`.

### 3\. `tests.py` (Pruebas Unitarias )

 Es un Script de aseguramiento de calidad diseñado para validar que la lógica de `manager.py` sea correcta.

  * **Contenido:**
      * Utiliza la librería estándar `unittest`.
      * Incluye casos de prueba para: Alineación simple, structs anidados, comportamiento de uniones, algoritmo de reordenamiento óptimo y manejo de errores.
      * **Reporte:** Al finalizar, genera un cuadro visual con el porcentaje de éxito (Cobertura funcional).

## 🚀 Cómo Ejecutar el Programa

Debe tener Python 3 instalado. Abre la  terminal en la carpeta del proyecto.

### A. Ejecutar el Simulador

Para iniciar el programa principal y definir tus propios tipos:

```bash
python main.py
```

**Ejemplo de sesión interactiva:**

```text
> ATOMICO int 4 4
Tipo atómico 'int' definido exitosamente.

> ATOMICO char 1 1
Tipo atómico 'char' definido exitosamente.

> STRUCT mi_registro char int char
Registro (Struct) 'mi_registro' definido exitosamente.

> DESCRIBIR mi_registro
Información del tipo 'mi_registro':
  * Sin empaquetar: Tamaño=12, Alineación=4, Desperdicio=6
  * Empaquetado: Tamaño=6, Alineación=1, Desperdicio=0
  * Reordenando los campos de manera óptima: Tamaño=8, Alineación=4, Desperdicio=2
```

### B. Ejecutar las Pruebas Unitarias

Para verificar que todo el código funciona correctamente y ver el reporte de cobertura:

```bash
python tests.py
```

**Salida esperada:**

```text
============================================================
       REPORTE DE PRUEBAS UNITARIAS
============================================================
Total de pruebas  : 6
Pruebas exitosas  : 6
Fallos / Errores  : 0
------------------------------------------------------------
PORCENTAJE DE ÉXITO: 100.00%
============================================================
```

-----

## 📚 Comandos Disponibles

Una vez dentro de `main.py`, puedes usar los siguientes comandos:

1.  **`ATOMICO <nombre> <tamaño> <alineación>`**

      * Define un tipo base.
      * Ejemplo: `ATOMICO int 4 4`

2.  **`STRUCT <nombre> <tipo1> <tipo2> ...`**

      * Crea una estructura con una lista de tipos existentes.
      * Ejemplo: `STRUCT punto int int`

3.  **`UNION <nombre> <tipo1> <tipo2> ...`**

      * Crea una unión donde todos los campos comparten memoria.
      * Ejemplo: `UNION dato int char`

4.  **`DESCRIBIR <nombre>`**

      * Muestra el análisis de memoria (Tamaño, Alineación y Desperdicio) bajo las tres estrategias (Naive, Packed, Optimal).

5.  **`SALIR`**

      * Cierra el programa.

-----

## 📋 Detalles de las Estrategias

  * **Sin empaquetar (Naive):** Simula un compilador de C estándar. Inserta bytes de relleno (padding) entre campos para respetar la alineación de cada tipo, y al final de la estructura para respetar la alineación total.
  * **Empaquetado (Packed):** Simula la directiva `__attribute__((packed))` de GCC. Fuerza la alineación a 1 byte, eliminando todo el desperdicio, pero con penalización de rendimiento en hardware real.
  * **Reordenamiento Óptimo:** Algoritmo que ordena los campos internos del struct descendentemente por su requerimiento de alineación (`double` -\> `int` -\> `short` -\> `char`). Esto minimiza matemáticamente el padding necesario.