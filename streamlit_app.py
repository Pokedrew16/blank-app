import streamlit as st

st.title("🎈 BMI calculator")
st.write(
    "Welcome to the BMI calculator."
)
weight = st.text_input("Enter your weight(kg): ")
height = st.text_input("Enter your height(m): ")

bmi = (weight / (height)^2)
if st.button('Click me'):
    st.write(
    "Your BMI is {bmi}."
)
