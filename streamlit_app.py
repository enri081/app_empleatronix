import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import joblib
import json

# Tituo y descripción
st.title("Empleatronix")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Tabla
table = pd.read_csv("./Data/employees.csv")
st.dataframe(table)

# Divisor
st.divider()

# Elecciones
col1, col2, col3 = st.columns(3)

with col1:
    color = st.color_picker("Elige un color para las barras", "#3475B3")

with col2:
    name = st.toggle("Mostrar el nombre")

with col3:
    earnings = st.toggle("Mostrar sueldo en la barra")


# Diagrama de barras
fig, ax = plt.subplots(figsize=(5, 3.5), dpi=120) 

ax.barh(range(len(table)), table["salary"], color=color)

ax.set_yticks(range(len(table)))
ax.set_yticklabels(table["full name"].astype(str) * int(name), fontsize=9)

xmax = table["salary"].max()
ax.set_xlim(0, xmax * 1.15)
pad = xmax * 0.01

for i, v in enumerate(table["salary"]):
    ax.text(v + pad, i, f"{int(v)}€", va="center", alpha=int(earnings), fontsize=7)

ax.tick_params(axis="x", labelsize=7, labelrotation=90)
ax.tick_params(axis="y", labelsize=7)

ax.invert_yaxis()
plt.tight_layout()
st.pyplot(fig, clear_figure=True, use_container_width=False)

# Nombre
st.write("© Enrique Moreno Alcántara - CPIFP Alan Turing")