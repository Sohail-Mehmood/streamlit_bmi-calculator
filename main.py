import streamlit as st

st.title("BMI Calculator of candidate of PIAIC-251009")

def calculate_bmi(weight, feet, inches):
    # Convert height to meters
    height_meters = (feet * 0.3048) + (inches * 0.0254)
    bmi = weight / (height_meters ** 2)
    return bmi

# User inputs
weight = st.number_input("Enter your weight in kg:", min_value=1.0, max_value=500.0, value=75.0, step=0.1, key="weight_input")
feet = st.number_input("Enter your height (feet):", min_value=2, max_value=8, value=5, key="feet_input")
inches = st.number_input("Enter additional height (inches):", min_value=0, max_value=11, value=6, key="inches_input")

# Calculate BMI
result = calculate_bmi(weight, feet, inches)

# Display result
st.write(f"**Your BMI is:** {result:.2f}")

# Interpretation of BMI categories
if result < 18.5:
    st.write("⚠️ **Hey, Man you are underweight.**")
elif 18.5 <= result <= 24.9:
    st.write("✅ **Hey, Man you have a normal weight.**")
elif 25 <= result <= 29.9:
    st.write("⚠️ **Hey, Man you are overweight.**")
else:
    st.write("🚨 **Hey, Man you are obese.**")
