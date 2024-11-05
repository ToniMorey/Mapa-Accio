import streamlit as st
from streamlit_folium import st_folium
import folium

# Título de la aplicación
st.title("Mapa Empreses Campiones")

# Cargar el mapa HTML de Folium
map_path = "mapa_empresas.html"  # Asegúrate de que la ruta sea correcta
with open(map_path, "r", encoding="utf-8") as file:
    mapa_html = file.read()

# CSS para centrar el mapa
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Mostrar el mapa dentro de un div centrado
st.markdown('<div class="center">', unsafe_allow_html=True)
st.components.v1.html(mapa_html, width=1000, height=500, scrolling=True)
st.markdown('</div>', unsafe_allow_html=True)
