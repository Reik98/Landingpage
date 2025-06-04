import streamlit as st

def show_header():
    # Logos + Spaltenstruktur
    col1, col2, col3 = st.columns([1, 3, 3])

    with col1:
        st.image("https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_1.png", width=120)

    with col2:
        st.image("https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_2.png", width=90)

    with col3:
        st.markdown("### Navigation")
        st.page_link("Home.py", label="🏠 Home")
        st.page_link("pages/Quiz.py", label="📋 Quiz")
