import streamlit as st

st.write("BMI Calculator")
st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kilograms")
height = st.number_input("Enter your height in meters")

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is {bmi}")
    if bmi < 18.5: 
        st.write("You are underweight")
    elif bmi >= 18.5 and bmi <= 24.9:
        st.write("You are normal weight")
    elif bmi >= 25 and bmi <= 29.9:
        st.write("You are overweight")
    elif bmi >= 30:
        st.write("You are obese")