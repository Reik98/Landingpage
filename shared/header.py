import streamlit as st

def show_header():
    # Style für Logo + Navigation (optional ergänzt)
    st.markdown("""
        <style>
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
        .logo-main { height: 90px; margin-right: 1rem; }
        .logo-partner { height: 45px; margin-right: 2rem; }
        .nav-container {
            display: flex;
            gap: 1.5rem;
            margin-left: auto;
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

    # Navigation (mittels Streamlit-native page_link)
    with st.container():
        st.markdown("<div class='nav-container'>", unsafe_allow_html=True)
        st.page_link("Home.py", label="🏠 Home")
        st.page_link("pages/Quiz.py", label="📋 Quiz")
        st.markdown("</div>", unsafe_allow_html=True)
