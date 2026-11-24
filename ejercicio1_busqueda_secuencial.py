"""
Ejercicio 1: Método de Búsqueda Secuencial (Lineal)
Problema: Localización de tickets de soporte técnico activos en una mesa de ayuda,
donde los reportes ingresan en tiempo real y sin ordenamiento previo.
"""


def obtener_tickets_soporte() -> list[dict]:
    """Retorna la lista desordenada de tickets activos en turno."""
    return [
        {"id": 408, "usuario": "Carlos Mendez", "equipo": "PC-LAB-04", "falla": "Sin acceso a red"},
        {"id": 115, "usuario": "Ana Lopez", "equipo": "LAP-DOC-12", "falla": "Actualizacion de controlador"},
        {"id": 932, "usuario": "Luis Chan", "equipo": "PC-LAB-19", "falla": "Monitor sin senal"},
        {"id": 274, "usuario": "Ana Lopez", "equipo": "IMP-ADM-02", "falla": "Atasco de papel"},
        {"id": 651, "usuario": "Maria Pech", "equipo": "PC-LAB-08", "falla": "Error en compilador Python"},
        {"id": 519, "usuario": "Jorge Hau", "equipo": "SRV-AULA-01", "falla": "Disco al 95% de capacidad"},
    ]


def busqueda_secuencial_por_id(tickets: list[dict], id_buscado: int) -> tuple[dict | None, int]:
    """
    Recorre la lista elemento por elemento desde el índice 0 hasta encontrar
    el ticket con 'id_buscado'. Retorna (ticket_encontrado, comparaciones).
    """
    comparaciones = 0
    for ticket in tickets:
        comparaciones += 1
        if ticket["id"] == id_buscado:
            return ticket, comparaciones
    return None, comparaciones


def ejecutar_ejercicio_secuencial() -> None:
    """Interfaz de ejecución del Ejercicio 1 (Búsqueda Secuencial)."""
    tickets = obtener_tickets_soporte()
    print("\n--- EJERCICIO 1: BÚSQUEDA SECUENCIAL (TICKETS DE SOPORTE) ---")
    print("Tickets activos registrados (orden de llegada, sin ordenar por ID):")
    for t in tickets:
        print(f"  ID: {t['id']} | Usuario: {t['usuario']} | Equipo: {t['equipo']} | Falla: {t['falla']}")

    try:
        id_objetivo = int(input("\nIngrese el ID del ticket a buscar (ej. 651 o 999): ").strip())
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    resultado, pasos = busqueda_secuencial_por_id(tickets, id_objetivo)
    if resultado:
        print(f"[ENCONTRADO] Ticket #{resultado['id']} encontrado en {pasos} comparación(es):")
        print(f"  Usuario: {resultado['usuario']} | Equipo: {resultado['equipo']} | Falla: {resultado['falla']}")
    else:
        print(f"[NO ENCONTRADO] El ticket #{id_objetivo} no existe tras {pasos} comparación(es).")


if __name__ == "__main__":
    ejecutar_ejercicio_secuencial()
