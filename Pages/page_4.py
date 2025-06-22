import streamlit as st
import plotly.express as px
from Modules.load_db import cargar_datos, pd
from Modules.text_process import normalizar_texto

st.title("Análisis de nivel o grado académico")
st.write("Visualiza la distribución porcentual por nivel o grado académico en la base de datos.")

archivo = st.session_state.get('archivo_base', None)

if archivo is not None:
    try:
        df = cargar_datos(archivo)
        # Buscar columna de nivel/grado académico
        posibles = ["nivel", "grado académico", "grado academico"]
        col_nivel = next((col for col in df.columns if normalizar_texto(col) in posibles), None)
        if col_nivel:
            # Normalizar valores para agrupar equivalentes (maestría/maestria, etc.)
            df[col_nivel + '_norm'] = df[col_nivel].apply(normalizar_texto)
            conteo = df[col_nivel + '_norm'].value_counts(normalize=True) * 100
            # Mostrar etiquetas originales más frecuentes para cada grupo normalizado
            etiquetas = df.groupby(col_nivel + '_norm')[col_nivel].agg(lambda x: x.value_counts().idxmax())
            fig = px.pie(
                names=[etiquetas[n] for n in conteo.index],
                values=conteo.values,
                title="Distribución porcentual por nivel o grado académico",
                hole=0.4
            )
            st.plotly_chart(fig)
        else:
            st.warning("No se encontró una columna de nivel o grado académico reconocida en el archivo.")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
else:
    st.info("Por favor, carga un archivo en la página 'Cargar base de datos' para visualizar la distribución por nivel o grado académico.")
