import streamlit as st

# Simple user database
users = {
    "devi": "1234",
    "santhosh": "5678",
    "user1": "password"
}

# Login Session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login Page
if not st.session_state.logged_in:
    st.title("Earthquake Prediction System - Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid Username or Password")

# Prediction Page
else:
    st.title("Earthquake Prediction System")

    magnitude = st.number_input("Magnitude")
    depth = st.number_input("Depth")
    latitude = st.number_input("Latitude")
    longitude = st.number_input("Longitude")

    if st.button("Predict"):
        if magnitude < 4:
            st.success("Low Earthquake")
        elif magnitude < 6:
            st.warning("Moderate Earthquake")
        else:
            st.error("Severe Earthquake")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
