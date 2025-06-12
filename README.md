# Prueba Técnica · Samuel Orduña  
**Puesto: Coordinador de Proyectos de Recursos Humanos**

Este repositorio contiene la solución estructurada a la prueba técnica para el puesto de **Coordinador de Proyectos RH**, con foco en **automatización de procesos**, **análisis de datos** y **manejo eficiente de información** usando herramientas como:

- 🐍 **Python 3.10+**
- 📊 **Pandas**, **NumPy**
- 📁 Procesamiento de archivos **CSV** y **Excel**

---

## Estructura del repositorio

Cada ejercicio fue resuelto en una **rama independiente** y documentado por separado. Este enfoque permite:

- Separar claramente la lógica de cada solución.
- Facilitar su validación y revisión.

📄 [Haz clic aquí para abrir la prueba técnica en PDF](./Prueba_tecnica_2025.pdf)
![Estructura del proyecto](./392c4713-b1a1-4b8c-b4ee-c1dd30cb960c.png)
---

## Ejercicio 1 – Formateo de nombres

Se resolvió el problema de transformar nombres desordenados en formato:  
**`Nombre(s) ApellidoPaterno ApellidoMaterno`**, preservando la `Clave Única` como texto.

Se implementaron **dos versiones comparativas**:

| Enfoque         | Archivo                        | Características principales                                   |
|-----------------|--------------------------------|---------------------------------------------------------------|
| Funcional       | `ejercicio_1_funcional.py`     | Lógica directa y vectorizada con `pandas`                     |
| Modular (SOLID) | `ejercicio_1_SOLID.py`         | Separación clara de responsabilidades en funciones pequeñas   |

Salidas:
- `resultado_funcional_ejercicio_1.xlsx`
- `resultado_ejercicio_1_SOLID.xlsx`

Ver análisis comparativo en [`ejercicio_1_README.md`](./ejercicio-1/ejercicio_1_README.md)

---

## Ejercicio 2 – Unión de correos

Se tomó el archivo de nombres completos del Ejercicio 1 y se integraron los correos por `Clave Única`, cuidando el tipo de dato y realizando un merge tipo **LEFT JOIN**.

Archivos involucrados:
- `correos.csv`
- `resultado_funcional_ejercicio_1.xlsx`

Salida generada:  
`resultado_ejercicio_2.xlsx`

Detalles en [`ejercicio_2_README.md`](./ejercicio-2/ejercicio_2_README.md)

---

## Ejercicio 3 – Cálculo de antigüedad

Se calculó la antigüedad acumulada de profesores a partir de su historial de clases por año, considerando las siguientes reglas:

- `1` = año completo
- `0.5` = un semestre
- Si pasan **más de 4 años sin actividad**, la antigüedad **se reinicia**.

Archivos:
- `matriz_antiguedad.xlsx`
- `resultado_ejercicio_2.xlsx`

Salida:  
`resultado_ejercicio_3.xlsx`

Explicación completa en [`ejercicio_3_README.md`](./ejercicio-3/ejercicio_3_README.md)

---

## Ejercicio 4 – Actualización con datos 2024

Este ejercicio actualiza la matriz de antigüedad con la información del año 2024 y detecta profesores nuevos.

Pasos clave:
- Limpieza y estandarización de encabezados (`2024` en vez de `2,024`)
- Unificación de datos por `Clave Única`
- Detección de profesores **que no estaban** en la matriz original

Archivos generados:
- `matriz_antiguedad_actualizada.xlsx`
- `profesores_nuevos_2024.xlsx`

Ver detalles técnicos en [`ejercicio_4_README.md`](./ejercicio-4/ejercicio_4_README.md)

---

## Notas adicionales

- Cada script fue validado para evitar errores comunes con claves numéricas (`Clave Unica`), encoding (`UTF-8`, `Windows-1252`) y formatos.
- Solo en el **Ejercicio 1** se incluyó una versión con principios **SOLID**, para demostrar habilidades en diseño limpio y escalable(:
- El resto de los ejercicios opta por soluciones más directas, suponiendo entornos con menor cambio y menor necesidad de modularidad.

---

## Agradecimiento

Gracias por la oportunidad de participar en este proceso.  
Espero que mis soluciones les resulten prácticas, limpias y bien documentadas.  

¡Estoy entusiasmado por esta oportunidad de aplicar al puesto de Coordinador de Proyectos de Recursos Humanos!

Saludos cordiales,
~Samuel Orduña.

[![Gracias <3](https://c.tenor.com/nQXlXRZLWgIAAAAd/tenor.gif)](https://youtube.com/shorts/JUKsboPi-Mo?si=_KGIUloB3bYSZfNs)