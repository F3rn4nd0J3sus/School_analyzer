import pandas as pd

def cargar_datos(archivo):
    if archivo.name.endswith("csv"):
        return pd.read_csv(archivo)
    else:
        return pd.read_excel(archivo)
