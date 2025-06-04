import streamlit as st
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
        .logo-main { height: 90px; }
        .logo-partner { height: 45px; }
        .centered-image {
            text-align: center;
            margin-bottom: 1rem;
        }
        .centered-heading {
            margin-top: 0.5rem;
            color: #003865;
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
            margin-top: 50px;
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
            color: #000;
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
        }
        .cta-button:hover {
            color: #000;
            text-decoration: none;
        }
        .feature-box {
            background-color: #ffffff;
            height: 400px;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }
        .feature-box h4 {
            margin-top: 0;
            color: #003865;
        }
        .divider {
            display: flex;
            align-items: center;
            text-align: center;
            margin: 2rem 0;
        }
        .divider::before,
        .divider::after {
            content: '';
            flex: 1;
            border-bottom: 2px solid #fddb3a;
        }
        .divider:not(:empty)::before {
            margin-right: 0.75em;
        }
        .divider:not(:empty)::after {
            margin-left: 0.75em;
        }
        .divider span {
            color: #444;
            font-weight: 600;
            font-size: 2.5rem;
        }
        footer {
            margin-top: 3rem;
            text-align: center;
            font-size: 0.9rem;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# Header mit Logos
st.markdown("""
<header>
    <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_1.png" class="logo-main" alt="Aicura Logo">
    <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_2.png" class="logo-partner" alt="Partner Logo">
</header>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <h1>Verändern Sie Ihre Organisation mit Künstlicher Intelligenz</h1>
    <p>Kulturwandel beginnt dort, wo Technologie auf Haltung trifft.</p>
    <a href="#form" class="cta-button">Kostenfreies Erstgespräch buchen</a>
</div>
""", unsafe_allow_html=True)

# Catchphrase
st.markdown("""
<div class="catchfrase">
    <h3>In vielen Organisationen basieren Kultur- und Change-Modelle auf klassischen Paradigmen:</h3>
    <p>Stabile Systeme, lineares Denken, Planbarkeit. Doch KI verändert die Spielregeln: Entscheidungen werden datenbasiert, Rollen verschwimmen, Führung wird adaptiv. Viele der bisher genutzten Modelle (z. B. Senge, Kotter) brauchen ein radikales Update.</p>
</div>
""", unsafe_allow_html=True)

# 📋 Mini-Quiz: Ist Ihre Organisation KI-fähig?
st.markdown("## 📋 Ist Ihre Organisation KI-fähig?")

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

# Button zum Auswerten
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

        # E-Mail-Erfassungsformular
        with st.form("email_form"):
            st.markdown("📩 **Sie möchten die Auswertung & Empfehlung per E-Mail?**")
            email = st.text_input("Ihre E-Mail-Adresse")
            send_email = st.form_submit_button("Absenden")
            if send_email:
                st.success(f"Vielen Dank! Ihre Empfehlung wurde an {email} gesendet.")
    else:
        st.error("Bitte beantworten Sie alle Fragen, bevor Sie das Ergebnis auswerten.")
