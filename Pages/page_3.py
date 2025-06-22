import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis de estado o provincia de nacimiento")
st.write("Visualiza la distribución porcentual por estado o provincia de nacimiento en la base de datos.")

archivo = st.session_state.get('archivo_base', None)

def cargar_datos(archivo):
    if archivo.name.endswith("csv"):
        return pd.read_csv(archivo)
    else:
        return pd.read_excel(archivo)

if archivo is not None:
    try:
        df = cargar_datos(archivo)
        # Buscar columna de estado/provincia de nacimiento
        posibles = [
            "estado de nacimiento", "provincia de nacimiento",
            "estado", "provincia"
        ]
        col_estado = next((col for col in df.columns if col.lower() in posibles), None)
        if col_estado:
            conteo = df[col_estado].value_counts(normalize=True) * 100
            fig = px.pie(
                names=conteo.index,
                values=conteo.values,
                title="Distribución porcentual por estado o provincia de nacimiento",
                hole=0.4
            )
            st.plotly_chart(fig)
        else:
            st.warning("No se encontró una columna de estado o provincia de nacimiento reconocida en el archivo.")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
else:
    st.info("Por favor, carga un archivo en la página 'Cargar base de datos' para visualizar la distribución por estado o provincia de nacimiento.")
