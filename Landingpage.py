import streamlit as st

st.set_page_config(page_title="KI als Kollege", layout="centered")

st.title("KI als Kollege")
st.markdown("### Mit strukturiertem Change Management zur erfolgreichen Team-Integration von KI-Agenten")

st.image("team_meeting.png")  # Optional: Bild lokal einbinden

st.markdown("""
**Warum Mitarbeiter KI ablehnen:**
- Verlustangst
- Misstrauen in Technologie
- Unklarer Nutzen
- Überforderung

**Unser Angebot:**
- Change-Workshops
- Meeting-Coachings mit KI
- Prompt-Toolkits
""")

if st.button("Kostenloses Erstgespräch buchen"):
    st.markdown("📧 Schreiben Sie uns an: kontakt@ki-beratung.de")
