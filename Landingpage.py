import streamlit as st

st.set_page_config(
    page_title="Kulturwandel durch KI – Ihre Organisationsberatung",
    layout="wide"
)

# Banner Video im Hintergrund
st.markdown("""
    <style>
        .video-background {
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
            object-fit: cover;
            opacity: 0.2;
        }
        .hero-text {
            position: relative;
            text-align: center;
            padding-top: 6rem;
            padding-bottom: 4rem;
            z-index: 2;
            color: #000;
        }
        .cta-button {
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

    <video autoplay loop muted playsinline class="video-background">
        <source src="Banner_Video.mp4" type="video/mp4">
    </video>
""", unsafe_allow_html=True)

# Hero-Sektion mit überlagertem Text
st.markdown("""
<div class="hero-text">
    <h1 style="font-size: 2.8rem;">Verändern Sie Ihre Organisation mit Künstlicher Intelligenz</h1>
    <p style="font-size: 1.2rem;">Kulturwandel beginnt dort, wo Technologie auf Haltung trifft.</p>
    <a href="#form" class="cta-button">Kostenfreies Erstgespräch buchen</a>
</div>
""", unsafe_allow_html=True)

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

# Formular
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
