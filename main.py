# main.py
# Simulación de chatbot de gestión de vacaciones
# TPI – Organización Empresarial – UTN TUP
# Autora: Agustina Nieva
#
# Implementa una Máquina de Estados explícita:
# INICIO → ESPERANDO_LEGAJO → VALIDANDO_LEGAJO → ESPERANDO_FECHA_INICIO
# → ESPERANDO_FECHA_FIN → CALCULANDO → EVALUANDO_SALDO → APROBADO / RECHAZADO

from datetime import datetime

# ─────────────────────────────────────────────
# BASE DE DATOS SIMULADA (reemplaza al Excel)
# ─────────────────────────────────────────────
empleados = {
    "101": {"nombre": "Ana Pérez",       "saldo_dias": 7},
    "102": {"nombre": "Juan Soto",       "saldo_dias": 14},
    "103": {"nombre": "Agustina Nieva",  "saldo_dias": 10},
}

# ─────────────────────────────────────────────
# ESTADOS DE LA MÁQUINA
# ─────────────────────────────────────────────
INICIO               = "INICIO"
ESPERANDO_LEGAJO     = "ESPERANDO_LEGAJO"
ESPERANDO_FECHA_INI  = "ESPERANDO_FECHA_INICIO"
ESPERANDO_FECHA_FIN  = "ESPERANDO_FECHA_FIN"
EVALUANDO_SALDO      = "EVALUANDO_SALDO"
APROBADO             = "APROBADO"
RECHAZADO            = "RECHAZADO"

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def parsear_fecha(texto):
    """Intenta parsear una fecha en formato DD/MM/AAAA.
    Retorna un objeto datetime o None si el formato es inválido."""
    try:
        return datetime.strptime(texto.strip(), "%d/%m/%Y")
    except ValueError:
        return None

def calcular_dias_habiles(inicio, fin):
    """Calcula la cantidad de días corridos entre dos fechas (inclusive)."""
    delta = (fin - inicio).days + 1
    return delta

# ─────────────────────────────────────────────
# FUNCIÓN PRINCIPAL – SIMULACIÓN DEL CHATBOT
# ─────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  CHATBOT – GESTIÓN DE VACACIONES (Simulación)")
    print("=" * 50)
    print("Escribí 'salir' en cualquier momento para cancelar.\n")

    # ── Estado inicial ──────────────────────────────
    estado = INICIO
    contexto = {}   # guarda legajo, empleado, fechas

    # ── INICIO → pedir activación ───────────────────
    activacion = input("Escribí 'Vacaciones' para iniciar: ").strip().lower()
    if activacion != "vacaciones":
        print("Comando no reconocido. Escribí 'Vacaciones' para comenzar.")
        return

    estado = ESPERANDO_LEGAJO

    # ── Loop principal de la máquina de estados ─────
    while estado not in (APROBADO, RECHAZADO):

        # ── ESPERANDO_LEGAJO ────────────────────────
        if estado == ESPERANDO_LEGAJO:
            legajo = input("\nIngresá tu número de legajo: ").strip()

            if legajo.lower() == "salir":
                print("Proceso cancelado.")
                return

            # Camino infeliz 1: no es numérico
            if not legajo.isdigit():
                print("⚠ El legajo debe ser numérico. Intentá de nuevo.")
                continue  # vuelve a ESPERANDO_LEGAJO

            # Camino infeliz 2: legajo no existe en BD
            if legajo not in empleados:
                print(f"⚠ No encontré el legajo {legajo} en el sistema. Verificá el número.")
                continue  # vuelve a ESPERANDO_LEGAJO

            # Camino feliz: legajo válido
            contexto["legajo"]   = legajo
            contexto["empleado"] = empleados[legajo]
            emp = contexto["empleado"]
            print(f"\n✅ Legajo válido. Hola, {emp['nombre']}.")
            print(f"   Tenés {emp['saldo_dias']} días disponibles.")
            estado = ESPERANDO_FECHA_INI

        # ── ESPERANDO_FECHA_INICIO ──────────────────
        elif estado == ESPERANDO_FECHA_INI:
            raw = input("\nIngresá la fecha de INICIO (DD/MM/AAAA): ").strip()

            if raw.lower() == "salir":
                print("Proceso cancelado.")
                return

            fecha = parsear_fecha(raw)
            if fecha is None:
                print("⚠ Formato inválido. Usá DD/MM/AAAA (ej: 10/07/2025).")
                continue

            contexto["fecha_inicio"] = fecha
            estado = ESPERANDO_FECHA_FIN

        # ── ESPERANDO_FECHA_FIN ─────────────────────
        elif estado == ESPERANDO_FECHA_FIN:
            raw = input("Ingresá la fecha de FIN     (DD/MM/AAAA): ").strip()

            if raw.lower() == "salir":
                print("Proceso cancelado.")
                return

            fecha = parsear_fecha(raw)
            if fecha is None:
                print("⚠ Formato inválido. Usá DD/MM/AAAA (ej: 15/07/2025).")
                continue

            # Camino infeliz 3: fecha fin anterior a fecha inicio
            if fecha < contexto["fecha_inicio"]:
                print("⚠ La fecha de fin debe ser posterior a la de inicio. Ingresalas de nuevo.")
                estado = ESPERANDO_FECHA_INI   # reinicia desde fecha inicio
                continue

            # Camino infeliz 4: misma fecha inicio y fin (0 días útiles en algunos criterios)
            dias = calcular_dias_habiles(contexto["fecha_inicio"], fecha)
            if dias <= 0:
                print("⚠ Las fechas no generan días válidos. Intentá de nuevo.")
                estado = ESPERANDO_FECHA_INI
                continue

            contexto["fecha_fin"]       = fecha
            contexto["dias_solicitados"] = dias
            estado = EVALUANDO_SALDO

        # ── EVALUANDO_SALDO ─────────────────────────
        elif estado == EVALUANDO_SALDO:
            emp            = contexto["empleado"]
            dias_sol       = contexto["dias_solicitados"]
            saldo          = emp["saldo_dias"]
            fi             = contexto["fecha_inicio"].strftime("%d/%m/%Y")
            ff             = contexto["fecha_fin"].strftime("%d/%m/%Y")

            print(f"\n   Días solicitados : {dias_sol}")
            print(f"   Saldo disponible : {saldo}")

            if dias_sol <= saldo:
                # Actualizar saldo en la BD simulada
                empleados[contexto["legajo"]]["saldo_dias"] -= dias_sol
                estado = APROBADO
            else:
                estado = RECHAZADO

    # ── Resultados finales ──────────────────────────
    emp   = contexto["empleado"]
    dias  = contexto["dias_solicitados"]
    fi    = contexto["fecha_inicio"].strftime("%d/%m/%Y")
    ff    = contexto["fecha_fin"].strftime("%d/%m/%Y")

    print("\n" + "=" * 50)
    if estado == APROBADO:
        saldo_restante = empleados[contexto["legajo"]]["saldo_dias"]
        print(f"✅ SOLICITUD APROBADA")
        print(f"   Período  : {fi} al {ff}")
        print(f"   Días     : {dias}")
        print(f"   Saldo restante: {saldo_restante} días")
    else:
        saldo = emp["saldo_dias"]
        print(f"❌ SOLICITUD RECHAZADA")
        print(f"   Solicitaste {dias} días pero solo tenés {saldo} disponibles.")
        print(f"   Podés solicitar hasta {saldo} días, o consultar con RRHH sobre anticipos.")
    print("=" * 50)


if __name__ == "__main__":
    main()
