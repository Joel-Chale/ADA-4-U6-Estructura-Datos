"""
Ejercicio 2: Método de Búsqueda Binaria
Problema: Consulta rápida de componentes electrónicos en un catálogo de almacén
previamente ordenado de forma ascendente por código numérico de pieza.
"""


def obtener_catalogo_ordenado() -> list[dict]:
    """Retorna el catálogo estático ordenado ascendentemente por 'codigo'."""
    return [
        {"codigo": 1012, "nombre": "Resistencia 10k Ohm", "pasillo": "A1", "precio": 2.50},
        {"codigo": 1045, "nombre": "Capacitor Electrolitico 100uF", "pasillo": "A2", "precio": 5.00},
        {"codigo": 1108, "nombre": "Diodo Rectificador 1N4007", "pasillo": "A4", "precio": 3.00},
        {"codigo": 1230, "nombre": "Microcontrolador ESP32", "pasillo": "B1", "precio": 145.00},
        {"codigo": 1350, "nombre": "Sensor Ultrasonico HC-SR04", "pasillo": "B3", "precio": 42.00},
        {"codigo": 1490, "nombre": "Modulo Rele 2 Canales 5V", "pasillo": "C1", "precio": 55.00},
        {"codigo": 1625, "nombre": "Pantalla OLED I2C 0.96", "pasillo": "C2", "precio": 98.00},
        {"codigo": 1780, "nombre": "Fuente Regulada 12V 2A", "pasillo": "D1", "precio": 160.00},
        {"codigo": 1910, "nombre": "Protoboard 830 Puntos", "pasillo": "D3", "precio": 75.00},
    ]


def busqueda_binaria_pieza(catalogo: list[dict], codigo_buscado: int) -> tuple[dict | None, int]:
    """
    Busca 'codigo_buscado' dividiendo el espacio de búsqueda a la mitad en cada paso.
    Retorna (pieza_encontrada, comparaciones_realizadas).
    """
    izquierda = 0
    derecha = len(catalogo) - 1
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        codigo_actual = catalogo[medio]["codigo"]

        if codigo_actual == codigo_buscado:
            return catalogo[medio], comparaciones
        elif codigo_actual < codigo_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None, comparaciones


def ejecutar_ejercicio_binaria() -> None:
    """Interfaz de ejecución del Ejercicio 2 (Búsqueda Binaria)."""
    catalogo = obtener_catalogo_ordenado()
    print("\n--- EJERCICIO 2: BÚSQUEDA BINARIA (CATÁLOGO DE COMPONENTES) ---")
    print("Catálogo ordenado por código de pieza:")
    for item in catalogo:
        print(f"  Código: {item['codigo']} | {item['nombre']} | Pasillo: {item['pasillo']} | ${item['precio']:.2f}")

    try:
        codigo_objetivo = int(input("\nIngrese el código de pieza a buscar (ej. 1625 o 1500): ").strip())
    except ValueError:
        print("Entrada inválida. Debe ingresar un código numérico entero.")
        return

    pieza, pasos = busqueda_binaria_pieza(catalogo, codigo_objetivo)
    if pieza:
        print(f"[ENCONTRADO] Pieza {pieza['codigo']} localizada en {pasos} comparación(es):")
        print(f"  Nombre: {pieza['nombre']} | Pasillo: {pieza['pasillo']} | Precio: ${pieza['precio']:.2f}")
    else:
        print(f"[NO ENCONTRADO] El código {codigo_objetivo} no está en el catálogo ({pasos} comparación(es)).")


if __name__ == "__main__":
    ejecutar_ejercicio_binaria()
