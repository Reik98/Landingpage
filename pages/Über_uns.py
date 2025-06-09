import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – Über uns",
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
    url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Über uns.JPG');
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
    <h1>Über uns</h1>
    <p>Unsere Vision: Transforming Culture. Responsibly.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>Aicura – Cultural Intelligence for the Age of AI</h3>
    <p>Wir sind eine junge Organisation mit einer großen Mission: Organisationen kulturell auf das Zeitalter der Künstlichen Intelligenz vorbereiten. 
    Unser Ansatz verbindet systemisches Denken, technologische Zukunftskompetenz und echte Kulturarbeit.</p>
</div>
""", unsafe_allow_html=True)

# --- Geschichte ---
st.markdown("""
### 🎓 Entstehung aus dem Campus

Aicura wurde 2025 von neun Studierenden gegründet – heraus aus einem interdisziplinären Semesterprojekt zur Frage: *Wie können KI-Agenten als vollwertige Partizipanten in Unternehmen integriert werden?*

Was als Experiment begann, wurde zum Impuls für ein wachsendes Netzwerk. Unser Ziel: Wir wollen mit Organisationen Wege finden, KI nicht nur technisch, sondern auch kulturell verantwortungsvoll zu integrieren.
""")

# --- Vision & Werte ---
st.markdown("""
### 🔮 Unsere Vision

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

