# Gestión de Vacaciones – Chatbot (TPI Organización Empresarial)

Este repositorio corresponde al Trabajo Práctico Integrador de la materia **Organización Empresarial** (UTN – TUP).

El objetivo es modelar y simular el proceso de **gestión de vacaciones** mediante un chatbot, alineado con un modelo BPMN 2.0.

## 1. Descripción del proyecto

El bot simula el flujo de solicitud de vacaciones:

- El usuario inicia el chat.
- Ingresa su legajo.
- El sistema valida el legajo contra una base de datos simulada (Excel).
- El usuario ingresa fechas de inicio y fin.
- El bot calcula los días solicitados y verifica el saldo disponible.
- Si alcanza el saldo → aprueba y registra.
- Si no alcanza → rechaza y ofrece alternativas.

## 2. Tecnologías propuestas

- **Lenguaje:** Python
- **Plataforma objetivo:** Telegram (simulado)
- **Librerías posibles:**
  - `python-telegram-bot` (para una implementación real)
  - `pandas` (para leer la base de datos simulada en Excel)

## 3. Estructura del repositorio

- `main.py`: esqueleto del bot (simulación de flujo).
- `data/empleados.xlsx`: base de datos simulada con legajo, nombre y saldo de días.
- `docs/`: diagramas BPMN (AS-IS, TO-BE, máquina de estados).
- `manual/`: manual de usuario del bot.

## 4. Ejecución (simulada)

Este proyecto se plantea como **simulación** del proceso. El archivo `main.py` contiene un flujo por consola que representa la lógica del chatbot.

```bash
python main.py


## 5. Autora

**Nombre:** Agustina Nieva  
**Carrera:** Tecnicatura Universitaria en Programación  
**Materia:** Organización Empresarial  
**Año:** 2026
