import pandas as pd

nombres_df = pd.read_excel("../ejercicio-1/resultado_funcional_ejercicio_1.xlsx")
# Excel a veces nos guarda los CSV con un BOM (Byte Order Mark), lo que rompe los encabezados.
# utf-8-sig permite que pandas lea bien la primera columna (evita errores como ï»¿Clave Unica).
correos_df = pd.read_csv("../correos.csv", encoding="utf-8-sig")

print("Encabezados detectados:", correos_df.columns.tolist())

nombres_df["Clave Unica"] = nombres_df["Clave Unica"].astype(str)
correos_df["Clave Unica"] = correos_df["Clave Unica"].astype(str)

resultado = pd.merge(nombres_df, correos_df, how="left", on="Clave Unica")

resultado = resultado.sort_values("Clave Unica")
resultado.to_excel("resultado_ejercicio_2.xlsx", index=False)
