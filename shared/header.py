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

with st.container():
    col1, col2, col3 = st.columns([1, 6, 1])
    with col3:
        st.page_link("Home.py", label="🏠 Home")
        st.page_link("pages/Quiz.py", label="📋 Quiz")

