import streamlit as st


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
