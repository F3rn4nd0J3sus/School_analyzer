import unicodedata
import pandas as pd

def normalizar_texto(texto):
    if pd.isnull(texto):
        return ""
    # Quitar tildes y pasar a minúsculas
    texto = unicodedata.normalize('NFKD', str(texto)).encode('ASCII', 'ignore').decode('utf-8').lower()
    # Quitar espacios extra
    return texto.strip()