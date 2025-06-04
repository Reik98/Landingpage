
import streamlit as st

st.set_page_config(
    page_title="Kulturwandel durch KI – Ihre Organisationsberatung",
    layout="wide"
)

# CSS mit Logo und Layout
st.markdown("""
    <style>
        html {
            scroll-behavior: smooth;
        }
        header {
            position: fixed;
            top: 60px;
            left: 0;
            width: 100%;
            height: 150px;
            background-color: white;
            z-index: 999;
            display: flex;
            align-items: center;
            padding: 0 20px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            }

        .logo-main {
            height: 90px;
            }

        .logo-partner {
            height: 45px;
            }
.centered-image {
    text-align: center;
    margin-bottom: 1rem;
}
.Logo-Bereiche {
    height: 90px;
    width: auto;
}



        .hero {
            position: relative;
            width: 100%;
            height: 600px;
            top: 20px;
            background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
            url('https://raw.githubusercontent.com/Reik98/Landingpage/main/image.png');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
            text-shadow: 0 0 10px rgba(0,0,0,0.6);
        }
        .hero h1 {
            font-size: 2.8rem;
            margin-bottom: 0.5rem;
        }
        .hero p {
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
        }
        .catchfrase {
            background-color: #ffffff;
            width: 100%;
            height: 200px;
            margin-top: 50px;  /* Feld weiter nach unten */
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
}

        .catchfrase h3 {
            font-size: 2.2rem;
            margin-bottom: 0.5rem;
        }
        .catchfrase p {
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
        }
       .cta-button {
        background-color: #fdbc00;
        color: #000;  /* <- sorgt für schwarze Schrift */
        padding: 1rem 2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
    }

    .cta-button:visited,
    .cta-button:active,
    .cta-button:hover {
        color: #000;  /* <- stellt sicher, dass die Farbe auch bei Hover & Klick schwarz bleibt */
        text-decoration: none;
    }
        .feature-box {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }

        .feature-box h4 {
            margin-top: 0;
            color: #003865;
        }
        footer {
            margin-top: 3rem;
            text-align: center;
            font-size: 0.9rem;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# Logo oben links
st.markdown("""
<header>
    <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_1.png" class="logo-main" alt="Aicura Logo">
    <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_2.png" class="logo-partner" alt="Partner Logo">
</header>
""", unsafe_allow_html=True)

# Hero-Sektion
st.markdown("""
<div class="hero">
    <h1>Verändern Sie Ihre Organisation mit Künstlicher Intelligenz</h1>
    <p>Kulturwandel beginnt dort, wo Technologie auf Haltung trifft.</p>
    <a href="#form" class="cta-button">Kostenfreies Erstgespräch buchen</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="catchfrase">
    <h3>In vielen Organisationen basieren Kultur- und Change-Modelle auf klassischen Paradigmen: </h3>
    <p>stabile Systeme, lineares Denken, Planbarkeit. Doch KI verändert die Spielregeln: Entscheidungen werden datenbasiert, Rollen verschwimmen, Führung wird adaptiv. Viele der bisher genutzten Modelle (z. B. Senge, Kotter) brauchen ein radikales Update.</p>
</div>
""", unsafe_allow_html=True)

# Zwei-Spalten-Layout der Leistungsangebote
st.markdown("""
<div style="display: flex; justify-content: space-between; gap: 2rem; padding: 2rem;">
  <div style="flex: 1;">
    <div class="feature-box">
  <div class="centered-image">
    <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Analyse.png" class="Logo-Bereiche">
  </div>
  <h4>Paradigmenanalyse</h4>
      <p>Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit.</p>
      <ul>
        <li>Luhmanns Systemtheorie im Abgleich mit KI-Dynamiken</li>
        <li>Kotters 8-Stufen-Modell in der KI-Adaption</li>
        <li>Systemisches Lernen nach Senge & Automatisierung</li>
      </ul>
    </div>
    <div class="feature-box">
      🧭<br><hr>
      <h4>Kulturdiagnostik</h4>
      <p>Tool-gestützte Analyse Ihrer aktuellen kulturellen Reife zur Integration von KI.</p>
    </div>
    <div class="feature-box">
      👥<br><hr>
      <h4>Change-Coaching</h4>
      <p>Begleitung Ihrer Führungskräfte beim Wandel zur KI-kompatiblen Unternehmenskultur.</p>
    </div>
  </div>
  <div style="flex: 1;">
    <div class="feature-box">
      🗣️<br><hr>
      <h4>KI-Framing Workshops</h4>
      <p>Wie muss KI kommunizieren, um akzeptiert zu werden? Narrative & Tonalitätsdesign.</p>
    </div>
    <div class="feature-box">
      🧠<br><hr>
      <h4>Systemisches Design</h4>
      <p>Neuausrichtung systemischer Ansätze im Zusammenspiel mit lernenden Maschinen.</p>
    </div>
    <div class="feature-box">
      🤖<br><hr>
      <h4>Prototypische Teams</h4>
      <p>Begleitung von Pilotteams mit echten KI-Agenten im Arbeitsalltag.</p>
    </div>
  </div>
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
