import streamlit as st

st.set_page_config(
    page_title="Kulturwandel durch KI – Ihre Organisationsberatung",
    layout="wide"
)

# CSS mit GitHub-Link zum Bild und Scroll-Verhalten
st.markdown("""
    <style>
        html {
            scroll-behavior: smooth;
        }
        .hero {
            position: relative;
            width: 100%;
            height: 450px;
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
        .cta-button {
            background-color: #fdbc00;
            color: #000;
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);  /* zwei Spalten */
            gap: 1.5rem;
            padding: 2rem;
        }

        .feature-box {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
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

# Hero-Sektion mit Scroll-Link
# Zweispaltige Leistungsübersicht
st.markdown("""
<div class="feature-columns">
    <div>
        <div class="feature-box">
            <h4>📊 Paradigmenanalyse</h4>
            <p>Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit.</p>
            <ul>
                <li>Luhmanns Systemtheorie im Abgleich mit KI-Dynamiken</li>
                <li>Adaptionsfähigkeit von Kotters 8-Stufen-Modell</li>
                <li>Evaluation von Lernprozessen nach Senge in KI-Kontexten</li>
            </ul>
        </div>
        <div class="feature-box">
            <h4>🧭 Kulturdiagnostik</h4>
            <p>Tool-gestützte Analyse Ihrer aktuellen kulturellen Reife zur Integration von KI.</p>
        </div>
        <div class="feature-box">
            <h4>👥 Change-Coaching</h4>
            <p>Begleitung Ihrer Führungskräfte beim Wandel zur KI-kompatiblen Unternehmenskultur.</p>
        </div>
    </div>
    <div>
        <div class="feature-box">
            <h4>🗣️ KI-Framing Workshops</h4>
            <p>Wie muss KI kommunizieren, um akzeptiert zu werden? Narrative & Tonalitätsdesign.</p>
        </div>
        <div class="feature-box">
            <h4>🧠 Systemisches Design</h4>
            <p>Neuausrichtung systemischer Ansätze im Zusammenspiel mit lernenden Maschinen.</p>
        </div>
        <div class="feature-box">
            <h4>🤖 Prototypische Teams</h4>
            <p>Begleitung von Pilotteams mit echten KI-Agenten im Arbeitsalltag.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# Anker für Formular
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
st.markdown('<footer>&copy; 2025 KI-Beratung GmbH – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
