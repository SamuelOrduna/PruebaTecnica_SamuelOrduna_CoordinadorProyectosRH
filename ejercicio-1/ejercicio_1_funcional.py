import pandas as pd
# Windows suele guardar archivos .csv en codificación cp1252 por defecto 
# El carácter é (como en "Pérez") no es válido en utf-8 si está guardado como cp1252
df = pd.read_csv("../nombres.csv", encoding="cp1252")

apellidos_df = df["Apellido"].str.split("/", n=1, expand=True).rename(columns={0: "Apellido1", 1: "Apellido2"}).fillna("")
nombres_df = df["Nombre"].str.split(" ", n=1, expand=True).rename(columns={0: "Nombre1", 1: "Nombre2"}).fillna("")

df["Nombre Completo"] = (
    nombres_df["Nombre1"].str.strip() + " " +
    nombres_df["Nombre2"].str.strip() + " " +
    apellidos_df["Apellido1"].str.strip() + " " +
    apellidos_df["Apellido2"].str.strip()
).str.replace(r"\s+", " ", regex=True).str.strip()

resultado = df[["Clave Unica", "Nombre Completo"]]
resultado["Clave Unica"] = resultado["Clave Unica"].astype(str) # así no nos pone comas en el excel.
resultado.to_excel("resultado_funcional_ejercicio_1.xlsx", index=False)
