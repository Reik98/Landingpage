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

        .logo-main {
            height: 90px;
            margin-right: 1rem;
        }

        .logo-partner {
            height: 45px;
            margin-right: 2rem;
        }

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

        /* 🔹 Mobile Optimierung */
        @media (max-width: 768px) {
            header {
                flex-direction: column;
                height: auto;
                padding: 1rem;
                align-items: flex-start;
            }

            .logo-main {
                height: 60px;
                margin-bottom: 0.5rem;
            }

            .logo-partner {
                height: 30px;
                margin-bottom: 1rem;
            }

            .nav-container {
                flex-direction: column;
                gap: 0.5rem;
                width: 100%;
                margin-left: 0;
            }

            .nav-container a {
                font-size: 1rem;
            }
        }

        /* 🔹 Dark Mode */
        @media (prefers-color-scheme: dark) {
            header {
                background-color: #1e1e1e;
                box-shadow: 0 2px 6px rgba(255,255,255,0.1);
            }

            .nav-container a {
                color: #ffffff;
            }

            .nav-container a:hover {
                color: #00c6d2;
                text-decoration: underline;
            }
        }
        </style>
    """, unsafe_allow_html=True)

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
