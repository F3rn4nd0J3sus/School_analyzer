import streamlit as st

st.title("Cargar base de datos")
st.write("Sube tu archivo de base de datos en formato Excel para comenzar el análisis.")

archivo = st.file_uploader(
    "Selecciona un archivo de Excel",
    type=["xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "odt"]
)

if archivo is not None:
    st.session_state['archivo_base'] = archivo
    st.success("Archivo cargado correctamente y listo para análisis en otras páginas.")
    # Aquí puedes agregar la lógica para mostrar o procesar el archivo
