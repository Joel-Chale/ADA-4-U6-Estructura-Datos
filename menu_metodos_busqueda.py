"""
Programa Principal con Menú Interactivo: Métodos de Búsqueda en Python
Integra y ejecuta los tres algoritmos investigados:
  1. Búsqueda Secuencial
  2. Búsqueda Binaria
  3. Búsqueda Hash
"""

from ejercicio1_busqueda_secuencial import ejecutar_ejercicio_secuencial
from ejercicio2_busqueda_binaria import ejecutar_ejercicio_binaria
from ejercicio3_busqueda_hash import ejecutar_ejercicio_hash


def mostrar_menu() -> None:
    """Despliega el menú principal de selección de métodos de búsqueda."""
    while True:
        print("\n=======================================================")
        print("      MENÚ PRINCIPAL - MÉTODOS DE BÚSQUEDA EN PYTHON")
        print("=======================================================")
        print("  1. Búsqueda Secuencial (Tickets de Soporte Técnico)")
        print("  2. Búsqueda Binaria (Catálogo de Componentes)")
        print("  3. Búsqueda Hash (Control de Acceso Estudiantil)")
        print("  4. Salir")
        print("=======================================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            ejecutar_ejercicio_secuencial()
        elif opcion == "2":
            ejecutar_ejercicio_binaria()
        elif opcion == "3":
            ejecutar_ejercicio_hash()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 4.")


if __name__ == "__main__":
    mostrar_menu()
