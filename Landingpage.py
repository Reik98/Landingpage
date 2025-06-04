import streamlit as st

# Seitenkonfiguration
st.set_page_config(
    page_title="Kulturwandel durch KI – Ihre Organisationsberatung",
    layout="wide"
)

# CSS für zweispaltige Darstellung
st.markdown("""
    <style>
        html {
            scroll-behavior: smooth;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
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
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
            color: #003865;
        }
        .feature-box ul {
            padding-left: 1.2rem;
            margin-top: 0.2rem;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Überschrift oder andere Inhalte optional hier
st.markdown("## 🧩 Unser Beratungsportfolio für den KI-Kulturwandel")

# HTML-Struktur der zweispaltigen Grid-Sektion
st.markdown("""
<div class="feature-grid">

  <!-- Linke Spalte -->
  <div class="feature-box">
    <h4>📊 Paradigmenanalyse</h4>
    <p>Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit.</p>
    <ul>
      <li>Luhmanns Systemtheorie im Abgleich mit KI-Dynamiken</li>
      <li>Adaptionsfähigkeit von Kotters 8-Stufen-Modell</li>
      <li>Evaluation von Lernprozessen nach Senge in KI-Kontexten</li>
    </ul>

    <h4>🧭 Kulturdiagnostik</h4>
    <p>Tool-gestützte Analyse Ihrer aktuellen kulturellen Reife zur Integration von KI.</p>

    <h4>👥 Change-Coaching</h4>
    <p>Begleitung Ihrer Führungskräfte beim Wandel zur KI-kompatiblen Unternehmenskultur.</p>
  </div>

  <!-- Rechte Spalte -->
  <div class="feature-box">
    <h4>🗣️ KI-Framing Workshops</h4>
    <p>Wie muss KI kommunizieren, um akzeptiert zu werden? Narrative & Tonalitätsdesign.</p>

    <h4>🧠 Systemisches Design</h4>
    <p>Neuausrichtung systemischer Ansätze im Zusammenspiel mit lernenden Maschinen.</p>

    <h4>🤖 Prototypische Teams</h4>
    <p>Begleitung von Pilotteams mit echten KI-Agenten im Arbeitsalltag.</p>
  </div>

</div>
""", unsafe_allow_html=True)
