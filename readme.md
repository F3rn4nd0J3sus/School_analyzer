# School Analyzer

School Analyzer es una aplicación interactiva desarrollada en Streamlit para analizar bases de datos escolares en formato Excel o CSV. Permite cargar una base de datos y visualizar análisis automáticos de género, estado/provincia de nacimiento, nivel/grado académico y categoría/tipo, normalizando los datos para evitar duplicados por tildes, mayúsculas o variantes ortográficas.

## Características principales
- **Carga de base de datos**: Sube archivos Excel en múltiples formatos.
- **Análisis de género**: Visualiza la distribución porcentual de género.
- **Análisis de estado/provincia de nacimiento**: Agrupa y normaliza los valores para mostrar la distribución.
- **Análisis de nivel/grado académico**: Agrupa equivalentes como "maestría" y "maestria".
- **Análisis de categoría/tipo**: Agrupa variantes como "categoría", "categoria" y "tipo".
- **Normalización automática**: Los análisis agrupan valores equivalentes aunque tengan tildes, mayúsculas o diferencias menores.

## Estructura del proyecto

```
School_analyzer/
├── main.py
├── Modules/
│   ├── load_db.py
│   └── text_process.py
├── Pages/
│   ├── page_1.py  # Cargar base de datos
│   ├── page_2.py  # Análisis de género
│   ├── page_3.py  # Análisis estado/provincia
│   ├── page_4.py  # Análisis nivel/grado académico
│   └── page_5.py  # Análisis categoría/tipo
└── readme.md
```

## Requisitos
- Python 3.8+
- streamlit >= 1.32
- pandas
- plotly

Instala las dependencias con:
```bash
pip install streamlit pandas plotly
```

## Uso
1. Ejecuta la app:
   ```bash
   streamlit run main.py
   ```
2. Sube tu archivo de base de datos en la página "Cargar base de datos".
3. Navega por las distintas páginas de análisis usando el menú lateral.

## Notas técnicas
- Los módulos en `Modules/` gestionan la carga y normalización de datos.
- Cada página de análisis busca automáticamente la columna relevante, normaliza los valores y muestra un gráfico de pastel.
- El menú lateral y la navegación multipágina se configuran en `main.py` usando la API moderna de Streamlit Pages.

## Créditos
Desarrollado por Fernando Jesús Castro Capote
