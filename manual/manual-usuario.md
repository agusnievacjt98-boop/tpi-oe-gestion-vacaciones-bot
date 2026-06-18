# Manual de Usuario – Chatbot de Gestión de Vacaciones

Este manual explica cómo utilizar la simulación del chatbot desarrollada para gestionar solicitudes de vacaciones.  
El sistema funciona por consola y guía al usuario paso a paso durante el proceso.

---

## 1. Inicio del Sistema

Para iniciar la simulación:

1. Abrir una terminal o consola.
2. Posicionarse en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main.py

---

## 2. Ingreso del Legajo

El chatbot solicitará:

“Ingrese su número de legajo:”

El usuario debe escribir un número válido que exista en la base de datos simulada (empleados.xlsx).

Ejemplo:
Ingrese su número de legajo:
102
Si el legajo no existe, el sistema mostrará un mensaje de error y pedirá ingresarlo nuevamente.

```

---

## 3. Ingreso de Fechas

Una vez validado el legajo, el chatbot solicitará:

Fecha de inicio de vacaciones

Fecha de fin de vacaciones

El formato esperado es:
DD/MM/AAAA
Ejemplo:
Ingrese fecha de inicio:
10/07/2026

Ingrese fecha de fin:
20/07/2026
Si el formato es incorrecto, el sistema pedirá repetir la fecha.

---

## 4. Cálculo de Días Solicitados

El chatbot calculará automáticamente:

Cantidad total de días solicitados

Comparación con el saldo disponible del empleado

Ejemplo de salida:
Días solicitados: 10
Saldo disponible: 14

---

## 5. Resultado de la Solicitud

Según el saldo disponible, el sistema mostrará uno de los siguientes mensajes:

✔️ Solicitud aprobada
Código
Solicitud aprobada.
Cuenta con saldo suficiente.
❌ Solicitud rechazada
Código
Solicitud rechazada.
Los días solicitados superan el saldo disponible.

---

## 6. Fin del Proceso
El chatbot finalizará la interacción mostrando un mensaje de cierre:

Código
Gracias por utilizar el sistema de gestión de vacaciones.

---

## 7. Requisitos del Sistema
Python 3.10 o superior

Librería Pandas instalada

Archivo empleados.xlsx ubicado en la carpeta /data

---

## 8. Contacto
Para consultas sobre el funcionamiento del sistema, comunicarse con la autora:

Agustina Nieva – UTN TUP
