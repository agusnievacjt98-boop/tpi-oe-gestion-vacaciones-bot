
# Chatbot – Gestión de Vacaciones

### Trabajo Práctico Integrador – Organización Empresarial (UTN – TUP)

> Autora: **Agustina Nieva** · Materia: Organización Empresarial · Año: 2026

Este repositorio contiene el desarrollo técnico del TPI cuyo objetivo es modelar, documentar y simular el proceso de **gestión de solicitudes de vacaciones** mediante un chatbot, alineado con un modelo BPMN 2.0.

---

## 1. Descripción del Proyecto

### Enfoque sistémico

La organización analizada es una **empresa mediana de servicios** con área de RRHH propia. Desde la perspectiva de la Teoría General de Sistemas se trata de un **sistema abierto**:

| Componente | Descripción |
|---|---|
| **Entradas** | Solicitud del empleado (legajo, fechas), saldo de días disponibles |
| **Procesos** | Validación de legajo, verificación de saldo, cálculo de días, registro |
| **Salidas** | Aprobación o rechazo, actualización del saldo |
| **Retroalimentación** | El saldo actualizado es la nueva entrada para solicitudes futuras |
| **Entorno** | Legislación laboral, calendario institucional, plataforma tecnológica |

### Áreas involucradas

- **Empleados** → generan la solicitud
- **RRHH / Bot** → validan, calculan y deciden

### Qué hace el bot

- Solicita y valida el número de legajo del empleado
- Consulta el saldo de días disponibles en la base de datos simulada
- Solicita y valida las fechas de inicio y fin
- Calcula los días solicitados con fechas reales
- Aprueba o rechaza la solicitud según el saldo disponible
- Actualiza el saldo al aprobar
- Maneja todos los errores de entrada (camino infeliz)

---

## 2. Tecnologías Utilizadas

- **Python 3** – simulación del chatbot por consola
- **datetime** (stdlib) – cálculo real de días entre fechas
- **BPMN 2.0** – modelado del proceso AS-IS y TO-BE
- **GitHub** – repositorio y documentación

> Para una versión productiva se reemplazaría el diccionario interno por `pandas` + `empleados.xlsx` y el input por consola por la API de Telegram (`python-telegram-bot`).

---

## 3. Estructura del Repositorio

```
tpi-oe-gestion-vacaciones-bot/
├── README.md
├── main.py               ← simulación del chatbot
├── requirements.txt
├── data/
│   └── empleados.xlsx    ← BD simulada (referencia)
├── docs/
│   ├── bpmn-as-is.jpeg
│   ├── bpmn-to-be.jpeg
│   └── maquina-estados.png
└── manual/
    └── manual-usuario.md
```

---

## 4. Diagramas BPMN

Los diagramas se encuentran en **/docs** y siguen la notación estándar BPMN 2.0:
- Pool único con dos **carriles (lanes)**: Usuario y RRHH/Bot
- El flujo **cruza entre carriles** representando la interacción real
- Dos **gateways exclusivos** (rombos) con exactamente dos ramas de salida cada uno

| AS-IS (proceso manual) | TO-BE (proceso automatizado) |
|---|---|
| ![AS-IS](docs/bpmn-as-is.1.jpeg) | ![TO-BE](docs/bpmn-to-be.1.jpeg) |

---

## 5. Base de Datos Simulada

Archivo: `data/empleados.xlsx`

| Legajo | Nombre | Saldo_dias |
|--------|--------|-----------|
| 101 | Ana Pérez | 7 |
| 102 | Juan Soto | 14 |
| 103 | Agustina Nieva | 10 |

---

## 6. Máquina de Estados

El bot implementa una **máquina de estados explícita** que le permite recordar en qué paso del proceso se encuentra el usuario:

```
INICIO
  └─▶ ESPERANDO_LEGAJO
        ├─ legajo inválido/inexistente ──▶ vuelve a ESPERANDO_LEGAJO
        └─ legajo válido ──▶ ESPERANDO_FECHA_INICIO
              └─▶ ESPERANDO_FECHA_FIN
                    ├─ fecha inválida / fin < inicio ──▶ vuelve a ESPERANDO_FECHA_INICIO
                    └─ fechas ok ──▶ EVALUANDO_SALDO
                          ├─ saldo suficiente ──▶ APROBADO → Fin
                          └─ saldo insuficiente ──▶ RECHAZADO → Fin
```

---

## 7. Caminos de Ejecución

### ✅ Camino Feliz

1. Usuario escribe `Vacaciones`
2. Ingresa legajo válido (ej: `102`)
3. Ingresa fechas válidas (ej: `10/07/2025` al `15/07/2025`)
4. Saldo suficiente → solicitud **aprobada**, saldo actualizado

```
=== Chatbot Gestión de Vacaciones (Simulación) ===
Escribí 'Vacaciones' para iniciar: Vacaciones
Ingresá tu número de legajo: 102
✅ Legajo válido. Hola, Juan Soto. Tenés 14 días disponibles.
Ingresá la fecha de INICIO (DD/MM/AAAA): 10/07/2025
Ingresá la fecha de FIN     (DD/MM/AAAA): 15/07/2025
   Días solicitados : 6
   Saldo disponible : 14
✅ SOLICITUD APROBADA
   Período  : 10/07/2025 al 15/07/2025
   Días     : 6
   Saldo restante: 8 días
```

### ❌ Caminos Infelices

| Error | Respuesta del bot | Acción |
|---|---|---|
| Legajo no numérico | `⚠ El legajo debe ser numérico.` | Vuelve a pedir legajo |
| Legajo inexistente | `⚠ No encontré el legajo X.` | Vuelve a pedir legajo |
| Formato fecha incorrecto | `⚠ Formato inválido. Usá DD/MM/AAAA.` | Vuelve a pedir esa fecha |
| Fecha fin < fecha inicio | `⚠ La fecha de fin debe ser posterior...` | Reinicia desde fecha inicio |
| Saldo insuficiente | `❌ Solicitaste X días pero solo tenés Y.` | Informa alternativas |

---

## 8. Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/agusnievacjt98-boop/tpi-oe-gestion-vacaciones-bot.git
cd tpi-oe-gestion-vacaciones-bot

# Ejecutar la simulación (no requiere dependencias externas)
python main.py
```

> Para cancelar en cualquier momento escribí `salir`.

---

## 9. Manual de Usuario

Disponible en [`manual/manual-usuario.md`](manual/manual-usuario.md).  
Incluye comandos, ejemplos de aprobación y rechazo, y manejo de errores.

---

## 10. Autora

**Agustina Nieva**  
Tecnicatura Universitaria en Programación · UTN  
Materia: Organización Empresarial · 2025/2026
