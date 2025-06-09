import streamlit as st

def show_header():
    st.markdown("""
    <style>
    .nav-row {
        display: flex;
        gap: 2rem;
        margin-left: auto;
        font-weight: bold;
        flex-direction: row; /* ✅ sorgt für nebeneinander */
    }

    .nav-row .stLinkButton > button {
        background-color: #008B92;
        color: #ffffff;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        font-size: 1.1rem;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .nav-row .stLinkButton > button:hover {
        background-color: #00c6d2;
    color: #000;
    text-decoration: none;
    }
    body {
        padding-top: calc(3.0rem + 110px);
    }
    </style>
    """, unsafe_allow_html=True)

    st.image("https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_1.png", width=150)
    st.image("https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_2.png", width=80)

    with st.container():
        st.markdown('<div class="nav-row">', unsafe_allow_html=True)

        # Hier: Interne Navigation mit page_link (keine Neuladung / kein neuer Tab)
        st.page_link("Home.py", label="Home")
        st.page_link("pages/Quiz.py", label="Quiz")
        st.page_link("pages/Events.py", label="Events")
        st.page_link("pages/Über_uns.py", label="Über uns")

        st.markdown('</div>', unsafe_allow_html=True)
