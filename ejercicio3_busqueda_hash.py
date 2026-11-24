"""
Ejercicio 3: Método de Búsqueda Hash (Tabla Hash con Encadenamiento Separado)
Problema: Verificación instantánea de credenciales estudiantiles por matrícula
para el control de acceso al laboratorio de cómputo.
"""


class TablaHashEstudiantes:
    """Implementación de una Tabla Hash con resolución de colisiones por encadenamiento."""

    def __init__(self, capacidad: int = 7) -> None:
        self.capacidad = capacidad
        self.cubetas: list[list[dict]] = [[] for _ in range(capacidad)]

    def _funcion_hash(self, matricula: str) -> int:
        """Calcula el índice de cubeta mediante suma polinómica modular sobre la matrícula."""
        suma = 0
        for indice, caracter in enumerate(matricula):
            suma += ord(caracter) * (indice + 1)
        return suma % self.capacidad

    def insertar(self, estudiante: dict) -> None:
        """Inserta o actualiza un registro de estudiante en su cubeta correspondiente."""
        indice = self._funcion_hash(estudiante["matricula"])
        cubeta = self.cubetas[indice]

        for i, registro in enumerate(cubeta):
            if registro["matricula"] == estudiante["matricula"]:
                cubeta[i] = estudiante
                return
        cubeta.append(estudiante)

    def buscar(self, matricula: str) -> tuple[dict | None, int, int]:
        """
        Busca un estudiante por matrícula en O(1) promedio.
        Retorna (estudiante_encontrado, indice_cubeta, elementos_revisados_en_cubeta).
        """
        indice = self._funcion_hash(matricula)
        cubeta = self.cubetas[indice]
        revisados = 0

        for registro in cubeta:
            revisados += 1
            if registro["matricula"] == matricula:
                return registro, indice, revisados

        return None, indice, revisados


def construir_tabla_laboratorio() -> TablaHashEstudiantes:
    """Carga el padrón inicial de alumnos autorizados en la Tabla Hash."""
    tabla = TablaHashEstudiantes(capacidad=7)
    alumnos = [
        {"matricula": "E25080114", "nombre": "Joel de Jesus Chale Matu", "carrera": "Ing. Sistemas", "semestre": 3},
        {"matricula": "E25080239", "nombre": "Valeria Gomez Uc", "carrera": "Ing. Sistemas", "semestre": 3},
        {"matricula": "E24080412", "nombre": "Diego Armando Balam", "carrera": "Ing. Informatica", "semestre": 5},
        {"matricula": "E25080587", "nombre": "Fernanda Canul Ek", "carrera": "Ing. Sistemas", "semestre": 3},
        {"matricula": "E23080901", "nombre": "Rodrigo Perez Moo", "carrera": "Ing. Electronica", "semestre": 7},
        {"matricula": "E25080345", "nombre": "Sofia Tuz Dzib", "carrera": "Ing. Sistemas", "semestre": 3},
    ]
    for alumno in alumnos:
        tabla.insertar(alumno)
    return tabla


def ejecutar_ejercicio_hash() -> None:
    """Interfaz de ejecución del Ejercicio 3 (Búsqueda Hash)."""
    tabla = construir_tabla_laboratorio()
    print("\n--- EJERCICIO 3: BÚSQUEDA HASH (CONTROL DE ACCESO AL LABORATORIO) ---")
    print("Distribución actual de cubetas en la Tabla Hash (capacidad = 7):")
    for idx, cubeta in enumerate(tabla.cubetas):
        matriculas = [est["matricula"] for est in cubeta]
        print(f"  Cubeta [{idx}]: {matriculas}")

    matricula_objetivo = input("\nIngrese la matrícula a verificar (ej. E25080114 o E25089999): ").strip().upper()
    estudiante, cubeta_idx, pasos = tabla.buscar(matricula_objetivo)

    if estudiante:
        print(f"[ACCESO PERMITIDO] Matrícula {estudiante['matricula']} hallada en Cubeta [{cubeta_idx}] ({pasos} paso(s)):")
        print(f"  Alumno: {estudiante['nombre']} | Carrera: {estudiante['carrera']} | Semestre: {estudiante['semestre']}")
    else:
        print(f"[ACCESO DENEGADO] Matrícula {matricula_objetivo} no registrada (Cubeta [{cubeta_idx}], {pasos} paso(s)).")


if __name__ == "__main__":
    ejecutar_ejercicio_hash()
