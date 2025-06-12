# Ejercicio 3 – Cálculo de antigüedad con reinicios

Este script resuelve el tercer ejercicio de la prueba técnica. A partir del historial de clases impartidas por año (`matriz_antiguedad.xlsx`), se calcula la antigüedad acumulada de cada profesor, aplicando reglas especiales cuando existe un periodo prolongado de inactividad.

---

## Archivos utilizados

- `matriz_antiguedad.xlsx`: contiene las claves únicas y los años en los que cada profesor dio clase (valor 1 o 0.5).
- `../ejercicio-2/resultado_ejercicio_2.xlsx`: contiene el nombre completo y correo electrónico de cada profesor.

---

## Reglas implementadas

- `1` = el profesor dio clase **todo el año** (dos semestres).
- `0.5` = solo dio clase en **un semestre**.
- Si un profesor acumula **más de 4 años consecutivos sin dar clase**, se considera una ruptura y su antigüedad se reinicia desde cero.
- Si existió al menos un reinicio, se registra el comentario: **"Se reinició la antigüedad"**.

---

## Descripción de la solución

1. **Carga de archivos**: se leen los historiales y la información de contacto.
2. **Cálculo por profesor**:
   - Se recorre cronológicamente el historial.
   - Se acumula la antigüedad.
   - Si hay 5 o más años sin clase, se reinicia el conteo.
3. **Fusión de resultados**: se unen los datos con nombre y correo por clave única.
4. **Exportación**: el resultado final se guarda en `resultado_ejercicio_3.xlsx`.

---

## Notas técnicas

- El cálculo se realiza sin estructuras cíclicas explícitas (`for`, `while`), usando `pandas.apply()`.
- Se maneja adecuadamente la presencia de valores vacíos en los historiales.
- El script es fácil de escalar si se agregan más años en el futuro.
