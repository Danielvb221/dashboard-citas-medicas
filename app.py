import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# LABORATORIO 13 - ACTIVIDAD 3 (PARTE A)
# Caso: Plataforma Inteligente de Gestión de Citas Médicas
# Hospital de Lima Norte
# ============================================================

# Configuración de la página
st.set_page_config(
    page_title='Dashboard de Gestión de Citas Médicas',
    page_icon='🏥',
    layout='wide'
)

# Cargar el dataset
try:
    df = pd.read_csv('citas_medicas.csv')
except FileNotFoundError:
    st.error("No se encontró el archivo 'citas_medicas.csv'. Colócalo en la misma carpeta que app.py.")
    st.stop()

# Título principal
st.title('Dashboard de Gestión de Citas Médicas')
st.caption('Plataforma Inteligente de Gestión de Citas Médicas en un Hospital de Lima Norte')

# Gráfico 1: Citas por especialidad
st.subheader('Citas por Especialidad')
fig1 = px.bar(
    df['especialidad'].value_counts(),
    labels={'value': 'Cantidad', 'index': 'Especialidad'},
    title='Cantidad de citas por especialidad'
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Estado de las citas
st.subheader('Estado de las Citas')
fig2 = px.pie(
    df,
    names='estado',
    title='Distribución de estados de las citas'
)
st.plotly_chart(fig2, use_container_width=True)

# Preparar la fecha y crear la variable mes
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month

# Agrupar citas por mes
citas_mes = df.groupby('mes').size().reset_index(name='cantidad')

# Gráfico 3: Citas por mes
st.subheader('Citas por Mes')
fig3 = px.line(
    citas_mes,
    x='mes',
    y='cantidad',
    markers=True,
    title='Cantidad de citas registradas por mes'
)
st.plotly_chart(fig3, use_container_width=True)
