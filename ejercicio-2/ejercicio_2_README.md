# Ejercicio 2 – Agregar correos a los nombres formateados

Este script resuelve el segundo ejercicio de la prueba técnica. El objetivo es tomar el archivo de nombres completos generado en el ejercicio anterior y añadir una columna de correos a cada persona, utilizando la clave única como identificador.

---

## Archivos utilizados

- `resultado_funcional_ejercicio_1.xlsx`: contiene los nombres completos generados previamente.
- `correos.csv`: contiene las claves únicas y los correos correspondientes.

---

## Descripción de la solución

El script sigue los siguientes pasos:

1. Se cargan ambos archivos: el Excel con los nombres completos y el CSV con los correos.
2. Se asegura que ambas columnas `Clave Unica` sean tratadas como texto para evitar problemas de merge (por ejemplo, formateo de miles).
3. Se realiza una combinación tipo `LEFT JOIN` entre ambos archivos usando la clave única.
4. Se ordena el resultado final por clave única.
5. Se exporta el nuevo DataFrame a un archivo Excel llamado `resultado_ejercicio_2.xlsx`.
