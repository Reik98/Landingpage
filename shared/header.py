import streamlit as st
import streamlit.components.v1 as components

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
        flex-direction: row;
    }

    .nav-button {
        background-color: #008B92;
        color: #ffffff;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        font-size: 1.1rem;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-decoration: none;
    }

    .nav-button:hover {
        background-color: #00c6d2;
        color: #000;
    }

    body {
        padding-top: calc(3.0rem + 110px);
    }

    </style>

    <header>
        <a href="/">
            <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_1.png" class="logo-main" alt="Aicura Logo">
        </a>
        <img src="https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_2.png" class="logo-partner" alt="Partner Logo">
        <div class="nav-container">
            <a class="nav-button" href="/">Home</a>
            <a class="nav-button" href="/Quiz">Quiz</a>
            <a class="nav-button" href="/Events">Events</a>
            <a class="nav-button" href="/Über_uns">Über uns</a>
        </div>
    </header>
    """, unsafe_allow_html=True)
