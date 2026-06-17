import streamlit as st

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
