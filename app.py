import streamlit as st
from datetime import date, timedelta
import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Function to calculate the days until next birthday
def days_until_birthday(birthdate):
    today = date.today()
    next_birthday = date(today.year, birthdate.month, birthdate.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birthdate.month, birthdate.day)
    return (next_birthday - today).days

# Function to display the day of the week of birth
def day_of_week(birthdate):
    return birthdate.strftime("%A")

# Streamlit app
st.title("🎉 Age Calculator 🎉")

# Input for birthdate
with st.container():
    birth_date = st.date_input("Enter your birthdate")

# Layout with columns
col1, col2, col3 = st.columns(3)

# Calculate age and display information
if birth_date:
    age = calculate_age(birth_date)
    days_left = days_until_birthday(birth_date)
    birth_day = day_of_week(birth_date)

    with col1:
        st.subheader("🎂 Your Age")
        st.write(f"**{age} years**")

    with col2:
        st.subheader("📅 Next Birthday")
        st.write(f"In **{days_left} days**")
        
    with col3:
        st.subheader("📆 Day of Birth")
        st.write(f"You were born on a **{birth_day}**")

# Additional insights: Age in months, weeks, and days
st.write("---")
st.subheader("📊 Additional Insights")
age_in_days = (date.today() - birth_date).days
age_in_months = age * 12
age_in_weeks = age_in_days // 7

st.write(f"Your age in months: **{age_in_months} months**")
st.write(f"Your age in weeks: **{age_in_weeks} weeks**")
st.write(f"Your age in days: **{age_in_days} days**")

# Add a reset button
if st.button("Reset"):
    st.experimental_rerun()
