# Ejercicio 4 – Actualización de matriz de antigüedad con datos 2024

Este script resuelve el cuarto ejercicio de la prueba técnica. El objetivo es **actualizar la matriz de antigüedad** con la información del archivo `2024.xlsx`, e identificar a los profesores que **dieron clases por primera vez** en ese año.

---

## Archivos utilizados

- `matriz_antiguedad.xlsx`: contiene los años anteriores con valores de antigüedad por profesor.
- `2024.xlsx`: contiene las claves únicas y el valor de actividad (1 o 0.5) correspondiente al año 2024.

---

## Descripción de la solución

1. **Carga y limpieza de datos:**
   - Se cargan ambos archivos con `pandas`.
   - Se estandariza el nombre de columna del archivo 2024 (se reemplaza `"2,023"` por `"2024"`).
   - Se convierten las claves únicas a `string` para evitar errores por separación con comas.

2. **Actualización de la matriz:**
   - Se elimina la columna `2024` de la matriz original si ya existía (esto evita columnas duplicadas).
   - Se realiza un `merge` tipo `outer` para añadir los datos de 2024.
   - Se eliminan comas de los encabezados (por ejemplo, `1,990` → `1990`).
   - Se rellenan celdas vacías con `0`.

3. **Identificación de profesores nuevos:**
   - Se identifican los profesores que no aparecían en la matriz original pero sí en el archivo 2024.
   - Se genera un archivo con sus claves únicas.

---

## Resultados generados

- `matriz_antiguedad_actualizada.xlsx`: contiene la matriz completa con el año 2024 ya integrado.
- `profesores_nuevos_2024.xlsx`: lista con los profesores que impartieron clases por primera vez en 2024.

---

## Consideraciones adicionales

- Se evita que el script agregue la columna 2024 varias veces si se ejecuta más de una vez.
- Se limpian los encabezados para evitar errores por formato regional con comas en números.
