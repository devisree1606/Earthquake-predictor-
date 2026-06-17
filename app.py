import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="🌍 Earthquake Prediction System",
    page_icon="🌎",
    layout="centered"
)

# Background Style
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #6dd5ed, #2193b0);
}
h1 {
    color: white;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# User Database
users = {
    "devi": "1234",
    "santhosh": "5678",
    "user1": "password"
}

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# Login Page
if not st.session_state.logged_in:

    st.markdown("<h1>🌍 Earthquake Prediction System 🌍</h1>", unsafe_allow_html=True)

    st.markdown("### 🔐 Login to Continue")

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("🚀 Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("✅ Login Successful!")
            st.balloons()
            st.rerun()
        else:
            st.error("❌ Invalid Username or Password")

# Main Application
else:

    st.markdown("<h1>🌎 Earthquake Prediction System 🌎</h1>", unsafe_allow_html=True)

    st.success(f"🎉 Welcome, {st.session_state.username}!")

    st.markdown("### 📊 Enter Earthquake Details")

    magnitude = st.number_input("📈 Magnitude", min_value=0.0)
    depth = st.number_input("🌊 Depth (km)", min_value=0.0)
    latitude = st.number_input("📍 Latitude")
    longitude = st.number_input("🗺️ Longitude")

    if st.button("🔍 Predict Earthquake Level"):

        if magnitude < 4:
            st.success("🟢 Low Earthquake Risk")
            st.snow()

        elif magnitude < 6:
            st.warning("🟡 Moderate Earthquake Risk")

        else:
            st.error("🔴 Severe Earthquake Risk ⚠️")
            st.balloons()

    st.markdown("---")
    st.markdown("### ℹ️ Prediction Levels")
    st.info("🟢 Low : Magnitude < 4")
    st.info("🟡 Moderate : Magnitude 4 - 6")
    st.info("🔴 Severe : Magnitude > 6")

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.markdown("---")
    st.markdown(
        "<center><h4>💙 Developed for Earthquake Analysis & Prediction 🌍</h4></center>",
        unsafe_allow_html=True
    )

