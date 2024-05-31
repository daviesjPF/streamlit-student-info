import streamlit as st

# Title of the app
st.title("Student Information") 

name = st.text_input("Your Name", "Tintin")
age = st.slider("Your Age?", 1, 100, 24) #min, max, default
if st.button('Display Information'):
    f"Students name: {name}"
    f"Students age: {age}"