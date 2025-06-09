
import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – Change-Coaching_Impulsformate",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Bild: https://lacobe.de/wp-content/uploads/2019/06/Coaching-Beratung.jpg---
st.markdown("""
<style>
.hero-about {
    position: relative;
    width: 100%;
    height: 700px;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
    url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Coaching.jpg');
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
    margin-bottom: 15.5rem;
}
.hero-about p {
    font-size: 1.3rem;
    margin-top: 15.5rem;
}
</style>
<div class="hero-about">
    <h1>Change-Coaching & Impulsformate</h1>
    <p>Begleitung Ihrer Führungskräfte beim Wandel zur KI-kompatiblen Unternehmenskultur.</p>
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
