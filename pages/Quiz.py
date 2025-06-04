import streamlit as st
from shared.header import show_header  # Header importieren

st.set_page_config(
    page_title="KI-Fähigkeit Ihrer Organisation prüfen – Aicura Quiz",
    layout="wide",
    initial_sidebar_state="collapsed"  # 👈 sorgt fürs Einklappen
)

show_header()  # Header anzeigen

# Optional: Intro-Abschnitt
st.markdown("""
<style>
 .quiz-intro {
        position: relative; width: 100%; height: 600px; top: 20px;
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
        url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Bild_Quiz.png');
        background-size: cover; background-position: center;
        display: flex; flex-direction: column;
        justify-content: center; align-items: center;
        color: white; text-align: center;
        text-shadow: 0 0 10px rgba(0,0,0,0.6);
        }
.feature-box {
            background-color: #ffffff; height: 400px;
            padding: 1.5rem; border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }
        
</style>
   
<div class="quiz-intro">
    <h2>📋 Ist Ihre Organisation KI-fähig?</h2>
    <p>Beantworten Sie 5 kurze Fragen und erhalten Sie direkt eine Einschätzung zur kulturellen und organisatorischen KI-Reife.</p>
</div>
""", unsafe_allow_html=True)

# Fragen
st.markdown("""
<div style="display: flex; justify-content: space-between; gap: 2rem; padding: 2rem;">
  <div style="flex: 1;">
    <div class="feature-box">
questions = {
    "1. Gibt es eine KI-Strategie im Unternehmen?": ["Ja, klar definiert", "Teilweise", "Nein"],
    "2. Wie hoch ist das Vertrauen der Mitarbeitenden in KI-Systeme?": ["Hoch", "Mittel", "Gering"],
    "3. Welche Rolle spielt KI in Entscheidungsprozessen?": ["Zentrale Rolle", "Unterstützend", "Keine Rolle"],
    "4. Gibt es Weiterbildungsangebote zu KI?": ["Regelmäßig", "Geplant", "Keine"],
    "5. Wie gut sind Ihre Datenprozesse auf KI vorbereitet?": ["Sehr gut", "Teilweise", "Schwach"]
}


responses = []
for q, options in questions.items():
    choice = st.radio(q, options, key=q)
    responses.append(choice)

# Ergebnis berechnen
if st.button("Ergebnis auswerten"):
    if all(responses):
        score = sum([questions[q].index(answer) for q, answer in zip(questions.keys(), responses)])

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

        # E-Mail zur Nachverfolgung
        with st.form("email_form"):
            st.markdown("📩 **Sie möchten die Auswertung & Empfehlung per E-Mail?**")
            email = st.text_input("Ihre E-Mail-Adresse")
            send_email = st.form_submit_button("Absenden")
            if send_email:
                st.success(f"Vielen Dank! Ihre Empfehlung wurde an {email} gesendet.")
    else:
        st.error("❗️Bitte beantworten Sie alle Fragen, bevor Sie das Ergebnis auswerten.")
