import streamlit as st
from shared.header import show_header  # Header importieren

st.set_page_config(
    page_title="Aicura - KI-Fähigkeit Ihrer Organisation prüfen",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Styling für Darkmode + Mobile ---
st.markdown("""
<style>
    .quiz-intro {
        position: relative;
        width: 100%;
        height: 500px;
        top: 20px;
        margin-bottom: 2rem; /* 👈 Abstand zum nächsten Abschnitt */
        margin-top: 1rem; /* 👈 Abstand zum nächsten Abschnitt */
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
        url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Bild_Quiz.png');
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
        font-size: 1.2rem;
    }

    /* Mobile */
    @media (max-width: 768px) {
        .quiz-intro {
            height: auto;
            padding: 2rem 1rem;
            text-align: center;
        }

        .quiz-intro h2 {
            font-size: 1.8rem;
        }

        .quiz-intro p {
            font-size: 1rem;
        }

        .feature-box {
            padding: 1rem;
        }

        .feature-box h4 {
            font-size: 1rem;
        }
    }

    /* Darkmode */
    @media (prefers-color-scheme: dark) {
        body, .quiz-intro, .feature-box {
            background-color: #1e1e1e !important;
            color: #ffffff !important;
        }

        .feature-box h4 {
            color: #00c6d2 !important;
        }

        .stRadio > div {
            background-color: #2a2a2a !important;
            color: #ffffff !important;
            border-radius: 5px;
            padding: 5px;
        }

        .stButton > button {
            background-color: #008B92 !important;
            color: #fff !important;
        }

        .stTextInput > div > input {
            background-color: #2a2a2a !important;
            color: #ffffff !important;
        }

        footer {
            color: #ccc !important;
        }
    }
</style>

<div class="quiz-intro">
    <h2>Ist Ihre Organisation KI-fähig?</h2>
    <p>Beantworten Sie 5 kurze Fragen und erhalten Sie direkt eine Einschätzung zur kulturellen und organisatorischen KI-Reife.</p>
</div>
""", unsafe_allow_html=True)

# --- Fragen & Antworten ---
questions = {
    "Gibt es eine KI-Strategie im Unternehmen?": ["Ja, klar definiert", "Teilweise", "Nein"],
    "Wie hoch ist das Vertrauen der Mitarbeitenden in KI-Systeme?": ["Hoch", "Mittel", "Gering"],
    "Welche Rolle spielt KI in Entscheidungsprozessen?": ["Zentrale Rolle", "Unterstützend", "Keine Rolle"],
    "Gibt es Weiterbildungsangebote zu KI?": ["Regelmäßig", "Geplant", "Keine"],
    "Wie gut sind Ihre Datenprozesse auf KI vorbereitet?": ["Sehr gut", "Teilweise", "Schwach"]
}

responses = []
for i, (question, options) in enumerate(questions.items(), 1):
    st.markdown(f'<div class="feature-box"><h4>{i}. {question}</h4>', unsafe_allow_html=True)
    choice = st.radio("", options, key=f"q{i}")
    responses.append(choice)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Ergebnis ---
if st.button("Ergebnis auswerten"):
    if all(responses):
        score = sum([questions[q].index(a) for q, a in zip(questions.keys(), responses)])

        st.subheader("📈 Ihr Ergebnis:")

        if score <= 3:
            st.success("✅ Sehr gute Voraussetzungen für KI-Einführung!")
            recommendation = "Sie sind bereit für komplexe KI-Projekte – denken Sie über agentenbasierte Automation nach."
        elif score <= 6:
            st.info("🟡 Gute Basis, aber es besteht Handlungsbedarf.")
            recommendation = "Fokussieren Sie sich auf Change-Kommunikation und interne Weiterbildung."
        else:
            st.warning("🔴 Ihre Organisation ist noch nicht KI-fähig.")
            recommendation = "Beginnen Sie mit einer Kulturdiagnose und ersten Pilotprojekten."

        st.markdown(f"**Empfehlung:** {recommendation}")

        with st.form("email_form"):
            st.markdown("📩 **Sie möchten die Auswertung & Empfehlung per E-Mail?**")
            email = st.text_input("Ihre E-Mail-Adresse")
            send_email = st.form_submit_button("Absenden")
            if send_email:
                st.success(f"Vielen Dank! Ihre Empfehlung wurde an {email} gesendet.")
    else:
        st.error("❗️Bitte beantworten Sie alle Fragen, bevor Sie das Ergebnis auswerten.")
        
# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
