import streamlit as st

def show_header():
    st.markdown("""
    <style>
    .custom-button > div > button {
        background-color: #008B92 !important;
        color: white !important;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        font-size: 1.1rem;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .custom-button > div > button:hover {
        background-color: #00c6d2 !important;
        color: #000000 !important;
    }

    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 1rem;
        border-bottom: 1px solid #ccc;
    }

    .logo {
        height: 70px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header-Bereich mit Logos
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_1.png", width=120)
    with col2:
        st.image("https://raw.githubusercontent.com/Reik98/Landingpage/main/Logo_2.png", width=80)

    # Navigations-Buttons nebeneinander
    nav1, nav2, nav3, nav4 = st.columns(4)
    with nav1:
        with st.container():
            st.page_link("Home.py", label="Home", icon="🏠", help="Zur Startseite", key="home", disabled=False)
            st.markdown('<div class="custom-button"></div>', unsafe_allow_html=True)
    with nav2:
        with st.container():
            st.page_link("pages/Quiz.py", label="Quiz", icon="❓", key="quiz")
            st.markdown('<div class="custom-button"></div>', unsafe_allow_html=True)
    with nav3:
        with st.container():
            st.page_link("pages/Events.py", label="Events", icon="📅", key="events")
            st.markdown('<div class="custom-button"></div>', unsafe_allow_html=True)
    with nav4:
        with st.container():
            st.page_link("pages/Über_uns.py", label="Über uns", icon="👥", key="ueber")
            st.markdown('<div class="custom-button"></div>', unsafe_allow_html=True)
