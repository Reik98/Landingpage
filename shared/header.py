import streamlit as st

def show_header():
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
            gap: 2rem;
            margin-left: auto;
            font-weight: bold;
        }
        .nav-container a {
            color: #003865;
            text-decoration: none;
            font-size: 1.1rem;
        }
        .nav-container a:hover {
            text-decoration: underline;
        }
        </style>
    """, unsafe_allow_html=True)

    # HTML-Struktur für Header und Navigation
    st.markdown("""
        <header>
            <a href="/">
                <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_1.png" class="logo-main" alt="Aicura Logo">
            </a>
            <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_2.png" class="logo-partner" alt="Partner Logo">
            <div class="nav-container">
                <a href="/">🏠 Home</a>
                <a href="/Quiz">📋 Quiz</a>
            </div>
        </header>
    """, unsafe_allow_html=True)


