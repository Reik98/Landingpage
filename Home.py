import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from shared.header import show_header


st.set_page_config(
    page_title="Kulturwandel durch KI – Ihre Organisationsberatung",
    layout="wide"
)

# Gemeinsamer Header
show_header()

# Hero
st.markdown("""
<div class="hero">
    <h1>Verändern Sie Ihre Organisation mit Künstlicher Intelligenz</h1>
    <p>Kulturwandel beginnt dort, wo Technologie auf Haltung trifft.</p>
    <a href="#form" class="cta-button">Kostenfreies Erstgespräch buchen</a>
</div>
""", unsafe_allow_html=True)

# Catchphrase
st.markdown("""
<div class="catchfrase">
    <h3>In vielen Organisationen basieren Kultur- und Change-Modelle auf klassischen Paradigmen:</h3>
    <p>Stabile Systeme, lineares Denken, Planbarkeit. Doch KI verändert die Spielregeln: Entscheidungen werden datenbasiert, Rollen verschwimmen, Führung wird adaptiv. Viele der bisher genutzten Modelle (z. B. Senge, Kotter) brauchen ein radikales Update.</p>
</div>
""", unsafe_allow_html=True)

# Divider
st.markdown('<div class="divider"><span>Unsere Leistungsangebote</span></div>', unsafe_allow_html=True)

# Leistungsangebote (2-Spalten-Layout)
st.markdown("""
<div style="display: flex; justify-content: space-between; gap: 2rem; padding: 2rem;">
  <div style="flex: 1;">
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Analyse.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Paradigmenanalyse</h4>
      </div>
      <p>Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit.</p>
      <ul>
        <li>Luhmanns Systemtheorie im Abgleich mit KI-Dynamiken</li>
        <li>Kotters 8-Stufen-Modell in der KI-Adaption</li>
        <li>Systemisches Lernen nach Senge & Automatisierung</li>
      </ul>
    </div>
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Analyse.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Kulturdiagnostik</h4>
      </div>
      <p>Tool-gestützte Analyse Ihrer aktuellen kulturellen Reife zur Integration von KI.</p>
    </div>
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Analyse.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Change-Coaching</h4>
      </div>
      <p>Begleitung Ihrer Führungskräfte beim Wandel zur KI-kompatiblen Unternehmenskultur.</p>
    </div>
  </div>
  <div style="flex: 1;">
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Analyse.png" class="Logo-Bereiche">
        <h4 class="centered-heading">KI-Framing Workshops</h4>
      </div>
      <p>Wie muss KI kommunizieren, um akzeptiert zu werden? Narrative & Tonalitätsdesign.</p>
    </div>
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Analyse.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Systemisches Design</h4>
      </div>
      <p>Neuausrichtung systemischer Ansätze im Zusammenspiel mit lernenden Maschinen.</p>
    </div>
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Analyse.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Prototypische Teams</h4>
      </div>
      <p>Begleitung von Pilotteams mit echten KI-Agenten im Arbeitsalltag.</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Quiz-Button
st.markdown("""
<div style="text-align: center; margin: 3rem 0;">
    <a href="/1_Quiz" class="cta-button" style="font-size: 1.5rem; padding: 1.5rem 3rem;">
        Jetzt kostenlos prüfen, ob Ihr Unternehmen KI-fähig ist
    </a>
</div>
""", unsafe_allow_html=True)

# Kontaktformular
st.markdown('<div id="form"></div>', unsafe_allow_html=True)
st.markdown("### Buchen Sie Ihr Erstgespräch")
with st.form("form", clear_on_submit=True):
    name = st.text_input("Name")
    email = st.text_input("E-Mail")
    company = st.text_input("Unternehmen")
    message = st.text_area("Worüber möchten Sie sprechen?")
    submitted = st.form_submit_button("Absenden")
    if submitted:
        st.success("Vielen Dank! Wir melden uns in Kürze bei Ihnen.")

# Footer
st.markdown('<footer>&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
