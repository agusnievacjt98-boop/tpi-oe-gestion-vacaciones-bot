

### 3. Esqueleto simple de `main.py` (simulación por consola)

# main.py
# Simulación de chatbot de gestión de vacaciones

empleados = {
    "101": {"nombre": "Ana Perez", "saldo_dias": 7},
    "102": {"nombre": "Juan Soto", "saldo_dias": 14},
    "103": {"nombre": "Agustina Nieva", "saldo_dias": 10},
}

def validar_legajo(legajo):
    return legajo in empleados

def calcular_dias(fecha_inicio, fecha_fin):
    # Simulación: no calculamos fechas reales, solo pedimos un número
    try:
        dias = int(input("Ingresá la cantidad de días solicitados: "))
        return dias
    except ValueError:
        print("El valor debe ser numérico.")
        return None

def main():
    print("=== Chatbot Gestión de Vacaciones (Simulación) ===")
    legajo = input("Ingresá tu legajo: ")

    if not validar_legajo(legajo):
        print("Legajo inválido. Fin del proceso.")
        return

    empleado = empleados[legajo]
    print(f"Hola, {empleado['nombre']}. Tenés {empleado['saldo_dias']} días disponibles.")

    fecha_inicio = input("Ingresá fecha de inicio (dd/mm): ")
    fecha_fin = input("Ingresá fecha de fin (dd/mm): ")

    dias_solicitados = calcular_dias(fecha_inicio, fecha_fin)
    if dias_solicitados is None:
        print("No se pudo procesar la solicitud.")
        return

    if dias_solicitados <= empleado["saldo_dias"]:
        print(f"Solicitud aprobada por {dias_solicitados} días.")
    else:
        print("No tenés saldo suficiente para esa cantidad de días.")

if __name__ == "__main__":
    main()
