import streamlit as st

def show_header():
    st.markdown("""
        <style>
        header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 110px;
            background-color: white;
            z-index: 999;
            display: flex;
            align-items: center;
            padding: 0 20px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }

        .logo-main {
            height: 70px;
            margin-right: 1rem;
            transition: filter 0.3s ease;
        }

        .logo-partner {
            height: 35px;
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

        body {
            padding-top: 120px;  /* 👈 Verhindert Überlagerung durch festen Header */
        }

        /* 🔹 Mobile */
        @media (max-width: 768px) {
            header {
                flex-direction: column;
                align-items: flex-start;
                height: auto;
                padding: 1rem;
            }

            .logo-main {
                height: 50px;
                margin-bottom: 0.5rem;
            }

            .logo-partner {
                height: 28px;
                margin-bottom: 0.5rem;
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

            body {
                padding-top: 150px;
            }
        }

        /* 🔹 Darkmode */
        @media (prefers-color-scheme: dark) {
            header {
                background-color: #1e1e1e;
                box-shadow: 0 2px 6px rgba(255,255,255,0.1);
            }

            .logo-main {
                filter: brightness(200%) contrast(120%);
            }

            .nav-container a {
                color: #ffffff;
            }

            .nav-container a:hover {
                color: #00c6d2;
            }

            body {
                background-color: #1e1e1e;
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
