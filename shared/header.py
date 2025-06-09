import streamlit as st

# Setze aktuelle Seite, wenn noch nicht vorhanden
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Navigationsfunktion
def set_page(page_name):
    st.session_state.page = page_name

# Header mit Navigation
def show_header():
    st.markdown("""
    <style>
    .nav-container {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    .nav-button {
        background-color: #008B92;
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        text-decoration: none;
        font-size: 1.1rem;
        border: none;
        cursor: pointer;
    }
    .nav-button:hover {
        background-color: #00c6d2;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## Aicura App")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Home"):
            set_page("Home")
    with col2:
        if st.button("Quiz"):
            set_page("Quiz")
    with col3:
        if st.button("Events"):
            set_page("Events")
    with col4:
        if st.button("Über uns"):
            set_page("Über uns")

# Inhalt je nach Seite anzeigen
def show_content():
    page = st.session_state.page

    if page == "Home":
        st.write("🏠 **Willkommen auf der Startseite!**")
    elif page == "Quiz":
        st.write("❓ **Hier beginnt dein Quiz!**")
    elif page == "Events":
        st.write("📅 **Event-Übersicht:** Hier findest du alle Events.")
    elif page == "Über uns":
        st.write("👥 **Wer wir sind:** Informationen über das Team.")

# App starten
show_header()
show_content()
