import streamlit as st

# Define las páginas
page_1 = st.Page("Pages/page_1.py", title="Cargar base de datos", icon="📂")
page_2 = st.Page("Pages/page_2.py", title="Análisis de género", icon="♀️")
page_3 = st.Page("Pages/page_3.py", title="Análisis estado/provincia", icon="🌎")
page_4 = st.Page("Pages/page_4.py", title="Análisis nivel/grado académico", icon="🎓")
page_5 = st.Page("Pages/page_5.py", title="Análisis categoría/tipo", icon="🏷️")

# Configura la navegación
pg = st.navigation([page_1, page_2, page_3, page_4, page_5])

# Ejecuta la página seleccionada
pg.run()
