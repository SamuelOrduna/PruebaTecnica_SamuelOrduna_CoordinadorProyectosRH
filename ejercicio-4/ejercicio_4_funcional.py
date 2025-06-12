import pandas as pd

antiguedad_df = pd.read_excel("../matriz_antiguedad.xlsx")
a2024_df = pd.read_excel("../2024.xlsx")

a2024_df.columns = ["Clave Unica", "2024"]

antiguedad_df["Clave Unica"] = antiguedad_df["Clave Unica"].astype(str)
a2024_df["Clave Unica"] = a2024_df["Clave Unica"].astype(str)

if "2024" in antiguedad_df.columns:
    antiguedad_df = antiguedad_df.drop(columns=["2024"])

antiguedad_actualizada = antiguedad_df.merge(a2024_df, on="Clave Unica", how="outer")

antiguedad_actualizada.columns = [
    str(col).replace(",", "") if col != "Clave Unica" else col
    for col in antiguedad_actualizada.columns
] # no sé pq no funcionó lol

años_col = [col for col in antiguedad_actualizada.columns if col != "Clave Unica"]
antiguedad_actualizada[años_col] = antiguedad_actualizada[años_col].fillna(0)

antiguedad_actualizada.to_excel("matriz_antiguedad_actualizada.xlsx", index=False)

claves_antiguas = set(antiguedad_df["Clave Unica"])
claves_2024 = set(a2024_df["Clave Unica"])
nuevos_2024 = claves_2024 - claves_antiguas

pd.DataFrame(sorted(nuevos_2024), columns=["Clave Unica"]).to_excel("profesores_nuevos_2024.xlsx", index=False)
