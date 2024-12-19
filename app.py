import pandas as pd
import streamlit as st
import plotly.express as px

df_car = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header("CAMBIA ESTO DESPUÉS.")  # creación de título

# creación del botón para activar la creación del histograma
hist_button = st.button("Hacer histograma")

if hist_button:  # verdadero cuando se haga clic
    # escribir un mensaje de activación
    st.write("Creando un histograma para los datos de venta de coches . . .")

    # creación del histograma
    fig = px.histogram(df_car, x='odometer')

    # mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)
