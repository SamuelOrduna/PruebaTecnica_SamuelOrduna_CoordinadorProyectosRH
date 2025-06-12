# Ejercicio 1 – Análisis técnico de soluciones
Este documento describe y contrasta dos soluciones para el problema de formatear nombres completos a partir de un archivo `.csv`. Ambas cumplen con las restricciones (uso de Pandas y NumPy, sin estructuras cíclicas), pero difieren en enfoque, estructura y escalabilidad.

---

## Solución funcional (`ejercicio_1_funcional.py`)

### Enfoque

La lógica se estructura en pasos vectorizados usando `pandas`, sin clases ni funciones auxiliares. Se separan nombres y apellidos con `.str.split()`, se limpian con `.str.strip()` y `.fillna("")`, y se previene el formato de miles en Excel forzando `Clave Unica` como tipo texto.

### Ventajas

- Fácil de leer.
- Robusta ante errores de encoding y formateo.
- Rápida de implementar.

### Desventajas

- La lógica está embebida en un solo bloque.
- Poco reutilizable o testeable.
- No separa responsabilidades.

---

## Solución SOLID (`ejercicio_1_SOLID.py`)

### Enfoque

Se divide el proceso en funciones pequeñas, muy específicas y reutilizables:
- `cargar_datos`: maneja lectura del CSV con codificación Windows.
- `construir_nombre_completo`: encapsula la lógica de formateo.
- `procesar_nombres`: transforma los datos.
- `exportar_excel`: guarda el resultado.

No se utiliza programación orientada a objetos ni interfaces, pero sí se aplica de forma clara el principio de separación de responsabilidades (:  

Aunque sí se podría también hacer con clases, en este caso pienso que sería demasiaaado innecesario y solo haría el código más largo sin aportar mucho realmente..


### Ventajas

- Modular y mantenible.
- Fácil de testear.
- Escalable si el sistema necesita crecer o adaptarse.
- Legible.

### Desventajas

- Requiere algo más de estructura inicial.
- Ligeramente más extensa que la versión funcional (me refiero a más lineas de código).

---

## Comparación técnica

| Criterio                | Solución funcional       | Solución SOLID               |
|-------------------------|--------------------------|------------------------------|
| Claridad inmediata      | Alta                     | Alta                         |
| Escalabilidad           | Limitada                 | Alta                         |
| Reutilización           | Baja                     | Alta                         |
| Separación de lógica    | Embebida                 | Clara por función            |
| Preparada para testing  | No                       | Sí                           |
| Código más compacto     | Sí                       | No                           |
| Curva de aprendizaje    | Baja                     | Baja                         |

---

## Conclusión

Ambas soluciones generan exactamente el mismo resultado y cumplen con los criterios técnicos, pero están pensadas para contextos distintos:

- Recomiendo la **funcional** si se busca rapidez, claridad y si el problema es estático.
- Recomiendo la **SOLID** si el sistema podría crecer, puede llegar a necesitar validaciones adicionales o simplemente se busca una solución más mantenible a largo plazo.

¡🐺!  
Nota: La elección ideal depende del contexto y de qué tan “vivo” será el sistema que lo utilice.

– Hasta aquí mi reporte, Joaquín.

[![Gracias <3](https://c.tenor.com/nQXlXRZLWgIAAAAd/tenor.gif)](https://youtube.com/shorts/JUKsboPi-Mo?si=_KGIUloB3bYSZfNs)

> ⚠️ **Nota**  
> Decidí incluir una versión adicional con principios SOLID únicamente en este ejercicio para mostrar que conozco y sé aplicar algunas buenas prácticas de diseño modular y mantenible.  
> En el resto de los ejercicios opté por enfoques más directos, partiendo del supuesto en que los sistemas donde se utilizarían estas soluciones no son tan dinámicos.
