import streamlit as st

def show_header():
    st.markdown("""
    <style>
    .nav-container {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
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
    cols = st.columns(4)
    with cols[0]:
        if st.button("Home", key="home", help="Zur Startseite"):
            st.switch_page("Home.py")
    with cols[1]:
        if st.button("Quiz", key="quiz", help="Zum Quiz"):
            st.switch_page("Quiz.py")
    with cols[2]:
        if st.button("Events", key="events", help="Zu den Events"):
            st.switch_page("Events.py")
    with cols[3]:
        if st.button("Über uns", key="about", help="Über uns"):
            st.switch_page("Über_uns.py")

show_header()
