import streamlit as st
from shared.header import show_header  # Header importieren

st.set_page_config(
    page_title="Paradigmenanalyse",
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
        url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Paradigmawechsel.jpg');
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
    .catchfrase {
        background-color: #ffffff;
        width: 100%;
        margin-top: 20px;
        padding: 1.5rem;
        text-align: center;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    .catchfrase h3 {
        font-size: 2rem;
        margin-bottom: 0.5rem;
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
st.markdown("""
<div class="catchfrase">
    <h3>Ob Impulsvortrag, Webinar oder interaktiver Talk –</h3>
    <p>Unsere Veranstaltungen bringen die Themen KI, Kulturwandel und systemische Veränderung dorthin, wo sie wirken: in Ihre Köpfe, Teams und Organisationen.</p>
</div>
""", unsafe_allow_html=True)

<div class="quiz-intro">
    <h2>Paradigmenanalyse</h2>
    <p>Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit.</p>
</div>
""", unsafe_allow_html=True)

