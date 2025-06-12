import pandas as pd

antiguedad_df = pd.read_excel("../matriz_antiguedad.xlsx")
info_df = pd.read_excel("../ejercicio-2/resultado_ejercicio_2.xlsx")

antiguedad_df["Clave Unica"] = antiguedad_df["Clave Unica"].astype(str)
info_df["Clave Unica"] = info_df["Clave Unica"].astype(str)

columnas_años = [col for col in antiguedad_df.columns if col != "Clave Unica"]

def calcular_antiguedad(row):
    historial = row[columnas_años].fillna(0).tolist()
    total = 0
    contador_inactivos = 0
    acumulado = 0
    reinicios = 0
    tramo_activo = []

    for valor in historial:
        if valor == 0:
            contador_inactivos += 1
        else:
            if contador_inactivos > 4:
                if acumulado > 0:
                    tramo_activo.append(acumulado)
                    reinicios += 1
                acumulado = valor
            else:
                acumulado += valor
            contador_inactivos = 0

    if acumulado > 0:
        tramo_activo.append(acumulado)

    antiguedad_total = max(tramo_activo) if reinicios else sum(historial)
    comentario = "Se reinició la antigüedad" if reinicios else ""

    return pd.Series([round(sum(tramo_activo), 1), comentario])

antiguedad_df[["Antigüedad", "Comentario"]] = antiguedad_df.apply(calcular_antiguedad, axis=1)

resultado = antiguedad_df.merge(info_df, on="Clave Unica", how="left")
resultado = resultado[["Clave Unica", "Nombre Completo", "Correo", "Antigüedad", "Comentario"]]
resultado = resultado.sort_values("Clave Unica")

resultado.to_excel("resultado_ejercicio_3.xlsx", index=False)
