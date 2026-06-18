# Gestión de Vacaciones – Chatbot  
### Trabajo Práctico Integrador – Organización Empresarial (UTN – TUP)

Este repositorio contiene el desarrollo técnico del Trabajo Práctico Integrador (TPI) de la materia **Organización Empresarial**, cuyo objetivo es modelar, documentar y simular el proceso de **gestión de vacaciones** mediante un chatbot, alineado con un modelo BPMN 2.0.

---

## 1. Descripción del Proyecto

El proyecto consiste en la simulación de un chatbot que gestiona solicitudes de vacaciones.  
El bot permite:

- Solicitar el legajo del empleado  
- Validar el legajo contra una base de datos simulada  
- Solicitar fechas de inicio y fin  
- Calcular días solicitados  
- Comparar contra el saldo disponible  
- Aprobar o rechazar la solicitud  

El objetivo es **representar el proceso TO‑BE automatizado**, basado en el análisis del proceso AS‑IS manual.

---

## 2. Tecnologías Utilizadas

- **Python** (simulación del chatbot)
- **Pandas** (lectura de base de datos simulada)
- **Excel** (persistencia simulada)
- **BPMN 2.0** (modelado del proceso)
- **GitHub** (repositorio y documentación)

---

## 3. Estructura del Repositorio

tpi-oe-gestion-vacaciones-bot/
├─ README.md
├─ main.py
├─ requirements.txt
├─ data/
│  └─ empleados.xlsx
├─ docs/
│  ├─ bpmn-as-is.png
│  ├─ bpmn-to-be.png
│  └─ maquina-estados.png
└─ manual/
└─ manual-usuario.md


---

## 4. Diagramas BPMN

Los diagramas del proceso se encuentran en la carpeta **/docs**:

- **AS‑IS:** `docs/bpmn-as-is.png`  
- **TO‑BE:** `docs/bpmn-to-be.png`  
- **Máquina de estados:** `docs/maquina-estados.png`

---

## 5. Base de Datos Simulada

La base de datos se encuentra en:

data/empleados.xlsx


Contiene:

| Legajo | Nombre | Saldo_dias |
|--------|---------|-------------|
| 101 | Ana Pérez | 7 |
| 102 | Juan Soto | 14 |
| 103 | Agustina Nieva | 10 |

---

```markdown
## 6. Ejecución del Proyecto (Simulación)

Este proyecto **no implementa un bot real**, sino una **simulación por consola** del flujo conversacional.

Para ejecutarlo:

```bash
python main.py

## 7. Lógica del Chatbot (main.py)
El archivo main.py contiene:

Validación de legajo

Solicitud de fechas

Cálculo de días

Comparación con saldo disponible

Aprobación o rechazo

---

## 8. Manual de Usuario
Disponible en:
 manual/manual-usuario.md
Incluye:

Cómo iniciar la solicitud

Cómo ingresar legajo

Cómo ingresar fechas

Ejemplos de aprobación y rechazo

---

## 9. Autora
Nombre: Agustina Nieva
Carrera: Tecnicatura Universitaria en Programación
Materia: Organización Empresarial
Año: 2026
