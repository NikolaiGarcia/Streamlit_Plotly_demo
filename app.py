import pandas as pd
import streamlit as st
import plotly.express as px

df_car = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header("CAMBIA ESTO DESPUÉS.")  # creación de título

# creación del botón para activar la creación del histograma
hist_button = st.checkbox("Hacer histograma")

if hist_button:  # verdadero cuando se haga clic
    # escribir un mensaje de activación
    st.write("Creando un histograma para los datos de venta de coches . . .")

    # creación del histograma
    fig = px.histogram(df_car, x='odometer')

    # mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

# creación del botón para activar la creación del gráfico de disperción
scatter_button = st.checkbox("Hacer gráfico de disperción")


if scatter_button:  # verdadero cuando se haga clic
    # escribir un mensaje de activación
    st.write(
        "Creando un gráfico de disperción para los datos de venta de coches . . .")

    # creación del histograma
    fig = px.scatter(df_car, x='odometer', y='price')

    # mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)
