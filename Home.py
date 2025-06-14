import streamlit as st
import time
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura - Cultural Intelligence for the Age of AI",
    layout="wide",
    initial_sidebar_state="collapsed"  # 👈 WICHTIG: Seitenleiste standardmäßig eingeklappt
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
            margin-bottom: 2rem; /* 👈 Abstand zum nächsten Abschnitt */
            margin-top: 1rem; /* 👈 Abstand zum nächsten Abschnitt */
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
            background-color: #ffffff; width: 100%; height: auto;
            margin-top: 20px; padding: 1.5rem;
            text-align: center;
            border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }

        .catchfrase h3 { font-size: 2.2rem; margin-bottom: 0.5rem; }
        .catchfrase p { font-size: 1.2rem; margin-bottom: 1.5rem; }

       .cta-button {
            background-color: #008B92;
            color: #FFFFFF;
            padding: 1rem 2rem;
            border-radius: 8px;
            font-weight: bold;
            display: inline-block;
            text-decoration: none; /* kein Unterstrich standardmäßig */
            }
            
        .cta-button:link, .cta-button:visited, .cta-button:active {
            background-color: #008B92;
            color: #FFFFFF;
            text-decoration: none;
            }
        .cta-button:hover {
            color: #FFFFFF;
            background-color: #008B92;
            text-decoration: underline;
            }

        .feature-box {
            background-color: #ffffff;
            height: 400px;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            cursor: pointer;
            text-decoration: none;
            color: inherit;
            display: block;
            box-shadow: none; /* Kein Schatten standardmäßig */
            }

        .feature-box:hover, .feature-box:focus, .feature-box:active, .feature-box:visited {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
            background-color: #f5f5f5;
            color: inherit;
            text-decoration: none;
            }
        .feature-box a,.feature-box a:visited, .feature-box a:active, .feature-box a:focus, .feature-box a:hover {
            color: inherit;
            text-decoration: none;
            display: block;
            }
        a.feature-link {
            text-decoration: none;
            color: inherit;
            display: block;
            }
        a.feature-link:visited, a.feature-link:focus, a.feature-link:active, a.feature-link:hover {
            text-decoration: none;
            color: inherit;
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

/* Responsive mobile optimizations */
@media (max-width: 768px) {
    .hero {
        height: auto;
        padding: 2rem 1rem;
    }
    .hero h1 {
        font-size: 1.8rem;
    }
    .hero p {
        font-size: 1rem;
    }
    .catchfrase {
        height: auto;
        padding: 1rem;
    }
    .catchfrase h3 {
        font-size: 1.5rem;
    }
    .catchfrase p {
        font-size: 1rem;
    }
    .cta-button {
        width: 100%;
        font-size: 1.1rem;
        padding: 1rem;
        display: block;
        margin: 0 auto;
    }
    .Logo-Bereiche {
        height: 70px;
    }
    .feature-box {
        height: auto;
        padding: 1rem;
    }
    .feature-box ul {
        padding-left: 1rem;
    }
    .centered-heading {
        font-size: 1.2rem;
    }
}
/* 🔹 Darkmode-Unterstützung */
@media (prefers-color-scheme: dark) {
    body, .hero, .catchfrase, .feature-box {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
    }
    .feature-box h4,
    .catchfrase h3,
    .centered-heading {
        color: #008B92 !important;
    }
    .divider span {
        color: #ffffff !important;
    }
    .cta-button {
        background-color: #008B92 !important;
        color: #ffffff !important;
    }
    .cta-button:hover {
        background-color: #008B92 !important;
        color: #ffffff !important;
    }
    footer {
        color: #ccc;
    }
}
</style>

""", unsafe_allow_html=True)

# --- Hero-Bereich ---
st.markdown("""
<div class="hero">
    <h1>Verändern Sie Ihre Organisation mit Künstlicher Intelligenz</h1>
    <p>Kulturwandel beginnt dort, wo Technologie auf Haltung trifft.</p>
    <a href="#buchen-sie-ihr-erstgespraech" class="cta-button">Kostenfreies Erstgespräch buchen</a>
</div>
""", unsafe_allow_html=True)

# --- Catchphrase ---
st.markdown("""
<div class="catchfrase">
    <h3>In vielen Organisationen basieren Kultur- und Change-Modelle auf klassischen Paradigmen.</h3>
    <p>Stabile Systeme, lineares Denken, Planbarkeit. Doch KI verändert die Spielregeln.</p>
    <p>Entscheidungen werden datenbasiert, Rollen verschwimmen, Führung wird adaptiv und systemische Modelle stoßen an ihre Grenzen.</p>
    <p>Sie wollen nicht nur KI einführen – Sie wollen Ihre Organisation darauf ausrichten? Dafür bieten wir keine Standardberatung, sondern maßgeschneiderte kulturelle Entwicklung.<p>
    <p>Wir helfen Ihnen dabei, Ihre Organisation neu zu denken!</p>
</div>
""", unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"><span>Unsere Leistungsangebote</span></div>', unsafe_allow_html=True)

# --- Leistungsangebote (2-Spalten-Layout) ---
st.markdown("""
<div style="display: flex; justify-content: space-between; gap: 2rem; padding: 2rem;">
  <div style="flex: 1;">
    <a href="/Paradigmenanalyse" class="feature-link">
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Analyse.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Paradigmenanalyse</h4>
      </div>
      <p>Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit.</p>
      <ul>
        <li>Analyse Ihrer bestehenden Veränderungslogik</li>
        <li>Bewertung aktueller Modelle auf Zukunftstauglichkeit</li>
        <li>Team-Workshop zur kollektiven Reflexion</li>
      </ul>
    </div>
    </a>
    <a href="/Kulturdiagnostik_Integrationsstrategie" class="feature-link">
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/culture.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Kulturdiagnostik & Integrationsstrategie</h4>
      </div>
      <p>Tool-gestützte Analyse Ihrer aktuellen kulturellen Reife zur Integration von KI.</p>
      <ul>
        <li>Tool-gestützte Ist-Erhebung kultureller Reife (z. B. Akzeptanzgrade KI, Wertekompass)</li>
        <li>Entwicklung von Rollenmodellen für „KI im Team“</li>
        <li>Integrationsstrategie inkl. kulturellem Re-Design</li>
      </ul>
    </div>
    </a>
    <a href="/Change_Coaching_Impulsformate" class="feature-link">
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/coaching.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Change-Coaching & Impulsformate</h4>
      </div>
      <p>Begleitung Ihrer Führungskräfte beim Wandel zur KI-kompatiblen Unternehmenskultur.</p>
      <ul>
        <li>„KI verändert Führung“ – Impulsvortrag für Führungskräfte</li>
        <li>„Systemisches Denken im Zeitalter von KI“ – Teamworkshop</li>
        <li>„Framing & Narrative für KI-Kommunikation“ – Kommunikationsstrategie</li>
      </ul>
    </div>
    </a>
  </div>
  <div style="flex: 1;">
    <a href="/KI_Framing_Workshops" class="feature-link">
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/meeting.png" class="Logo-Bereiche">
        <h4 class="centered-heading">KI-Framing Workshops</h4>
      </div>
      <p>Wie muss KI kommunizieren, um akzeptiert zu werden? Narrative & Tonalitätsdesign.</p>
      <ul>
        <li>Entwicklung von akzeptanzfördernden Narrativen für KI-Einsatz</li>
        <li>Gestaltung emotionaler Tonalitäten für KI-Kommunikation</li>
        <li>Wie unterscheidet sich KI-Kommunikation von zwischenmenschlicher Kommunikation?</li>
      </ul>
    </div>
    </a>
    <a href="/Systemisches_Design" class="feature-link">
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/systemic.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Systemisches Design</h4>
      </div>
      <p>Neuausrichtung systemischer Ansätze im Zusammenspiel mit lernenden Maschinen.</p>
      <ul>
        <li>Analyse und Weiterentwicklung bestehender systemischer Logiken</li>
        <li>Übersetzung systemischer Prinzipien auf lernende Maschinen</li>
        <li>Design neuer Interaktionsmuster zwischen Mensch und KI im organisationalen Kontext</li>
      </ul>
    </div>
    </a>
    <a href="/Prototypische_Teams" class="feature-link">
    <div class="feature-box">
      <div class="centered-image">
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/prototyp.png" class="Logo-Bereiche">
        <h4 class="centered-heading">Prototypische Teams</h4>
      </div>
      <p>Begleitung von Pilotteams mit echten KI-Agenten im Arbeitsalltag.</p>
      <ul>
        <li>Identifikation geeigneter Pilotbereiche für KI-Integration</li>
        <li>Begleitung interdisziplinärer Teams mit real eingesetzten KI-Agenten</li>
        <li>Evaluation von Akzeptanz, Effizienz und kulturellem Impact im Arbeitsalltag</li>
      </ul>
    </div>
    </a>
  </div>
</div>
""", unsafe_allow_html=True)

# --- Quiz-Button (intern) ---
st.markdown("""
<div style="text-align: center; margin: 3rem 0;">
    <a href="/Quiz" class="cta-button" style="font-size: 1.5rem; padding: 1.5rem 3rem;">
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

# --- Divider ---
st.markdown('<div class="divider"><span>Was unsere Kunden sagen</span></div>', unsafe_allow_html=True)

# Kundenstimmen (Slider)
# Testimonials
testimonials = [
    {
        "text": "„Wir dachten, wir führen nur ein Tool ein – aber unsere gesamte Führungskultur hat sich verändert. Der Prozess war nicht immer bequem, aber absolut transformativ.“\n\n**— Leitung HR, Speditions-Unternehmen, 300 Mitarbeitende**",
        "logo": "https://raw.githubusercontent.com/Reik98/Landingpage/main/Logixon.png"
    },
    {
        "text": "„Mit KI-Framing verstehen wir jetzt besser, wie wir Akzeptanz für intelligente Systeme kommunizieren müssen. Vieles nutzen wir auch in der Kommunikation außerhalb der KI!“\n\n**— Leitung Kommunikation, Energieversorger, 1100 Mitarbeitende**",
        "logo": "https://raw.githubusercontent.com/Reik98/Landingpage/main/Energiewerte.png"
    },
    {
        "text": "„Wir haben echte Veränderungsbereitschaft entfacht und gleichzeitig bewusst Ängste thematisiert. In kurzer Zeit konnten wir so einen konstruktiven Perspektivenwechsel ermöglichen.“\n\n**— Projektleiter, Tech-Unternehmen, 120 Mitarbeitende**",
        "logo": "https://raw.githubusercontent.com/Reik98/Landingpage/main/Technova.png"
    }
]

# Session state verwalten
if "testimonial_index" not in st.session_state:
    st.session_state.testimonial_index = 0
if "last_switch_time" not in st.session_state:
    st.session_state.last_switch_time = time.time()

# Automatischer Wechsel alle 6 Sekunden
if time.time() - st.session_state.last_switch_time > 6:
    st.session_state.testimonial_index = (st.session_state.testimonial_index + 1) % len(testimonials)
    st.session_state.last_switch_time = time.time()

# Spaltenaufteilung mit Pfeilen
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("←", key="prev"):
        st.session_state.testimonial_index = (st.session_state.testimonial_index - 1) % len(testimonials)
        st.session_state.last_switch_time = time.time()
with col3:
    if st.button("→", key="next"):
        st.session_state.testimonial_index = (st.session_state.testimonial_index + 1) % len(testimonials)
        st.session_state.last_switch_time = time.time()

# Anzeige
with col2:
    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between;
                background-color: #f9f9f9; padding: 2rem; border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05); min-height: 200px;">
        <div style="flex: 1; font-size: 1.2rem; color: #333; margin-right: 2rem;">
            {testimonials[st.session_state.testimonial_index]['text']}
        </div>
        <div style="flex-shrink: 0; width: 100px; height: 100px; border-radius: 50%;
                    overflow: hidden; border: 2px solid #eee;">
            <img src="{testimonials[st.session_state.testimonial_index]['logo']}"
                 style="width: 100%; height: auto; object-fit: contain;">
        </div>
    </div>
    """, unsafe_allow_html=True)




# --- Footer ---
st.markdown('<footer>&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
