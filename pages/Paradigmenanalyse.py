import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – Paradigmenanalyse",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Bild ---
st.markdown("""
<style>
.hero-about {
    position: relative;
    width: 100%;
    height: 700px;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
    url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Paradigmawechsel.jpg');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
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
    margin-bottom: 0.5rem;
}
.hero-about p {
    font-size: 1.3rem;
}
</style>
<div class="hero-about">
    <h1>Paradigmenanalyse</h1>
    <p>Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>Seite im Aufbau</h3>
    <p>Weitere Inhalte folgen.</p>
</div>
""", unsafe_allow_html=True)

# --- Geschichte ---
st.markdown("""
### 🎓 Erstens

...
""")

# --- Vision & Werte ---
st.markdown("""
### 🔮 Zweitens

> **Transforming Culture. Responsibly.**

Wir glauben, dass technologischer Fortschritt nur dann nachhaltig ist, wenn er kulturell verankert wird. Deshalb begleiten wir Organisationen im Wandel – achtsam, systemisch und mit Begeisterung für neue Denkweisen.

### 💭 Unsere Werte

- **Verantwortung**: KI braucht Haltung. Wir stehen für eine ethisch fundierte Anwendung.
- **Partizipation**: Kulturveränderung gelingt nur gemeinsam.
- **Systemisches Denken**: Wir sehen Organisationen als lebendige Systeme, nicht als Maschinen.
- **Mut zum Wandel**: Wir provozieren neue Perspektiven und hinterfragen Bestehendes.
""")

# --- Teamvorstellung ---
st.markdown("""
### 🤝 Unser Team

Wir sind interdisziplinär: Systemiker:innen, KI-Spezialist:innen, Organisationsentwickler:innen, Kommunikationsstrateg:innen und Designer:innen. Gemeinsam vereinen wir wissenschaftliche Fundierung mit kreativer Praxis.

Unser Netzwerk wächst stetig und lebt von der Überzeugung, dass Kulturentwicklung im Zeitalter von KI mehr als ein Projekt ist – es ist eine Haltung.
""")

# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
