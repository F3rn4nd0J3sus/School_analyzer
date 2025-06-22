import streamlit as st
from Modules.load_db import cargar_datos,pd
import plotly.express as px

st.title("Análisis de género")
st.write("Visualiza la distribución porcentual de género en la base de datos.")

archivo = st.session_state.get('archivo_base', None)

if archivo is not None:
    try:
        df = cargar_datos(archivo)
        # Buscar columna de género (asumiendo nombres comunes)
        posibles = ["genero", "género", "sexo", "gender"]
        col_genero = next((col for col in df.columns if col.lower() in posibles), None)
        if col_genero:
            conteo = df[col_genero].value_counts(normalize=True) * 100
            fig = px.pie(
                names=conteo.index,
                values=conteo.values,
                title="Distribución porcentual de género",
                hole=0.4
            )
            st.plotly_chart(fig)
        else:
            st.warning("No se encontró una columna de género reconocida en el archivo.")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
else:
    st.info("Por favor, carga un archivo en la página 'Cargar base de datos' para visualizar la distribución de género.")
