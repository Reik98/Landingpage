import streamlit as st

def show_header():
    st.markdown("""
    <style>
    header {
        position: fixed;
        top: 3.0rem;
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
    background-color: #008B92;
    color: #ffffff;
    padding: 0.6rem 1.2rem;
    border-radius: 6px;
    text-decoration: none;
    font-size: 1.1rem;
    transition: background-color 0.3s ease;
}

.nav-container a:hover {
    background-color: #00c6d2;
    color: #000;
    text-decoration: none;
}

    body {
        padding-top: calc(3.0rem + 110px);
    }

    @media (max-width: 768px) {
        header {  
            flex-wrap: wrap;
            justify-content: space-between;
            height: auto;
            padding: 1rem;
            align-items: flex-start;
        }

        .logo-main { height: 50px; margin-bottom: 0.5rem; }
        .logo-partner { height: 28px; margin-bottom: 0.5rem; }

        .nav-container {
            flex-direction: row; /* ✅ sorgt für nebeneinander */
            gap: 1rem;
            margin-top: 0.5rem;
            flex-wrap: wrap;
        }

        .nav-container a {
            font-size: 1rem;
        }

        body {
            padding-top: calc(3.0rem + 140px);
        }
    }

    @media (prefers-color-scheme: dark) {
        header {
            background-color: #ffffff !important;
        }

        .nav-container a {
            color: #ffffff !important;
        }

        .nav-container a:hover {
            color: #ffffff !important;
            text-decoration: underline;
        }

        .logo-main {
            filter: brightness(200%) contrast(120%);
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
                <a href="/">Home</a>
                <a href="/Quiz">Quiz</a>
                <a href="/Events">Events</a>
                <a href="/Über_uns">Über uns</a>
            </div>
        </header>
    """, unsafe_allow_html=True)
