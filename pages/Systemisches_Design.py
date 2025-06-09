


import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – Systemisches_Design",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Bild: https://www.iis.fraunhofer.de/de/ff/lv/net/jcr:content/stage/stageParsys/stage_slide/image.img.png/1643987344631/20211018-Vernetzung-AdobeStock-285478116-v4-WEB.png---
st.markdown("""
<style>
.hero-about {
    position: relative;
    width: 100%;
    height: 700px;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
    url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Systemdesign_1.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: top;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
    text-shadow: 0 0 10px rgba(0,0,0,0.6);
}
.hero-about h1 {
    font-size: 3rem;
    margin-bottom: 11.5rem;
    margin-top: 8.5rem;
}
.hero-about p {
    font-size: 1.3rem;
    margin-top: 3.5rem;
}
</style>
<div class="hero-about">
    <h1>Systemisches Design</h1>
    <p>Neuausrichtung systemischer Ansätze im Zusammenspiel mit lernenden Maschinen.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase
st.markdown("""
<div class="catchfrase">
    <h3>Seite im Aufbau</h3>
    <p>Weitere Inhalte folgen.</p>
</div>
""", unsafe_allow_html=True)

# --- Geschichte ---
st.markdown("""
### Erstens

...
""")

# --- Vision & Werte ---
st.markdown("""
### Zweitens

...
""")

# --- Teamvorstellung ---
st.markdown("""
### Drittens

...
""")

# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)

