import pandas as pd

def cargar_datos(ruta_csv: str) -> pd.DataFrame:
    """Carga el CSV con codificación compatible con acentos."""
    return pd.read_csv(ruta_csv, encoding="cp1252")

def construir_nombre_completo(nombre: str, apellido: str) -> str:
    """Combina nombre y apellidos con limpieza de espacios."""
    nombres = (nombre or "").split(" ", 1) + [""]
    apellidos = (apellido or "").split("/", 1) + [""]
    
    resultado = f"{nombres[0].strip()} {nombres[1].strip()} {apellidos[0].strip()} {apellidos[1].strip()}"
    return " ".join(resultado.split())

def procesar_nombres(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega la columna de nombre completo al DataFrame."""
    df["Nombre Completo"] = df.apply(
        lambda row: construir_nombre_completo(row["Nombre"], row["Apellido"]),
        axis=1
    )
    df["Clave Unica"] = df["Clave Unica"].astype(str)
    return df[["Clave Unica", "Nombre Completo"]]

def exportar_excel(df: pd.DataFrame, ruta_salida: str) -> None:
    """Guarda el resultado en un archivo Excel."""
    df.to_excel(ruta_salida, index=False)

# Entrada 

if __name__ == "__main__":
    ruta_entrada = "../nombres.csv"
    ruta_salida = "resultado_ejercicio_1_SOLID.xlsx"

    datos = cargar_datos(ruta_entrada)
    resultado = procesar_nombres(datos)
    exportar_excel(resultado, ruta_salida)
