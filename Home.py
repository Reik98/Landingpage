import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Kulturwandel durch KI – Ihre Organisationsberatung",
    layout="wide"
)

show_header()  # Logos & Navigation

# --- CSS Styling ---
st.markdown("""
    <style>
        html { scroll-behavior: smooth; }
        .centered-image { text-align: center; margin-bottom: 1rem; }
        .centered-heading { margin-top: 0.5rem; color: #003865; }
        .Logo-Bereiche { height: 90px; width: auto; }

        .hero {
            position: relative; width: 100%; height: 600px; top: 20px;
            background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
            url('https://raw.githubusercontent.com/Reik98/Landingpage/main/image.png');
            background-size: cover; background-position: center;
            display: flex; flex-direction: column;
            justify-content: center; align-items: center;
            color: white; text-align: center;
            text-shadow: 0 0 10px rgba(0,0,0,0.6);
        }
        .hero h1 { font-size: 2.8rem; margin-bottom: 0.5rem; }
        .hero p { font-size: 1.2rem; margin-bottom: 1.5rem; }

        .catchfrase {
            background-color: #ffffff; width: 100%; height: 200px;
            margin-top: 50px; padding: 1.5rem;
            border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }

        .catchfrase h3 { font-size: 2.2rem; margin-bottom: 0.5rem; }
        .catchfrase p { font-size: 1.2rem; margin-bottom: 1.5rem; }

        .cta-button {
            background-color: #fdbc00; color: #000;
            padding: 1rem 2rem; border-radius: 8px;
            text-decoration: none; font-weight: bold; display: inline-block;
        }
        .cta-button:hover { color: #000; text-decoration: none; }

        .feature-box {
            background-color: #ffffff; height: 400px;
            padding: 1.5rem; border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }
        .feature-box h4 { margin-top: 0; color: #003865; }

        .divider {
            display: flex; align-items: center; text-align: center;
            margin: 2rem 0;
        }
        .divider::before, .divider::after {
            content: ''; flex: 1; border-bottom: 2px solid #fddb3a;
        }
        .divider:not(:empty)::before { margin-right: 0.75em; }
        .divider:not(:empty)::after { margin-left: 0.75em; }
        .divider span {
            color: #444; font-weight: 600; font-size: 2.5rem;
        }
        footer {
            margin-top: 3rem; text-align: center;
            font-size: 0.9rem; color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero-Bereich ---
st.markdown("""
<div class="hero">
    <h1>Verändern Sie Ihre Organisation mit Künstlicher Intelligenz</h1>
    <p>Kulturwandel beginnt dort, wo Technologie auf Haltung trifft.</p>
    <a href="#form" class="cta-button">Kostenfreies Erstgespräch buchen</a>
</div>
""", unsafe_allow_html=True)

# --- Catchphrase ---
st.markdown("""
<div class="catchfrase">
    <h3>In vielen Organisationen basieren Kultur- und Change-Modelle auf klassischen Paradigmen:</h3>
    <p>Stabile Systeme, lineares Denken, Planbarkeit. Doch KI verändert die Spielregeln: Entscheidungen werden datenbasiert, Rollen verschwimmen, Führung wird adaptiv. Viele der bisher genutzten Modelle (z. B. Senge, Kotter) brauchen ein radikales Update.</p>
</div>
""", unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"><span>Unsere Leistungsangebote</span></div>', unsafe_allow_html=True)

# --- Leistungsangebote (2-Spalten-Layout) ---
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

# --- Quiz-Button (intern) ---
st.markdown("""
<div style="text-align: center; margin: 3rem 0;">
    <a href="/1_Quiz" class="cta-button" style="font-size: 1.5rem; padding: 1.5rem 3rem;">
        Jetzt kostenlos prüfen, ob Ihr Unternehmen KI-fähig ist
    </a>
</div>
""", unsafe_allow_html=True)

# --- Kontaktformular ---
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

# --- Footer ---
st.markdown('<footer>&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
