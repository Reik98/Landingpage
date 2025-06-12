import streamlit as st
from shared.header import show_header  # falls du eine Header-Datei nutzt
from datetime import datetime

st.set_page_config(
    page_title="Aicura - Events & Vorträge",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Sektion ---
st.markdown("""
<style>
.events-hero {
    position: relative;
    width: 100%;
    height: 500px;
    margin-top: 20px;
    background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
    url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Events.png');
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
.events-hero h1 {
    font-size: 2.8rem;
    margin-bottom: 0.5rem;
}
.events-hero p {
    font-size: 1.2rem;
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
.event-box {
    background-color: #ffffff;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.event-box h4 {
    color: #003865;
    margin-bottom: 0.5rem;
}
.event-box span {
    font-weight: bold;
}
</style>

<div class="events-hero">
    <h1>Events & Vorträge</h1>
    <p>Inspirationen für Ihre Transformation – live, praxisnah und systemisch gedacht</p>
</div>
""", unsafe_allow_html=True)

# --- Catchphrase ---
st.markdown("""
<div class="catchfrase">
    <h3>Ob Impulsvortrag, Webinar oder interaktiver Talk –</h3>
    <p>Unsere Veranstaltungen bringen die Themen KI, Kulturwandel und systemische Veränderung dorthin, wo sie wirken: in Ihre Köpfe, Teams und Organisationen.</p>
</div>
""", unsafe_allow_html=True)

# --- Events ---
events = [
    {
        "title": "Systemisches Denken im Zeitalter von KI",
        "date": "2025-09-17 10:00",
        "type": "Live-Webinar",
        "desc": "Erleben Sie, wie klassische OE-Modelle auf KI-Prinzipien treffen – mit Praxisbeispielen und Diskussion.",
    },
    {
        "title": "Framing KI – Narrative für mehr Akzeptanz",
        "date": "2025-10-03 14:00",
        "type": "Online-Talk",
        "desc": "Welche Geschichten funktionieren, wenn Maschinen mitreden? Tonalität, Kultur und semantische KI-Verankerung.",
    },
    {
        "title": "KI + Team: Prototypische Zusammenarbeit im Live-Test",
        "date": "2025-11-07 11:30",
        "type": "Keynote + Demo",
        "desc": "Ein echter KI-Agent im Teammeeting: Sehen Sie live, wie Zusammenarbeit auf Augenhöhe aussieht.",
    }
]

for event in events:
    date_obj = datetime.strptime(event["date"], "%Y-%m-%d %H:%M")
    formatted = date_obj.strftime("%d.%m.%Y · %H:%M Uhr")

    st.markdown(f"""
    <div class="event-box">
        <h4>{event['title']}</h4>
        <p><span>{event['type']}</span> · {formatted}</p>
        <p>{event['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    
# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
