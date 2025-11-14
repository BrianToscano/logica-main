#!/usr/bin/env python

import pandas as pd
import streamlit as st
import altair as alt

# Configuración de la aplicación
st.set_page_config(page_title="Analizador de Palabras Psicológicas", layout="centered", page_icon="🧠")

st.title("🧠 Analizador de Palabras Clave en Psicología")

st.write("""
Esta aplicación permite **buscar y analizar palabras relacionadas con la psicología**, 
como emociones, comportamientos, trastornos o terapias.  
Puedes **subir un archivo con palabras** o usar la **lista de ejemplo** incluida.
""")

# Cargar archivo o usar datos de ejemplo
uploaded_file = st.file_uploader("📂 Carga un archivo CSV o TSV con una columna llamada 'palabra'", type=["csv", "tsv"])

if uploaded_file is not None:
    sep = "\t" if uploaded_file.name.endswith(".tsv") else ","
    df = pd.read_csv(uploaded_file, sep=sep).fillna("")
    st.success(f"Archivo cargado correctamente: {uploaded_file.name}")
else:
    st.info("No se subió ningún archivo. Se usará una lista de palabras clave psicológicas de ejemplo.")
    df = pd.DataFrame({
        "palabra": [
            "ansiedad", "estrés", "autoestima", "motivación", "depresión", "empatía",
            "atención", "memoria", "percepción", "conducta", "emoción", "aprendizaje",
            "terapia", "trauma", "bienestar", "personalidad", "autoconcepto", "neurociencia",
            "resiliencia", "inteligencia emocional", "autoeficacia", "trastorno", "psicoterapia"
        ]
    })

# Formulario de búsqueda
with st.form(key="buscar"):
    query = st.text_input("🔍 Escribe una palabra o raíz para buscar (ej. 'emo', 'estrés', 'terapia')")
    boton = st.form_submit_button("Buscar")

# Si el usuario presiona buscar
if boton:
    resultados = df[df["palabra"].str.contains(query, case=False, na=False)]
    st.success(f"🔎 Se encontraron **{len(resultados)}** palabras relacionadas con '{query}'.")
    
    if not resultados.empty:
        st.table(resultados)

        # Frec
