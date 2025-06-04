import streamlit as st

st.set_page_config(page_title="Kulturwandel durch KI – Ihre Organisationsberatung", layout="wide")

# Custom CSS für Layout und Design
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #222;
        }
        .headline {
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            padding-top: 2rem;
        }
        .subheadline {
            text-align: center;
            font-size: 1.2rem;
            margin-bottom: 1rem;
        }
        .cta-button {
            display: flex;
            justify-content: center;
            margin-top: 1rem;
            margin-bottom: 2rem;
        }
        .cta-button a {
            background-color: #fdbc00;
            color: #000;
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
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

# Hero Section
st.markdown('<div class="headline">Verändern Sie Ihre Organisation mit Künstlicher Intelligenz</div>', unsafe_allow_html=True)
st.markdown('<div class="subheadline">Kulturwandel beginnt dort, wo Technologie auf Haltung trifft.</div>', unsafe_allow_html=True)
st.markdown('<div class="cta-button"><a href="#form">Kostenfreies Erstgespräch buchen</a></div>', unsafe_allow_html=True)

# Feature Grid
st.markdown('<div class="feature-grid">', unsafe_allow_html=True)

features = [
    ("Paradigmenanalyse", "Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit."),
    ("Kulturdiagnostik", "Tool-gestützte Analyse Ihrer aktuellen kulturellen Reife zur Integration von KI."),
    ("Change-Coaching", "Begleitung Ihrer Führungskräfte beim Wandel zur KI-kompatiblen Unternehmenskultur."),
    ("KI-Framing Workshops", "Wie muss KI kommunizieren, um akzeptiert zu werden? Narrative & Tonalitätsdesign."),
    ("Systemisches Design", "Neuausrichtung systemischer Ansätze im Zusammenspiel mit lernenden Maschinen."),
    ("Prototypische Teams", "Begleitung von Pilotteams mit echten KI-Agenten im Arbeitsalltag.")
]

for title, desc in features:
    st.markdown(f"""
        <div class="feature-box">
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Kontaktformular (Leadgenerierung)
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
