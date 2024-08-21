import streamlit as st

st.title("🎈 BMI calculator")
st.write(
    "Welcome to the BMI calculator."
)
weight = st.text_input("Enter your weight(kg): ")
height = st.text_input("Enter your height(m): ")

if st.button('Click me'):
    if weight == "" or height == "":
        st.write("Please enter your height and weight."
    else:
         bmi = weight / (height ** 2)
    st.write(
    "Your BMI is {bmi}."
)
