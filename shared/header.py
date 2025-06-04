import streamlit as st

def show_header():
    st.markdown("""
        <style>
            .global-header {
                position: relative;
                width: 100%;
                height: 100px;
                background-color: white;
                z-index: 999;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 30px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            }
            .logo-main { height: 70px; }
            .logo-partner { height: 40px; margin-left: 1rem; }
            .nav-links a {
                margin-left: 2rem;
                font-size: 1rem;
                text-decoration: none;
                color: #003865;
                font-weight: 600;
            }
            .nav-links a:hover {
                color: #fdbc00;
            }
        </style>
        <div class="global-header">
            <div>
                <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_1.png" class="logo-main">
                <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_2.png" class="logo-partner">
            </div>
            <div class="nav-links">
                <a href="/">🏠 Home</a>
                st.page_link("pages/Quiz.py", label="📋 Quiz", icon="🧠")
            </div>
        </div>
    """, unsafe_allow_html=True)
