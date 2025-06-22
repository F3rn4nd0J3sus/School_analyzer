import streamlit as st
import plotly.express as px
from Modules.load_db import cargar_datos, pd
from Modules.text_process import normalizar_texto

st.title("Análisis de categoría o tipo")
st.write("Visualiza la distribución porcentual por categoría o tipo en la base de datos.")

archivo = st.session_state.get('archivo_base', None)

if archivo is not None:
    try:
        df = cargar_datos(archivo)
        # Buscar columna de categoría/tipo
        posibles = ["categoria", "categoría", "tipo"]
        col_cat = next((col for col in df.columns if normalizar_texto(col) in posibles), None)
        if col_cat:
            # Normalizar valores para agrupar equivalentes
            df[col_cat + '_norm'] = df[col_cat].apply(normalizar_texto)
            conteo = df[col_cat + '_norm'].value_counts(normalize=True) * 100
            etiquetas = df.groupby(col_cat + '_norm')[col_cat].agg(lambda x: x.value_counts().idxmax())
            fig = px.pie(
                names=[etiquetas[n] for n in conteo.index],
                values=conteo.values,
                title="Distribución porcentual por categoría o tipo",
                hole=0.4
            )
            st.plotly_chart(fig)
        else:
            st.warning("No se encontró una columna de categoría o tipo reconocida en el archivo.")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
else:
    st.info("Por favor, carga un archivo en la página 'Cargar base de datos' para visualizar la distribución por categoría o tipo.")
