import pandas as pd
import streamlit as st

# Cargar datos desde GitHub
url = "https://raw.githubusercontent.com/WeTALKUPC/CRT-V3/main/CONSOLIDADO%20REEMPLAZOS%202024%20V2.xlsx"
@st.cache_data
def load_data(url):
    # Leer el archivo Excel desde GitHub
    data = pd.read_excel(url, engine="openpyxl")
    return data

# Cargar los datos
data = load_data(url)

# Configuración de la aplicación
st.title("CRT v3 - Gestión de Reemplazos")
st.sidebar.header("Filtros")

# Filtros
program_filter = st.sidebar.selectbox("Seleccionar Programa", data['PROGRAMA'].unique())
instructor_filter = st.sidebar.selectbox("Seleccionar Instructor Titular", data['INSTRUCTOR TITULAR'].unique())

# Filtrar datos según selección
filtered_data = data[(data['PROGRAMA'] == program_filter) & (data['INSTRUCTOR TITULAR'] == instructor_filter)]

# Métricas clave
st.subheader(f"Resumen para el Programa: {program_filter}")
st.write(f"Instructor Seleccionado: **{instructor_filter}**")
st.write(f"Total de Reemplazos Realizados: **{len(filtered_data)}**")
st.write("Reemplazos por Motivo:")
st.write(filtered_data['MOTIVO DE REEMPLAZO'].value_counts())

# Gráfico de barras
st.subheader("Gráfico - Reemplazos por Motivo")
st.bar_chart(filtered_data['MOTIVO DE REEMPLAZO'].value_counts())

# Agregar métricas adicionales
st.subheader("Métricas Adicionales")
total_reemplazos = len(data[data['INSTRUCTOR TITULAR'] == instructor_filter])
cumplimiento_porcentaje = round((len(filtered_data) / total_reemplazos) * 100, 2)
st.write(f"Porcentaje de Reemplazos del Instructor: **{cumplimiento_porcentaje}%**")

# Visualización de datos
st.subheader("Detalle de los Reemplazos")
st.dataframe(filtered_data)
