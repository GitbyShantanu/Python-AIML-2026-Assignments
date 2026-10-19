# Stream for celcius to fahrenheit converter
import streamlit as st 

st.title("Celcius to Fahrenheit Converter") 

celcius = st.number_input("Enter Celcius : ", min_value=-40.0, max_value=100.0, step=0.1) 

def convert_celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

if st.button("Convert"):
    st.success(f"The temperature in Fahrenheit is : {convert_celcius_to_fahrenheit(celcius)}")  