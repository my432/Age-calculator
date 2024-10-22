# Save this code in a Python file (e.g., `app.py`)

import streamlit as st
from datetime import date

# Function to calculate age
def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Streamlit app
st.title("Age Calculator")

# Input for birthdate
birth_date = st.date_input("Enter your birthdate")

# Calculate age
if birth_date:
    age = calculate_age(birth_date)
    st.write(f"Your age is: {age} years")
